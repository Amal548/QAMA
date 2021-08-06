#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Description: This is a test case for Sign In/Sign Up/Sign Out testing via ST welcome modal.
Note: Smart Tasks tile enabled
@author: Ivan
@create_date: Sep 26, 2019
'''

import os
import logging
import pytest
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.smarttasks.smart_tasks import SmartTasks
from MobileApps.libs.flows.mac.smart.screens.scan.scan_result import ScanResult
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility

pytest.app_info = "DESKTOP"


class Test_Suite_01_HPID_Smart_Tasks(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_ui = MainUI(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.smart_tasks = SmartTasks(self.driver)
        self.appname = smart_const.APP_NAME.SMART
        self.printer_bonjour_name = "HP ENVY Photo 7800 series [093B66]"
        self.username = "stagegotham@gmail.com"
        self.password = "aio1test"

    def test_01_install_smart_tasks_printer(self):
        '''
        Setup test precondition--install a printer.
        '''
        logging.debug("Install the instant ink printer")
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()

    def test_02_sign_in_via_st_welcome_modal_get_started(self):
        '''
        TestRail: #C14715862
        Sign in via 'Get Started' on ST welcome modal, verify user can sign in without issue
        '''
        logging.debug("Go to smart tasks screen")
        self.main_ui.click_smart_tasks_tile()
        self.smart_tasks.wait_for_smart_tasks_welcome_modal()
        logging.debug("Click Get Stared button to sign in")
        self.common_flows.sign_in_hp_account_from_smart_task(self.username, self.password)

        if (self.smart_tasks.wait_for_create_smart_tasks_screen(raise_e=False)):
            self.tool_bar.click_home_btn()
            self.smart_tasks.wait_for_exit_without_saving_changes_dialog()
            self.smart_tasks.click_yes_btn_on_exit_dialog()
        elif(self.smart_tasks.wait_for_my_smart_tasks_screen(raise_e=False)):
            self.tool_bar.click_home_btn()

        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        self.main_ui.wait_for_screen_load()

        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.common_flows.close_HPSmart_app()

    def test_03_sign_in_via_st_welcome_modal_already_link(self):
        '''
        TestRail: #C14715864
        Sign in via 'Already have Smart Tasks? Sign in' on ST welcome modal, verify user can sign in without issue
        '''
        logging.debug("Setup precondition for next step")
        smart_utility.delete_all_files(os.path.expanduser('~/Library/Containers/com.hp.SmartMac/Data/Library/Application Support/HP Smart'))
        self.system_flows.delete_all_printers_and_fax()
        self.system_flows.install_printer_using_printer_name(self.printer_bonjour_name)
        sleep(10)
        self.common_flows.launch_HPSmart_app(self.appname)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()

        logging.debug("Go to smart tasks screen")
        self.main_ui.click_smart_tasks_tile()
        self.smart_tasks.wait_for_smart_tasks_welcome_modal()
        logging.debug("Click 'Already have Smart Tasks? Sign in' link to sign in")
        self.common_flows.sign_in_hp_account_from_smart_task(self.username, self.password, get_started=False)

        if (self.smart_tasks.wait_for_empty_smart_tasks_screen_load(raise_e=False)):
            pass
        elif(self.smart_tasks.wait_for_my_smart_tasks_screen(raise_e=False)):
            pass

        self.tool_bar.click_home_btn()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        self.main_ui.wait_for_screen_load()

        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.main_ui.wait_for_screen_load()

    def test_04_sign_in_via_smart_tasks_tile(self):
        '''
        TestRail: #C14728410
        Sign in via Smart Tasks tile after welcome modal is dismissed, verify user can sign in without issue
        '''
        self.main_ui.click_smart_tasks_tile()
        self.common_flows.go_through_sign_in_flow(self.username, self.password)

        if (self.smart_tasks.wait_for_empty_smart_tasks_screen_load(raise_e=False)):
            pass
        elif(self.smart_tasks.wait_for_my_smart_tasks_screen(raise_e=False)):
            pass

        self.tool_bar.click_home_btn()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        self.main_ui.wait_for_screen_load()

        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.main_ui.wait_for_screen_load()

    def test_05_sign_in_via_scan_result_smart_tasks(self):
        '''
        TestRail: #C14715878
        Sign in via Scan Result via ST flyout "Sign in", verify user can sign in without issue
        '''
        logging.debug("Go to scan result page... ")
        self.common_flows.go_to_scan_screen_from_main_ui()
        self.common_flows.scan_on_scanner()
        scan_result = ScanResult(self.driver)
        scan_result.click_smart_tasks_btn()
        scan_result.wait_for_smart_task_sign_in_flyout_screen_load()
        scan_result.click_sign_in_btn_on_flyout()
        self.common_flows.go_through_sign_in_flow(self.username, self.password)
        scan_result.wait_for_screen_load()

        logging.debug("Back to Main UI from scan result screen.")
        self.tool_bar.click_home_btn()
        scan_result.wait_for_exit_without_saving_dialog()
        scan_result.click_yes_btn_on_exit_dialog()
        self.common_flows.close_print_anywhere_smart_task_dialog_on_main_ui()
        self.main_ui.wait_for_screen_load()

        logging.debug("Sign out by clicking Person Icon")
        self.common_flows.sign_out_hp_account()
        self.main_ui.wait_for_screen_load()
        self.common_flows.close_HPSmart_app()
