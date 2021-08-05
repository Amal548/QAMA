from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from selenium.common.exceptions import TimeoutException
import pytest

pytest.app_info = "SMART"

class Test_Suite_05_Scan_Unavailable(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        
        # Define variables
        cls.fc.set_hpid_account("hp+", claimable=True)

        cls.fc.reset_app()  # reset to make sure there are no printers
    
    def test_01_scan_feature_unavailable_from_tile(self):
        """
        C17225296
        Description:
            1/ Load Home Screen
            2/ Select "Printer Scan" tile
            3/ Dismiss "Feature Unavailable" popup
        Expected Result:
            "Feature Unavailable" popup appears and is dismissable
            Verify:
                1/ Feature Unavailable popup
                2/ Home screen is present after dismissing popup
        """
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        self.home.dismiss_feature_unavailable_popup()
        self.home.verify_home_nav()

    def test_02_scan_feature_unavailable_from_actionbar(self):
        """
        C17225296
        Description:
            1/ Load Home Screen
            2/ Select "Printer Scan" button on action bar
            3/ Dismiss "Feature Unavailable" popup
        Expected Result:
            "Feature Unavailable" popup appears and is dismissable
            Verify:
                1/ Feature Unavailable popup
                2/ Home screen is present after dismissing popup
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.home.dismiss_feature_unavailable_popup()
        self.home.verify_home_nav()
