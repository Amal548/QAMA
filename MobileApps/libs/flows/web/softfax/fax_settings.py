from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class MissingSingleCoverPageException(Exception):
    pass

class MissingSingleSenderProfileException(Exception):
    pass

class FaxSettings(SoftFaxFlow):
    flow_name = "fax_settings"

    COVER_PAGES_OPT = "cover_pages_opt"
    SEND_PROFILES_OPT = "sender_profiles_opt"
    CONTACTS_OPT = "contacts_opt"
    TERMS_OF_SERVICES_OPT = "terms_of_services_opt"
    BUSINESS_ASSOCIATE_AGREEMENT_OPT = "business_agreement_opt"
    COVER_PAGE_SELECT_BTN = "cover_page_select_btn"
    COVER_PAGE_CANCEL_BTN = "cover_page_cancel_btn"
    SENDER_PROFILE_SELECT_BTN = "sender_profile_select_btn"
    SENDER_PROFILE_CANCEL_BTN = "sender_profile_cancel_btn"
    CONTACT_SELECT_BTN = "contact_select_btn"
    CONTACT_CANCEL_BTN = "contact_cancel_btn"
    MENU_COMPOSE_NEW_FAX_BTN = "menu_compose_new_fax"
    MENU_FAX_HISTORY_BTN = "menu_fax_history"
    MENU_HOME_BTN = "menu_home"
    
    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def click_fax_settings_option(self, opt_name):
        """
        Click on a option in Fax Settings menu
        :param opt_name: using class constant
                COVER_PAGES_OPT
                SEND_PROFILES_OPT
                CONTACTS_OPT
                TERMS_OF_SERVICES_OPT
                BUSINESS_ASSOCIATE_AGREEMENT_OPT
        """
        self.driver.wait_for_object(opt_name)
        self.driver.click(opt_name)
    
    def click_menu_option_btn(self, btn_name):
        """
        Click on a button in Menu Option
        :param btn_name: using class constant
                MENU_COMPOSE_NEW_FAX_BTN
                MENU_FAX_HISTORY_BTN
                MENU_HOME_BTN
        """
        self.driver.click("3_dots_menu_btn")
        self.driver.wait_for_object(btn_name, timeout=5)
        self.driver.click(btn_name)
    
    def click_edit_cancel_btn(self, btn_name):
        """
        Click on SELECT or Cancel button on Cover Pages screen Or Sender Profile screen or Contacts screen
        :param btn_name: using class constant
                SELECT_BTN
                CANCEL_BTN
        """
        self.driver.click(btn_name)
    
    #-------------------        Cover Page function         -----------------------------
    def click_create_cover_page_btn(self):
        """
        Click on Create a Cover Page button
        """
        self.driver.wait_for_object("create_cover_page_btn")
        self.driver.click("create_cover_page_btn")

    def add_edit_cover_page(self, cover_page_name, cover_page_subject, is_new=True):
        """
        Successfully add or edit a cover page
        :param cover_page_name
        :param cover_page_subject
        """
        if is_new:
            self.driver.wait_for_object("add_cover_page_title")
        else:
            self.driver.wait_for_object("edit_cover_page_title")
        self.driver.send_keys("cover_page_page_name_tf", cover_page_name)
        self.driver.send_keys("subject_tf", cover_page_subject)
        self.driver.click("save_btn")
        return cover_page_name
    
    def select_single_cover_page(self, cover_page_name):
        """
        Select single cover page on Cover Page screen
        :param cover_page_name
        """
        self.driver.click("cover_pages_name", format_specifier=[cover_page_name])

    def click_cover_pages_delete_btn(self, is_edited=True):
        """
        Click on Delete button on Cover Pages or Edit Cover Page screen
        :param is_edited:
          - if is_edited, means click delete button on Edit Cover Page screen
          - Otherwise, click delete button on Cover Pages screen
        """
        if is_edited:
            self.driver.click("edit_cover_page_delete_btn")
        else:
            self.driver.click("cover_pages_delete_btn")
    
    def dismiss_delete_confirmation_popup(self, is_deleted=True):
        """
        Dismiss Are you sure? popup which is for confirming deletion
        :param is_deleted:
        """
        if is_deleted:
            self.driver.click("are_you_sure_popup_delete_btn")
        else:
            self.driver.click("are_you_sure_popup_cancel_btn")

    def delete_multiple_cover_pages(self, cover_page_name, raise_e=True):
        """
        Delete all specific cover page from cover page list screen
        """
        self.driver.wait_for_object("cover_page_header", timeout=20)
        bottom = False
        timeout = time.time() + 90
        while not bottom and time.time() < timeout:
            cover_pages = self.driver.find_object("cover_page_cell", multiple=True)
            for each_cover_page in cover_pages:
                if cover_page_name in each_cover_page.text:
                    self.select_single_cover_page(each_cover_page.text)
            bottom = self.driver.swipe(check_end=True)[1]
        try:
            self.fax_settings.click_cover_pages_delete_btn(is_edited=False)
            self.dismiss_delete_confirmation_popup(is_deleted=True)
            return True
        except (TimeoutException, NoSuchElementException) as ex:
            if raise_e:
                raise ex
            return False

    #-------------------        Sender Profiles Function         -----------------------------
    def click_create_a_new_sender_profile_btn(self):
        """
        Click on Create a New Sender Profile button
        """
        self.driver.wait_for_object("create_new_sender_profiles_btn")
        self.driver.click("create_new_sender_profiles_btn")
    
    def add_edit_sender_profile_page(self, profile_title, profile_name, phone_number, is_new=True):
        """
        Successfully add or edit a new sender profile
        :param profile_title
        :param profile_name
        :param phone_number
        :param is_new
        """
        if is_new:
            self.driver.wait_for_object("new_sender_profile_title")
        else:
            self.driver.wait_for_object("edit_sender_profiles_title")
        self.driver.send_keys("profile_title_tf", profile_title)
        self.driver.send_keys("name_tf", profile_name)
        self.driver.send_keys("phone_number_tf", phone_number)
        self.driver.click("profile_save_btn")
        return profile_title
    
    def select_single_sender_profiles(self, sender_profile_name):
        """
        Select single sender profile on Sender Profiles screen 
        :param sender_profile_name
        """
        timeout = time.time() + 60
        # Try to find it in long list
        while time.time() < timeout:
            if self.driver.click("sender_profile_name", format_specifier=[sender_profile_name], raise_e=False):
                return True
            else:
                self.driver.swipe()
        raise NoSuchElementException("There is no '{}' in the sender profile list".format(sender_profile_name))

    def click_sender_profiles_delete_btn(self, is_edited=True):
        """
        Click on Delete button on Sender Profiles or Edit Sender Profiles screen
        :param is_edited:
          - if is_edited, means click delete button on Edit Cover Page screen
          - Otherwise, click delete button on Cover Pages screen
        """
        if is_edited:
            self.driver.click("edit_sender_profile_delete_btn")
        else:
            self.driver.click("sender_profile_delete_btn")
    
    #-------------------        Contacts Function         -----------------------------
    def click_add_a_contact_btn(self):
        """
        Click on Add a Contact button
        """
        self.driver.wait_for_object("create_a_contact_btn")
        self.driver.click("create_a_contact_btn")
    
    def click_contact_delete_btn(self):
        """
        Click on Delete button on Contact or Edit Contact screen
        """
        self.driver.click("contact_delete_btn")

    def dismiss_edit_delete_confirmation(self, is_deleted=True):
        """
        Dismiss Are you sure? popup after clicking Delete button on navigation bar of Edit Contact screen
        """
        if is_deleted:
            self.driver.click("edit_are_you_sure_popup_delete_btn")
        else:
            self.driver.click("edit_are_you_sure_popup_cancel_btn")
    
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # ********************************************************************************
    def verify_fax_settings_screen(self):
        """
        Verify current screen is Fax Settings screen visible or invisible via:
            - title
            - Send Fax button
        """
        self.driver.wait_for_object("fax_settings_title")
        self.driver.wait_for_object("sending_item")
        self.driver.wait_for_object("about_mobile_fax")
    
    def verify_cover_page_screen(self):
        """
        Verify current screen is cover pages screen via:
            - title
            - create a  cover page button
        If cover page screen is empty list, then verify empty message
        :param is_empty
        """
        self.driver.wait_for_object("cover_pages_title", timeout=20)
        self.driver.wait_for_object("create_cover_page_btn")
    
    def verify_empty_cover_page_screen(self, raise_e=True):
        """
        Verify current screen is cover pages screen via:
            - verify empty message
        :param is_empty
        """
        return self.driver.wait_for_object("empty_cover_page_message", raise_e=raise_e)
    
    def verify_cover_page(self, cover_page_name, invisible=False, raise_e=True):
        """
        Verify cover_page visible or invisible on Cover Page screen
        :param cover_page_name
        :param invisible
        """
        return self.driver.wait_for_object("cover_pages_name", format_specifier=[cover_page_name], invisible=invisible, raise_e=raise_e)
    
    def verify_cover_page_edit_screen(self):
        """
        Verify current screen is cover pages edit screen via:
            - title
            - cancel button
        """
        self.driver.wait_for_object("cover_pages_title", timeout=20)
        self.driver.wait_for_object("cover_page_cancel_btn")
    
    def verify_cover_page_delete_popup(self):
        """
        Verify Cover Pages delete popup screen via:
            - title
            - CANCEL btn
            - DELETE button
        """
        self.driver.wait_for_object("are_you_sure_popup_title", timeout=20)
        self.driver.wait_for_object("are_you_sure_popup_delete_btn")
        self.driver.wait_for_object("are_you_sure_popup_cancel_btn")
    
    def verify_edit_cover_page_screen(self):
        """
        Verify Edit Cover Page screen via:
            - title
            - Delete button
        """
        self.driver.wait_for_object("edit_cover_page_title", timeout=20)
        self.driver.wait_for_object("edit_cover_page_delete_btn")
    
    def verify_sender_profiles_screen(self, is_empty=False):
        """
        Verify current screen is sender profiles screen via:
            - title
            - create a New Sender Profile button
        :param is_empty: if True, then verify empty sender profile list
        """
        self.driver.wait_for_object("sender_profiles_title", timeout=20)
        self.driver.wait_for_object("create_new_sender_profiles_btn")
        if is_empty:
            self.driver.wait_for_object("empty_sender_profiles_message")
    
    def verify_sender_profile_list(self, sender_profile_name, invisible=False, raise_e=True):
        """
        Verify sender profile name is visible or invisible on Cover Page screen
        :param sender_profile_name
        :param invisible
        """
        return self.driver.wait_for_object("sender_profile_name", format_specifier=[sender_profile_name], invisible=invisible, raise_e=raise_e)

    def verify_sender_profiles_edit_screen(self):
        """
        Verify current screen is sender profiles edit screen via:
            - Title
            - Cancel button
        """
        self.driver.wait_for_object("sender_profiles_title", timeout=20)
        self.driver.wait_for_object("sender_profile_cancel_btn")
    
    def verify_edit_sender_profile_screen(self):
        """
        Verify current screen is edit sender profile screen via:
            - Title
            - Delete button
        """
        self.driver.wait_for_object("edit_sender_profiles_title", timeout=20)
        self.driver.wait_for_object("edit_sender_profile_delete_btn")
    
    def verify_empty_contact_screen(self, raise_e=True):
        """
        Verify current screen is empty contacts screen via:
         - verify empty message
        :param is_empty
        """
        return self.driver.wait_for_object("empty_contact_message", raise_e=raise_e)
    
    def verify_contact_screen(self):
        """
        Verify current screen contacts screen via:
         - Title
         - Add a Contact button
        """
        self.driver.wait_for_object("contacts_title")
        self.driver.wait_for_object("create_a_contact_btn")
    
    def verify_contact_edit_screen(self):
        """
        Verify current screen is contact edit screen via:
            - Title
            - Cancel button
        """
        self.driver.wait_for_object("contacts_title")
        self.driver.wait_for_object("contact_cancel_btn")
    
    def verify_edit_contact_screen(self):
        """
        Verify current screen is edit contact screen via:
            - Title: Edit Contact
            - Delete button
        """
        self.driver.wait_for_object("edit_contact_title")
        self.driver.wait_for_object("contact_delete_btn")