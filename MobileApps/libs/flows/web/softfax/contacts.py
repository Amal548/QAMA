import logging
from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException


class Contacts(SoftFaxFlow):
    flow_name = "contacts"

    RECENT_TAB_BTN = "recent_tab"
    SAVED_TAB_BTN = "saved_tab"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_add(self):
        """
        Click Add button
        """
        self.driver.click("add_btn")

    def add_edit_contact(self, fax_number, name, is_new=True):
        """
        Successfully add or edit a new contact
        :param fax_number:
        :param name:
        :param country_code: default 1 for USA
        """
        if is_new:
            self.driver.wait_for_object("add_contact_title", timeout=10)
        else:
            self.driver.wait_for_object("edit_contact_title", timeout=10)
        country_code = self.driver.get_attribute("country_code_edit_tf", "value")
        self.driver.send_keys("fax_number_edit_tf", fax_number)
        self.driver.send_keys("name_edit_tf", name)
        self.driver.click("save_btn")
        return country_code, fax_number, name

    def click_tab_btn(self, tab_name):
        """
        Click on Recent or Saved tab button
        :param tab_name: tab name. Use class constant
                    -   RECENT_TAB_BTN
                    -   SAVED_TAB_BTN
        """
        self.driver.click(tab_name)

    def select_saved_contact(self, phone_number, contact_name):
        """
        Select a contact
        :param phone_number:
        :param contact_name:
        """
        contact_cells = self.driver.find_object("contact_cell", multiple=True)
        for contact in contact_cells:
            try:
                self.driver.wait_for_object("saved_contact_phone_number", root_obj=contact,
                                            format_specifier=[phone_number], displayed=False)
                self.driver.wait_for_object("saved_contact_title", root_obj=contact, format_specifier=[contact_name],
                                            displayed=False)
                contact.click()
                return True
            # Invisible elements are detected causing click failure so added an exception
            except(TimeoutException, ElementNotVisibleException):
                continue
        raise TimeoutException(
            "There is no saved contact with phone number: {} and contact name: {}".format(phone_number, contact_name))

    def click_edit_contact_delete(self):
        """
        Click on Delete button on Edit Contact screen
        """
        self.driver.click("edit_contact_delete_btn")

    def dismiss_edit_delete_confirmation_popup(self, is_deleted=True):
        """
        Dismiss Are you sure? popup which is for confirming deletion
        :param is_deleted: dismiss by clicking on Delete button if it is True. Otherwise, click on Cancel button
        """
        if is_deleted:
            self.driver.click("are_you_sure_popup_delete_btn")
        else:
            self.driver.click("are_you_ure_popup_cancel_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_contacts_screen(self):
        """
        Verify Contact screen via:
            - title
            - Add button
            - Recent and Save tabs
        """
        self.driver.wait_for_object("title", timeout=30)
        self.driver.wait_for_object("add_btn", timeout=5)
        self.driver.wait_for_object("recent_tab", timeout=5)
        self.driver.wait_for_object("saved_tab", timeout=5)

    def verify_contact_screen_title(self, raise_e=False):
        return self.driver.wait_for_object("title", raise_e=raise_e) is not False

    def verify_empty_contact_list(self, is_saved=True, raise_e=True):
        """
        Verify empty Recent/Saved contact list.
        Note: Although there is a contact on list, the empty message is still on screen.
              Therefore, check no contact cell on screen
        :param is_saved: contact is in saved tab (True) or recent tab (False)
        """
        if is_saved:
            obj = "saved_empty_contact_message"
        else:
            obj = "recent_empty_contact_message"
        return self.driver.wait_for_object(obj, raise_e=raise_e) is not False and \
               self.driver.wait_for_object("contact_cell", invisible=True, raise_e=raise_e) is not False

    def verify_contact(self, phone_number, contact_name=None, is_saved=True, invisible=False):
        """
        Verify visible contact on Recent/Saved tab
        :param phone_number:
        :param contact_name: None (default) if verifying Recent tab
        :param is_saved: contact is in saved tab (True) or recent tab (False)
        :param invisible
        """
        # If empty list and invisible=False, raise TimeoutException
        if self.verify_empty_contact_list(is_saved=is_saved, raise_e=False):
            if invisible:
                return True
            else:
                raise TimeoutException(
                    "There is no contact with phone number: {} and contact name: {}".format(phone_number, contact_name))

        self.driver.wait_for_object("contact_cell")
        contact_cells = self.driver.find_object("contact_cell", multiple=True)
        for contact in contact_cells:
            try:
                self.driver.wait_for_object("saved_contact_phone_number", root_obj=contact,
                                            format_specifier=[phone_number])
                if is_saved and contact_name:
                    self.driver.wait_for_object("saved_contact_title", root_obj=contact,
                                                format_specifier=[contact_name])
                if invisible:
                    raise TimeoutException(
                        "There is a contact with invisible ({}) with phone number: {} and contact name: {}".format(
                            invisible, phone_number, contact_name))
                else:
                    return True
            except TimeoutException:
                continue
        if not invisible:
            raise TimeoutException(
                "There is no contact with invisible ({}) with phone number: {} and contact name: {}".format(invisible,
                                                                                                            phone_number,
                                                                                                            contact_name))

    def verify_edit_contact_screen(self):
        """
        Verify Edit Contact screen:
            - title
            - Delete button
        """
        self.driver.wait_for_object("edit_contact_title", timeout=30)
        self.driver.wait_for_object("edit_contact_delete_btn", timeout=5)

    def verify_edit_delete_confirmation_popup(self):
        """
        Verify Are you sure? popup for deleting confirmation:
            - title
            - Cancel and Delete buttons
        """
        self.driver.wait_for_object("are_you_sure_popup_title", timeout=30)
        self.driver.wait_for_object("are_you_ure_popup_cancel_btn", timeout=10)
        self.driver.wait_for_object("are_you_sure_popup_delete_btn", timeout=10)

    def verify_phone_invalidation_message(self, fax_number, name, is_new=True):
        """
        Verify invalidation message after entering invalid recipient phone on Add Contacts or Edit Contacts screen
        :param fax_number:
        :param name
        :param is_new:
        """
        if is_new:
            self.driver.wait_for_object("add_contact_title")
        else:
            self.driver.wait_for_object("edit_contact_title")
        self.driver.send_keys("fax_number_edit_tf", fax_number)
        self.driver.send_keys("name_edit_tf", name)
        self.driver.wait_for_object("invalid_format_phone_number_msg")

    def verify_and_select_saved_contact(self, phone_number, contact_name, select_contact=False, select_info=False,
                                        raise_e=False):
        contact_found = False
        contact_list = self.driver.find_object("saved_contact_list", multiple=True, raise_e=False)
        if contact_list is False:
            logging.info("Saved Contact list is empty")
            return contact_found
        for contact in contact_list:
            contact_info = contact.text
            if phone_number in contact_info and contact_name in contact_info:
                if select_contact:
                    self.driver.click("saved_contact_title", root_obj=contact, format_specifier=[contact_name])
                elif select_info:
                    self.driver.click("saved_i_icon_btn", root_obj=contact)
                contact_found = contact
                break
        if not contact_found and raise_e:
            raise TimeoutException(
                "There is no contact with phone number: {} and contact name: {}".format(phone_number, contact_name))
        else:
            return contact_found

    def verify_add_btn(self, raise_e=False):
        return self.driver.wait_for_object("add_btn", timeout=5, raise_e=raise_e) is not False

    def select_info_icon(self, element):
        self.driver.click("saved_i_icon_btn", root_obj=element)

    def get_contact_list(self, index=0, multiple=True, raise_e=False):
        return self.driver.find_object("saved_contact_list", index=index, multiple=multiple, raise_e=raise_e)


class MobileContacts(Contacts):
    context = "NATIVE_APP"

    def click_saved_contact_info(self, phone_number, contact_name):
        """
        Click on i icon of a contact on Saved contact list
        Note: Click() on this element is unsuccessful in Webview without any error.
              Therefore, it is in Native App 
        @param phone_number: target contact's phone number
        @param contact_name: target contact's name
        """
        self.driver.scroll("saved_i_icon_btn", format_specifier=[phone_number, contact_name], click_obj=True)

    def click_tab_btn_native(self, tab_name):
        """
        Click on Recent or Saved tab button
        :param tab_name: tab name. Use class constant
                    -   RECENT_TAB_BTN
                    -   SAVED_TAB_BTN
        """
        self.driver.click(tab_name)

    def clear_edit_contact_text(self):
        elements = ["fax_number_edit_tf", "name_edit_tf"]
        for element in elements:
            self.driver.click(element)
            if self.driver.wait_for_object("select_all_btn", raise_e=False) is False:
                self.driver.click(element)
            self.driver.click("select_all_btn")
            self.driver.click("cut_btn")
