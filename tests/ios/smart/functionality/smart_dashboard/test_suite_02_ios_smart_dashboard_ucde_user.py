import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_02_Ios_Smart_Dashboard_Ucde_User(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.account = ma_misc.get_hpid_account_info(stack=cls.stack, a_type="ucde")
    
    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, request):
        self.fc.go_home(reset=True, stack=self.stack, username=self.account["email"], password=self.account["password"])
        self.fc.navigate_to_smart_dashboard("ucde")
        self.fc.fd["hp_connect"].click_menu_toggle()


    def test_01_verify_hamburger_menu(self):
        """
        C28734590 - verify menu items for flex user
        """
        self.fc.fd["hp_connect"].verify_smart_dashboard_menu_screen(timeout=15, invisible=True)

    def test_02_chat_with_virtual_agent(self):
        """
        C28746932 - chat with virtual agent -> cancel
        TODO: C28746933 - chat with virtual agent -> start chat 
        """
        self.fc.fd["hp_connect"].verify_smart_dashboard_menu_screen(timeout=15, invisible=True)
        self.fc.fd["hp_connect"].select_chat_with_virtual_agent()
        self.fc.fd["hp_connect"].verify_virtual_chat_popup()
        self.fc.fd["hp_connect"].select_virtual_agent_cancel()
        self.fc.fd["hp_connect"].verify_account_profile_screen()
