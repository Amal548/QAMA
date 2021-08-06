import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_08_Contacts(object):

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
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.contacts = cls.fc.fd["softfax_contacts"]
        cls.name = 'test' + cls.fc.get_random_str()
        cls.name1 = 'update' + cls.fc.get_random_str()
        cls.fc.go_home(stack=cls.stack, button_index=2)
        cls.email, cls.password = cls.fc.create_account_from_homepage()
        cls.fc.nav_to_compose_fax(new_user=True)

    def test_01_verify_empty_contacts_screen(self):
        """
        Verify contacts screen with no contacts - C24829085
        """
        self.fc.nav_to_contacts_screen()
        assert self.contacts.verify_empty_contact_list(is_saved=False, raise_e=False) is not False
        assert self.contacts.verify_add_btn() is not False
        self.contacts.click_tab_btn_native(self.contacts.SAVED_TAB_BTN)
        assert self.contacts.verify_empty_contact_list(raise_e=False) is not False
        assert self.contacts.verify_add_btn() is not False


