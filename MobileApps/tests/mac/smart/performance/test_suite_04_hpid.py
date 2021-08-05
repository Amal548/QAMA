'''
Description: This is a test case to calculate hp id login time and create account time.

@author: Sophia
@create_date: September 25, 2020
'''
import pytest
import logging
import os
from time import sleep

from selenium.common.exceptions import TimeoutException

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.resources.const.mac.const import TEST_DATA

from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI


pytest.app_info = "DESKTOP"


class Test_Suite_04_HPID(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.main_screen = MainUI(self.driver)

        # Define variables
        self.appname = smart_const.APP_NAME.SMART
        self.os_pw = ma_misc.load_json_file(TEST_DATA.MAC_SMART_ACCOUNT)["mac_smart"]["account_os_user"]["password"]
        self.package_path = ma_misc.load_json_file(TEST_DATA.MAC_SMART_APP_INFO)["mac_smart"]["build_package_path"]["latest_build_path"]
        self.username = ma_misc.load_json_file(TEST_DATA.MAC_SMART_ACCOUNT)["mac_smart"]["hpid_stage_user"]["username"]
        self.user_pw = ma_misc.load_json_file(TEST_DATA.MAC_SMART_ACCOUNT)["mac_smart"]["hpid_stage_user"]["password"]
        self.run_times = 1

    def test_01_install_app(self):
        '''
        This is a method to setup test precondition--install hp smart.
        '''
        logging.debug("Start to installed hp smart... ")
        #smart_utility.install_app(self.package_path, self.password)

    def test_02_check_login_flow(self):
        '''
        This is a method to check hpid login time.
        '''
        for run_time in range(self.run_times):
            logging.debug("Start to calculate login time...  run time:" + str(run_time))
 
            if(run_time > 0):
                sleep(5)
 
            try:
                self.common_flows.launch_HPSmart_app(self.appname)
                self.common_flows.go_to_main_page_from_welcome_screen_with_sign_in(self.username, self.user_pw)
            except TimeoutException as e:
                # TO DO list
                logging.debug("Error: %s - %s." % (e.strerror))
            finally:
                if self.main_screen.wait_for_app_windows():
                    self.common_flows.sign_out_hp_account()
                    self.common_flows.close_HPSmart_app()

    def test_03_check_create_new_aacount(self):
        '''
        This is a method to check create hpid account time.
        '''
        for run_time in range(self.run_times):
            logging.debug("Start to calculate create account time...  run time:" + str(run_time))

            if(run_time > 0):
                sleep(5)

            try:
                self.common_flows.launch_HPSmart_app(self.appname)
                self.common_flows.sign_up_hp_account_from_main_ui()
            except TimeoutException as e:
                # TO DO list
                logging.debug("Error: %s - %s." % (e.strerror))
            finally:
                if self.main_screen.wait_for_app_windows():
                    self.common_flows.sign_out_hp_account()
                    self.common_flows.close_HPSmart_app()

    def test_04_clean_up_app(self):
        logging.debug("Start to remove hp smart... ")
        #smart_utility.uninstall_app(self.password)
