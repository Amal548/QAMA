#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Sign In/Sign Up/Sign Out testing from Main UI.
@author: Ivan
@create_date: Sep 25, 2019
'''

import logging
import pytest

import MobileApps.resources.const.mac.const as smart_const

pytest.app_info = "DESKTOP"


class Test_Suite_01_HPID_Main_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.appname = smart_const.APP_NAME.SMART
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
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()

    def test_02_sign_in_out_from_person_icon(self):
        '''
        TestRail: #C14715857, #C14715859
        Sign in via person icon on (shell) title bar, verify user can sign in without issue
        Sign out via person icon on (shell) title bar, verify user can sign out without issue
        '''
        logging.debug("Sign in by clicking Person Icon")
        self.common_flows.sign_in_hp_account_from_main_ui(self.username, self.password)
        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()

    def test_03_sign_in_from_bell_icon(self):
        '''
        TestRail: #C14715860
        Sign in via bell icon on(shell) title bar, verify user can sign in without issue
        '''
        logging.debug("Sign in by clicking Bell Icon")
        self.common_flows.sign_in_hp_account_from_main_ui(self.username, self.password, default_click_icon=False)
        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.common_flows.close_HPSmart_app()
