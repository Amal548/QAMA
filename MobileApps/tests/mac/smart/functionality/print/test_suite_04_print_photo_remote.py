#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case to test function -- print photo with remote printer.

@author: Sophia
@create_date: Aug 15, 2019
'''

import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const


pytest.app_info = "DESKTOP"


class Test_Suite_04_Print_Photo_Remote(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        # Define variables
        self.appname = smart_const.APP_NAME.SMART
        self.printer_name = "HP ENVY Photo 7800 series"
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.printer_type = smart_const.OWS_TYPE.PALERMO_GEN2_INKJET

    def test_01_install_printer(self):
        '''
        This is a method to setup test precondition--install a printer.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_navigate_to_main_ui(self):
        '''
        TestRail:#
        This is a method to set up test precondition--choose remote printer in carousel.
        '''
        logging.debug("Launch app with remote printer to main UI... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_after_post_oobe(self.printer_type)

    def test_03_print_photo_default_settings(self):
        logging.debug("Print photo with default settings... ")

        self.common_flows.print_file_using_default_settings(smart_const.PRINT_TYPE.PHOTO, self.photo_name)
