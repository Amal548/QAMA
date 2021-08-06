#!/usr/local/bin/python2.7
# encoding: utf-8
'''
test_Suite_02_menubar_edit_printers

@author: ten
@create_date: July 20, 2019
'''
import time
import logging
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.smart.screens.menubar.feedback import Feedback
from MobileApps.libs.flows.mac.smart.screens.common.welcome import Welcome
from MobileApps.libs.flows.mac.smart.screens.common.agreement import Agreement
from MobileApps.libs.flows.mac.smart.screens.menubar.menu_bar import MenuBar
from MobileApps.libs.flows.mac.smart.screens.menubar.hp_account_information import Hpaccountinformation
from MobileApps.libs.flows.mac.smart.screens.menubar.check_for_updates_dialog import CheckforupdatesDialog
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.device_picker import DevicePicker
from MobileApps.libs.flows.mac.smart.screens.menubar.invite_to_print import InviteToPrint
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_02_Menubar_Edit_Printers(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.feedback = Feedback(self.driver)
        self.menu_bar = MenuBar(self.driver)
        self.welcome = Welcome(self.driver)
        self.hp_account_information = Hpaccountinformation(self.driver)
        self.agreement = Agreement(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.main_ui = MainUI(self.driver)
        self.printer_setup_incomplete_dialog = PrinterSetupIncompleteDialog(self.driver)
        self.device_picker = DevicePicker(self.driver)
        self.invite_to_print = InviteToPrint(self.driver)
        self.checkforupdates_dialog = CheckforupdatesDialog(self.driver)
        self.printer_hostname = "CJ020006"
        self.package_path = "/Users/itest/Desktop/HP\ Smart-3.0.203.pkg -target /"
        self.password = "Spytester123"

    def test_01_check_edit_button(self):
        '''
        TestRail:#C14590877
        click Edit button on Menu Bar verify both option'copy'&'paste'display there
        '''
        logging.debug("click Edit button on Menu Bar verify both option'copy'&'paste'display there, but they are grey out and not clickable[C14590877]")
        self.welcome.wait_for_screen_load()
        self.menu_bar.click_menubar_edit()
        self.menu_bar.verify_edit_options()

    def test_02_check_printersmenu_before_oobe(self):
        '''
        TestRail:#C14590878
        click Printers and verify the dropdown list is expanded before OOBE
        '''
        logging.debug("click Printers and verify the dropdown list is expanded before OOBE[C14590878]")
        self.menu_bar.click_menubar_edit()
        time.sleep(1)
        self.menu_bar.click_menubar_printers()
        self.menu_bar.verify_before_oobe_printersmenu()

    def test_03_check_printersmenu_after_oobe(self):
        '''
        TestRail:#C14590878
        click Printers and verify the dropdown list is expanded after OOBE
        '''
        logging.debug("click Printers and verify the dropdown list is expanded after OOBE[C14590878]")
        self.menu_bar.click_menubar_printers()
        self.welcome.click_get_started_button()
        self.agreement.choose_check_box()
        self.agreement.click_continue_button()
        time.sleep(10)
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn()
        self.main_ui.wait_for_find_printer_icon_display()
        self.menu_bar.click_menubar_printers()
        self.menu_bar.verify_after_oobe_printersmenu()

    def test_04_check_printersmenu_withprinterselected(self):
        '''
        TestRail:#C14590879
        PreConditions Printer must be added to the Main UI and verify printers Menu
        '''
        logging.debug("PreConditions Printer must be added to the Main UI and verify printers Menu[C14590879]")
        self.menu_bar.click_menubar_printers()
        self.main_ui.click_find_printer_icon()
        self.device_picker.wait_for_screen_load()
        self.device_picker.set_value_to_search_box(self.printer_hostname)
        self.device_picker.click_searched_printer()
        time.sleep(5)
        self.tool_bar.click_home_btn()
        self.printer_setup_incomplete_dialog.click_ok_btn()
        self.main_ui.wait_for_printer_status_load()
        time.sleep(10)
        self.menu_bar.click_menubar_printers()
        self.menu_bar.verify_printersmenu_withprinterselected()

    def test_05_click_selectdifferentprinter(self):
        '''
        TestRail:#C14590881
        Click Printers->Select a Different Printer Expected Result Verify Device Picker is opened
        '''
        logging.debug("Click Printers->Select a Different Printer Expected Result Verify Device Picker is opened[C14590881]")
        self.menu_bar.click_menubar_printers_select_different_printer()
        self.device_picker.wait_for_screen_load()

    def test_06_click_invitetoprint(self):
        '''
        TestRail:#C14590883,#C14610672
        Click Printers->Invite to Print on Menu Bar
        Click HP Smart/Printers
        '''
        logging.debug("Click Printers->Invite to Print on Menu Bar.verify Print from other devices screen displays[C14590883]")
        logging.debug("Click HP Smart/Printers -> Any items which will open a new screen.Click Home button.Expected Result Verify the Home screen will display after click Home button.[C14610672]")
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_printer_status_load()
        self.menu_bar.click_menubar_printers()
        self.menu_bar.click_menubar_printers_invite_to_print()
        self.invite_to_print.wait_for_screen_load()

    def test_07_click_forgetthisprinter(self):
        '''
        TestRail:#C14590882,#C14610672
        Click Printers->Forget this Printer
        Click HP Smart/Printers
        '''
        logging.debug("Click Printers->Forget this Printer... on Menu Bar.Expected Result Verify the printer current in the center of the carousel is removedVerify if the printer is the only one on carousel, the big + icon will show[C14590882]")
        logging.debug("Click HP Smart/Printers -> Any items which will open a new screen.Click back button.Expected Result Verify the Home screen will display after click Back button.[C14610672]")
        time.sleep(5)
        self.tool_bar.click_back_btn()
        self.main_ui.wait_for_printer_status_load()
        time.sleep(3)
        self.menu_bar.click_menubar_printers()
        self.menu_bar.click_menubar_printers_forget_printer()
        self.main_ui.click_forget_printer_btn()
        self.main_ui.wait_for_find_printer_icon_display()

    def test_08_checkforupdate(self):
        '''
        TestRail:#C14590872
        Click the 'Check for Updates
        '''
        logging.debug("HP Smart App must not be up to dateIf the app under test is smaller than the released app version1. Go back to menu bar -> HP Smart2. Click the 'Check for Updates...'[C14590872]")
        time.sleep(3)
        self.tool_bar.click_close_btn()
        time.sleep(2)
        smart_utility.uninstall_app(self.password)
        time.sleep(10)
        smart_utility.install_app(self.package_path, self.password)
        time.sleep(10)
        self.common_flows.launch_hpsmart_app("HP Smart")
        self.checkforupdates_dialog.wait_for_new_software_available_load()
        self.checkforupdates_dialog.verify_new_update_availabled_dialog()
