#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_01_OOBE_AWC

@author: ten
@create_date: July 25, 2019
'''
import time
import logging
import pytest
import os

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_to_wifi import ConnectPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_help_dialog import ConnectPrinterHelpDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.select_wifi_network_dialog import SelectaWiFiNetworkDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi import ConnectingPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected_to_wifi import PrinterConnectedtoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.print_from_other_devices import PrintFromOtherDevices
from MobileApps.libs.flows.mac.smart.screens.oobe.print_from_other_devices_dialog import PrintFromOtherDevicesDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.link_sent import LinkSent
from MobileApps.libs.flows.mac.smart.screens.oobe.setup_is_almost_finished import Setupisalmostfinished
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_lets_print import PrinterSetupLetsPrint

# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_01_OOBE_AWC(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__

        # Defines driver and flows
        self.driver, self.common_flows, self.system_flows = mac_smart_setup

        self.tool_bar = ToolBar(self.driver)
        self.we_found_your_printer = WeFoundYourPrinter(self.driver)
        self.ows = OWS(self.driver)
        self.printer_setup_incomplete_dialog = PrinterSetupIncompleteDialog(self.driver)
        self.connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        self.connect_printer_help_dialog = ConnectPrinterHelpDialog(self.driver)
        self.select_wifi_network_dialog = SelectaWiFiNetworkDialog(self.driver)
        self.connecting_printer_to_wifi = ConnectingPrintertoWiFi(self.driver)
        self.printer_connected_to_wifi = PrinterConnectedtoWiFi(self.driver)
        self.print_from_other_devices_dialog = PrintFromOtherDevicesDialog(self.driver)
        self.print_from_other_devices = PrintFromOtherDevices(self.driver)
        self.link_sent = LinkSent(self.driver)
        self.setup_is_almost_finished = Setupisalmostfinished(self.driver)
        self.printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
        self.incorrectpassword = '123456'
        self.correctpassword = '12345678'

    def test_01_check_printer_found(self):
        '''
        TestRail:#C12607633, #C12607635, #C12857912
        This is a method to check APP can find beaconing printer when there has 1 beaconing printer in OOBE AWC flow.
        '''
        logging.debug("Check APP find printer in OOBE AWC flow")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.we_found_your_printer.wait_for_screen_load(90)
        self.we_found_your_printer.verify_ui_string()
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.wait_for_screen_load()
        self.printer_setup_incomplete_dialog.click_back_btn()

    def test_02_check_printer_network(self):
        '''
        Check “Connect printer to Wi-Fi” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “Connect printer to Wi-Fi” screen, verify functionality[C12607637]")
        self.we_found_your_printer.click_continue_btn()
        time.sleep(30)
        self.connect_printer_to_wifi.wait_for_screen_load()
        self.connect_printer_to_wifi.verify_ui_string()
        self.connect_printer_to_wifi.click_info_btn()
        self.connect_printer_help_dialog.wait_for_screen_load()
        self.connect_printer_help_dialog.verify_screen_display()
        self.connect_printer_help_dialog.click_continue_btn()
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.wait_for_screen_load()
        self.printer_setup_incomplete_dialog.click_back_btn()
        self.connect_printer_to_wifi.click_change_network_link()
        self.select_wifi_network_dialog.wait_for_screen_load()
        self.select_wifi_network_dialog.verify_screen_display()
        self.select_wifi_network_dialog.click_network_btn()
        time.sleep(5)
        self.select_wifi_network_dialog.click_system_preferences_close_btn()
        time.sleep(2)
        self.select_wifi_network_dialog.click_continue_btn()
        self.connect_printer_to_wifi.input_enter_wifi_password_box(self.incorrectpassword)
        self.connect_printer_to_wifi.click_continue_btn()
        self.connect_printer_to_wifi.verify_incorrectpassword_waring()
        self.connect_printer_to_wifi.clear_enter_wifi_password_box()
        self.connect_printer_to_wifi.input_enter_wifi_password_box(self.correctpassword)
        self.connect_printer_to_wifi.click_continue_btn()

    def test_03_check_connecting_printer_to_wifi(self):
        '''
        Check “Connecting printer to Wi-Fi...” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “Connecting printer to Wi-Fi...” screen, verify functionality[C12610932]")
        self.connecting_printer_to_wifi.wait_for_screen_load(33)
        self.connecting_printer_to_wifi.verify_ui_string()

    def test_04_check_printer_connected(self):
        '''
        Check “Printer connected to Wi-Fi” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “Printer connected to Wi-Fi” screen, verify functionality[C12610935]")
        self.printer_connected_to_wifi.wait_for_screen_load()
        self.printer_connected_to_wifi.verify_ui_string()
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.wait_for_screen_load()
        self.printer_setup_incomplete_dialog.click_back_btn()
        self.printer_connected_to_wifi.click_continue_btn()

    def test_05_check_print_from_other_devices(self):
        '''
        Check “print from other devices” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “print from other devices” screen, verify functionality[C12610936]")
        self.print_from_other_devices.verify_collecting_your_printer_status_screen_display()
        self.ows.wait_for_enjoy_hp_account_load(40)
        self.ows.click_continue_btn_enjoy_hp_account()
        time.sleep(30)
        self.print_from_other_devices.click_sign_in_close_btn()
        self.ows.wait_for_cartridges_install_load()
        self.ows.click_continue_btn_cartridges_install()
        time.sleep(10)
        os.system("pkill Safari")
        self.print_from_other_devices.verify_ui_string()
        self.print_from_other_devices.click_info_btn()
        self.print_from_other_devices_dialog.verify_screen_display()
        self.print_from_other_devices_dialog.click_ok_btn()
        self.print_from_other_devices.click_send_link_btn()
        self.print_from_other_devices.click_send_link_btn()

    def test_06_check_link_sent_screen(self):
        '''
        Check “link sent” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “link sent” screen, verify functionality[C12612352]")
        self.link_sent.wait_for_screen_load(33)
        self.link_sent.verify_ui_string()
        self.link_sent.click_info_btn()
        self.print_from_other_devices_dialog.verify_screen_display()
        self.print_from_other_devices_dialog.click_ok_btn()
        self.link_sent.click_send_another_link_btn()
        self.link_sent.verify_pop_up_share_dialog_display()
        self.link_sent.click_done_btn()
        self.link_sent.click_done_btn()

    def test_07_check_setup_is_almost_finished_screen(self):
        '''
        Check “setup is almost finished” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “setup is almost finished” screen, verify functionality[C12612354]")
        self.setup_is_almost_finished.wait_for_screen_load()
        self.setup_is_almost_finished.verify_ui_string()
        self.setup_is_almost_finished.click_printers_scanners_btn()
        # install printer#
        self.setup_is_almost_finished.click_printers_scanners_close_btn()
        time.sleep(2)
        self.setup_is_almost_finished.click_printers_scanners_btn()

    def test_06_check_first_print(self):
        '''
        Check “Printer Setup, Let’s print!” screen
        :parameter:
        :return:
        '''
        logging.debug("Check “Printer Setup, Let’s print!” screen, verify functionality[C12612358]")
        self.printer_setup_lets_print.wait_for_screen_load()
        self.printer_setup_lets_print.verify_ui_string()
        self.printer_setup_lets_print.click_not_now_btn()
        time.sleep(30)
        self.main_ui.wait_for_printer_status_load()
