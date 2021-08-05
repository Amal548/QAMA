from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Load_Smart_Dashboard_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.hp_connect_account = cls.fc.flow[FLOW_NAMES.HP_CONNECT_ACCOUNT]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.fc.flow_home_smart_dashboard_account_menu()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_account_profile(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Account Profile button

        Expected Result:
          5. Verify Account Profile screen
        """
        self.hp_connect_account.click_account_profile_btn()
        self.hp_connect.verify_account_profile_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_view_notifications(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on View Notifications button

        Expected Result:
          5. Verify View Notification screen
        """
        self.hp_connect_account.click_view_notifications_btn()
        self.hp_connect_account.verify_view_notifications_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_03_notification_settings(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Notification Settings button

        Expected Result:
          5. Verify Notification Settings screen
        """
        self.hp_connect_account.click_notification_settings_btn()
        self.hp_connect_account.verify_notification_settings_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_04_privacy_settings(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Privacy Settings button

        Expected Result:
          5. Verify Privacy Settings screen
        """
        self.hp_connect_account.click_privacy_settings_btn()
        self.hp_connect_account.verify_privacy_settings_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_05_billing_info(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Billing button

        Expected Result:
          5. Verify Billing screen
        """
        self.hp_connect_account.click_billing_btn()
        self.hp_connect_account.verify_billing_screen()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_06_shipping(self, account_type):
        """
        Description:
          1. Load to Home screen with hp plus account
          2. Click on Account button on navigation bar of Home screen
          3. Click on More option
          4. Click on Account button
          5. Click on Shipping button

        Expected Result:
          5. Verify Shipping screen
        """
        self.hp_connect_account.click_shipping_btn()
        self.hp_connect_account.verify_shipping_screen()