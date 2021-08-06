from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

class Test_Suite_04_Additional_Help_And_Support(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.fc.load_smart_dashboard_help_center_additional_help_and_support()
    
    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_print_anywhere_online_support(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Additional Help and Support item
          6. Click on Print Anywhere Online Support

        Expected Result:
          5. Verify Print Anywhere Online Support in a browser
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_ANYWHERE_ONLINE_SUPPORT)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_shortcuts_online_support(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Additional Help and Support item
          6. Click on Shortcuts Online Support button

        Expected Result:
          5. Verify Shortcuts Online Support in a browser
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SHORTCUTS_SUPPORT)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_03_hp_mobile_printing(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Additional Help and Support item
          6. Click on HP Mobile Printing button

        Expected Result:
          5. Verify HP Mobile Printing in a browser
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.HP_MOBILE_PRINTING)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"