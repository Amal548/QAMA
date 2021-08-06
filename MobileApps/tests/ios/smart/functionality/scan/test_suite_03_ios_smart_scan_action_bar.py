import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_03_Ios_Smart_Scan_Action_Bar(object):
    
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")
    
    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])

    def test_01_verify_scan_pop_up_printer_scan_tile(self):
        """
         Verify scan pop up after fresh app install- Printer scan tile- C27655112
        """
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fc.fd["camera"].verify_adjust_scan_coach_mark() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        assert self.fc.fd["scan"].verify_scanner_or_camera_popup_displayed(popup=True) is False
        self.fc.fd["scan"].select_close()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        assert self.fc.fd["scan"].verify_scanner_or_camera_popup_displayed(popup=True) is False
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].select_close()

    def test_02_verify_scan_pop_up_camera_tile(self):
        """
         Verify scan pop up after fresh app install Camera tile- C27655113
        """
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fc.fd["camera"].verify_adjust_scan_coach_mark() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["scan"].select_close()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        assert self.fc.fd["scan"].verify_scanner_or_camera_popup_displayed(popup=True) is False
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["scan"].select_close()

    def test_03_verify_last_selected_scan_source_preserved_scanner(self):
        """
         Verify last selected scan source is preserved - C27655115
        """
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].select_scanner_option()
        self.fc.fd["scan"].select_close()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].select_scan_icon()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["scan"].verify_scanner_screen()
        self.fc.fd["scan"].select_close()
    
    def test_04_verify_last_selected_scan_source_preserved_camera(self):
        """
         Verify last selected scan source is preserved - C27655115
         Similar test case as above when source selected is camera
        """
        self.fc.fd["home"].verify_rootbar_scan_icon()
        self.fc.fd["home"].select_scan_icon()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["scan"].select_close()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].select_scan_icon()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["scan"].select_close()




