import os
import pytest
import logging

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.microsoft_excel.microsoft_excel import MicrosoftExcel
from selenium.common.exceptions import NoSuchElementException


pytest.app_info = "MICROSOFT_EXCEL"

class Test_Suite_HPPS_microsoft_excel(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        self.excel = MicrosoftExcel(self.driver)
        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']


    def test_01_microsoft_excel_system_ui(self):
        self.excel.open_excel()
        self.excel.verify_home_screen()
        self.excel.look_for_excel_file_and_select()
        self.excel.select_3_dot_button()
        self.excel.select_print_in_3_dot_menu()
        self.excel.select_print_in_print_options()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type="document")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)