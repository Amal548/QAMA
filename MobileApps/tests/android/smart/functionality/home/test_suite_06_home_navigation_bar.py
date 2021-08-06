from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_06_Home_Navigation_Bar(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]

    def test_01_home_nav_notification_btn(self):
        """
        Description:
         1. Load Home screen
         2. Click on notification button on Home top navigation bar
        Expected Results:
         2. Verify notification screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_notifications_icon()
        self.home.verify_notification_screen()

    def test_02_home_nav_scan_btn(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Click on scan button on Home bottom navigation bar
        Expected Results:
         2. Verify Scan screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_load_scan_screen(self.p, from_tile=False)

    def test_03_home_nav_capture_btn(self):
        """
        Description:
         1. Load Home screen
         2. Click on Capture button on Home bottom navigation bar
         3. Click on back button on notification screen
        Expected Results:
         2. Verify No Camera Access screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, is_permission=False)
        self.camera_scan.verify_capture_no_access_screen()

    def test_04_home_nav_view_print_btn(self):
        """
        Description:
         1. Load Home screen
         2. Click on View and Print button button on Home bottom navigation bar
        Expected Results:
         2. Verify Files and Photos screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN, is_permission=False)
        self.file_photos.verify_files_photos_screen()

    def test_05_home_nav_app_settings_btn(self):
        """
        Description:
         1. Load Home screen
         2. Click on View and Print button button on Home bottom navigation bar
        Expected Results:
         2. Verify Files and Photos screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN, is_permission=False)
        self.app_settings.verify_app_settings()