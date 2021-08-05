from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_04_Fax_Settings_Contacts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]
        cls.contacts = cls.fc.flow[FLOW_NAMES.SOFTFAX_CONTACTS]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.udid = cls.driver.driver_info["desired"]["udid"]

    def test_01_empty_contacts(self):
        """
        Description:
            1. Load to Compose Fax with a new HPID account
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Contacts

        Expected Result:
            3. Verify Contacts empty screen with:
               - Title
               - Add a contact button
               - Empty contact message "You don't have any contacts"
        """
        self.__load_contacts_screen()
        self.fax_settings.verify_empty_contact_screen()
    
    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_02_delete_contacts(self, btn_name):
        """
        Description:
            1. Load to contacts screen with contacts list
            2. Click on Edit button
            3. Select a contact
            4. Click on Delete button
            5. If btn = "cancel", then click on Cancel button
               If btn = "delete", then click on Delete button

        Expected Result:
            4. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            5. If btn = "cancel", then verify Contacts edit screen
               If btn = "delete", then verify Contacts screen
        """
        self.__load_contacts_screen()
        phone, name = self.__add_new_contact("test_02_{}_{}".format(btn_name, self.udid))
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.contacts.select_saved_contact(phone, name)
        self.fax_settings.click_contact_delete_btn()
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_contact_edit_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_contact_screen()
            self.contacts.verify_contact(phone_number=phone, contact_name=name, invisible=True)
            
    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_03_delete_edit_contacts(self, btn_name):
        """
        Description:
            1. Load to Contacts screen with contacts list
            2. Select any contact
            3. Click on Delete button
            4. If btn = "cancel", then click on Cancel button
               If btn = "delete", then click on Delete button

        Expected Result:
            2. Verify Edit Contact screen
            3. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            4. If btn = "cancel", then verify Edit Contacts screen
               If btn = "delete", then verify Contacts screen
        """
        self.__load_contacts_screen()
        phone, name = self.__add_new_contact("test_03_{}_{}".format(btn_name, self.udid))
        self.contacts.select_saved_contact(phone, name)
        self.fax_settings.verify_edit_contact_screen()
        self.fax_settings.click_contact_delete_btn()
        if btn_name == "cancel":
            self.fax_settings.dismiss_edit_delete_confirmation(is_deleted=False)
            self.fax_settings.verify_edit_contact_screen()
        else:
            self.fax_settings.dismiss_edit_delete_confirmation(is_deleted=True)
            self.fax_settings.verify_contact_screen()
            self.contacts.verify_contact(phone_number=phone, contact_name=name, invisible=True)
    
    def test_04_create_a_contact(self):
        """
        Description:
            1. Load to Compose Fax with an new account
            2. Click on 3 dot menu/ Fax Settings
            3. Click Contacts
            4. Click on Add a Contact screen
            5. Add Fax Number and Name
            6. Click on Save button
            
        Expected Result:
            3. Verify Add Contact screen with:
               - Title: Title
               - Fax Number & Name fields
            6. Verify Contacts screen with contact saved success
        """
        self.__load_contacts_screen()
        self.__add_new_contact("test_04_{}".format(self.udid))
        
    def test_05_contacts_edit_cancel(self):
        """
        Description:
            1. Load to Compose Fax with HPID account login
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Contacts
            4. Click on Edit button
            5. Click on Cancel button

        Expected Result:
            3. Verify Contacts screen with:
               - Title
               - Contact Lists
            4. Verify Contacts Edit screen with:
               - Title
               - Cancel button
            5. Verify Contacts screen with:
               - Title
               - Contact Lists
        """
        self.__load_contacts_screen()
        self.__add_new_contact("test_05_{}".format(self.udid))
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_SELECT_BTN)
        self.fax_settings.verify_contact_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.CONTACT_CANCEL_BTN)
        self.fax_settings.verify_contact_screen()

    def test_06_edit_contacts_save(self):
        """
        Description:
            1. Load to Contacts screen with a new HPID account
            2. click any contact from the contacts list
            3. Update Fax number
            4. Click on Save button

        Expected Result:
            4. Verify Contacts save success
        """
        self.__load_contacts_screen()
        phone, name = self.__add_new_contact("test_06_{}".format(self.udid))
        self.contacts.select_saved_contact(phone, name)
        code, updated_phone, updated_name = self.contacts.add_edit_contact(phone[phone.find(" ") + 1:], "{}_updated".format(name), is_new=False)
        self.contacts.verify_contact(phone_number="{} {}".format(code, updated_phone), contact_name=updated_name, invisible=False)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_contacts_screen(self):
        """
        - Load Compose Fax screen with HPID account login or created a new HPID account
        - Click on Fax Settings on from More Option menu
        - Click on Contacts on Fax Settings screen
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()
        self.fax_settings.click_fax_settings_option(self.fax_settings.CONTACTS_OPT)
        self.fax_settings.verify_contact_screen()
    
    def __add_new_contact(self, contact_name):
        """
        At Contacts screen, add a new contact
        :return contact phone and name
        """
        self.fax_settings.click_add_a_contact_btn()
        code, phone, name = self.contacts.add_edit_contact(self.recipient_info["phone"], contact_name, is_new=True)
        self.fax_settings.verify_contact_screen()
        self.contacts.verify_contact(phone_number="{} {}".format(code, phone), contact_name=contact_name)
        return "{} {}".format(code, phone), name