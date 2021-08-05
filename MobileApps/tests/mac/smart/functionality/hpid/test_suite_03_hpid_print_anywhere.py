#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Sign In/Sign Up/Sign Out testing from Print Anywhere screen.
Note: GEN2 device for testing
@author: Ivan
@create_date: Sep 25, 2019
'''

import logging
import pytest

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.printersettings.print_anywhere import Printer_Anywhere

pytest.app_info = "DESKTOP"


class Test_Suite_01_HPID_Print_Anywhere(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.appname = smart_const.APP_NAME.SMART
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.username = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_install_gen2_printer(self):
        '''
        Setup test precondition--install a printer.
        '''
        logging.debug("Install the instant ink printer")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

    def test_02_sign_in_via_print_anywhere(self):
        '''
        TestRail: #C14715872
        Sign in via 'Sign In' on PA screen(not signed in), verify user can sign in without issue
        '''
        logging.debug("Go to print anywhere screen")
        self.common_flows.go_to_print_anywhere_from_main()

        logging.debug("sign in at anywhere screen")
        self.common_flows.sign_in_hp_account_from_anywhere_screen(self.username, self.password)
        printer_anywhere = Printer_Anywhere(self.driver)
        printer_anywhere.wait_for_print_anywhere_enabled_load(120)

    def test_03_sign_out_from_print_anywhere(self):
        '''
        Sign out HP account for next testing.
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        main_ui = MainUI(self.driver)
        main_ui.wait_for_screen_load()

        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.common_flows.close_HPSmart_app()
