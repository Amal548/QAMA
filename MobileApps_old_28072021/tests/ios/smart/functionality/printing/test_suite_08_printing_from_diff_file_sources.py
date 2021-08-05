import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"


class Test_Suite_08_Printing_From_Diff_File_Sources(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")

        # Printer variables
        cls.fc.go_home(stack=cls.stack)
        cls.fc.add_printer_by_ip(cls.p.get_printer_information()["ip address"])

    def test_01_verify_printing_from_print_documents_tile(self):
        """
        verify_printing_from_print_documents- C24720494
        :return:
        """
        # General Setup
        file_name= "test_pdf_file"
        self.fc.scan_and_save_file_in_hp_smart_files(self.p, file_name)
        self.fc.select_a_file_and_go_to_print_preview(file_name)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_02_verify_printing_from_print_photos_tile(self):
        """
        verify_printing_from_print_photos- C24720502
        :return:
        """
        # General Setup
        self.fc.select_multiple_photos_to_preview(select_tile=True, no_of_photos=1)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_03_verify_printing_from_camera_scan_tile(self):
        """
        verify_printing_from_print_photos- C24720503
        :return:
        """
        # General Setup
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.multiple_manual_camera_capture(1)
        self.fc.select_print_button_and_verify_print_job(self.p)

    def test_04_verify_printing_from_print_scan_tile(self):
        """
        verify_printing_from_print_photos- C24720504
        :return:
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.select_print_button_and_verify_print_job(self.p)




