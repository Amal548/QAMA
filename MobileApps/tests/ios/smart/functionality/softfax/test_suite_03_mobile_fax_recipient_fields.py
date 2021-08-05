import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_03_Mobile_Fax_Recipient_Fields(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.recipient_phone = cls.fc.recipient_info_for_os()["phone"]
        # self.recipient_info["phone"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.contacts = cls.fc.fd["softfax_contacts"]
        cls.fc.go_home(stack=cls.stack, create_account=True)
        cls.fc.nav_to_compose_fax(new_user=True)
        cls.name1 = 'test1' + cls.fc.get_random_str()
        cls.name2 = 'test2' + cls.fc.get_random_str()

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        if self.compose_fax.verify_compose_fax_screen(raise_e=False) is False:
            self.fc.nav_to_compose_fax(stack=self.stack)
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)

    def test_01_validate_recipient_phone_default(self):
        """
        Load Compose fax screen, validate recipient phone number field with
        default/empty values - C16932524
        """
        self.compose_fax.enter_recipient_information('', name='a')
        assert self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=False,
                                                                raise_e=False) is not False

    @pytest.mark.parametrize("value_type", ["short", "long"])
    def test_02_validate_recipient_phone_with_diff_values(self, value_type):
        """
        Load Compose fax screen, validate recipient phone number field with
        short and long value  -- C13927760, C24628883
        """
        phone_no = {"short": "1234", "long": "123456789012345"}
        self.compose_fax.enter_recipient_information(phone_no[value_type], name='a')
        assert self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG,
                                                                is_sender=False, raise_e=False) is not False
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)

    def test_03_save_this_contact(self):
        """
        Enter Fax Number and Name under To section and save - C24829088
        """
        self.compose_fax.enter_recipient_information(self.recipient_phone, self.name1)
        self.compose_fax.verify_save_this_contact_btn()
        self.compose_fax.click_save_this_contact_btn()
        self.compose_fax.verify_save_this_contact_btn(invisible=True, raise_e=True)
        self.compose_fax.verify_saved_btn()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)

    def test_04_send_fax_using_saved_contact(self):
        """
        Send fax by selected saved contact and verify fax sent successfully - C19440586
        """
        self.check_and_add_contact(self.recipient_phone, self.name1)
        self.contacts.verify_and_select_saved_contact(self.recipient_phone, self.name1, select_contact=True)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_my_photos()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        # # Long timeout is to verify fax sent screen
        self.send_fax_details.verify_send_fax_status(timeout=600)

    def test_05_add_invalid_contact(self):
        """
        Navigate to contacts screen, add an invalid contact and
        verify invalid format message - C24829087
        """
        self.fc.nav_to_contacts_screen()
        self.contacts.click_add()
        self.contacts.verify_phone_invalidation_message(1234567890123, 'inavlid_format')

    def test_06_add_valid_contact(self):
        """
        Navigate to contacts screen and add a valid contact and
        verify contact added to saved tab - C16932534
        """
        self.check_and_add_contact(self.recipient_phone, self.name2)
        self.contacts.verify_contacts_screen()
        self.contacts.click_tab_btn_native(self.contacts.SAVED_TAB_BTN)
        assert self.contacts.verify_and_select_saved_contact(self.recipient_phone, self.name2) is not False

    def test_07_edit_saved_contact(self):
        """
        Navigate to contacts screen-> Saved Tab , open saved contact, edit and save and
        verify contact updated - C24829089, C24829091
        """
        self.check_and_add_contact(self.recipient_phone, self.name1)
        self.contacts.verify_and_select_saved_contact(self.recipient_phone, self.name1, select_info=True)
        self.contacts.verify_edit_contact_screen()
        self.contacts.clear_edit_contact_text()
        code, updated_phone, updated_name = self.contacts.add_edit_contact('(229) 226-2811',
                                                                           "{}_updated".format(self.name1), is_new=False)
        assert self.contacts.verify_and_select_saved_contact(updated_phone, updated_name) is not False

    def test_08_verify_send_fax_with_no_info(self):
        """
        Send fax with no information entered - C24628885, C16932539, C16932578
        """
        self.compose_fax.click_send_fax_native_btn(change_check=False)
        assert self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG,
                                                                raise_e=False) is not False
        self.compose_fax.enter_recipient_information(phone_no='8769099876', name='a')
        assert self.compose_fax.verify_sender_name_error_message(raise_e=False) is not False
        assert self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=True,
                                                                raise_e=False) is not False

    def test_09_verify_delete_from_saved_tab(self):
        self.check_and_add_contact(self.recipient_phone, self.name2)
        self.contacts.verify_and_select_saved_contact(self.recipient_phone, self.name2, select_info=True)
        self.fc.delete_contact()
        assert self.contacts.verify_and_select_saved_contact(self.recipient_phone, self.name2) is False

    def check_and_add_contact(self, phone, name):
        self.fc.nav_to_contacts_screen()
        self.contacts.click_tab_btn_native(self.contacts.SAVED_TAB_BTN)
        if self.contacts.verify_and_select_saved_contact(phone, name) is False:
            self.contacts.click_add()
            self.contacts.add_edit_contact(phone, name)