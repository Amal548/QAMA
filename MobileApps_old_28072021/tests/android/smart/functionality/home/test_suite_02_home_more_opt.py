from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Home_More_Opt(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.about = cls.fc.flow[FLOW_NAMES.ABOUT]

    def test_01_home_nav_opt_menu_btn(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots icon on Home top navigation bar
        Expected Result:
         2. Verify More Option screen with below check points:
            + App Settings
            + Help Center
            + About
            + Debug Settings
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options()
        self.home.verify_more_options()

    def test_02_home_more_opt_app_settings(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots icon on Home top navigation bar
         3. Click on App Settings button
        Expected Result:
         3. Verify App Settings screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_app_settings()
        self.app_settings.verify_app_settings()

    def test_03_home_more_opt_help_center(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on Help Center button
        Expected Result:
         3. Verify Help Center screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_help_center()
        self.app_settings.verify_help_support_screen()

    def test_04_home_more_opt_about(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on About button
        Expected Result:
         3. Verify About screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_about()
        self.about.verify_about_screen()
        