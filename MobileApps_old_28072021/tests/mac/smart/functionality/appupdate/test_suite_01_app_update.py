#!/usr/local/bin/python2.7
# encoding: utf-8
'''
App Update

@author: ten
@create_date: Sep 3, 2019
'''

import pytest
import time
import logging
import os

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.menubar.menu_bar import MenuBar
from MobileApps.libs.flows.mac.smart.screens.menubar.check_for_updates_dialog import CheckforupdatesDialog
from MobileApps.libs.flows.mac.smart.screens.menubar.developer_tools_dialog import DeveloperToolsDialog
from MobileApps.libs.flows.mac.smart.screens.appupdate.download_dialog import DownloadDialog
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility

pytest.app_info = "SMART"


class Test_Suite_01_App_Update(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.menu_bar = MenuBar(self.driver)
        self.checkforupdates_dialog = CheckforupdatesDialog(self.driver)
        self.text = "0.5"
        self.package_path = "/Users/itest/Desktop/HP\ Smart-3.5.260.pkg -target /"
        self.password = "Spytester123"

    def test_01_check_no_update_dialog(self):
        '''
        TestRail:#C15541031 #C15541032 #C15541033 #C15541034 #C15541035
        check 'No software update is available'
        '''
        logging.debug("go to Main UI")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

        logging.debug("verify no update dialog")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_checkforupdates_btn()
        self.checkforupdates_dialog.wait_for_no_software_update_available_load()
        self.checkforupdates_dialog.verify_no_software_update_available_dialog()

        logging.debug("verify 'Check for Updates..' option is grayed out")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.verify_checkforupdates_option_grayed_out()

        logging.debug("click ok button")
        self.checkforupdates_dialog.click_ok_btn()
        self.checkforupdates_dialog.click_ok_btn()
        self.checkforupdates_dialog.verify_no_software_update_available_dialog_dismissed()

    def test_02_check_new_update_dialog(self):
        '''
        TestRail:#C15541036 #C15541037 #C15541038 #C15541039 #C15541040 #C15541051 #C15541054 #C15541055
        check 'New Software Available' dialog
        '''
        logging.debug("modify some settings in developer tools dialog")
        developer_tools_dialog = DeveloperToolsDialog(self.driver)
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_abouthpsmart_btn()
        self.menu_bar.click_menu_bar_about_hp_smart_image_ten_times()
        developer_tools_dialog.wait_for_screen_load()
        developer_tools_dialog.input_override_app_version(self.text)
        self.menu_bar.click_close_btn()

        logging.debug("verify new software available dialog")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_checkforupdates_btn()
        self.checkforupdates_dialog.wait_for_new_software_available_load()
        self.checkforupdates_dialog.verify_new_update_availabled_dialog()

        logging.debug("uninstall current and install old build")
        self.checkforupdates_dialog.click_no_btn()
        self.common_flows.close_HPSmart_app()
        smart_utility.uninstall_app(self.password)
        time.sleep(10)
        smart_utility.install_app(self.package_path, self.password)
        time.sleep(10)
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.checkforupdates_dialog.wait_for_new_software_available_load()
        self.checkforupdates_dialog.click_checkbox_btn()
        self.checkforupdates_dialog.click_no_btn()
        self.common_flows.close_HPSmart_app()
        time.sleep(5)
        self.common_flows.launch_HPSmart_app("HP Smart")
        self.checkforupdates_dialog.verify_new_update_availabled_dialog_no_appear()

    def test_03_check_download_unsuccessful_dialog(self):
        '''
        TestRail:#C15541041 #C15541042 #C15541043 #C15541044
        check 'download unsuccessful' dialog
        '''
        logging.debug("check 'download unsuccessful' dialog")
        download_dialog = DownloadDialog(self.driver)
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.common_flows.click_home_exit_flow_to_main_ui()
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_checkforupdates_btn()
        self.checkforupdates_dialog.wait_for_new_software_available_load()
        os.system("networksetup -setairportpower en1 off")
        time.sleep(10)
        self.checkforupdates_dialog.click_yes_btn()
        download_dialog.wait_for_screen_load()
        download_dialog.verify_download_unsuccessful_dialog_string()
        download_dialog.click_ok_btn()

    def test_04_check_download_successful_dialog(self):
        '''
        TestRail:#C15541045 #C15541046 #C15541047 #C15541048
        check 'download successful' dialog
        '''
        logging.debug("check 'download successful' dialog")
        download_dialog = DownloadDialog(self.driver)
        os.system("networksetup -setairportpower en1 on")
        time.sleep(20)
        self.checkforupdates_dialog.click_yes_btn()
        download_dialog.wait_for_screen_load(300)
        download_dialog.verify_download_successful_dialog_string()
