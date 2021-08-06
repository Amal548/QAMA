#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Enable Print Anywhere Gen1 printer

@author: ten
@create_date: Sep 16, 2019
'''

import pytest
import logging
import time


import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.print_anywhere_flyer import PrintAnywhereFlyer

pytest.app_info = "DESKTOP"


class test_Suite_04_Enable_Print_Anywhere_Gen1(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.print_anywhere_flyer = PrintAnywhereFlyer(self.driver)
        self.printer_bonjour_name = "HP ENVY 4520 series [DB987D]"

    def test_01_install_printer(self):
        '''
        TestRail:#C14590898
        This is a method to test printer installed.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)

    def test_02_check_print_anywhere_dialog_not_displayed(self):
        '''
        TestRail:#C14590898
        check print anywhere dialog Not displayed
        '''
        logging.debug("Go to Main UI ")
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

        logging.debug("Skip Smart Task dialog")
        self.main.wait_for_smart_task_dialog_display()
        self.main.click_close_btn_on_smart_task_dialog()

        logging.debug("check print anywhere dialog not display")
        self.main_ui.click_printer_settings_tile()
        time.sleep(3)
        self.common_flows.back_main_ui_from_printer_settings()
        self.print_anywhere_flyer.verify_print_anywhere_dialog_no_display()
