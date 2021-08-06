from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_01_Load_Smart_Dashboard_Features(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_connect_features = cls.fc.flow[FLOW_NAMES.HP_CONNECT_FEATURES]

        # Define the variable
        cls.fc.set_hpid_account("hp+", True, True)
        
    def test_01_print_anywhere(self):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Features button
          5. Click on Print Anywhere button

        Expected Result:
          4. Verify Print Anywhere screen
        """
        self.fc.flow_home_smart_dashboard_features_menu()
        self.hp_connect_features.click_print_anywhere_btn()
        self.hp_connect_features.verify_print_anywhere_screen()

    def test_02_other_solutions(self):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Features button
          5. Click on Other Features button

        Expected Result:
          5. Verify Other Features screen
        """
        self.fc.flow_home_smart_dashboard_features_menu()
        self.hp_connect_features.click_other_features_btn()
        self.hp_connect_features.verify_other_features_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_03_smart_security(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Features button
          5. Click on Smart security button

        Expected Result:
          5. Verify Privacy Settings screen
        """
        # Make sure the test won't get affected by previous test
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.fc.flow_home_smart_dashboard_features_menu()
        self.hp_connect_features.click_smart_security_btn()
        self.hp_connect_features.verify_smart_security_screen()