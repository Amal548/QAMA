# encoding: utf-8
'''
Description: This is a test case to check crash in collection view controller.

@author: Sophia
@create_date: May 21, 2019
'''
import pytest
import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException
import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.print_anywhere_flyer import PrintAnywhereFlyer


pytest.app_info = "DESKTOP"


class Test_Suite_01_Collection_View_Controller(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.main_screen = MainUI(self.driver)

        # Define variables
        self.appname = smart_const.APP_NAME.SMART
        self.printer_1 = {"printerBonjourName": "HP ENVY Photo 7800 series [BADBAD]", "printerIP": "192.168.10.108"}
        self.printer_2 = {"printerBonjourName": "HP PageWide Pro MFP 772-777z [98301E]", "printerIP": "192.168.10.161"}
        self.printer_3 = {"printerBonjourName": "HP ENVY 5000 series [D950AB]", "printerIP": "192.168.10.147"}
        self.printers = [self.printer_1, self.printer_2, self.printer_3]
        self.run_times = 1

    def test_01_install_printer(self):
        '''
        This is a method to setup test precondition--install a printer.
        '''
        logging.debug("Start to installed a printer... ")
        for printer_info in self.printers:
            self.system_flows.install_printer_using_printer_name(printer_info["printerBonjourName"])

    def test_02_check_crash(self):
        '''
        This is a method to check crash in collection view controller.
        '''
        for run_time in range(self.run_times):
            logging.debug("Start to check crash in collection view controller...  :" + str(run_time))

            if(run_time > 0):
                sleep(10)

            try:
                logging.debug("Start to add printer to main UI... ")
                self.common_flows.launch_HPSmart_app(self.appname)
                self.common_flows.navigate_to_agreements_screen()
                self.common_flows.navigate_to_main_ui_skip_oobe_flow(is_multi_printers=True)
                self.common_flows.add_printers_to_carousel(self.printers, is_skip_ows=True)
                # App workflow changed
                # self.print_anywhere_screen = PrintAnywhereFlyer(self.driver)
                # if(self.print_anywhere_screen.wait_for_screen_load(raise_e=False)):
                #    self.print_anywhere_screen.click_close_btn()
                self.common_flows.close_HPSmart_app()

                sleep(5)
                logging.debug("Relaunch app and close for testing... ")
                self.common_flows.launch_HPSmart_app(self.appname)
                # App workflow changed
                # if(self.print_anywhere_screen.wait_for_screen_load(timeout=60, raise_e=False)):
                #    self.print_anywhere_screen.click_close_btn()
                self.main_screen.wait_for_screen_load(60)
            except NoSuchElementException as e:
                if(self.main_screen.wait_for_app_windows()):
                    logging.debug("Error: %s - %s." % (e.filename, e.strerror))
                else:
                    raise NoSuchElementException("There have crash, please save the log and check the screenshot...")
            finally:
                if(self.main_screen.wait_for_app_windows()):
                    self.common_flows.close_HPSmart_app()
