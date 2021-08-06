#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Sign In/Sign Up/Sign Out testing from HP Instant Ink tile on Main UI.
Precondition:
1. HPC Region
2. Computer time is correct
3. Printer must be enrolled in Instant Ink
4. Printer must be installed on the computer
@author: Ivan
@create_date: Sep 24, 2019
'''

import os
import logging
import pytest

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.hpid.hp_id_instant_ink import HPIDInstantInk

pytest.app_info = "DESKTOP"


class Test_Suite_01_HPID_Instant_Ink(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.appname = smart_const.APP_NAME.SMART
        self.main_ui = MainUI(self.driver)
        self.hp_id_instant_ink = HPIDInstantInk(self.driver)
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.username = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_install_instant_ink_printer(self):
        '''
        Setup test precondition--install a printer.
        '''
        logging.debug("Install the instant ink printer")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

    def test_02_sign_in_from_instant_ink(self):
        '''
        TestRail: #C14715876
        Sign in via HP Instant Ink tile on main UI, verify user can sign in without issue
        '''
        self.main_ui.click_get_ink_tile()
        self.hp_id_instant_ink.sign_in_successfully_flow(self.username, self.password)
        logging.debug("Sign out for next sign in.")
        self.hp_id_instant_ink.click_sign_out_button()
        self.hp_id_instant_ink.wait_for_screen_load(90)
        os.system("pkill Safari")
        self.common_flows.close_HPSmart_app()
