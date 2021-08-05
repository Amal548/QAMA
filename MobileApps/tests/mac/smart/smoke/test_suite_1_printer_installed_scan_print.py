# encoding: utf-8
'''
Description: This is a smoke test for app. In the smoke test, it include install printer,
welcome flow, post OOBE flow, main UI checking, print flow and scan flow.

@author: Sophia
@create_date: May 6, 2019
'''
import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI

pytest.app_info = "DESKTOP"


class Test_Suite_1_Printer_Installed_Scan_Print(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        #self.printer = load_printers_session

        # Define variables
        self.appname = smart_const.APP_NAME.SMART
        self.printer_name = "HP ENVY Photo 7800 series"
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [784F07]"  # self.printer.get_printer_information()["bonjour name"]
        # self.printer_bonjour_name = "HP ENVY Photo 7800 series [BADBAD]"  # request.config.getoption("--printer_name")
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET
        self.doc_name = "Test.pdf"
        self.photo_name = "Tulips.jpg"

    def test_01_install_printer(self):
        '''
        TestRail:#C13220506
        This is a method to test printer installed.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_check_welcome(self):
        '''
        TestRail:#C12341702
        This is a method to check welcome flow.
        '''
        logging.debug("Start to check welcome workflow... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()

    def test_03_check_main_ui_with_printer(self):
        '''
        TestRail:#C13890709, #C13890710
        This is a method to check post OOBE flow and main UI screen.
        '''
        logging.debug("Start to check post OOBE workflow... ")
#       self.common_flows.go_to_main_ui_after_post_oobe(self.printer_type)
        self.common_flows.navigate_to_main_ui_skip_oobe_flow()

        logging.debug("Start to check main workflow with installed printer... ")
        main_screen = MainUI(self.driver)
        main_screen.verify_printer_name_main_ui(self.printer_name)

    def test_04_check_print(self):
        '''
        TestRail:#C12341708, #C12341709
        This is a method to check print document flow and print photo flow.
        '''
        logging.debug("Print documents with default settings... ")
        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.DOCUMENT, self.doc_name)

        logging.debug("Print photo with default settings... ")
        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.PHOTO, self.photo_name)

    def test_05_check_scan(self):
        '''
        TestRail:#C13227880
        This is a method to check scan flow.
        '''
        logging.debug("Scan file using scanner... ")
        self.common_flows.scanner_using_default_settings()
        self.common_flows.close_HPSmart_app()
