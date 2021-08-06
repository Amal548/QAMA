#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Forget a printer from Main UI,verify flow

@author: ten
@create_date: Sep 23, 2019
'''

import pytest
import logging
import time
import os


import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.forget_printer_dialog import FogetPrinterDialog

pytest.app_info = "SMART"


class Test_suite_01_ForgetThisPrinter_Main_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.forget_printer_dialog = FogetPrinterDialog(self.driver)
        self.printer = {"printerIP": "192.168.10.186"}

    def test_01_go_to_main_ui(self):
        '''
        GO to Main UI
        '''
        logging.debug("GO to Main UI")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

    def test_02_right_click_on_plus_sign(self):
        '''
        TestRail:#C14555227
        Right click on plus sign,verify Forget this printer does not appear
        '''
        logging.debug("Right click on plus sign,verify Forget this printer does not appear")
        self.main_ui.right_click_find_printer_icon()
        self.main_ui.verify_forget_printer_option_notdisplay()

    def test_03_right_click_on_printer_in_carousel(self):
        '''
        TestRail:#C14555200 #C14555201 #C14555202 #C14555219 #C14555220 #C14555221 #C14555222
                 #C14555223 #C14555224
        Right click on plus sign,verify Forget this printer does not appear
        '''
        logging.debug("chose a printer")
        self.common_flows.add_printer_to_carousel(self.printer, is_skip_ows=True)
        self.main_ui.right_click_print_image()
        self.main_ui.wait_for_forget_printer_option_display()
        self.main_ui.click_forget_printer_option()
        self.forget_printer_dialog.wait_for_screen_load()
        self.forget_printer_dialog.verify_ui_string()

        logging.debug("click cancel button")
        self.forget_printer_dialog.click_cancel_btn()
        self.forget_printer_dialog.verify_dialog_disappear()

        logging.debug("click forget button")
        self.main_ui.right_click_print_image()
        self.main_ui.wait_for_forget_printer_option_display()
        self.main_ui.click_forget_printer_option()
        self.forget_printer_dialog.wait_for_screen_load()
        self.forget_printer_dialog.click_forget_printer_btn()
        self.forget_printer_dialog.wait_for_find_printer_icon_display()

    def test_04_right_click_on_printer_with_offline(self):
        '''
        TestRail:#C14555226
        Right click on printer when it is offline, verify Forget this Printer option shows
        '''
        logging.debug("click on printer when it is offline, verify Forget this Printer option shows")
        self.common_flows.add_printer_to_carousel(self.printer, is_skip_ows=True)
        os.system("networksetup -setairportpower en1 off")
        time.sleep(10)
        self.main_ui.right_click_print_image()
        self.main_ui.wait_for_forget_printer_option_display()
        self.main_ui.click_forget_printer_option()
        self.forget_printer_dialog.wait_for_screen_load()
        self.forget_printer_dialog.click_forget_printer_btn()
        self.forget_printer_dialog.wait_for_find_printer_icon_display()
