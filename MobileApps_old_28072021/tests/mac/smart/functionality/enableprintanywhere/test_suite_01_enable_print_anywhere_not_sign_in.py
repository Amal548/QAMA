#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Enable Print Anywhere with not sign in

@author: ten
@create_date: Sep 9, 2019
'''

import pytest
import logging
import time
import os

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.print_anywhere_flyer import PrintAnywhereFlyer
from MobileApps.libs.flows.mac.smart.screens.printersettings.print_anywhere import Printer_Anywhere
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility

pytest.app_info = "DESKTOP"


class Test_Suite_01_Enable_print_Anywhere_Not_Sign_In(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.print_anywhere_flyer = PrintAnywhereFlyer(self.driver)
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [0B46DD]"

    def test_01_install_printer(self):
        '''
        TestRail:#C14072381
        This is a method to test printer installed.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_check_print_anywhere_dialog(self):
        '''
        TestRail:#C14061904 #C14062597
        check print anywhere dialog UI String
        '''
        logging.debug("Go to Main UI ")
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
 
        logging.debug("Skip Smart Task dialog")
        self.main_ui.wait_for_smart_task_dialog_display()
        self.main_ui.click_close_btn_on_smart_task_dialog()
 
        logging.debug("Go to print anywhere dialog")
        self.main_ui.click_printer_settings_title()
        time.sleep(3)
        self.common_flows.back_main_ui_from_printer_settings()
        self.print_anywhere_flyer.wait_for_screen_load()
        self.print_anywhere_flyer.verify_ui_string()

    def test_03_click_get_started_btn(self):
        '''
        TestRail:#C14062606 #C14064356 #C14064366 #C14064595 #C14064330 #C14064355
        Check "Get Started" button
        '''
        logging.debug("Click get started button with not signed in")
        printer_anywhere = Printer_Anywhere(self.driver)
        self.print_anywhere_flyer.click_get_started_btn()
        printer_anywhere.wait_for_screen_load()
        printer_anywhere.verify_screen_shows_with_sign_in_button()
 
        logging.debug("go to print anywhere screen from printer settings")
        self.common_flows.back_main_ui_from_printer_settings()
        time.sleep(3)
        self.common_flows.go_to_print_anywhere_from_main()
        printer_anywhere.wait_for_screen_load()
        printer_anywhere.verify_screen_shows_with_sign_in_button()

        logging.debug("click 'get more help' link")
        printer_anywhere.click_get_more_help_link()
        time.sleep(10)
        os.system("pkill Safari")
