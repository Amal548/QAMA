#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Enable Print Anywhere with sign in

@author: ten
@create_date: Sep 11, 2019
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


class Test_Suite_02_Enable_print_Anywhere_Sign_In(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.print_anywhere_flyer = PrintAnywhereFlyer(self.driver)
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [0B46DD]"
        self.printer_bonjour_name_claimed = "HP ENVY Photo 7800 series [093B66]"
        self.usename = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_install_printer(self):
        '''
        TestRail:#C14072381
        This is a method to test printer installed.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_click_get_started_btn_on_anywhere_dialog(self):
        '''
        TestRail:#C14062637 #C14062644 #C14064357 #C14064360 #C16942965 #C14064334 #C14064357 #C14064360
                 #C16942965 #C14064361 #C14064363 #C14590863 #C16946971 #C17155848
        Check "Get Started" button
        '''
        logging.debug("Go to Main UI ")
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

        logging.debug("Skip Smart Task dialog")
        self.main_ui .wait_for_smart_task_dialog_display()
        self.main_ui .click_close_btn_on_smart_task_dialog()

        logging.debug("Sign in HP account")
        self.common_flows.sign_in_hp_account_from_main_ui(self.usename, self.password)

        logging.debug("Go to print anywhere dialog")
        time.sleep(10)
        self.main_ui.click_printer_settings_title()
        time.sleep(3)
        self.common_flows.back_main_ui_from_printer_settings()
        self.print_anywhere_flyer.wait_for_screen_load()

        logging.debug("Click get started button with signed in,not claimed")
        printer_anywhere = Printer_Anywhere(self.driver)
        self.print_anywhere_flyer.click_get_started_btn()
        printer_anywhere.wait_for_screen_load()
        time.sleep(30)
        printer_anywhere.verify_screen_shows_with_enable_button()
 
        logging.debug("go to print anywhere screen from printer settings")
        self.common_flows.back_main_ui_from_printer_settings()
        time.sleep(3)
        self.common_flows.go_to_print_anywhere_from_main()
        time.sleep(20)
        printer_anywhere.verify_screen_shows_with_enable_button()
 
        logging.debug("Click get started button with signed in, printer claimed")
        self.common_flows.close_HPSmart_app()
        smart_utility.delete_all_files(os.path.expanduser('~/Library/Application Support/HP Smart'))
        self.system_flows.delete_all_printers_and_fax()
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name_claimed)
        time.sleep(10)
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.main_ui.wait_for_smart_task_dialog_display()
        self.main_ui.click_close_btn_on_smart_task_dialog()
        self.main_ui.click_printer_settings_title()
        time.sleep(3)
        self.common_flows.back_main_ui_from_printer_settings()
        self.print_anywhere_flyer.wait_for_screen_load()
        self.print_anywhere_flyer.click_get_started_btn()
        printer_anywhere.wait_for_print_anywhere_enabled_load()
        printer_anywhere.verify_print_anywhere_enabled_screen()
 
        logging.debug("go to print anywhere screen from printer settings")
        self.common_flows.back_main_ui_from_printer_settings()
        time.sleep(3)
        self.common_flows.go_to_print_anywhere_from_main(claimed=True)
        printer_anywhere.wait_for_print_anywhere_enabled_load()
        printer_anywhere.verify_print_anywhere_enabled_screen()

        logging.debug("click 'send link' button")
        printer_anywhere.click_send_link_btn()
        printer_anywhere.wait_for_print_from_other_devices_screen_load()
