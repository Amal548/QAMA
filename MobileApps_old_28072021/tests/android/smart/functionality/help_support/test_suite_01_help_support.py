import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES

pytest.app_info = "SMART"


class Test_Suite_01_Help_Support(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]

    def test_01_help_support_via_tile(self):
        """
        Descriptions:
            1. Launch app to Home screen (should use app.reset so that there is no connected printer)
            2. Click on 'Get HP Help and Support' tile
        Expected Result:
            2. Online Help Support display
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.HELP_SUPPORT), is_permission=False)
        if self.app_settings.verify_accept_cookies_popup(raise_e=False):
            self.app_settings.dismiss_accept_cookies_popup()
        self.google_chrome.handle_welcome_screen_if_present()
        self.app_settings.verify_help_support_screen()

    @pytest.mark.capture_screen
    def test_02_help_support_via_more_option_help_center(self):
        """
        Descriptions:
            1. Launch app to Home screen (should use app.reset so that there is no connected printer)
            2. Click on 'Help Center' on More Option menu
        Expected Result:
            2. Online Help Support display
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_help_center()
        if self.app_settings.verify_accept_cookies_popup(raise_e=False):
            self.app_settings.dismiss_accept_cookies_popup()
        self.app_settings.verify_help_support_screen()
