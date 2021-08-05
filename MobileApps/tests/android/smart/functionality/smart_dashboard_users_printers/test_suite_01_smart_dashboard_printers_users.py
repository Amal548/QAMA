from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_01_Load_Smart_Dashboard_Printers_Users(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_connect_printers_users = cls.fc.flow[FLOW_NAMES.HP_CONNECT_PRINTERS_USERS]

        # Define the variable
        cls.fc.set_hpid_account("hp+", True, True)

    def test_01_users_screen(self):
        """
        Description:
          1. Load to Home screen with hp plus account or ucde account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Users button

        Expected Result:
          4. Verify Users screen
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_menu_toggle()
        self.hp_connect_printers_users.click_users_btn()
        self.hp_connect_printers_users.verify_users_screen()
        
    @pytest.mark.parametrize("account_type",["hp+", "ucde"])
    def test_02_printers_screen(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Printers button

        Expected Result:
          4. Verify Printers screen
        """
        # Make sure the test won't get affected by previous test
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.hp_connect.click_menu_toggle()
        self.hp_connect_printers_users.click_printers_btn()
        self.hp_connect_printers_users.verify_printers_screen()