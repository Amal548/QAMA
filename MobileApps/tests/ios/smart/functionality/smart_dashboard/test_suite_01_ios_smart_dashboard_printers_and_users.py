import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Smart_Dashboard_Printers_and_Users(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def go_to_dashboard_menu(self, account_type):
        self.account = ma_misc.get_hpid_account_info(stack=self.stack, a_type=account_type)
        self.fc.go_home(reset=True, stack=self.stack, username=self.account["email"], password=self.account["password"])
        self.fc.navigate_to_smart_dashboard(account_type)

    @pytest.mark.parametrize("account_type",["hp+", "ucde"])
    def test_01_users_screen(self):
        """
        1. Load to Home screen with hp plus account or ucde account
        2. Click on Account button on navigation bar of Home screen
        3. Click on More option
        4. Click on Users button
        5. Verify Users screen
        """
        self.fc.fd["hp_connect"].click_menu_toggle()
        self.fc.fd["hpc_printers_users"].click_users_btn()
        self.fc.fd["hpc_printers_users"].verify_users_screen()

    @pytest.mark.parametrize("account_type",["hp+", "ucde"])
    def test_02_printers_screen(self):
        """
        1. Load to Home screen with hp plus account
        2. Click on Account button on navigation bar of Home screen
        3. Click on More option
        4. Click on Printers button
        5. Verify Printers screen
        """
        self.fc.fd["hp_connect"].click_menu_toggle()
        self.fc.fd["hpc_printers_users"].click_printers_btn()
        self.fc.fd["hpc_printers_users"].verify_printers_screen()
