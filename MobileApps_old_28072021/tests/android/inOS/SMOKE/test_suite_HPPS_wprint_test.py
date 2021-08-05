import os
import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.wprint_test.wprint_test import WPrintTest

pytest.app_info = "WPRINT_TEST"
class Test_Suite_HPPS_wprint_test(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup
        self.sys_config = ma_misc.load_system_config_file()
        self.wprint_test = WPrintTest(self.driver)
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']


    def test_01_wprint_test_app_print_document_backdoor(self):
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_document_via_backdoor()
        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        # self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.set_printer_options_in_trap_door(file_type="document")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        #     self.fc.flow["trap_door"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_trapdoor(self.p,self.printer_bonjour_name)

    def test_02_wprint_test_app_print_photo_backdoor(self):
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_photo_via_backdoor()

        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        # self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.set_printer_options_in_trap_door(file_type="image")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        #     self.fc.flow["trap_door"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_trapdoor(self.p,self.printer_bonjour_name)

    def test_03_wprint_test_app_print_document_system_ui(self):
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
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    def test_04_wprint_test_app_print_photo_system_ui(self):
        self.wprint_test.open_wprint_test()
        self.wprint_test.select_print_photo_via_print_system()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui("image")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)



