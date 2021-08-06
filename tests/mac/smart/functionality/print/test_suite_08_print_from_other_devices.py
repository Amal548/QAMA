#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: It defines classes_and_methods

@author: Sophia
@create_date: Sep 12, 2019
'''

import pytest
import logging

import MobileApps.resources.const.mac.const as smart_const

from MobileApps.libs.flows.mac.smart.screens.printersettings.print_from_other_devices import PrinterFromOtherDevices


pytest.app_info = "DESKTOP"


class Test_Suite_04_Print_Photo_Remote(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        # Define variables
        self.appname = smart_const.APP_NAME.SMART

    def test_01_install_printer(self):
        '''
        This is a method to setup test precondition--install a printer.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_check_print_from_other_devices(self):
        '''
        TestRail:#
        This is a method to check printer from other device in the printer settings.
        '''
        logging.debug("Launch app with local printer to main UI... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_after_post_oobe(self.printer_type)

        logging.debug("Go to print other devices tab... ")
        self.common_flows.go_to_printer_from_other_devices_from_main_ui()

        printer_from_other_devices = PrinterFromOtherDevices(self.driver)
        printer_from_other_devices.click_send_link_btn()
        self.common_flows.close_HPSmart_app()