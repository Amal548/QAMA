#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_01_devicepicker

@author: ten
@create_date: July 25, 2019
'''
import time
import logging
import pytest
from MobileApps.libs.ma_misc import ma_misc

from MobileApps.libs.flows.mac.system.flows.flows_system import SystemFlows
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.device_picker import DevicePicker
from MobileApps.libs.flows.mac.smart.screens.menubar.menu_bar import MenuBar
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
import os

# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_01_DevicePicker(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.tool_bar = ToolBar(self.driver)
        self.main_ui = MainUI(self.driver)
        self.printer_setup_incomplete_dialog = PrinterSetupIncompleteDialog(self.driver)
        self.device_picker = DevicePicker(self.driver)
        self.menu_bar = MenuBar(self.driver)
        self.ows = OWS(self.driver)
        self.printerBonjourName = "HP DeskJet 5000 series [F305EA]"
        self.printer_IP = "192.168.10.101"
        self.printer_hostname = "CJ020004"
        self.offsubnet_printer_IP = "10.10.56.165"
        self.offsubnet_printer_hostname = "HPD950AB"
        self.invalid_printer_IP = "3.3.3.3"
        self.invalid_printer_hostname = "Gotham"

    def test_01_goto_device_picker_screen(self):
        '''
        GO to Main UI
        '''
        logging.debug("GO to Main UI")
        self.common_flows.navigate_to_agreements_screen()
        self.common_flows.go_to_oobe_initial_screen()
        self.common_flows.go_to_main_ui_skip_post_oobe()

    def test_02_check_device_picker_ui(self):
        '''
        TestRail:#C13258919,#C13258918,#C12585899,#C12494940,#C13794791
        Click on the + to add a printer Check UI layout, form and fit against the attached screen shotRe-size app to check UI form and fit
        '''
        logging.debug("Click on the + to add a printer Check UI layout, form and fit against the attached screen shotRe-size app to check UI form and fit(withprintersetup)[C13258919][C13258918][C12585899][C12494940][C13794791]")
        self.main_ui.click_find_printer_icon()
        self.device_picker.wait_for_screen_load()
        self.device_picker.verify_device_picker_string()

    def test_03_device_discovery_with_no_printers_found(self):
        '''
        TestRail:#C12494939
        Make sure there is no printer on the network/or connected to device.Launch Gotham appClick the '+' button.Wait until the searching is completed
        '''
        logging.debug("Make sure there is no printer on the network/or connected to device.Launch Gotham appClick the '+' button.Wait until the searching is completed.[C12494939]")
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_find_printer_icon_display()
        os.system("networksetup -setairportpower en1 off")
        time.sleep(10)
        self.main_ui.click_find_printer_icon()
        self.device_picker.wait_for_screen_load()
        self.device_picker.verify_no_printers_available_screen()
        os.system("networksetup -setairportpower en1 on")

    def test_04_click_each_btn(self):
        '''
        TestRail:#C12494942,#C12577951
        click on Refresh link and setup a new printer link
        '''
        logging.debug("click on Refresh link[C12494942]")
        time.sleep(10)
        self.device_picker.click_refresh_btn()
        self.device_picker.wait_for_busy_icon_display()

        logging.debug("click on 'Setup a new printer' link[C12577951]")
        time.sleep(90)
        self.device_picker.click_setup_new_printer_btn()
        time.sleep(10)
        self.device_picker.verify_oobe_flow_starts()

    def test_05_input_IP_or_hostname_in_searchbox_subnet(self):
        '''
        TestRail:#C13251414
        Input an IP addres and hostname in the search box on subnet
        '''
        logging.debug("Input an IP address  in the search boxShould be able to find printer on subnet via IP[C13251414]")
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn()
        self.main_ui.click_find_printer_icon()
        self.device_picker.wait_for_screen_load()
        self.device_picker.set_value_to_search_box(self.printer_IP)
        self.device_picker.verify_printer_info()

        logging.debug("Input a  hostname in the search boxShould be able to find printer on subnet via hostname[C13251413][C13802143]")
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.printer_hostname)
        self.device_picker.verify_printer_info()

    def test_06_input_IP_or_hostname_in_searchbox_offsubnet(self):
        '''
        TestRail:#C12494941,#C13251419
        Input an IP addres and hostname in the search box on off subnet
        '''
        logging.debug("Input an IP address  in the search boxShould be able to find printer on subnet via IP[C12494941]")
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.offsubnet_printer_IP)
        self.device_picker.verify_printer_info_off_subnet()

        logging.debug("Input a  hostname in the search boxShould be able to find printer on subnet via hostname[C13251419]")
        time.sleep(20)
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.offsubnet_printer_hostname)
        self.device_picker.verify_printer_info_off_subnet()

#     def test_07_enter_keyword_in_searchbox(self):
#         logging.debug("Launch the app and go to Device PickerEnter a partial printer name- for example, office (jet) Should be able to find printer using keywords (like Office Jet))[C13258785]")
#         self.device_picker.click_search_box_delete_btn()
#         time.sleep(2)
#         self.device_picker.set_value_to_search_box()
#         self.device_picker.wait_for_find_printer_display()

    def test_08_input_invalid_IP_or_hostname(self):
        '''
        TestRail:#C12577950
        Input an invalid IP in the search box
        '''
        logging.debug("Input an invalid IP in the search box on Printers screen and then search[C12577950]")
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.invalid_printer_IP)
        self.device_picker.verify_warning_message_display()

        logging.debug("Input an invalid hostname in the search box on Printers screen and then search")
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.invalid_printer_hostname)
        self.device_picker.verify_warning_message_display()

    def test_09_verify_printer_not_show_in_device_picker_with_added_to_carousel(self):
        '''
        TestRail:#C15965602
        User has printers already added to carouselLaunch the app and go to Device Picker Observe printers available
        '''
        logging.debug("User has printers already added to carouselLaunch the app and go to Device Picker Observe printers available[C15965602]")
        self.device_picker.click_search_box_delete_btn()
        time.sleep(2)
        self.device_picker.set_value_to_search_box(self.printer_hostname)
        self.device_picker.click_searched_printer()
        time.sleep(10)
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn_for_choose_printer()
        time.sleep(3)
        self.printer_setup_incomplete_dialog.click_ok_btn_for_choose_printer()
        time.sleep(30)
        self.tool_bar.click_select_printer_btn()
        self.device_picker.wait_for_screen_load()
        self.device_picker.set_value_to_search_box(self.printer_hostname)
        self.device_picker.verify_warning_message_display()

    def test_10_click_installed_printer_device_picker(self):
        '''
        TestRail:#C13311464
        One printer must be installed on the computer
        Launch app and navigate to Device Picker Click on installed printer
        '''
        # Description: One printer must be installed on the computer
        logging.debug("Launch app and navigate to Device Picker Click on installed printer[C13311464]")
        self.tool_bar.click_home_btn()
        time.sleep(10)
        self.menu_bar.click_menubar_Printers()
        self.menu_bar.click_menubar_Printers_Forget_Printer()
        self.main_ui.click_forget_printer_btn()
        self.main_ui.wait_for_find_printer_icon_display()
        self.system_flows.install_printer_using_printer_name(self.printerBonjourName)
        self.main_ui.click_find_printer_icon()
        self.device_picker.wait_for_screen_load()
        self.device_picker.set_value_to_search_box(self.printer_hostname)
        self.device_picker.click_searched_printer()
        time.sleep(30)
        self.ows.wait_for_enjoy_hp_account_load()

    def test_11_click_installed_printer_device_picker(self):
        '''
        TestRail:#C13258914
        Printer must be in beaconing mode
        Launch app and go to Add a Printer Find and click on beaconing printer
        '''
        logging.debug("Launch app and go to Add a Printer Find and click on beaconing printer[C13258914]")
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn()
        time.sleep(10)
        self.tool_bar.click_select_printer_btn()
        time.sleep(30)
        self.device_picker.wait_for_screen_load()
        self.device_picker.click_set_up_words()
        time.sleep(10)
        self.device_picker.verify_beaconing_printer_initiate_oobe()
