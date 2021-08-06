#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Enable Print Anywhere(not signed in/claimed) flow

@author: ten
@create_date: Sep 17, 2019
'''

import pytest
import logging
import time


import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.printersettings.print_anywhere import Printer_Anywhere

pytest.app_info = "DESKTOP"


class test_Suite_05_Enable_Print_Anywhere_Not_Sign_In_Claimed_Flow(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.usename = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_install_printer(self):
        '''
        This is a method to test printer installed.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_go_to_enable_print_anywhere_flow(self):
        '''
        TestRail:#C14064611
        go to enable print anywhere flow.
        '''
        logging.debug("Go to Main UI ")
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

        logging.debug("Go to print anywhere screen")
        self.common_flows.go_to_print_anywhere_from_main_ui()

        logging.debug("sign in at anywhere screen")
        printer_anywhere = Printer_Anywhere(self.driver)
        self.common_flows.sign_in_hp_account_from_anywhere_screen(self.usename, self.password)
        printer_anywhere.wait_for_print_anywhere_enabled_load(60)

    def test_03_fail_to_enable_print_anywhere_flow(self):
        '''
        TestRail:#C14064620
        fail_to_enable_print_anywhere_flow
        '''
        logging.debug("click enable button")
        printer_anywhere = Printer_Anywhere(self.driver)
        printer_anywhere.click_enable_btn()
        printer_anywhere.wait_for_print_connected_another_account_screen_load(60)


