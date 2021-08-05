import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_09_Mobile_Fax_From_Fields(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.fax_settings = cls.fc.fd["fax_settings"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.contacts = cls.fc.fd["softfax_contacts"]
        cls.fc.go_home(stack=cls.stack, button_index=1)
        cls.name1 = 'test1' + cls.fc.get_random_str()
        cls.name2 = 'test2' + cls.fc.get_random_str()
        cls.fc.nav_to_compose_fax()

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        if self.compose_fax.verify_compose_fax_screen(raise_e=False) is False:
            self.fc.nav_to_compose_fax(stack=self.stack)
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)

    @pytest.mark.parametrize("value_type", ["short", "long"])
    def test_01_validate_sender_phone_with_diff_values(self, value_type):
        """
        Load Compose fax screen, validate sender phone number field with
        short and long value  -- C13972853, C16977190
        """
        phone_no = {"short": "1234", "long": "123456789012345"}
        self.compose_fax.enter_sender_information('a', phone_no[value_type])
        assert self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG,
                                                                is_sender=True, raise_e=False) is not False

    def test_02_verify_add_optional_info_from_section(self):
        """
        Verify sender add optional information section and collapse btn-
                       C24829095, C24829096
        """
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_optional_info_btn()
        self.compose_fax.verify_organization_name()
        self.compose_fax.verify_email()
        self.compose_fax.verify_reply_fax_number()
        self.compose_fax.verify_collapse_btn()
        self.compose_fax.click_collapse_btn()
        assert self.compose_fax.verify_add_optional_info_btn(raise_e=False) is not False
        assert self.compose_fax.verify_collapse_btn(raise_e=False) is False
        assert self.compose_fax.verify_organization_name(raise_e=False) is False

    @pytest.mark.parametrize("save_option", ["cancel", "save"])
    def test_03_save_as_a_profile(self, save_option):
        """
        Verify Sender information save as profile sender Save and Cancel options
        C27725946, C27725953
        """
        sender_profile = self.compose_fax.get_sender_profile_label()
        # self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_CLEAR_FIELDS_BTN)
        if sender_profile is not False:
            self.delete_sender_profile(sender_profile)
            self.fc.nav_to_compose_fax()
        profile_name= "test_profile_"+self.fc.get_random_str()
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_save_as_profile_btn()
        self.compose_fax.verify_name_your_profile_screen()
        if save_option == "cancel":
            self.compose_fax.click_cancel_btn()
            assert self.compose_fax.verify_profile_label(raise_e=False) is False
        else:
            self.compose_fax.enter_profile_name(profile_name)
            self.compose_fax.click_save_btn()
            assert self.compose_fax.verify_profile_label(raise_e=False) is not False
            # clean up, delete saved profile
            self.delete_sender_profile(profile_name)

    def delete_sender_profile(self, profile_name):
        self.fc.nav_to_fax_settings_screen(self.fax_settings.SEND_PROFILES_OPT)
        self.fax_settings.select_single_sender_profiles(profile_name)
        self.fax_settings.verify_edit_sender_profile_screen()
        self.fax_settings.click_sender_profiles_delete_btn()
        self.fax_settings.dismiss_delete_confirmation_popup()