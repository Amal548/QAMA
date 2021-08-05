#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Enable Print Anywhere Add a remote printer

@author: ten
@create_date: Sep 19, 2019
'''

import pytest
import logging
import time
import os

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.system.screens.network_page import NetworkPage

pytest.app_info = "SMART"


class Test_Suite_06_Enable_print_Anywhere_remote_printer(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.usename = "test2.yc+hpidstage0203cxm@outlook.com"
        self.password = "Aio1test"
        self.printer = {"printerIP": "192.168.10.186"}

    def test_01_go_to_main_ui(self):
        '''
        GO to Main UI
        '''
        logging.debug("GO to Main UI")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

    def test_02_add_remote_printer_check_screen(self):
        '''
        TestRail:#C14717949
        Sign in with the wrong account for a claim printer (printer is on the same/different network), verify printer does not become a remote printer
        '''
        logging.debug("Sign in HP account")
        self.common_flows.sign_in_hp_account_from_main_ui(self.usename, self.password)

        logging.debug("add remote printer which is claim to another account")
        self.common_flows.add_printer_to_carousel(self.printer, is_skip_ows=True)

        logging.debug("change pc network to another one")
        network_page = NetworkPage(self.driver)
        main_ui = MainUI(self.driver)
        os.system("networksetup -setairportnetwork en1 gothom-A-56 1234567890")
        time.sleep(5)
        network_page.click_dialog_done_btn()
        time.sleep(30)
        main_ui.verify_printer_status_is_offine()







