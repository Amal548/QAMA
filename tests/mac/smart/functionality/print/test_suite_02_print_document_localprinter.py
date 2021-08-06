#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case to test function -- print document with local printer.

@author: Sophia
@create_date: June 17, 2019
'''
import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.printfile.print_screen import PrintScreen


pytest.app_info = "DESKTOP"


class Test_Suite_02_Print_Document_Localprinter(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.appname = smart_const.APP_NAME.SMART
        self.printer_name = "HP ENVY Photo 7800 series"
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [BADBAD]"
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET
        self.doc_name = ""
        self.customer_settings = {}

    def test_01_install_printer(self):
        '''
        This is a method to setup test precondition--install a printer.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printerBonjourName)

    def test_02_cancel_print_document(self):
        '''
        TestRail:#C
        This is a method to test cancel print job.
        '''
        logging.debug("Launch app with local printer to main UI... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_after_post_oobe(self.printer_type)

        logging.debug("Go to print dialog... ")
        self.doc_name = "Test.pdf"
        self.common_flows.go_to_print_document_dialog(self.doc_name)

        logging.debug("Check print dialog... ")
        print_screen = PrintScreen(self.driver)
        print_screen.verify_print_dialog_with_default_settings(self.printer_name)

        logging.debug("Print photo and cancel job... ")
        self.common_flows.cancel_print_job()

    def test_03_print_document_default_settings(self):
        logging.debug("Print document with default settings... ")

        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.DOCUMENT, self.doc_name)

    def test_04_print_document_customer_settings(self):
        logging.debug("Print document with customer settings... ")

        self.photo_name = "pikachu.png"
        self.customer_settings[smart_const.PRINT_SETTINGS.PRESETS] = 4
        self.customer_settings[smart_const.PRINT_SETTINGS.TWO_SIDE] = smart_const.CHECKBOX_VALUE.UNCHECK
        self.customer_settings[smart_const.PRINT_SETTINGS.PAPER_SIZE] = smart_const.PAPER_SIZE.X46
        self.customer_settings[smart_const.PRINT_SETTINGS.ORIENTATION] = smart_const.ORIENTATION.VERTICAL
        self.customer_settings[smart_const.PRINT_SETTINGS.POPUP_SECTION] = 2
        self.common_flows.print_file_using_customer_settings(smart_const.PRINT_TYPE.PHOTO, self.photo_name)

    def test_05_print_document_with_multiple_pages(self):
        logging.debug("Print document with multiple pages... ")

        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.DOCUMENT, self.doc_name)

    def test_06_print_document_with_password(self):
        logging.debug("Print document with password... ")

        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.DOCUMENT, self.doc_name)
