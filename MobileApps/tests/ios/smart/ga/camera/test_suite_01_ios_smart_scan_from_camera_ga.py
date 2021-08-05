import pytest
import SPL.driver.driver_factory as p_driver_factory

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_suite_01_ios_smart_scan_from_camera_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup, load_printers_session):

        cls = cls.__class__

        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        # cls.printer_ip = cls.p.p_obj.ipAddress
        cls.printer_info = cls.p.get_printer_information()

        # Printer variables
        cls.printer_ip = cls.printer_info['ip address']

        cls.fc.go_home(verify_ga=True)

    def test_01_scan_by_camera_max_ga(self):


        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_camera_screen_from_home()
        self.fc.fd["camera"].capture_manual_photo_by_camera()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["scan_edit"].select_scan_editing_for_rotate_and_crop(SCAN_EDIT_ROTATE.LEFT, SCAN_EDIT_CROP.A4)
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].handle_share_preview_screen()
        self.fc.fd["preview"].select_file_converting_format(PREVIEW_FILE_TYPE.PDF)
        self.fc.fd["preview"].select_save()
        # Clean up Steps
        self.fc.fd["scan"].select_back()
        self.fc.fd["scan"].verify_preview_navigate_back_popup()
        self.fc.fd["preview"].select_yes_btn()

    def test_02_scan_by_camera_print_edit_max_ga(self):

        self.fc.go_camera_screen_from_home()
        self.fc.fd["camera"].capture_manual_photo_by_camera()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["camera"].capture_manual_photo_by_camera()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["print_edit"].select_print_edit_options_for_ga(re_size=PRINT_EDIT_RESIZE_AND_MOVE.MANUAL)