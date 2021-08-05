import logging

from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
from selenium.common.exceptions import NoSuchElementException


class ComposeFax(SoftFaxFlow):
    flow_name = "compose_fax"

    FILES_PHOTOS_BTN = "files_photos_btn"
    CAMERA_BTN = "camera_btn"
    SCANNER_BTN = "scanner_btn"
    MENU_SAVE_DRAFT_BTN = "menu_save_draft"
    MENU_CLEAR_FIELDS_BTN = "menu_clear_fields"
    MENU_FAX_HISTORY_BTN = "menu_fax_history"
    MENU_FAX_SETTINGS_BTN = "menu_fax_settings"
    MENU_HOME_BTN = "menu_home"
    MENU_NEW_COMPOSE_BTN = "menu_new_compose"
    EMPTY_PHONE_MSG = "empty_phone_number_msg"
    INVALID_FORMAT_MSG = "invalid_format_phone_number_msg"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    # -------------------       Files and Cover Page        -----------------------------
    def click_files_and_cover_page(self):
        """
        Click on Files and Cover Page on Compose Fax screen
        """
        self.driver.click("files_cover_page_dropdown")

    def enter_subject(self, name):
        """
        Enter a subject name
        :param name: required parameter
        """
        self.driver.wait_for_object("subject_name_edit_tf")
        self.driver.send_keys("subject_name_edit_tf", name)

    def click_trash_icon(self):
        """
        Click on Trash icon under Files and Cover Page section
        """
        self.driver.click("trash_icon")

    def click_save_cover_page_template(self):
        """
        Click on Save cover page template under Files and Cover Page section
        """
        self.driver.click("save_cover_page_template_btn")

    def enter_cover_page_name(self, cover_page_name):
        """
        Enter a cover page name
        :param name: required parameter
        """
        self.driver.wait_for_object("cover_page_name_edit_tf")
        self.driver.send_keys("cover_page_name_edit_tf", cover_page_name)

    def click_cancel_btn(self):
        """
        Click on CANCEL button on Name your cover page template screen
        """
        self.driver.click("cancel_btn")

    def click_save_btn(self):
        """
        Click on Sve button on Name your cover page template screen
        """
        self.driver.click("save_btn")

    def click_template_btn(self):
        """
        Click on Template button under Files and Cover Page section
        """
        self.driver.click("template_title")

    def click_none_option(self):
        """
        Click on None on Template option list
        """
        self.driver.click("none_option")

    def click_create_a_new_cover_page_template_option(self):
        """
        Click on Creaet a new cover page template on option list
        """
        self.driver.click("create_a_new_cover_page_template_option")

    def click_edit_btn(self):
        """
        Click on Edit button on option list
        """
        self.driver.click("edit_btn")

    def click_add_files_option_btn(self, btn_name):
        """
        Click on a button in Add File
        :param btn_name: using class constant
                        FILES_PHOTOS_BTN
                        CAMERA_BTN
                        SCANNER_BTN
        """
        self.click_files_and_cover_page()
        if not self.driver.wait_for_object(btn_name, invisible=False, timeout=10):
            self.driver.click("files_cover_page_dropdown")
        self.driver.click(btn_name)

    def click_recipient_dropdown(self):
        self.driver.click("recipient_dropdown")

    def verify_add_your_files_options(self):
        self.click_files_and_cover_page()
        self.driver.wait_for_object(self.FILES_PHOTOS_BTN)
        self.driver.wait_for_object(self.CAMERA_BTN)
        self.driver.wait_for_object(self.SCANNER_BTN)

    def delete_added_file(self):
        """
        Click on trash icon in files and cover page after adding new file
        """
        self.driver.click("delete_icon_btn")

    def get_added_file_information(self):
        """
        Get information of added file:
        :return: file name and number of page
        """
        self.driver.wait_for_object("files_cover_page_dropdown", timeout=10)
        self.driver.click("files_cover_page_dropdown")
        file_name = self.driver.find_object("file_name").text
        number_pages = self.driver.find_object("file_number_pages").text
        return file_name, number_pages

    def verify_file_added(self, raise_e=False):
        return self.driver.wait_for_object("file_name", raise_e=raise_e)

    # -------------------       To and From section        -----------------------------
    def enter_recipient_information(self, phone_no, name=None):
        """
        Enter recipient information
        :param phone_no: required parameter
        :param country_code: country code. Example: +1 , 1
        :param name: optional parameter.
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("recipient_phone_edit_tf", timeout=5)
        self.driver.send_keys("recipient_phone_edit_tf", phone_no)
        if name:
            self.driver.send_keys("recipient_name_edit_tf", name)

    def get_recipient_information(self):
        """
        Get Recipient Information
        :return: (phone number, name)
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("recipient_phone_edit_tf", timeout=5)
        phone = self.driver.get_attribute("recipient_phone_edit_tf", "value")
        country_code = self.driver.get_attribute("recipient_phone_country_code", "value")
        name = self.driver.get_attribute("recipient_name_edit_tf", "value")
        return phone, name, country_code

    def click_contacts_icon(self):
        """
        From Compose Fax screen, Clicking on person icon in To area
        """
        self.driver.wait_for_object("recipient_dropdown", timeout=10)
        self.driver.click("recipient_dropdown")
        self.driver.click("recipient_contact_icon")

    def enter_sender_information(self, name, phone_no):
        """
        Enter a sender information
        :param name: required parameter
        :param phone_no: required parameter
        :param country_code: country code. Example: +1, 1
        """
        # Make sure start from top of screen
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("sender_phone_edit_tf", timeout=5)
        self.driver.send_keys("sender_phone_edit_tf", phone_no)
        self.driver.send_keys("sender_name_edit_tf", name)

    def get_sender_information(self):
        """
        Get Recipient Information
        :return: (phone number, name)
        """
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        # Switch back to Native App for this element
        self.driver.wait_for_object("sender_phone_edit_tf", timeout=5)
        phone = self.driver.get_attribute("sender_phone_edit_tf", "value")
        name = self.driver.get_attribute("sender_name_edit_tf", "value")
        return phone, name

    def click_send_fax(self, raise_e=True):
        """
        Click on Sex Fax button
        """
        self.driver.wait_for_object("send_fax_btn")
        return self.driver.click("send_fax_btn", change_check={"wait_obj": "send_fax_btn", "invisible": True},
                                 raise_e=raise_e)

    def click_menu_option_btn(self, btn_name):
        """
        Click on a button in Menu Option
        :param btn_name: using class constant
                MENU_SAVE_DRAFT_BTN
                MENU_CLEAR_FIELDS_BTN
                MENU_FAX_HISTORY_BTN
                MENU_FAX_SETTINGS_BTN
                MENU_HOME_BTN
                MENU_NEW_COMPOSE_BTN
        :return:
        """
        self.driver.click("3_dots_menu_btn")
        self.driver.wait_for_object(btn_name, timeout=5)
        self.driver.click(btn_name)

    def verify_3_dots_menu_options(self):
        options_missing = []
        options = [self.MENU_SAVE_DRAFT_BTN, self.MENU_CLEAR_FIELDS_BTN, self.MENU_FAX_HISTORY_BTN,
                   self.MENU_FAX_SETTINGS_BTN, self.MENU_HOME_BTN]
        self.driver.click("3_dots_menu_btn")
        for option in options:
            if self.driver.wait_for_object(option, raise_e=False) is False:
                options_missing.append(option)
        if len(options_missing) > 0:
            logging.info("Following options {}:not displayed".format(options_missing))
            return False
        else:
            return True

    def verify_save_as_draft_pop_up(self):
        """
        Verify save as draft pop_up elements: title, message and buttons
        """
        self.driver.wait_for_object("save_as_draft_popup_title")
        self.driver.wait_for_object("save_as_drat_popup_msg")
        self.driver.wait_for_object("save_as_draft_popup_save_draft_btn")
        self.driver.wait_for_object("save_as_draft_popup_exit_bn")
        self.driver.wait_for_object("save_as_draft_popup_cancel_btn")

    def dismiss_save_as_draft_popup(self, is_saved=False, is_cancel=False):
        """
        Dismiss Save as a  draft? if it displays
        :param is_saved: True -> click on Save as Draft button. False -> click on Exit button
        """
        if self.driver.wait_for_object("save_as_draft_popup_title", timeout=10, raise_e=False):
            if is_saved:
                self.driver.click("save_as_draft_popup_save_draft_btn")
            elif is_cancel:
                self.driver.click("save_as_draft_popup_cancel_btn")
            else:
                self.driver.click("save_as_draft_popup_exit_bn")

    def click_save_this_contact_btn(self):
        """
        Click on Save this contact button on Compose Fax screen
        """
        self.driver.click("save_this_contact_btn")

    def click_add_optional_info_btn(self):
        """
        Click on Add Optional info button under From section
        """
        self.driver.click("add_optional_info_btn")

    def verify_add_optional_info_btn(self, raise_e=True):
        return self.driver.wait_for_object("add_optional_info_btn", raise_e=raise_e)

    def click_save_as_profile_btn(self):
        """
        Click on Save as profile button under From section
        """
        self.driver.click("save_as_profile_btn")

    def click_collapse_btn(self):
        """
        Click on Collapse button under From section
        """
        self.driver.click("collapse_btn")

    def verify_collapse_btn(self, raise_e=True):
        return self.driver.wait_for_object("collapse_btn", raise_e=raise_e)

    def verify_reply_fax_number(self):
        self.driver.wait_for_object("reply_fax_number")

    def enter_profile_name(self, profile_name):
        """
        Enter a profile name
        :param name: profile_name
        """
        self.driver.wait_for_object("profile_name_edit_tf")
        self.driver.send_keys("profile_name_edit_tf", profile_name)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_compose_fax_screen(self, timeout=60, raise_e=True):
        """
        Verify current screen is Compose Fax screen via:
            - title
            - Send Fax button
        """
        return self.driver.wait_for_object("title", timeout=timeout,
                                           raise_e=raise_e) is not False and self.driver.wait_for_object("send_fax_btn",
                                                                                                         timeout=10,
                                                                                                         raise_e=raise_e) is not False

    # -------------------       To and From section       -----------------------------
    def verify_phone_validation_message(self, error_msg, is_sender=False, raise_e=True):
        """
        Verify validation message after entering invalid recipient phone (visible/invisible)
        :param error_msg: using class constant
                EMPTY_PHONE_MSG
                INVALID_FORMAT_MSG
        :param raise_e:
        """
        if is_sender:
            self.driver.wait_for_object("sender_dropdown", timeout=10)
            self.driver.click("sender_dropdown")
        else:
            self.driver.click("recipient_dropdown")
        return self.driver.wait_for_object(error_msg, timeout=10, raise_e=raise_e)

    def verify_sender_name_error_message(self, raise_e=True):
        """
        Verify error message after entering invalid sender name
        :param raise_e:
        """
        self.driver.wait_for_object("sender_dropdown", timeout=10)
        self.driver.click("sender_dropdown")
        return self.driver.wait_for_object("sender_name_error_message", timeout=10, raise_e=raise_e)

    def verify_save_this_contact_btn(self, invisible=False, raise_e=True):
        """
        Verify Save this contact button is invisible or not on Compose Fax screen
        """
        return self.driver.wait_for_object("save_this_contact_btn", invisible=invisible, raise_e=raise_e)

    def verify_saved_btn(self, invisible=False, raise_e=True):
        """
        Verify Saved button is invisible or not on Compose Fax screen
        """
        return self.driver.wait_for_object("saved_btn", invisible=invisible, raise_e=raise_e)

    def verify_organization_name(self, invisible=False, raise_e=True):
        """
        Verify organization name label is invisible or not under From section
        """
        return self.driver.wait_for_object("organization_name", invisible=invisible, raise_e=raise_e)

    def verify_email(self, invisible=False, raise_e=True):
        """
        Verify email label is invisible or not under From section
        """
        return self.driver.wait_for_object("organization_name", invisible=invisible, raise_e=raise_e)

    def verify_name_your_profile_screen(self):
        """
        Verify current screen is Name your profile screen via:
            - title
            - CANCEL and SAVE button
        """
        self.driver.wait_for_object("name_your_profile_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("save_btn")

    def verify_profile_label(self, raise_e=True):
        """
        Verify Profile: label under from section:
        """
        return self.driver.wait_for_object("profile_label", raise_e=raise_e)

    def get_sender_profile_label(self):
        self.driver.click("sender_dropdown")
        if self.verify_profile_label(raise_e=False) is not False:
            return self.driver.get_attribute("sender_profile_label", "text")
        else:
            return False

    # -------------------       Files and Cover Page        -----------------------------
    def verify_added_pages_number(self, page_number):
        """
        Verify page number in file and cover page
        :param page_number:
        :type page_number: int
        """
        # Make sure start from top of screen
        self.driver.wait_for_object("files_cover_page_dropdown", timeout=10)
        self.driver.click("files_cover_page_dropdown")
        self.driver.wait_for_object("file_number_pages", timeout=10)
        actual_page = int(self.driver.find_object("file_number_pages").text.split(" ")[0])
        if actual_page != page_number:
            raise ValueError(
                "Expected {} page(s) is not on the screen. Actual: {} page(s)".format(page_number, actual_page))

    def verify_uploaded_file(self, timeout=30):
        """
        Verify file is uploaded successfully.
        :param timeout: uploading timeout
        """
        # Make sure start from top of screen
        self.click_files_and_cover_page()
        self.driver.wait_for_object("file_name", timeout=timeout)
        self.driver.wait_for_object("file_number_pages", timeout=10)

    def verify_no_updated_file(self):
        """
        Verify that there is no file which i added by visible:
            - file & photos button
            - camera button
            - printer scanner button
        """
        self.click_files_and_cover_page()
        self.driver.wait_for_object("files_photos_btn", timeout=10)
        self.driver.wait_for_object("camera_btn", timeout=10)
        self.driver.wait_for_object("scanner_btn", timeout=10)

    def verify_subject(self, invisible=False):
        """
        Verify Subject * under Files and Cover Page section
        """
        self.driver.wait_for_object("subject_name_edit_tf", invisible=invisible)

    def verify_message(self):
        """
        Verify Message under Files and Cover Page section
        """
        self.driver.wait_for_object("message_name_edit_tf")

    def verify_subject_invalid_message(self):
        """
        Verify message "Fax Subject is required"
        """
        self.driver.wait_for_object("subject_invalid_message")

    def verify_name_your_cover_page_template(self):
        """
        Verify name your cover page template screen with:
        - Title
        - CANCEL & SAVE button
        """
        self.driver.wait_for_object("save_cover_page_template_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("save_btn")

    def verify_no_cover_page_template_title_message(self):
        """
        Verify message "A cover page template title is required"
        """
        self.driver.wait_for_object("no_cover_page_template_title_message")

    def verify_cover_template(self, invisible=False, raise_e=True):
        """
        Verify Template: under Files and Cover Page section
        """
        self.driver.wait_for_object("template_title", invisible=invisible, raise_e=raise_e)

    def verify_cover_template_option_screen(self):
        """
        Verify Template option screen with:
        - None
        - Create a new cover page template
        - Currently template list
        """
        self.driver.wait_for_object("none_option")
        self.driver.wait_for_object("list_option")
        self.driver.wait_for_object("create_a_new_cover_page_template_option")

    def verify_template_list(self, template_name):
        """
        Verify template name is visible or invisible under Files and Cover Page / Template section
        :param template_name
        :param invisible
        """
        self.driver.wait_for_object("template_name", format_specifier=[template_name], displayed=True)


class MobileComposeFax(ComposeFax):
    context = "NATIVE_APP"

    def click_send_fax_native_btn(self, change_check={"wait_obj": "send_fax_btn", "invisible": True}):
        """
        Click on Send Fax button
        """
        self.driver.click("send_fax_btn", change_check=change_check, timeout=10)

    def toggle_need_a_cover_page_on_off(self, on=True):
        """
        switch on/off button for need a cover page
        :param enable: True or False
        """
        on_off_switch = self.driver.find_object("need_a_cover_page_btn")
        if on != (on_off_switch.get_attribute("checked").lower() == "true"):
            on_off_switch.click()

    def verify_cover_page(self, invisible=False):
        """
        Verify Cover Page on compose fax screen
        """
        self.driver.wait_for_object("cover_page", invisible=invisible)

    def verify_one_cover_page(self, invisible=False):
        """
        Verify 1 page under Files and Cover Page section
        """
        self.driver.wait_for_object("one_cover_page", invisible=invisible)
