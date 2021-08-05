import os, random
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.hpps.flow_container import Flow_Container
from MobileApps.libs.flows.android.wprint_test.wprint_test import WPrintTest

pytest.app_info="WPRINT_TEST"

class Test_Suite_HPPS_sent_multiple_print_jobs(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        # Apps instantiation
        self.wprint_test = WPrintTest(self.driver)

        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()

        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']

    def test_01_cancel_pdf_print_job_sent_from_system_ui(self):
        """
            Test cases covered: C77943, C77944, C77945, C77946, C77947, C77948

            Only 1 test case needed based on development team request
        """      
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_document_via_print_system()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui("document")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p, cancel_job=True)

    def test_02_cancel_image_print_job_from_trapdoor(self):
        """
            Test cases covered: C77950

            Only 1 test case needed based on development team request
        """
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_photo_via_backdoor()

        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.set_printer_options_in_trap_door(file_type="image")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.select_print_and_verify_results_for_trapdoor(self.p, self.printer_bonjour_name, jobs=1, cancel_job=True)
