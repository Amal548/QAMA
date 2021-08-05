from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_GA_Copy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.hpps = cls.fc.flow[FLOW_NAMES.HPPS]
        cls.copy = cls.fc.flow[FLOW_NAMES.COPY]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress

    def test_01_ga_copy(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from search icon)
        - Verify Home Screen with printer connected
        - Click on digital_copy Tile on Home screen
        - Verify Permission allow screen
        - Click on Allow button
        - Verify No Camera Access screen
        - Click on ALL ACCESS button
        - Verify HP Smart to take picture permission screen
        - Click on Allow button
        - Verify digital_copy screen
        - Click on Flash button
        - Click on Capture button
        - Verify digital_copy preview screen
        - Click on Resize button
        - Choose Fit to Page
        - Click on Copies
        - Choose 2 copies
        - Click on Add new page button
        - Verify digital_copy screen
        - Click on Capture button
        - Verify digital_copy preview screen
        - Click on Start Black button
        - Click on Skip button
        - Verify Permission allow screen
        - Click on Allow button
        - Close the App
        """
        self.driver.wdvr.start_activity(PACKAGE.SMART, LAUNCH_ACTIVITY.SMART)
        self.home.verify_add_new_printer()
        self.home.__verify_all_tiles_ga()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_printer(self.printer_ip, wifi_direct=False)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.__verify_all_tiles_ga()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.COPY), is_permission=False)
        self.home.check_run_time_permission_photo_ga()

        self.camera_scan.verify_capture_no_access_screen(is_camera=True)
        self.camera_scan.select_camera_access_allow(is_camera=True)
        self.camera_scan.verify_camera_permission_access_screen()
        self.camera_scan.select_camera_permission_allow_btn()
        self.camera_scan.verify_capture_screen(from_camera=True)

        # Design for the second testing cases to GA Dashboard
        self.copy.select_flash_btn()
        self.copy.select_paper_size(paper_size_type=self.copy.PAPER_SIZE_LETTER)
        self.camera_scan.capture_photo(ga=True)
        self.copy.verify_capture_successful()
        self.copy.verify_copy_preview_screen()

        # Design for the third testing cases to GA Dashboard
        self.copy.select_resize_type(resize_type=self.copy.FIT_TO_PAGE)
        self.copy.select_copies_btn(copies_num=2)

        # Design for the event click on add more page button, don't need for GA dashboard
        self.copy.select_add_btn()
        self.camera_scan.verify_capture_screen(from_camera=True)
        self.camera_scan.capture_photo(ga=False)
        self.copy.verify_copy_preview_screen()

        self.copy.select_black_copy_btn()
        self.copy.select_ok_btn()

        self.hpps.agree_and_accept_terms_and_condition_if_present()
        self.hpps.check_run_time_permission(ga=True)