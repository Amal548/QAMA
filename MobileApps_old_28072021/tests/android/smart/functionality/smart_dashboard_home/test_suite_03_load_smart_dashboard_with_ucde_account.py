from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *


pytest.app_info = "SMART"

class Test_Suite_03_Load_Smart_Dashboard_With_Ucde_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]

        # Define the variable
        cls.fc.set_hpid_account("ucde", True, False)

    def test_01_load_smart_dashboard_by_ucde_account(self):
        """
        Description:
          1. Load to Home screen with an UCDE account
          2. Click on Account button on navigation bar of Home screen

        Expected Result:
          3. Verify Account Profile screen
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_smart_dashboard()

    def test_02_toggle_menu(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an UCDE account
          2. Click on Toggle Menu button on Smart Dashboard screen

        Expected Result:
          2. Verify Smart Dashboard menu screenw with:
             + Home button is invisible
             + HP + Print Plans item
             + Printers item
             + Users item
             + Features item
             + Account item
             + Help Center item
             + Chat with Virtual Agent item
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_menu_toggle()
        self.hp_connect.verify_smart_dashboard_menu_screen(timeout=15, invisible=True)

    @pytest.mark.parametrize("btn", ["cancel_btn", "start_chat_btn"])
    def test_03_virtual_agent(self, btn):
        """
        Description:
          1. Load to Smart Dashboard screen with an UCDE account
          2. Click on Virtual Agent button on Smart Dashboard screen
          3. If btn == "cancel_btn", Click on Cancel button
             If btn == "start_chat_btn", Click on Start Chat button

        Expected Result:
          2. Verify Virtual Agent screen through:
          - Cancel button
          - Start Chat button
          3. If btn == "cancel_btn", verify Account Dashboard screen
             If btn == "start_chat_btn", verify start chat page
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.select_chat_with_virtual_agent()
        self.hp_connect.verify_virtual_chat_popup(timeout=20)
        if btn == "cancel_btn":
            self.hp_connect.select_virtual_agent_cancel()
            self.hp_connect.verify_account_profile_screen()
        else:
            self.hp_connect.select_start_chat()
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"