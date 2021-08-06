#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: Test script for the basic testing of Advanced Settings with an online non-application printer(USB)
Note: Please set the password to 1234567890 on test printer EWS.
@author: Ivan
@create_date: Sep 4, 2019
'''

import pytest
import logging

from time import sleep
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.printersettings.advanced_settings import AdvancedSettings

pytest.app_info = "DESKTOP"


class Test_Suite_01_Advanced_Settings_Password_Protected(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.ews = AdvancedSettings(self.driver)
        self.appname = smart_const.APP_NAME.SMART
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.correct_password = "1234567890"
        self.incorrect_password = "12345678"

    def test_01_go_through_flow_to_security_dialog(self):
        '''
        TestRail: #C15541112
        Go to "Advance Settings" with a password protected printer, verify windows security dialog pops up.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        logging.debug("Start to check welcome workflow... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        logging.debug("Start to check post OOBE workflow... ")
        self.common_flows.go_to_main_ui_skip_post_oobe()

        main_screen = MainUI(self.driver)
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        if (main_screen.wait_for_right_arrow_icon_display(raise_e=False)):
            main_screen.click_right_arrow_icon()
        main_screen.click_printer_settings_tile()

        self.ews.wait_for_printer_home_page_item_load()
        self.ews.click_printer_home_page_item()
        self.ews.wait_for_screen_load()
        sleep(2)
        self.ews.click_scan_tile_on_ews()
        self.ews.wait_for_security_dialog_load()

    def test_02_enter_incorrect_password(self):
        '''
        TestRail:#C15541113
        Enter incorrect user info on the OS security dialog to access EWS, verify the dialog prompts again.
        '''
        self.ews.enter_password_on_dialog(self.incorrect_password)
        self.ews.wait_for_security_dialog_load()

    def test_03_enter_correct_password(self):
        '''
        TestRail:#C15541113
        Enter correct user info on the OS security dialog to access EWS, verify EWS content shows.
        '''
        self.ews.enter_password_on_dialog(self.correct_password)
        self.ews.wait_for_security_dialog_disappear()
        self.ews.wait_for_screen_load()
        self.common_flows.close_HPSmart_app()
