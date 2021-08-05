import logging
import pytest
import time
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_06_Printer_Scan_Enhancement(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        cls.scan = cls.fc.fd["scan"]

    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        cls.fc.go_home(reset=True,stack=cls.stack)
    
    def test_01_verify_all_scan_setting_options(self):
        """
        C28774684  - Scan Settings page
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_settings_wheel()
        self.scan.verify_array_of_elements(self.scan.SCAN_SETTINGS)
        #
        self.scan.verify_an_element_and_click(self.scan.QUALITY)
        self.scan.verify_an_element_and_click(SCAN_QUALITY.BEST, click=False)
        self.scan.verify_an_element_and_click(SCAN_QUALITY.DRAFT, click=False)
        self.scan.verify_an_element_and_click(SCAN_QUALITY.NORMAL, click=False)
        self.scan.select_navigate_back()
        self.scan.verify_an_element_and_click(self.scan.COLOR)
        self.scan.verify_an_element_and_click(SCAN_COLOR.COLOR, click=False)
        self.scan.verify_an_element_and_click(SCAN_COLOR.GRAYSCALE, click=False)
    
    def test_02_verify_transform(self):
        """
        C28868621 - "Transform" button on print preview (iOS only)
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.scan.select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.navigate_to_transform_screen()
    
    def test_03_verify_photo_n_document_scan(self):
        """
        C28761361
        """
        self.fc.go_scan_screen_from_home(self.p)
        for _ in range (0, 4):
            self.scan.select_scan_job_button()
            self.fc.fd["preview"].verify_detect_edges_screen()
            self.scan.select_navigate_back()
    
    def test_04_verify_replace_option(self):
        """
        C28761372 - Verify new Location and Style for "Add" button on Landing Page
        C28777186 - Verify Replace option from Landing page
        """
        self.fc.go_scan_screen_from_home(self.p)
        no_of_pages = 2
        self.fc.add_multi_pages_scan(no_of_pages)
        self.fc.fd["preview"].verify_an_element_and_click(self.fc.fd["preview"].DELETE_PAGE_ICON)
        self.fc.fd["preview"].verify_array_of_elements(self.fc.fd["preview"].PREVIEW_EDIT_OPTIONS)
        self.fc.fd["preview"].select_replace_btn_on_preview()
        # close coach marks
        if self.scan.verify_second_close_btn() is not False:
            self.scan.select_second_close_btn()
        self.scan.verify_scanner_screen()
    
    def test_05_verify_scan_coachmarks(self):
        """
        C28989778 - Coach Mark on printer scan
        C28991967 - Coach Mark 2-nd page
        C28991968 - Coach Mark 3-rd page
        C28991969 - Coach Mark 4-th page
        C28992224 - Verify "<" back button on coach mark
        C28991972 - Coach Mark shows up only 1 time
        C28991971 - Coach Mark (tapping anywhere on screen) behavior
        """
        self.fc.go_home(reset=True, stack=self.stack)
        p = self.p.get_printer_information()
        # Screen scrolled down on launch causing element not found.
        self.driver.scroll(HOME_TILES.TILE_INSTANT_INK, direction="up", scroll_object="tile_collection_view")
        if self.fc.fd["home"].verify_printer_added() is False:
            self.fc.add_printer_by_ip(printer_ip=p["ip address"])
            time.sleep(2)
        # close coach marks
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        assert self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_COACH_MARK, raise_e=False) is not False
        self.driver.click_by_coordinates(area="mm")
        self.fc.go_to_home_screen()
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK)
        self.scan.select_next_on_coachmark()
        self.scan.verify_coachmark_on_scan_page(self.scan.START_SCAN_COACHMARK)
        self.scan.select_navigate_back()
        self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK)
        for coachmark in self.scan.SCAN_COACH_MARKS:
            self.scan.verify_coachmark_on_scan_page(coachmark)
            self.scan.select_next_on_coachmark()
        self.scan.verify_scanner_screen()
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        assert self.scan.verify_coachmark_on_scan_page(self.scan.ADJUST_SCAN_CAPTURE_COACH_MARK, raise_e=False) is False
        assert self.scan.verify_coachmark_on_scan_page(self.scan.START_SCAN_COACHMARK, raise_e=False) is False 
        assert self.scan.verify_coachmark_on_scan_page(self.scan.SCAN_SOURCE_COACHMARK, raise_e=False) is False

    def test_06_verify_gear_btn_functionality(self):
        """
        C28761385 - Verify 'Gear' button functionality from top bar
        C28774732 - Printer Scan UI (Base user)
        """
        self.fc.go_scan_screen_from_home(self.p)
        if self.scan.verify_second_close_btn() is not False:
            self.scan.select_second_close_btn()
        self.scan.verify_an_element_and_click(self.scan.PHOTO_MODE, click=False, raise_e=True)
        self.scan.verify_an_element_and_click(self.scan.DOCUMENT_MODE, click=False, raise_e=True)
        self.scan.verify_an_element_and_click(self.scan.BATCH_MODE, click=False, raise_e=True)
        # Verify gear btn
        self.scan.select_gear_setting_btn()
        self.scan.verify_an_element_and_click(self.scan.AUTO_ENHANCEMENT_SWITCH, click=False)
        self.scan.verify_an_element_and_click(self.scan.AUTO_ORIENTATION_SWITCH, click=False)


