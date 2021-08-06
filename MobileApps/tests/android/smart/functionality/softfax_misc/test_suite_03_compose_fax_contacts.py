import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA, GOOGLE_PHOTOS, WEBVIEW_CONTEXT

pytest.app_info = "SMART"


class Test_Suite_03_Compose_Fax_Contacts(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.contacts = cls.fc.flow[FLOW_NAMES.SOFTFAX_CONTACTS]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        # Define variables
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_empty_contacts_list(self):
        """
        Description:
            1/ Load Contacts screen with creating new hpid
            2/ Click on each tab and verify
        Expected Result:
            2/ Ech tab have empty list
        """
        self.__load_contacts_screen(check_onboarding=False)
        self.contacts.click_tab_btn(self.contacts.RECENT_TAB_BTN)
        self.contacts.verify_empty_contact_list(is_saved=False)
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_empty_contact_list(is_saved=True)

    def test_02_add_new_contact(self):
        """
        Description:
            1/ Load Contacts screen with login account
            2/ Click on Add button
            3/ Add new contact successfully
            4/ Click on Saved tab
        Expected Result:
            4/ Verify new contact on Saved list on Contacts screen.
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen(check_onboarding=False)
        self.__add_new_contact(self.recipient_phone, "test_02_{}".format(self.udid), self.recipient_code)
    
    def test_03_cancel_deleting_saved_contact(self):
        """
        Description:
            1/ Load Contacts screen with login account
            2/ Click on i icon of contact
            3/ Click on Delete button
            4/ Click on Cancel button
        Expected Result:
            2/ Verify Edit Contact screen
                - Edit Contact title
                - Delete button
            3/ Verify Are you sure? popup
            4/ Verify Edit Contact screen
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, "test_03_{}".format(self.udid), self.recipient_code)
        self.__load_edit_contact_screen("{} {}".format(self.recipient_code, self.recipient_phone), "test_03_{}".format(self.udid))
        self.contacts.click_edit_contact_delete()
        self.contacts.verify_edit_delete_confirmation_popup()
        self.contacts.dismiss_edit_delete_confirmation_popup(is_deleted=False)
        self.contacts.verify_edit_contact_screen()

    def test_04_delete_saved_contact(self):
        """
        Description:
            1/ Load Contacts screen with login hpid
            2/ Click on i icon of contact
            3/ Click on Delete button
            4/ Click on Delete button
            5/ Click on Saved tab
            6/ Verify contact on Saved tab
        Expected Result:
            2/ Verify Edit Contact screen
                - Edit Contact title
                - Delete button
            3/ Verify Are you sure? popup
            4/ Verify Contact screen
            6/ Empty list on Contacts screen/Saved tab
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen(check_onboarding=False)
        self.__add_new_contact(self.recipient_phone, "test_04_{}".format(self.udid), self.recipient_code)
        self.__load_edit_contact_screen("{} {}".format(self.recipient_code, self.recipient_phone), "test_04_{}".format(self.udid))
        self.contacts.click_edit_contact_delete()
        self.contacts.verify_edit_delete_confirmation_popup()
        self.contacts.dismiss_edit_delete_confirmation_popup(is_deleted=True)
        self.contacts.verify_contacts_screen()
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_contact(self.recipient_phone, "test_04_{}".format(self.udid), is_saved=True, invisible=True)

    def test_05_edit_saved_contact(self):
        """
        Description:
            1/ Load Contacts screen with log in hpid
            2/ Add new contact
            3/ Click on i icon of contact
            4/ Changing name
        Expected Result:
            2/ New contact on Saved list on Contacts screen
            4/ Updated contact replace for old one
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen()
        self.__add_new_contact(self.recipient_phone, "test_05_{}".format(self.udid), self.recipient_code)
        self.__load_edit_contact_screen("{} {}".format(self.recipient_code, self.recipient_phone), "test_05_{}".format(self.udid))
        self.contacts.add_edit_contact("(254) 572-5943", "{}_updated".format(self.udid), is_new=False)
        self.contacts.verify_contact(phone_number="(254) 572-5943", contact_name="{}_updated".format(self.udid), is_saved=True, invisible=False)
        self.contacts.verify_contact(self.recipient_phone, "test_05_{}".format(self.udid), is_saved=True, invisible=True)

    def test_06_send_fax_by_saved_contact(self):
        """
        Description:
            1/ Load Contacts screen with log in hpid
            2/ Add new contact
            3/ Select this contact for sending fax
            4/ enter valid sender information and adding a file
            5/ Click on Send Fax
        Expected Result:
            3/ Compose Fax screen display
            5/ Verify Send Fax Details screen
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen()
        phone, contact_name = self.__add_new_contact(self.recipient_phone, "test_06_{}".format(self.udid), self.recipient_code)
        self.contacts.select_saved_contact(phone, contact_name)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_album_photo_by_index(GOOGLE_PHOTOS.JPG)
        self.preview.select_next()
        self.compose_fax.verify_existed_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.verify_uploaded_file(timeout=60)
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_send_fax()
        self.send_fax_details.verify_send_fax_detail_screen()

    def test_07_add_new_contact_with_invalid_formart(self):
        """
        Description:
            1. Load Contacts screen with log in hpid
            2. Click on Add button
            3. Input invalid fax number & name
        Expected Result:
            3. Verify new contact on Saved list on Contacts screen.
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_contacts_screen()
        self.contacts.click_add()
        self.contacts.verify_phone_invalidation_message(1234567890123, self.test_07_add_new_contact_with_invalid_formart.__name__, is_new=True)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_contacts_screen(self, check_onboarding=True):
        """
        Load to Contacts screens:
            - Load Compose Fax screen
            - Click on person icon in To area
            - Verify Contacts screen as current screen
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=check_onboarding)
        self.compose_fax.click_contacts_icon()
        self.contacts.verify_contacts_screen()

    def __add_new_contact(self, phone, contact_name, code):
        """
        At Contacts screen, add a new contact
        :return contact phone and name
        """
        self.contacts.click_add()
        self.contacts.add_edit_contact(phone, contact_name, is_new=True)
        # phone, name = self.contacts.add_edit_contact(self.recipient_info["phone"], contact_name, is_new=True)
        self.contacts.verify_contacts_screen()
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.verify_contact(phone_number="{} {}".format(code, phone), contact_name=contact_name, is_saved=True)
        return "{} {}".format(code, phone),contact_name

    def __load_edit_contact_screen(self, phone_number, contact_name):
        """
        At Contacts/ Saved tab, load Edit Contact screen
        :param phone_number:
        :param contact_name:
        """
        self.contacts.click_tab_btn(self.contacts.SAVED_TAB_BTN)
        self.contacts.click_saved_contact_info(phone_number=phone_number, contact_name=contact_name)
        self.contacts.verify_edit_contact_screen()