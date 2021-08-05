from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_02_Camera_Scan_With_Smart_Advance_Feature(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        # Define the variable
        cls.fc.set_hpid_account("hp+", True, False)

    def test_01_camera_scan_screen(self):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar

        Expected Results:
        2. Verify Camera scan slider menu with below option:
        """
        self.fc.reset_app()
        self.__load_camera_capture_screen()
        self.camera_scan.verify_slider_button_on_capture_screen(self.camera_scan.MULTI_ITEM_MODE)
        self.camera_scan.verify_slider_button_on_capture_screen(self.camera_scan.BOOK_MODE)

    def test_02_top_bar_menu(self):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button

        Expected Results:
        3. Verify top bar menu on Camera scan screen with:
           + Settings button
           + X button
           + Flash button
        """
        self.__load_camera_capture_screen()
        self.camera_scan.verify_top_bar_menu_on_capture_screen(invisible=False)

    @pytest.mark.parametrize("btn_name", ["x_btn", "settings_btn"])
    def test_03_camera_scan_top_menu_button(self, btn_name):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. btn_name == x_btn: Click on X button
           btn_name == settings_btn: Click on Settings button

        Expected Results:
        4. btn_name == x_btn: App will go to Home screen
           btn_name == settings_btn: Verify Preference screen with option:
            + Title
            + Auto-Enhancements item
            + Auto-Heal item
            + Auto-Orientation item
            + Flatten Book Pages item
        """
        self.__load_camera_capture_screen()
        if btn_name == "x_btn":
            self.camera_scan.select_x_button()
            self.home.verify_home_nav()
        else:
            self.camera_scan.select_settings_button()
            self.camera_scan.verify_preference_screen()

    def test_04_camera_scan_auto_option(self):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. Click on Batch mode
        5. Click on Photo mode

        Expected Results:
        3. Auto option displays on screen
        4. Auto option displays on screen
        5. Auto option displays on screen
        """
        self.__load_camera_capture_screen()
        self.camera_scan.select_capture_mode(self.camera_scan.PHOTO_MODE)
        self.camera_scan.verify_top_bar_menu_on_capture_screen(invisible=False)
        self.camera_scan.select_capture_mode(self.camera_scan.BATCH_MODE)
        self.camera_scan.verify_top_bar_menu_on_capture_screen(invisible=False)

    @pytest.mark.parametrize("capture_mode", ["photo", "document"])
    def test_05_camera_scan_with_photo_mode(self, capture_mode):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. Click on Photo mode when capture mode == photo
           Or click on Document mode when capture mode == document
        5. Click on Capture button
        6. Click on Next button

        Expected Results:
        6. Verify Preview screen with:
           + Title
           + Print / Share / Shortcuts /Save / Fax button
        """
        capture_modes = {
            "photo": self.camera_scan.PHOTO_MODE,
            "document": self.camera_scan.DOCUMENT_MODE
        }
        self.__load_camera_capture_screen()
        self.camera_scan.capture_photo(mode=capture_modes[capture_mode], number_pages=1, manual=True)
        self.camera_scan.verify_camera_adjust_screen()
        self.camera_scan.select_adjust_next_btn()
        self.preview.verify_preview_nav()

    def test_06_camera_scan_replace_option(self):
        """
        Description:
        1. Install and Launch app with an hp+ account login
        2. Click on Camera Scan icon from navigation button bar
        3. Click on Allow Access button
        4. Click on Batch mode
        5. Click on capture button
        6. Click on Next button
        7. Click on 3 dots icon -> Replace button

        Expected Results:
        7. App go back to Camera screen with Auto option displays
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages()
        self.preview.verify_preview_nav()
        self.preview.select_preview_image_opts_btn(self.preview.REPLACE_BTN)
        self.camera_scan.verify_top_bar_menu_on_capture_screen(invisible=False)

    # ---------------     PRIVATE FUNCTIONS     ----------------------
    def __load_camera_capture_screen(self):
        """
        1. Click on Camera Scan tile on Home screen
        2. Allow Access to camera
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        if self.camera_scan.verify_capture_no_access_screen(raise_e=False):
            self.camera_scan.select_camera_access_allow()
            self.camera_scan.check_run_time_permission()
        self.camera_scan.verify_capture_screen()