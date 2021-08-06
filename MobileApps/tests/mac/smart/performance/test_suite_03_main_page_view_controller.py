# encoding: utf-8
'''
Description: This is a test case to check crash in main page view controller.

@author: Sophia
@create_date: May 21, 2019
'''
import pytest
import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.print_anywhere_flyer import PrintAnywhereFlyer


pytest.app_info = "DESKTOP"


class Test_Suite_03_Main_Page_View_Controller(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.main_screen = MainUI(self.driver)

        # Define variables
        self.appname = smart_const.APP_NAME.SMART
        self.printerBonjourName = "HP ENVY Photo 7800 series [BADBAD]"
        self.run_times = 1

    def test_01_install_printer(self):
        '''
        This is a method to setup test precondition--install a printer.
        '''
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printerBonjourName)

    def test_02_check_crash(self):
        '''
        This is a method to check crash in main page view controller.
        '''
        for run_time in range(self.run_times):
            logging.debug("Start to check crash in main page view controller...  :" + str(run_time))

            if(run_time > 0):
                sleep(10)

            try:
                self.common_flows.launch_HPSmart_app(self.appname)
                self.common_flows.navigate_to_agreements_screen()
                self.common_flows.navigate_to_main_ui_skip_oobe_flow()

                self.common_flows.go_to_printer_status_tab_from_main_ui()
                self.common_flows.back_to_main_ui_from_printer_settings()
                self.print_anywhere_screen = PrintAnywhereFlyer(self.driver)
                if(self.print_anywhere_screen.wait_for_screen_load()):
                    self.print_anywhere_screen.click_close_btn()
            except (NoSuchElementException, TimeoutException) as e:
                if(self.main_screen.wait_for_app_windows()):
                    logging.debug("Error: %s - %s." % (e.filename, e.strerror))
                else:
                    raise NoSuchElementException("There have crash, please save the log and check the screenshot...")
            finally:
                if(self.main_screen.wait_for_app_windows()):
                    self.common_flows.close_HPSmart_app()
