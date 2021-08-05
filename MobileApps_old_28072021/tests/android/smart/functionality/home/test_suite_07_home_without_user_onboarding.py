from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT

pytest.app_info = "SMART"

class Test_Suite_07_Home_Without_User_Onboarding(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]

    @pytest.mark.parametrize("tile_name", ["print_photos", "print_docs", "scan", "camera_scan", "copy", "smart_tasks", "mobile_fax"])
    def test_01_tiles_without_user_onboarding(self, tile_name):
        """
        Description:
         1. Load Home screen without user onboarding account login
         2. Enable tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on tile on Home screen
        Expected Result:
         4. Verify OWS value prop screen with:
         
        """
        tiles_name = {"print_photos": TILE_NAMES.PRINT_PHOTOS,
                        "print_docs": TILE_NAMES.PRINT_DOCUMENTS,
                        "scan": TILE_NAMES.PRINTER_SCAN,
                        "camera_scan": TILE_NAMES.CAMERA_SCAN,
                        "copy": TILE_NAMES.COPY,
                        "smart_tasks": TILE_NAMES.SMART_TASKS,
                        "mobile_fax": TILE_NAMES.FAX}
        # Add clear cache here as there are multiple test suites on Home folder, and all test cases here require Smart app isn't logged into any HPID account
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        if tile_name == "copy" or tile_name == "scan":
            self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        if not self.home.verify_tile(self.home.get_text_from_str_id(tiles_name[tile_name]), raise_e=False):
            self.home.select_personalize_tiles()
            self.personalize.toggle_tile_by_name(self.personalize.get_text_from_str_id(tiles_name[tile_name]), on=True)
            self.personalize.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(tiles_name[tile_name]))
        # Currently HPID take 10-20s to load to value prop screen.
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True, timeout=20)
    
    def test_02_navigation_bar_without_user_onboarding(self):
        """
        Description:
         1. Load Home screen without user onboarding account login

        Expected Result:
         2. Below buttons are invisible on Home screen:
            - Printer Scan button
            - Camera Scan button
            - View & Print button
        """
        # Add clear cache here as there are multiple test suites on Home folder, and this test cases here require Smart app isn't logged into any HPID account
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN, invisible=True)