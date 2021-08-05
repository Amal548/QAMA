import pytest
import SPL.driver.driver_factory as p_driver_factory

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_suite_01_ios_smart_scan_from_printer_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        cls.fc.go_home(verify_ga=True)

    def test_01_scan_max_ga(self):


        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["home"].select_scan_icon()
        self.fc.fd["scan"].select_scanner_if_first_time_popup_visible()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].select_scan_job_with_cancel_for_ga()
        self.fc.fd["scan"].verify_top_left_knob_on_scan_screen()
        self.fc.fd["scan"].select_scan_settings_wheel()
        self.fc.fd["scan"].verify_scan_settings_screen()
        self.fc.fd["scan"].select_scan_settings_by_type_and_value(SCAN_SETTINGS.INPUT_TYPE, SCAN_INPUT_TYPE.DOCUMENT)
        self.fc.fd["scan"].select_scan_settings_by_type_and_value(SCAN_SETTINGS.QUALITY, SCAN_QUALITY.DRAFT)
        self.fc.fd["scan"].select_scan_settings_by_type_and_value(SCAN_SETTINGS.INPUT_SOURCE, SCAN_INPUT_SOURCE.SCANNER_GLASS)
        self.fc.fd["scan"].select_scan_settings_by_type_and_value(SCAN_SETTINGS.COLOR, SCAN_COLOR.GRAYSCALE)
        self.fc.fd["scan"].select_done()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].select_scan_job()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["scan_edit"].select_scan_editing_for_rotate_and_crop(rotate_value=SCAN_EDIT_ROTATE.LEFT, crop_value=SCAN_EDIT_CROP.A4)
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].handle_share_preview_screen()
        self.fc.fd["preview"].select_file_converting_format(PREVIEW_FILE_TYPE.PDF)

        # TODO: Save to hp smart,,, then do action and add ga on that event (appium limitation to click on save button)
        # self.fc.fd["preview"].select_save_icon_on_preview()
        # self.fc.fd["preview"].select_save_to_hp_smart_btn()
        # self.fc.fd["preview"].verify_success_screen_for_save_print_share()

        # Cleaning steps
        self.fc.fd["scan"].select_back()
        self.fc.fd["scan"].verify_preview_navigate_back_popup()
        self.fc.fd["scan"].select_no_button_to_scanner_screen()

    def test_02_scan_edit_ga_coverage_flow_1(self):


        self.fc.fd["scan"].select_preview_on_scanner_screen()
        self.fc.fd["scan"].verify_scanning_screen()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].verify_top_left_knob_on_scan_screen()
        self.fc.fd["scan"].select_scan_job()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].select_scan_job()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["scan_edit"].select_arrange_pages_in_edit_for_ga()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].handle_share_preview_screen()
        self.fc.fd["preview"].rename_scanned_file()
        self.fc.fd["preview"].select_delete_pages_in_current_job()

        # TODO:Share to mail or some,then do action and add ga on that event(appium limitation to click on share button)
        # self.fc.fd["preview"].select_share_icon_on_preview()
        # self.fc.fd["preview"].select_share_to_???()
        # self.fc.fd["preview"].verify_success_screen_for_save_print_share()