from time import sleep

import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer, logging
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_App_Background_Tests(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(printer_ip=cls.p.get_printer_information()["ip address"])

    def test_01_verify_print_with_app_background(self):
        """
        Verify print functionality backgrounding app multiple times
        AIOI-11620, Test Case-C28248769
        :return:
        """
        # General Setup
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.fc.fd["preview"].go_to_print_preview_pan_view()
        assert self.fc.fd["preview"].verify_button(Preview.PRINT) is not False
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        sleep(1)
        assert self.fc.fd["preview"].verify_button(Preview.PRINT) is not False
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        sleep(1)
        assert self.fc.fd["preview"].verify_button(Preview.PRINT) is not False
        # Validation
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_scan_with_app_background(self):
        """
        AIOI-11644, Verify scan functionality backgrounding app multiple times
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.add_multi_pages_scan(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.add_multi_pages_scan(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def test_03_verify_camera_scan_with_app_background(self):
        """
        AIOI-11644, Verify camera scan functionality backgrounding app multiple times
        """
        self.fc.go_camera_screen_from_home(self.p)
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].verify_home_tile(raise_e=True)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def test_04_verify_photo_save_with_app_background(self):
        """
        AIOI-11644, Verify share functionality with app backgrounding app multiple times
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        # Background app
        self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_BTN)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["preview"].rename_file("test_app_background")
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        sleep(1)
        # Background app
        self.fc.fd["ios_system"].launch_ios_settings()
        sleep(10)
        self.driver.launch_app(BUNDLE_ID.SMART)
        sleep(1)
        self.fc.fd["preview"].select_button(Preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["share"].verify_share_popup()
        self.fc.fd["share"].select_save_to_hp_smart()
        self.fc.go_hp_smart_files_screen_from_home()
        # Validate file saved with selected format
        self.fc.fd["files"].verify_file_name_exists("test_app_background.jpg")
        # Test clean up
        self.fc.go_hp_smart_files_and_delete_all_files()