# encoding: utf-8
'''
Description: It defines common flows in the hp smart application.

@author: Sophia
@create_date: May 6, 2019
'''

import pytest
import logging
import datetime
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.flows.flows_oobe import OOBEFlows
from MobileApps.libs.flows.mac.smart.screens.common.welcome import Welcome
from MobileApps.libs.flows.mac.smart.screens.common.agreement import Agreement
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.device_picker import DevicePicker
from MobileApps.libs.flows.mac.smart.screens.common.open_file_dialog import OpenFileDialog
from MobileApps.libs.flows.mac.smart.screens.common.save_dialog import SaveDialog
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.common.choose_a_printer_sheet import ChooseAPrinterSheet
from MobileApps.libs.flows.mac.smart.screens.printfile.print_screen import PrintScreen
from MobileApps.libs.flows.mac.smart.screens.scan.scanner import Scanner
from MobileApps.libs.flows.mac.smart.screens.scan.scan_result import ScanResult
from MobileApps.libs.flows.mac.smart.screens.scan.import_screen import ImportScreen
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.let_find_your_printer import FindYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.switch_to_using_wifi import SwitchToUsingWiFi
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_setting_scroll import PrinterSettingScroll
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_status import PrinterStatus
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_information import PrinterInformation
from MobileApps.libs.flows.mac.smart.screens.printersettings.printer_from_other_devices import PrinterFromOtherDevices
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
from MobileApps.libs.flows.mac.smart.screens.oobe.install_driver_to_print import InstallDriverToPrint
from MobileApps.libs.flows.mac.smart.screens.oobe.initialize_page import InitializePage
from MobileApps.libs.flows.mac.smart.screens.menubar.menu_bar import MenuBar
from MobileApps.libs.flows.mac.smart.screens.hpid.person_icon_flyout import PersonIconFlyout
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_in_page import SignInPage
from MobileApps.libs.flows.mac.smart.screens.hpid.getting_the_most_out_of_your_account import GettingTheMostOutOfYourAccount
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_in_dialog import SigninDialog
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_up_dialog import SignUpDialog
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_out_dialog import SignoutDialog
from MobileApps.libs.flows.mac.smart.screens.printersettings.print_anywhere import Print_Anywhere
from MobileApps.libs.flows.mac.smart.screens.smarttasks.smart_tasks import SmartTasks
from MobileApps.libs.flows.mac.smart.screens.printersettings.print_quality_tools import PrintQualityTools
from MobileApps.libs.flows.mac.smart.screens.printersettings.network_information import NetworkInformation
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connection import PrinterConnection
from MobileApps.libs.flows.mac.smart.screens.printersettings.advanced_settings import AdvancedSettings
from MobileApps.libs.flows.mac.smart.screens.menubar.privacy_settings import PrivacySettings
from MobileApps.libs.flows.mac.smart.screens.printersettings.forget_this_printer import ForgetThisPrinter
from MobileApps.libs.flows.mac.smart.screens.common.forget_printer_dialog import FogetPrinterDialog
from MobileApps.libs.flows.mac.smart.screens.common.sign_in_to_printer_dialog import SignInToPrinterDialog
from MobileApps.libs.flows.mac.smart.screens.common.find_the_printer_pin_dialog import FindThePrinterPINDialog
from MobileApps.libs.flows.mac.smart.screens.hpid.instant_ink_p2_page import InstantInkP2Page
from MobileApps.libs.flows.mac.smart.screens.menubar.reset_device_region import ResetDeviceRegion
from MobileApps.libs.flows.mac.smart.screens.mobilefax.mobile_fax_value_prop import MobileFaxValueProp
from MobileApps.libs.flows.mac.smart.screens.mobilefax.mobile_fax_agreement_page import MobileFaxAgreementPage
from MobileApps.libs.flows.mac.smart.screens.mobilefax.mobile_fax_home_page import MobileFaxHomePage
from MobileApps.libs.flows.mac.smart.screens.menubar.personalize_tiles import PersonalizeTiles
from MobileApps.libs.flows.mac.smart.screens.activitycenter.activity_center_flyout import ActivityCenterFlyout
from MobileApps.libs.flows.mac.smart.screens.activitycenter.activity_center_print import ActivityCenterPrint
from MobileApps.libs.flows.mac.smart.screens.activitycenter.activity_center_smart_tasks import ActivityCenterSmartTasks
from MobileApps.libs.flows.mac.smart.screens.helpsupport.help_support import HelpSupport
from MobileApps.libs.flows.mac.smart.screens.menubar.feedback import Feedback
from MobileApps.libs.flows.mac.smart.screens.common.save_this_password_dialog import Savethispassworddialog
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.smart.screens.psdr.diagnose_fix import DiagnoseFix
from MobileApps.libs.flows.mac.smart.screens.webapp.web_app_screen import WebAppScreen
from MobileApps.libs.flows.mac.smart.screens.hpid.to_sign_in_and_signing_out_dialog import ToSignInAndSigningOutDialog
from MobileApps.libs.flows.mac.smart.screens.common.cookie_settings_banner import CookieSettingsBanner
from MobileApps.libs.flows.mac.smart.screens.common.connected_printing_services import ConnectedPrintingServices


from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import ItemTypeError
from MobileApps.resources.const.mac.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.smart.utility.virtualprinter_utilities import SshHost


class CommonFlows(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def launch_HPSmart_app(self, app_name):
        '''
        This is a method to launch hp smart app.
        :parameter:
        :return:
        '''
        logging.debug("Launching HP Smart...")

        self.driver.open_app(app_name)

    def close_HPSmart_app(self):
        '''
        This is a method to close hp smart app.
        :parameter:
        :return:
        '''
        logging.debug("Closing HP Smart...")

        tool_bar = ToolBar(self.driver)
        tool_bar.click_close_btn()

    def navigate_to_main_page_from_welcome_page_without_sign_in(self, app_name):
        '''
        This is a flow from Welcome page to Main page Without Sign in.
        :parameter:
        :return:
        '''
        logging.debug("Go to Main page from Welcome page...")
        self.launch_HPSmart_app(app_name)
        self.go_to_main_page_from_welcome_screen_without_sign_in()

    def navigate_to_main_page_from_welcome_page_with_sign_in(self, app_name, username, password):
        '''
        This is a flow from Welcome page to Main page With Sign in.
        :parameter:
        :return:
        '''
        logging.debug("Go to Main page from Welcome page...")
        self.launch_HPSmart_app(app_name)
        self.go_to_main_page_from_welcome_screen_with_sign_in(username, password)

    def navigate_to_device_picker_from_welcome_page_without_sign_in(self, app_name):
        '''
        This is a flow from Welcome page to device_picker Without Sign in.
        :parameter:
        :return:
        '''
        logging.debug("Go to device_picker from Welcome page...")
        self.launch_HPSmart_app(app_name)
        self.go_to_sign_in_page_from_welcome_screen()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.click_sign_in_page_set_up_printer_btn()
        device_picker = DevicePicker(self.driver)
        device_picker.wait_for_screen_load(300)

    def go_to_sign_in_page_from_welcome_screen(self):
        '''
        This is a flow from Welcome to HP Smart screen to Sign In page.
        :parameter:
        :return:
        '''
        logging.debug("Go to Sign In screen from Welcome to HP Smart screen... ")

        welcome_screen = Welcome(self.driver)
        welcome_screen.wait_for_screen_load(300)
        sleep(5)
        welcome_screen.click_welcome_to_hp_smart_continue_btn()

        agreement_screen = Agreement(self.driver)
        agreement_screen.wait_for_screen_load(60)
        agreement_screen.click_yes_btn()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.wait_for_screen_load()

    def go_to_main_page_from_welcome_screen_with_sign_in(self, username, password):
        '''
        This is a flow from Welcome to HP Smart screen to Main page With Sign in.
        :parameter:
        :return:
        '''
        self.go_to_sign_in_page_from_welcome_screen()

        self.go_through_sign_in_flow_from_sign_in_page(username, password)

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(timeout=120)
        self.driver.performance.stop_timer("hpid_login", raise_e=False)

    def go_to_main_page_from_welcome_screen_without_sign_in(self):
        '''
        This is a flow from Welcome to HP Smart screen to Main page Without Sign in.
        :parameter:
        :return:
        '''
        self.go_to_sign_in_page_from_welcome_screen()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.click_sign_in_page_explore_hp_smart_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(timeout=120)
        main_screen.wait_for_find_printer_icon_display(timeout=120)

    def navigate_to_agreements_screen(self):
        '''
        This is a flow from welcome screen to agreement screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to Agreements screen from Welcome to HP Smart screen... ")

        welcome_screen = Welcome(self.driver)
        welcome_screen.wait_for_screen_load(120)
        welcome_screen.click_continue_btn()

        agreement_screen = Agreement(self.driver)
        agreement_screen.wait_for_screen_load(60)

    def go_to_oobe_initial_screen(self):
        '''
        This is a flow from agreement screen to OOBE initial screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to OOBE screen from Agreements screen... ")

        agreement_screen = Agreement(self.driver)
        agreement_screen.click_yes_btn()

    def navigate_to_oobe_flow(self, app_name):
        '''
        This is a flow from launch HP smart to post OOBE initial screen.
        :parameter:
        :return:
        '''
        self.launch_HPSmart_app(app_name)
        self.navigate_to_agreements_screen()
        self.go_to_oobe_initial_screen()

    def go_to_main_ui_after_post_oobe(self, printer_type, is_multi_printers=False, printer_name=None):
        '''
        This is a flow from OOBE initial screen then go through OWS flow and end with main UI.
        :parameter: is_multi_printers--If there has more than 1 printer installed in the system.
                    printer_name--If there has more than 1 printer installed, which printer app need choose.
        :return:
        '''
        logging.debug("Go to Main UI screen after post OOBE workflow... ")

        self.go_to_oobe_initial_screen()

        if is_multi_printers:
            # TODO:
            pass

        oobe_flow = OOBEFlows(self.driver)
        oobe_flow.go_through_ows_flow(printer_type)

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(timeout=120)

    def navigate_to_main_ui_skip_oobe_flow(self, is_multi_printers=False, printer_name=None):
        '''
        This is flow from OOBE initial screen to main UI with skipping OWS flow.
        :parameter: is_multi_printers--If there has more than 1 printer installed in the system.
                    printer_name--If there has more than 1 printer installed, which printer app need choose.
        :return:
        '''
        logging.debug("Go to Main UI screen skip post OOBE workflow... ")

        self.go_to_oobe_initial_screen()

        if is_multi_printers:
            choose_a_printer_sheet = ChooseAPrinterSheet(self.driver)
            choose_a_printer_sheet.wait_for_screen_load()

            if printer_name is None:
                choose_a_printer_sheet.click_skip_btn()
            else:
                pass  # TODO List

        sign_in_to_printer_dialog = SignInToPrinterDialog(self.driver)
        if sign_in_to_printer_dialog.wait_for_screen_load(raise_e=False):
            sign_in_to_printer_dialog.click_cancel_btn()
        find_the_printer_pin_dialog = FindThePrinterPINDialog(self.driver)
        if find_the_printer_pin_dialog.wait_for_screen_load(timeout=2, raise_e=False):
            find_the_printer_pin_dialog.click_cancel_btn()

        self.back_to_main_ui_by_click_home_btn()

    def print_file_using_default_settings(self, printtype, filename, is_print=False, is_remote_printer=False):
        '''
        This is a method to print documents or print photo with app default settings.
        :parameter:
        :return:
        '''
        if (smart_const.PRINT_TYPE.PHOTO == printtype):
            logging.debug("Print photo ...")
            self.go_to_print_photo_dialog(filename)
        elif (smart_const.PRINT_TYPE.DOCUMENT == printtype):
            logging.debug("Print document ...")
            self.go_to_print_document_dialog(filename)
        else:
            raise ItemTypeError("Print type is incorrect, please check ...")

        print_screen = PrintScreen(self.driver)

        if is_print:
            print_screen.click_print_btn()
        else:
            self.cancel_print_job()
            if (smart_const.PRINT_TYPE.PHOTO == printtype):
                print_screen.click_cancel_btn_on_print_photo()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def print_file_using_default_settings_with_remote_printer(self, filename):
        '''
        This is a method to print documents or print photo with app default settings.
        :parameter:
        :return:
        '''
        print_screen = PrintScreen(self.driver)
        self.go_to_print_document_dialog(filename)
        sleep(60)
        print_screen.click_print_btn_with_remote_printer()
        print_screen.wait_for_file_sent_dialog_load(120)
        print_screen.click_file_sent_dialog_ok_btn()
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def print_file_using_customer_settings(self, printtype, filename, customer_settings, is_print=False):
        '''
        This is a method to print documents or print photo with customer settings.
        :parameter:
        :return:
        '''
        if(smart_const.PRINT_TYPE.PHOTO == printtype):
            logging.debug("Print photo ...")
            self.go_to_print_photo_dialog(filename)
        elif(smart_const.PRINT_TYPE.DOCUMENT == printtype):
            logging.debug("Print document ...")
            self.go_to_print_document_dialog(filename)
        else:
            raise ItemTypeError("Print type is incorrect, please check ...")

        print_screen = PrintScreen(self.driver)
        print_screen.set_up_print_settings(customer_settings)

        if is_print:
            print_screen.click_print_btn()
        else:
            self.cancel_print_job()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def print_file_from_scan(self, is_print=False):
        '''
        This is a method to print documents or print photo with app default settings.
        :parameter:
        :return:
        '''
        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.click_print_btn()

        print_screen = PrintScreen(self.driver)
        if is_print:
            print_screen.click_print_btn()
        else:
            self.cancel_print_job()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def go_to_print_photo_dialog(self, filename):
        '''
        This is a flow from main UI screen to print photo dialog.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

        sleep(1)
        main_screen.click_print_photo_tile()

        print_screen = PrintScreen(self.driver)
        print_screen.click_browser_btn()

        self.select_photo(filename)

    def go_to_print_document_dialog(self, filename):
        '''
        This is a flow from main UI screen to print document dialog.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

        sleep(1)
        main_screen.click_print_document_tile()

        print_screen = PrintScreen(self.driver)
        if(print_screen.wait_for_support_sheet_load(raise_e=False)):
            print_screen.click_ok_support_file()

        self.select_file(filename)

    def cancel_print_job(self):
        '''
        This is a method to cancel print job
        :parameter:
        :return:
        '''
        print_screen = PrintScreen(self.driver)
        print_screen.click_cancel_btn()

    def go_through_start_smart_tasks_flow(self):
        '''
        This is a flow to start a smart tasks.
        :parameter:
        :return:
        '''
        scanner_screen = Scanner(self.driver)
        if scanner_screen.wait_for_new_scan_auto_enhancements_dialog_load(raise_e=False):
            scanner_screen.click_new_scan_auto_enhancements_dialog_get_started_btn()
        scanner_screen.wait_for_screen_load()

        sleep(5)
        scanner_screen.click_scan_btn()

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.wait_for_scan_result_smart_tasks_screen_load(120)
        scan_result_screen.click_start_smart_task_btn()
        scan_result_screen.verify_your_smart_task_is_on_its_way_dialog()
        scan_result_screen.click_your_smart_task_is_on_its_way_dialog_home_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def go_to_scan_screen_from_main_ui(self):
        '''
        This is a flow from main UI to scanner screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to Scan screen from main UI...")

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

        main_screen.click_scan_tile()

        scanner_screen = Scanner(self.driver)
        if scanner_screen.wait_for_new_scan_auto_enhancements_dialog_load(raise_e=False):
            scanner_screen.click_new_scan_auto_enhancements_dialog_get_started_btn()
        scanner_screen.wait_for_screen_load()

    def scan_on_scanner(self):
        '''
        This is a flow from scanner screen to scan result screen.
        :parameter:
        :return:
        '''
        logging.debug("Scan on Scanner Screen...")

        scanner_screen = Scanner(self.driver)
        scanner_screen.wait_for_screen_load()

        sleep(5)
        scanner_screen.click_scan_btn()

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.wait_for_screen_load(120)

    def go_to_scan_result_page_from_main_ui(self):
        '''
        This is a flow from main ui to scan result page
        :parameter:
        :return:
        '''
        logging.debug("go to scan result page from main ui")
        self.go_to_scan_screen_from_main_ui()
        self.scan_on_scanner()

    def scanner_using_default_settings(self):
        '''
        This is a method to scan a document with app default settings.
        :parameter:
        :return:
        '''
        logging.debug("Scanner ...")

        self.go_to_scan_screen_from_main_ui()

        self.scan_on_scanner()

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.click_save_btn()

        save_screen = SaveDialog(self.driver)
        save_screen.wait_for_screen_load()

        save_screen.click_save_btn()
        save_screen.click_ok_btn_file_saved_sheet()

        self.go_to_main_ui_from_scan_result()

    def import_file_using_default_settings(self, filename, is_first_import=True):
        '''
        This is a method to import a file in the scan section.
        :parameter:
        :return:
        '''
        logging.debug("Import photo...")

        self.go_to_scan_screen_from_main_ui()

        self.go_to_open_import_file_from_scanner(
            is_first_import=is_first_import)

        self.select_file(filename)

        self.go_to_scan_result_from_adjust_boundary()

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.click_save_btn()

        save_screen = SaveDialog(self.driver)
        save_screen.wait_for_screen_load()

        save_screen.click_save_btn()
        save_screen.click_ok_btn_file_saved_sheet()

        self.go_to_main_ui_from_scan_result()

    def go_to_open_import_file_from_scanner(self, is_first_import=True):
        '''
        This is a flow from scanner screen to open file dialog in the import section.
        :parameter:
        :return:
        '''
        logging.debug("Go to import file screen from scanner screen...")

        scanner_screen = Scanner(self.driver)
        scanner_screen.click_import_btn()

        import_screen = ImportScreen(self.driver)
        if(is_first_import & import_screen.wait_for_first_import_dialog()):
            import_screen.click_get_started_btn_on_first_import_sheet()

        open_file_dialog = OpenFileDialog(self.driver)
        open_file_dialog.wait_for_screen_load()

    def go_to_scan_result_from_adjust_boundary(self):
        '''
        This is a flow from adjust boundary screen to screen result screen.
        :parameter:
        :return:
        '''
        logging.debug(
            "Go to scan result screen from adjust boundary screen...")

        import_screen = ImportScreen(self.driver)
        import_screen.wait_for_screen_load()

        import_screen.click_apply_btn()

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.wait_for_screen_load()

    def go_to_main_ui_from_scan_result(self):
        '''
        This is a flow from scan result screen to main UI.
        :parameter:
        :return:
        '''
        logging.debug("Go to main UI from scan result screen...")

        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.wait_for_screen_load()

        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()
        if scan_result_screen.wait_for_exit_without_saving_dialog(timeout=3, raise_e=False):
            scan_result_screen.click_yes_btn_on_exit_dialog()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def select_photo(self, filename):
        '''
        This is a method to select photo in the open file dialog.
        :parameter:
        :return:
        '''
        logging.debug("Select photo :" + filename + "...")

        open_file_dialog = OpenFileDialog(self.driver)
        open_file_dialog.wait_for_screen_load()

        open_file_dialog.select_file_by_coordinates(filename)
        open_file_dialog.click_open_btn()

    def select_file(self, filename):
        '''
        This is a method to select file in the open file dialog.
        :parameter:
        :return:
        '''
        logging.debug("Select file :" + filename + "...")

        open_file_dialog = OpenFileDialog(self.driver)
        open_file_dialog.wait_for_screen_load()

        open_file_dialog.select_file_by_coordinates(filename)
        open_file_dialog.click_open_btn()

    def go_to_printer_settings_from_main_ui(self):
        '''
        This is flow from main UI to printer settings.
        :parameter:
        :return:
        '''
        logging.debug("Go to printer settings from main UI...")

        main_screen = MainUI(self.driver)
        main_screen.click_printer_settings_tile()

        printer_settings = PrinterInformation(self.driver)
        printer_settings.wait_for_screen_load()

        return printer_settings

    def go_to_print_anywhere_from_main_local_printer(self, claimed=False, sign_in=False):
        '''
        This is a method to go to Print Anywhere screen from Main UI for local printer.
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        printer_settings.click_print_anywhere_tab()

        print_anywhere_tab = Print_Anywhere(self.driver)
        if not claimed:
            print_anywhere_tab.verify_print_anywhere_screen(sign_in)
        elif sign_in:
            print_anywhere_tab.verify_manage_print_anywhere_screen()
        else:
            print_anywhere_tab.verify_print_anywhere_screen(sign_in)

    def go_to_print_anywhere_from_main_remote_printer(self, owned_remote_printer=True):
        '''
        This is a method to go to Print Anywhere screen from Main UI for remote printer.
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        printer_settings.click_print_anywhere_tab()

        print_anywhere_tab = Print_Anywhere(self.driver)
        if owned_remote_printer:
            print_anywhere_tab.verify_manage_print_anywhere_screen()
        else:
            print_anywhere_tab.verify_print_anywhere_enabled_screen()

    def go_to_print_quality_tools_from_main(self, gen2=True):
        '''
        This is a method to go to print quality tools from Main UI
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        if gen2:
            printer_settings.click_print_quality_tools_tab()
        else:
            printer_settings.click_printer_reports_tab()
        print_quality_tools = PrintQualityTools(self.driver)
        print_quality_tools.wait_for_screen_load()

    def go_to_network_information_from_main(self, LEDM=True, offline=False):
        '''
        This is a method to go to Network Information page from Main UI
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        sleep(5)
        printer_settings.click_network_information_tab()

        network_information = NetworkInformation(self.driver)
        if offline:
            printer_settings.wait_for_screen_load()
        else:
            if LEDM:
                network_information.wait_for_screen_load()
            else:
                network_information.wait_for_screen_load_non_ledm()

    def go_to_advanced_settings_from_main(self):
        '''
        This is a method to go to Advanced Settings page from Main UI
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        printer_settings.click_advanced_settings_tab()

        ews = AdvancedSettings(self.driver)
        ews.wait_for_screen_load()

    def go_to_printer_from_other_devices_from_main_ui(self):
        '''
        This is flow from main UI to printer settings.
        :parameter:
        :return:
        '''
        logging.debug("Go to printer from other devices from main UI...")

        printer_settings = self.go_to_printer_settings_from_main_ui()
        printer_settings.click_print_from_other_devices_tab()

        printer_from_other_devices = PrinterFromOtherDevices(self.driver)
        printer_from_other_devices.wait_for_screen_load()

    def go_to_forget_this_printer_from_main_ui(self):
        '''
        This is flow from main UI to Forget This Printer screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to Forget This Printer from main UI...")

        self.go_to_printer_settings_from_main_ui()
        printer_settings = PrinterSettingScroll(self.driver)
        printer_settings.click_forget_this_printer_tab()

        forget_this_printer = ForgetThisPrinter(self.driver)
        forget_this_printer.verify_forget_this_printer_screen()

    def go_to_printer_status_tab_from_main_ui(self):
        '''
        This is flow from main UI to printer status tab.
        :parameter:
        :return:
        '''
        logging.debug("Go to printer status tab from main UI...")

        main_screen = MainUI(self.driver)
        main_screen.click_printer_status_image()

        printer_status_tab = PrinterStatus(self.driver)
        printer_status_tab.wait_for_screen_load()

    def back_to_main_ui_from_printer_settings(self):
        '''
        This is flow from printer settings to main UI.
        :parameter:
        :return:
        '''
        logging.debug("Back to main UI from printer settings...")

        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def go_to_device_picker_from_main_page(self, is_first_add=True):
        '''
        This is a flow method to go to device picker screen from main page.
        :parameter: is_first_add - True means HP Smart is the first time to add a printer, you should click Big Plus icon; False means it's not the first time to add the printer, you should click small plus icon.
        :return:
        '''
        logging.debug("Click Big Plus icon or Small plus icon to go to device picker screen")

        if is_first_add:
            main_screen = MainUI(self.driver)
            main_screen.click_find_printer_icon()
        else:
            tool_bar = ToolBar(self.driver)
            tool_bar.click_select_printer_btn()

        device_picker = DevicePicker(self.driver)
        device_picker.wait_for_screen_load(300)
        return device_picker

    def select_a_printer_on_device_picker(self, printer):
        '''
        This is a method to select a printer with IP on Device picker screen.
        :parameter:
        :return:
        '''
        device_picker = DevicePicker(self.driver)
        device_picker.click_search_box()
        device_picker.set_value_to_search_box(printer["printerIP"])
        if device_picker.wait_for_trying_to_communicate_string_load(timeout=2, raise_e=False):
            device_picker.wait_for_trying_to_communicate_string_disappear(60)
        device_picker.wait_for_first_searched_printer_load()
        device_picker.click_searched_printer()

    def add_printers_to_carousel(self, printers, is_skip_ows=False):
        '''
        This is a method to add more than 1 printers in the carousel.
        :parameter:
        :return:
        '''
        logging.debug("Start to add printers to carousel...")

        add_time = 0
        for printer in printers:
            sleep(2)

            if(add_time > 0):
                self.add_printer_to_carousel(printer, is_first_add=False, is_skip_ows=is_skip_ows)
            else:
                self.add_printer_to_carousel(printer, is_skip_ows=is_skip_ows)
            add_time += 1

    def add_printer_to_carousel(self, printer, is_first_add=True, is_skip_ows=False, is_usb=False, is_remote=False):
        '''
        This is a method to add 1 printer into carousel.
        :parameter:
        :return:
        '''
        logging.debug("Start to add printer to carousel...")

        device_picker = self.go_to_device_picker_from_main_page(is_first_add=is_first_add)
        if is_remote:
            device_picker.input_remote_to_search_box()
            device_picker.wait_for_first_searched_printer_load()
            device_picker.click_remote_printer(printer['printerBonjourName'])
        else:
            if is_usb:
                device_picker.click_usb_text()
                printer_connection = PrinterConnection(self.driver)
                if printer_connection.wait_for_screen_load(raise_e=False):
                    printer_connection.click_not_now_btn()
            else:
                self.select_a_printer_on_device_picker(printer)

            sleep(2)
            if is_skip_ows:
                ows_screen = OWS(self.driver)
                install_driver_to_print = InstallDriverToPrint(self.driver)
                sign_in_to_printer_dialog = SignInToPrinterDialog(self.driver)
                if sign_in_to_printer_dialog.wait_for_screen_load(raise_e=False):
                    sign_in_to_printer_dialog.click_cancel_btn()
                connected_printing_services = ConnectedPrintingServices(self.driver)
                if connected_printing_services.wait_for_screen_load(timeout=120, raise_e=False):
                    sleep(2)
                    connected_printing_services.click_connected_printing_sevices_continue_btn()
                if (ows_screen.wait_for_enjoy_hp_account_load(timeout=60, raise_e=False) or ows_screen.wait_for_hp_instant_ink_advertisement_load(timeout=10, raise_e=False) or ows_screen.wait_for_time_to_install_ink_load(timeout=10, raise_e=False) or ows_screen.wait_for_help_hp_make_better_load(timeout=10, raise_e=False)):
                    tool_bar = ToolBar(self.driver)
                    tool_bar.click_home_btn()
                    printer_setup = PrinterSetupIncompleteDialog(self.driver)
                    printer_setup.wait_for_screen_load()
                    printer_setup.click_ok_btn()
                elif install_driver_to_print.wait_for_install_success_screen_load(timeout=120, raise_e=False):
                    install_driver_to_print.click_ok_btn()
            else:
                if connected_printing_services.wait_for_screen_load(180, raise_e=False):
                    connected_printing_services.click_connected_printing_sevices_continue_btn()
                oobe_flow = OOBEFlows(self.driver)
                oobe_flow.go_through_ows_flow(printer["printerType"])

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(120)

    def click_add_another_printer_from_menu_bar(self):
        '''
        This is a method to add printer from menu bar.
        :parameter:
        :return:
        '''
        logging.debug("add printer from menu bar...")

        menu_bar = MenuBar(self.driver)
        menu_bar.click_menubar_printers()
        menu_bar.click_add_setup_a_printer()
        device_picker = DevicePicker(self.driver)
        device_picker.wait_for_screen_load(300)

    def go_to_about_hp_smart_screen(self):
        '''
        This is a method to go to About HP Smart screen
        :parameter:
        :return:
        '''
        logging.debug("go to About HP Smart screen...")

        menu_bar = MenuBar(self.driver)
        menu_bar.click_menubar_hpsmart()
        menu_bar.click_menubar_hpsmart_abouthpsmart_btn()
        menu_bar.wait_for_about_hp_smart_screen_display()

    def set_up_a_new_printer_device_picker(self, is_first_add=True):
        '''
        This is a method to start OOBE flow by clicking set up a new printer from device picker screen.
        :parameter:
        :return:
        '''
        logging.debug("Click set up a new printer to start from device picker screen...")

        device_picker = self.go_to_device_picker_from_main_page(is_first_add=is_first_add)
        device_picker.click_setup_new_printer_btn()

    def click_back_on_printer_setup_incomplete_dialog(self):
        '''
        click back button to dismiss printer setup incomplete dialog.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()

        printer_setup = PrinterSetupIncompleteDialog(self.driver)
        printer_setup.wait_for_screen_load()
        printer_setup.click_back_btn()

    def back_to_main_ui_by_click_home_btn(self):
        '''
        click Home button to back to main UI.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()

        printer_setup = PrinterSetupIncompleteDialog(self.driver)
        if printer_setup.wait_for_screen_load(timeout=3, raise_e=False):
            printer_setup.click_ok_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(180)

    def back_to_main_ui_by_click_back_btn(self):
        '''
        click Back button to back to main UI.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_back_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(60)

    def back_to_main_ui_from_scan_results(self):
        '''
        This is a method to click Home button to back to main UI from Scan Results screen.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()

        scan_result = ScanResult(self.driver)
        scan_result.wait_for_exit_without_saving_dialog()
        scan_result.click_yes_btn_on_exit_dialog()
        self.close_flyer_on_main_ui()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def close_smart_tasks_awareness_modal(self):
        '''
        This is a method to close Smart Tasks Awareness modal on main page.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.wait_for_smart_tasks_awareness_modal_display(60)
        main_screen.click_close_btn_on_smart_tasks_awareness_modal()

    def close_mobile_fax_awareness_modal(self):
        '''
        This is a method to close Mobile Fax Awareness modal on main page.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(60)

        main_screen.wait_for_mobile_fax_awareness_modal_display()
        main_screen.click_close_btn_on_mobile_fax_awareness_modal()

    def close_flyer_on_main_ui(self):
        '''
        This is a method to close the print anywhere or smart task dialog on main ui.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        if main_screen.wait_for_smart_tasks_awareness_modal_display(raise_e=False):
            main_screen.click_close_btn_on_smart_tasks_awareness_modal()
        if main_screen.wait_for_mobile_fax_awareness_modal_display(raise_e=False):
            main_screen.click_close_btn_on_mobile_fax_awareness_modal()

    def go_through_sign_up_hp_account_flow(self, firstname, lastname, password, email_address=None):
        '''
        This is a flow to sign up HP account.
        :parameter:
        :return:
        '''
        if pytest.mac_os_version != "10.15":
            to_sign_in_or_create_hp_account_dialog = ToSignInAndSigningOutDialog(self.driver)
            to_sign_in_or_create_hp_account_dialog.wait_for_screen_load()
            to_sign_in_or_create_hp_account_dialog.click_dialog_continue_btn()

        sign_up_dialog = SignUpDialog(self.driver)
        sign_up_dialog.wait_for_screen_load(120)
        sleep(5)
        sign_up_dialog.input_first_name(firstname)
        sign_up_dialog.input_last_name(lastname)
        if not email_address:
            username = ma_misc.load_json_file(TEST_DATA.MAC_SMART_ACCOUNT)["mac_smart"]["email"]["username"]
            domain = username.split("@")[1]
            # use + to create sub email from main email account
            email_address = "{}+{:%Y_%m_%d_%H_%M_%S}@{}".format(username[0:username.rfind("@")], datetime.datetime.now(), domain)
        sign_up_dialog.input_email_address(email_address)
        sign_up_dialog.input_phone_number("5417534160")
        sign_up_dialog.input_password(password)
        sign_up_dialog.click_email_address_textfield()
        sign_up_dialog.input_confirm_password(password)
        sign_up_dialog.click_create_account_btn()
        self.driver.performance.start_timer("hpid_create_account")

        if pytest.mac_os_version != "10.15":
            save_this_password_dialog = Savethispassworddialog(self.driver)
            if (save_this_password_dialog.wait_for_screen_load(raise_e=False)):
                save_this_password_dialog.click_not_now_btn()
            do_you_want_to_allow_open_hp_smart_dialog = WebAppScreen(self.driver)
            do_you_want_to_allow_open_hp_smart_dialog.wait_for_do_you_want_to_allow_to_open_hp_smart_dialog_load()
            do_you_want_to_allow_open_hp_smart_dialog.click_do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn()

        getting_the_most_out_of_your_account_page = GettingTheMostOutOfYourAccount(self.driver)
        getting_the_most_out_of_your_account_page.wait_for_screen_load(60)
        getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_title()
        getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_continue_btn()

    def sign_up_hp_account_from_main_ui(self, firstname="GothamAuto", lastname="TestAuto", password="Aio1test", email_address=None):
        '''
        This is a method to sign up HP account from Main UI
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(timeout=120)

        tool_bar = ToolBar(self.driver)
        tool_bar.click_person_btn()

        person_icon_flyout = PersonIconFlyout(self.driver)
        person_icon_flyout.verify_person_icon_flyout_before_sign_in()
        person_icon_flyout.click_create_account_btn()

        self.go_through_sign_up_hp_account_flow(firstname, lastname, password, email_address)
        main_ui = MainUI(self.driver)
        main_ui.wait_for_screen_load(60)
        self.driver.performance.stop_timer("hpid_create_account")

    def sign_up_hp_account_from_mobile_fax(self, firstname="GothamAuto", lastname="TestAuto", password="Aio1test", email_address=None):
        '''
        This is a method to sign up HP account from Mobile Fax tile.
        :parameter:
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_mobile_fax_tile()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.wait_for_screen_load()
        sign_in_page.click_sign_in_page_create_account_btn()

        self.go_through_sign_up_hp_account_flow(firstname, lastname, password, email_address)

        logging.debug("Mobile Fax Value prop screen and Agreement page will show only one time for a new account")
        self.go_to_mobile_fax_agreement_page_from_value_page()

        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.verify_mobile_fax_home_page()

    def sign_up_hp_account_from_smart_tasks(self, firstname="GothamAuto", lastname="TestAuto", password="Aio1test", email_address=None):
        '''
        This is a method to sign up HP account from Smart Tasks tile wo Smart Tasks Welcome screen.
        :parameter:
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_smart_tasks_tile()

        sign_in_page = SignInPage(self.driver)
        sign_in_page.wait_for_screen_load()
        sign_in_page.click_sign_in_page_create_account_btn()

        self.go_through_sign_up_hp_account_flow(firstname, lastname, password, email_address)

    def go_through_sign_in_flow(self, username, password):
        '''
        This is a flow to sign in on HPID popup dialog.
        :parameter:
        :return:
        '''
        sign_in_dialog = SigninDialog(self.driver)
        sign_in_dialog.wait_for_screen_load(60)
        sign_in_dialog.input_username_inputbox(username)
        sign_in_dialog.click_sign_in_dialog_next_btn()
        sleep(5)
        sign_in_dialog.wait_for_sign_in_dialog_password_inputbox_load(60)
        sign_in_dialog.input_password_inputbox(password)
        sign_in_dialog.click_sign_in_dialog_sign_in_btn()
        self.driver.performance.start_timer("hpid_login")

        if pytest.mac_os_version != "10.15":
            save_this_password_dialog = Savethispassworddialog(self.driver)
            if (save_this_password_dialog.wait_for_screen_load(raise_e=False)):
                save_this_password_dialog.click_not_now_btn()
            do_you_want_to_allow_open_hp_smart_dialog = WebAppScreen(self.driver)
            do_you_want_to_allow_open_hp_smart_dialog.wait_for_do_you_want_to_allow_to_open_hp_smart_dialog_load()
            do_you_want_to_allow_open_hp_smart_dialog.click_do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn()
        else:
            sign_in_dialog.verify_dialog_disappear()
            sleep(1)

        getting_the_most_out_of_your_account_page = GettingTheMostOutOfYourAccount(self.driver)
        if getting_the_most_out_of_your_account_page.wait_for_screen_load(raise_e=False):
            getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_title()
            getting_the_most_out_of_your_account_page.click_getting_the_most_out_of_your_account_continue_btn()

    def go_through_sign_in_flow_from_sign_in_page(self, username, password):
        '''
        This is a flow to sign in on HPID popup dialog from Sign In Page.
        :parameter:
        :return:
        '''
        sign_in_page = SignInPage(self.driver)
        sign_in_page.wait_for_screen_load()
        sign_in_page.click_sign_in_page_sign_in_btn()

        if pytest.mac_os_version != "10.15":
            to_sign_in_or_create_hp_account_dialog = ToSignInAndSigningOutDialog(self.driver)
            to_sign_in_or_create_hp_account_dialog.wait_for_screen_load(60)
            to_sign_in_or_create_hp_account_dialog.click_dialog_continue_btn()

        self.go_through_sign_in_flow(username, password)

    def sign_in_hp_account_from_main_ui(self, username, password):
        '''
        This is a method to sign in HP account from Main UI
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_person_btn()

        person_icon_flyout = PersonIconFlyout(self.driver)
        person_icon_flyout.verify_person_icon_flyout_before_sign_in()
        person_icon_flyout.click_create_account_btn()

        if pytest.mac_os_version != "10.15":
            to_sign_in_or_create_hp_account_dialog = ToSignInAndSigningOutDialog(self.driver)
            to_sign_in_or_create_hp_account_dialog.wait_for_screen_load()
            to_sign_in_or_create_hp_account_dialog.click_dialog_continue_btn()

        sign_up_dialog = SignUpDialog(self.driver)
        sign_up_dialog.wait_for_screen_load(120)
        sign_up_dialog.click_already_have_an_hp_account_sign_in_btn()

        self.go_through_sign_in_flow(username, password)

        self.confirm_person_icon_in_sign_in_state()

    def sign_in_hp_account_from_anywhere_screen(self, username, password):
        '''
        This is a method to sign in HP account from anywhere screen
        :parameter:
        :return:
        '''
        print_anywhere = Print_Anywhere(self.driver)
        print_anywhere.click_sign_in_btn()
        self.go_through_sign_in_flow(username, password)

    def sign_in_hp_account_from_smart_task(self, username, password):
        '''
        This is a method to sign in HP account from Smart Tasks screen
        :parameter:
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_smart_tasks_tile()

        self.go_through_sign_in_flow_from_sign_in_page(username, password)

    def sign_in_hp_account_from_scan_result_smart_tasks(self, username, password):
        '''
        This is a method to sign in HP account from Smart Tasks on Scan Result screen
        :parameter:
        :return:
        '''
        self.go_to_scan_screen_from_main_ui()
        self.scan_on_scanner()
        scan_result = ScanResult(self.driver)
        scan_result.click_smart_tasks_btn()
        scan_result.wait_for_smart_task_sign_in_flyout_screen_load()
        scan_result.click_sign_in_btn_on_flyout()
        self.go_through_sign_in_flow(username, password)

    def sign_in_hp_account_from_p2_page(self, username, password):
        '''
        This is a method to sign in HP account from p2 page
        :parameter:
        :return:
        '''
        instant_ink_p2_page = InstantInkP2Page(self.driver)
        instant_ink_p2_page.click_try_it_free_for_a_month_btn()
        self.go_through_sign_in_flow(username, password)

    def sign_in_hp_account_from_print_photo(self, username, password):
        '''
        This is a method to sign in HP account from Print Photo title on Main UI.
        :parameter:
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_print_photo_tile()

        self.go_through_sign_in_flow_from_sign_in_page(username, password)

    def sign_out_hp_account(self):
        '''
        This is a method to sign in HP account from Main UI
        :parameter:
        :return:
        '''
#         for i in range(3):
#             tool_bar = ToolBar(self.driver)
#             tool_bar.click_person_btn(is_sign_in=True)
#             person_icon_flyout = PersonIconFlyout(self.driver)
#             if person_icon_flyout.wait_for_screen_load_sign_in(raise_e=False):
#                 flag_1 = person_icon_flyout.wait_for_screen_load_sign_in(raise_e=False)
#                 sleep(2)
#                 if flag_1:
#                     break
#             else:
#                 tool_bar.click_person_btn(is_sign_in=True)

        tool_bar = ToolBar(self.driver)
        tool_bar.click_person_btn(is_sign_in=True)

        person_icon_flyout = PersonIconFlyout(self.driver)
        person_icon_flyout.wait_for_screen_load_sign_in()
        person_icon_flyout.click_sign_out_btn()

        if pytest.mac_os_version != "10.15":
            signing_out_of_your_hp_account_dialog = ToSignInAndSigningOutDialog(self.driver)
            signing_out_of_your_hp_account_dialog.wait_for_screen_load()
            signing_out_of_your_hp_account_dialog.click_dialog_continue_btn()

            do_you_want_to_allow_open_hp_smart_dialog = WebAppScreen(self.driver)
            do_you_want_to_allow_open_hp_smart_dialog.wait_for_do_you_want_to_allow_to_open_hp_smart_dialog_load(120)
            do_you_want_to_allow_open_hp_smart_dialog.click_do_you_want_to_allow_to_open_hp_smart_dialog_allow_btn()
        else:
            sign_out_dialog = SignoutDialog(self.driver)
            sign_out_dialog.wait_for_screen_load(60)
            sign_out_dialog.click_sign_out_btn()
            sign_out_dialog.wait_for_sign_out_safari_dialog_load()
            sign_out_dialog.verify_dialog_disappear()

        main_page = MainUI(self.driver)
        main_page.wait_for_screen_load()
        sleep(5)

    def confirm_person_icon_in_sign_in_state(self):
        '''
        This is a method to confirm person icon turns to sign in state after sign in the account.
        :parameter:
        :return:
        '''
        main_ui = MainUI(self.driver)
        main_ui.wait_for_screen_load(60)

        tool_bar = ToolBar(self.driver)
        person_icon_flyout = PersonIconFlyout(self.driver)

        for i in range(3):
            tool_bar.click_person_btn(is_sign_in=True)
            if person_icon_flyout.wait_for_screen_load_sign_in(raise_e=False):
                break

    def align_printheads_semi_auto_flow(self):
        '''
        This is a method to go to align_printheads_flow
        :parameter:
        :return:
        '''
        print_quality_tools = PrintQualityTools(self.driver)
        print_quality_tools.click_align_printheads_image()
        print_quality_tools.wait_for_align_printheads_dialog_title_display()
        print_quality_tools.click_print_scan_alignment_page_btn()
        print_quality_tools.wait_for_busy_icon_display()
        print_quality_tools.wait_for_align_printheads_dialog_title_display(timeout=240)
        print_quality_tools.click_print_scan_alignment_page_btn()
        print_quality_tools.wait_for_busy_icon_display()
        print_quality_tools.wait_for_alignment_complete_title_display()

    def align_printheads_auto_flow(self):
        '''
        This is a method to go to align_printheads_auto_flow
        :parameter:
        :return:
        '''
        print_quality_tools = PrintQualityTools(self.driver)
        print_quality_tools.click_align_printheads_image()
        print_quality_tools.wait_for_busy_icon_display()
        print_quality_tools.wait_for_alignment_complete_title_display()

    def go_to_privacy_settings_from_menu_bar(self):
        '''
        This is a method to go to privacy settings screen
        :parameter:
        :return:
        '''
        menubar = MenuBar(self.driver)
        menubar.click_menubar_hpsmart()
        menubar.click_menubar_hpsmart_privacy_settings_btn()

        privacy_settings = PrivacySettings(self.driver)
        privacy_settings.wait_for_screen_load()

    def forget_printer_from_printer_settings(self, multiple_printer=False):
        '''
        This is a method to forget current printer from printer settings
        :parameter:
        :return:
        '''
        self.go_to_forget_this_printer_from_main_ui()
        forget_this_printer = ForgetThisPrinter(self.driver)
        forget_this_printer.click_forget_this_print_btn()
        forget_this_printer_dialog = FogetPrinterDialog(self.driver)
        forget_this_printer_dialog.verify_forget_this_printer_dialog()
        forget_this_printer_dialog.click_forget_printer_btn()
        main_ui = MainUI(self.driver)
        if not multiple_printer:
            main_ui.wait_for_find_printer_icon_display(60)
        else:
            main_ui.wait_for_screen_load()

    def go_to_p2_page_from_main_ui(self):
        '''
        This is a method to go to P2 page
        :parameter:
        :return:
        '''
        main_ui = MainUI(self.driver)
        main_ui.click_get_ink_tile()

    def make_ews_to_password_modal(self, password):
        '''
        This is a method to set password in ews only applicable to some printer
        '''
        ews = AdvancedSettings(self.driver)
        self.go_to_advanced_settings_from_main()
        ews.click_settings_tile_on_ews()
        if ews.wait_for_redirecting_to_secure_page_dialog_load(raise_e=False):
            ews.click_redirecting_to_secure_page_dialog_checkbox()
            ews.click_redirecting_to_secure_page_dialog_ok_btn()
        ews.wait_for_settings_item_load()
        ews.click_security_item_on_settings_page()
        sleep(2)
        ews.click_password_setting_on_settings_page()
        sleep(3)
        ews.enter_password(password)
        ews.confirm_password(password)
        ews.click_apply_btn_on_settings()
        ews.wait_for_changes_updated_successfully()
        self.back_to_main_ui_from_printer_settings()

    def update_ews_password(self, old_password, new_password):
        '''
        This is a method to update ews password for a password protected printer
        '''
        self.go_to_advanced_settings_from_main()
        ews = AdvancedSettings(self.driver)
        ews.click_settings_tile_on_ews()
        ews.wait_for_security_dialog_load()
        ews.enter_password_on_dialog(old_password)
        ews.click_security_dialog_ok_btn()
        ews.wait_for_security_dialog_disappear()
        ews.click_security_item_on_settings_page(password=True)
        sleep(2)
        ews.click_password_setting_on_settings_page()
        sleep(3)
        ews.enter_password(new_password)
        ews.confirm_password(new_password)
        ews.click_apply_btn_on_settings()
        ews.wait_for_changes_updated_successfully()
        self.back_to_main_ui_from_printer_settings()

    def remove_ews_password_from_printer_settings(self, password):
        '''
        This is a method to remove ews password from printer settings
        '''
        ews = AdvancedSettings(self.driver)
        ews.wait_for_screen_load()
        ews.click_settings_tile_on_ews()
        if ews.wait_for_security_dialog_load(raise_e=False):
            ews.enter_password_on_dialog(password)
            ews.click_security_dialog_ok_btn()
            ews.wait_for_security_dialog_disappear()
        ews.wait_for_settings_item_load()
        ews.click_security_item_on_settings_page(password=True)
        ews.click_password_setting_on_settings_page()
        sleep(2)
        ews.clear_password()
        ews.clear_confirm_password()
        ews.click_password_box()
        ews.click_apply_btn_on_settings()
        ews.wait_for_changes_updated_successfully()
        self.back_to_main_ui_from_printer_settings()

    def go_to_reset_device_region_screen_from_main_ui(self):
        '''
        This is a method to go to Reset Device Region Screen from Main UI.
        '''
        menu_bar = MenuBar(self.driver)
        menu_bar.click_menubar_hpsmart()
        menu_bar.verify_hp_smart_drop_down_list()
        menu_bar.click_menubar_hpsmart_abouthpsmart_btn()
        menu_bar.click_crtl_shift_on_about_hp_smart_screen()

        reset_device_region = ResetDeviceRegion(self.driver)
        reset_device_region.verify_reset_device_region_screen()

    def go_to_persionalize_tiles_page(self):
        '''
        This is a method to go to Persionalize Tiles screen
        :parameter:
        :return:
        '''
        menu_bar = MenuBar(self.driver)
        personalize_tiles_page = PersonalizeTiles(self.driver)
        menu_bar.click_menubar_hpsmart()
        menu_bar.click_menubar_personalize_tiles_btn()
        personalize_tiles_page.wait_for_screen_load()

    def check_mobile_fax_item_on_persionalize_tiles_page(self):
        '''
        This is a method to Check Mobile Fax item shows on personalize tiles page for supported fax printer.
        '''
        self.go_to_persionalize_tiles_page()
        personalize_tiles_page = PersonalizeTiles(self.driver)
        personalize_tiles_page.wait_for_mobile_fax_item_load()

    def enable_mobile_fax_tile_from_persionalize_tiles_page(self):
        '''
        This is a method to Enable Mobile Fax tiles from personalize tiles page.
        '''
        self.check_mobile_fax_item_on_persionalize_tiles_page()
        personalize_tiles_page = PersonalizeTiles(self.driver)
        personalize_tiles_page.click_mobile_fax_on_radio()
        self.back_to_main_ui_by_click_home_btn()

    def disable_mobile_fax_tile_from_persionalize_tiles_page(self):
        '''
        This is a method to Disable Mobile Fax tiles from personalize tiles page.
        '''
        self.check_mobile_fax_item_on_persionalize_tiles_page()
        personalize_tiles_page = PersonalizeTiles(self.driver)
        personalize_tiles_page.click_mobile_fax_off_radio()
        self.back_to_main_ui_by_click_home_btn()

    def go_to_mobile_fax_agreement_page_from_value_page(self):
        '''
        This is a flow to go to Mobile Fax Agreement page from Mobile Fax Value page.
        '''
        cookie_settings_banner = CookieSettingsBanner(self.driver)
        if cookie_settings_banner.wait_for_screen_load(raise_e=False):
            cookie_settings_banner.click_cookie_settings_banner_close_btn()
        mobile_fax_value_prop = MobileFaxValueProp(self.driver)
        mobile_fax_value_prop.verify_mobile_fax_value_prop_screen()
        sleep(2)
        mobile_fax_value_prop.click_get_started_btn()

        mobile_fax_agreement_page = MobileFaxAgreementPage(self.driver)
        mobile_fax_agreement_page.verify_mobile_fax_agreement_page()
        logging.debug("Click the check box on the mobile fax agreement screen, verify continue button is enabled")
        mobile_fax_agreement_page.click_i_agree_to_check_box()
        mobile_fax_agreement_page.select_no_option()
        mobile_fax_agreement_page.verify_continue_btn_enable()
        mobile_fax_agreement_page.click_continue_btn()

    def click_mobile_fax_tile_to_compose_fax_page_flow_without_sign_in(self, username, password):
        '''
        This is a flow to compose fax page from Main UI by clicking Mobile Fax Tiles (HPID not sign in before clicking).
        :parameter: username - Required HPID username
                    password - Required HPID password
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_mobile_fax_tile()

        self.go_through_sign_in_flow_from_sign_in_page(username, password)

        mobile_fax_value_prop = MobileFaxValueProp(self.driver)
        logging.debug("Mobile Fax Value prop screen and Agreement page will show only one time for a new account")
        if mobile_fax_value_prop.wait_for_screen_load(raise_e=False):
            self.go_to_mobile_fax_agreement_page_from_value_page()

        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.verify_mobile_fax_home_page()

    def click_mobile_fax_tile_to_compose_fax_page_flow_with_sign_in(self):
        '''
        This is a flow to compose fax page from Main UI by clicking Mobile Fax Tiles (HPID sign in before clicking).
        :parameter:
        :return:
        '''
        main_page = MainUI(self.driver)
        main_page.click_mobile_fax_tile()

        mobile_fax_value_prop = MobileFaxValueProp(self.driver)
        if mobile_fax_value_prop.wait_for_screen_load(raise_e=False):
            self.go_to_mobile_fax_agreement_page_from_value_page()

        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.verify_mobile_fax_home_page()

    def click_activity_center_mobile_fax_to_compose_fax_page_flow(self):
        '''
        This is a flow to compose fax page from Activity Center by clicking Mobile Fax option.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_bell_btn()
        activity_center_flyout = ActivityCenterFlyout(self.driver)
        activity_center_flyout.verify_activity_center_flyout_screen()
        activity_center_flyout.click_activity_center_mobile_fax()

        mobile_fax_value_prop = MobileFaxValueProp(self.driver)
        mobile_fax_home_page = MobileFaxHomePage(self.driver)
        if mobile_fax_value_prop.wait_for_screen_load(raise_e=False):
            logging.debug("Mobile Fax Value prop screen and Agreement page will show only one time for a new account")
            self.go_to_mobile_fax_agreement_page_from_value_page()
        elif mobile_fax_home_page.wait_for_fax_delivered_page_load(timeout=5, raise_e=False) or mobile_fax_home_page.wait_for_empty_sent_page_load(timeout=5, raise_e=False):
            logging.debug("Sent page shows after clicking mobile fax option from bell menu if the signed account is not the first sign in.")
            mobile_fax_home_page.click_compose_fax_menu()

        mobile_fax_home_page.wait_for_compose_fax_page_load(120)

    def mobile_fax_media_tab_scanner_flow(self):
        '''
        This is a flow to add a scan page by clicking Scanner option under Media tab.
        :parameter:
        :return:
        '''
        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.click_media_tab()
        mobile_fax_compose_fax_page.click_media_tab_scanner()

        scanner_screen = Scanner(self.driver)
        if scanner_screen.wait_for_new_scan_auto_enhancements_dialog_load(timeout=10, raise_e=False):
            scanner_screen.click_new_scan_auto_enhancements_dialog_get_started_btn()
        scanner_screen.wait_for_screen_load()
        scanner_screen.click_scan_btn()

        scan_result_mobile_fax = ScanResult(self.driver)
        scan_result_mobile_fax.wait_for_scan_result_mobile_fax_screen_load(120)
        scan_result_mobile_fax.click_continue_to_fax_btn()

    def send_a_fax_job_scanner_flow(self, recipient_phone_num, sender_fax_number, sender_name):
        '''
        This is a flow to add a scan page by clicking Scanner option under Media tab to send a fax.
        :parameter: recipient_phone_num - Fax number input under Recipient tab
                    sender_fax_number - Fax number input under Sender tab
                    sender_name - Fax name input under Sender tab
        :return:
        '''
        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.input_mobile_fax_recipient_information_flow(recipient_phone_num)
        mobile_fax_compose_fax_page.input_mobile_fax_sender_information_flow(sender_fax_number, sender_name)
        self.mobile_fax_media_tab_scanner_flow()
        mobile_fax_compose_fax_page.click_send_fax_btn_on_compose_fax_page_flow()

    def send_a_fax_job_files_photo_flow(self, recipient_phone_num, sender_fax_number, sender_name, file_name):
        '''
        This is a flow to add a supported file by clicking Files&Photo option under Media tab to send a fax.
        :parameter: recipient_phone_num - Fax number input under Recipient tab
                    sender_fax_number - Fax number input under Sender tab
                    sender_name - Fax name input under Sender tab
                    file_name - The selected file name
        :return:
        '''
        mobile_fax_compose_fax_page = MobileFaxHomePage(self.driver)
        mobile_fax_compose_fax_page.click_compose_fax_menu()
        mobile_fax_compose_fax_page.input_mobile_fax_recipient_information_flow(recipient_phone_num)
        mobile_fax_compose_fax_page.input_mobile_fax_sender_information_flow(sender_fax_number, sender_name)
#         sleep(1)
        mobile_fax_compose_fax_page.mobile_fax_media_tab_files_photo_flow(file_name)
        mobile_fax_compose_fax_page.click_send_fax_btn_on_compose_fax_page_flow()

    def go_to_supply_status_from_main_ui(self):
        '''
        This is a method to go to supply status from Main UI
        :parameter:
        :return:
        '''
        printer_settings = self.go_to_printer_settings_from_main_ui()
        printer_settings.click_supply_status_tab()

    def go_to_check_activity_center_fly_out_screen(self):
        '''
        This is a flow to go to Activity Center Fly-out screen by clicking bell icon.
        :parameter:
        :return:
        '''
        tool_bar = ToolBar(self.driver)
        tool_bar.click_bell_btn()

        activity_center_flyout = ActivityCenterFlyout(self.driver)
        activity_center_flyout.verify_activity_center_flyout_screen()

    def go_to_check_no_print_activity_available_screen(self):
        '''
        This is a flow to go to check No print Activity Available screen.
        :parameter:
        :return:
        '''
        self.go_to_check_activity_center_fly_out_screen()

        activity_center_flyout = ActivityCenterFlyout(self.driver)
        activity_center_flyout.click_activity_center_print()

        activity_center_print = ActivityCenterPrint(self.driver)
        activity_center_print.verify_no_print_activity_available_screen()
        activity_center_print.click_print_activity_center_close_btn()

    def go_to_check_smart_task_activity_center_screen(self, no_printer=False):
        '''
        This is a flow to go to check Smart Task Activity Center screen.
        :parameter:
        :return:
        '''
        self.go_to_check_activity_center_fly_out_screen(no_printer)

        activity_center_flyout = ActivityCenterFlyout(self.driver)
        activity_center_flyout.click_activity_center_smart_tasks()

        activity_center_st = ActivityCenterSmartTasks(self.driver)
        activity_center_st.wait_for_screen_load()

    def go_to_help_support_from_main_ui(self):
        '''
        This is a method to go to help support from Main UI
        :parameter:
        :return:
        '''
        main_ui = MainUI(self.driver)
        help_support = HelpSupport(self.driver)
        main_ui.click_help_center_tile()
        if help_support.wait_for_cookies_banner_screen(timeout=60, raise_e=False):
            help_support.click_cookies_banner_accept_all_cookies_btn()
        help_support.wait_for_screen_load()

    def go_to_give_us_feedback_screen_from_main_ui(self):
        '''
        This is a method to go to feedback from Main UI
        :parameter:
        :return:
        '''
        menu_bar = MenuBar(self.driver)
        feedback_screen = Feedback(self.driver)
        menu_bar.click_menubar_hpsmart()
        menu_bar.wait_for_hp_smart_drop_down_list_display()
        menu_bar.click_menubar_hpsmart_sendfeedback_btn()
        feedback_screen.wait_for_screen_load()

    def create_print_smart_tasks_flow(self, st_name):
        '''
        This is a flow to create a print smart task with default settings.
        :parameter: st_name - a smart tasks name
        :return:
        '''
        smart_tasks_screen = SmartTasks(self.driver)
        smart_tasks_screen.wait_for_create_smart_tasks_screen()
        smart_tasks_screen.input_smart_tasks_name(st_name)
        smart_tasks_screen.click_create_smart_tasks_print_destination()
        smart_tasks_screen.click_print_destination_on_toggle_btn()
        smart_tasks_screen.click_create_smart_tasks_done_btn()
        if smart_tasks_screen.wait_for_saved_dialog(timeout=60, raise_e=False):
            smart_tasks_screen.verify_saved_dialog()
            smart_tasks_screen.click_saved_dialog_back_to_smart_tasks_btn()
        else:
            smart_tasks_screen.verify_you_just_created_a_smart_task_dialog()
            smart_tasks_screen.click_you_just_created_a_smart_task_dialog_ok_btn()
        smart_tasks_screen.verify_my_smart_tasks_screen()

    def check_different_status_messages_of_printer(self, hostip, serial_number, printer_name):
        cj_printer_code = ma_misc.load_json_file(TEST_DATA.MAC_SMART_CJ_PIRNTER_CODE)[printer_name]
        main_screen = MainUI(self.driver)
        printer_settings = PrinterInformation(self.driver)
        sshhost = SshHost(hostip)
        for code, result in cj_printer_code.items():
                sshhost.control_virtual_printer(hostip, serial_number, code_number=code, method='setup')
                sleep(15)
                main_screen.verify_printer_status(result)
                self.go_to_printer_settings_from_main_ui()
                printer_settings.verify_status_value(result)
    #             except AssertionError as e:
    #                 logging.error("Verification error")
    #                 logging.exception(e)
                sshhost.control_virtual_printer(hostip, serial_number, method='resume')
                sleep(10)
                self.back_to_main_ui_from_printer_settings()
                main_screen.verify_printer_status_is_ready()

    def check_error_status_messages_in_printer_status_screen(self, hostip, serial_number, printer_name):
        cj_printer_code = ma_misc.load_json_file(TEST_DATA.MAC_SMART_CJ_PIRNTER_ERROR_CODE)[printer_name]
        main_screen = MainUI(self.driver)
        printer_status = PrinterStatus(self.driver)
        sshhost = SshHost(hostip)
        for code, string in cj_printer_code.items():
            sshhost.control_virtual_printer(hostip, serial_number, code_number=code, method='setup')
            sleep(10)
            main_screen.click_printer_status_image()
            printer_status.click_printer_status_title_1_item()
            printer_status.verify_printer_error_status_for_title(string['title'])
            for index in range(len(string['content'])):
                printer_status.verify_printer_error_status_for_contents(index, string['content'][index])
            for key, contents in string.items():
                if 'link' in key:
#                     printer_status.click_link_btn((len(string['content'])-1))
                    printer_status.click_link_btn(string['content'].index(string['link']))
                    printer_status.check_web_page_url(string['link'])
                if 'button' in key:
                    if (len(string['button'])) == 2:
#                     if printer_status.wait_for_left_btn_display(raise_e=False):
                        printer_status.verify_left_button(string['button'][0])
                        printer_status.verify_right_button(string['button'][1])
                    else:
                        printer_status.verify_button(string['button'][0])
            sshhost.control_virtual_printer(hostip, serial_number, method='resume')
            sleep(10)
            self.back_to_main_ui_from_printer_settings()
            main_screen.verify_printer_status_is_ready()

    def check_warning_status_messages_in_printer_status_screen(self, hostip, serial_number, printer_name):
        cj_printer_code = ma_misc.load_json_file(TEST_DATA.MAC_SMART_CJ_PIRNTER_WARNING_CODE)[printer_name]
        main_screen = MainUI(self.driver)
        printer_status = PrinterStatus(self.driver)
        sshhost = SshHost(hostip)
        for code, result in cj_printer_code.items():
            sshhost.control_virtual_printer(hostip, serial_number, code_number=code, method='setup')
            sleep(10)
            main_screen.click_printer_status_image()
            printer_status.verify_warning_text(result)
            sshhost.control_virtual_printer(hostip, serial_number, method='resume')
            sleep(10)
            self.back_to_main_ui_from_printer_settings()
            main_screen.verify_printer_status_is_ready()

    def create_email_smart_tasks_flow(self, st_name, email_address):
        '''
        This is a flow to create an email smart task with default settings.
        :parameter: st_name - a smart tasks name; email_address - the entered email recipients
        :return:
        '''
        smart_tasks_screen = SmartTasks(self.driver)
        smart_tasks_screen.wait_for_create_smart_tasks_screen()
        smart_tasks_screen.input_smart_tasks_name(st_name)
        smart_tasks_screen.click_create_smart_tasks_email_destination()
        smart_tasks_screen.click_email_destination_on_toggle_btn()
        smart_tasks_screen.input_email_recipients(email_address)
        smart_tasks_screen.click_create_smart_tasks_done_btn()
        if smart_tasks_screen.wait_for_saved_dialog(timeout=60, raise_e=False):
            smart_tasks_screen.verify_saved_dialog()
            smart_tasks_screen.click_saved_dialog_back_to_smart_tasks_btn()
        else:
            smart_tasks_screen.verify_you_just_created_a_smart_task_dialog()
            smart_tasks_screen.click_you_just_created_a_smart_task_dialog_ok_btn()
        smart_tasks_screen.verify_my_smart_tasks_screen()

    def create_save_to_smart_tasks_flow(self, st_name, email_address, password):
        '''
        This is a flow to create a print smart task with default settings.
        :parameter: st_name - a smart tasks name
        :return:
        '''
        smart_tasks_screen = SmartTasks(self.driver)
        smart_tasks_screen.wait_for_create_smart_tasks_screen()
        smart_tasks_screen.input_smart_tasks_name(st_name)
        smart_tasks_screen.click_create_smart_tasks_save_to_destination()
        smart_tasks_screen.click_save_to_destination_dropbox_on_toggle_btn()
        if smart_tasks_screen.wait_for_dropbox_login_dialog_load(60, raise_e=False):
            smart_tasks_screen.input_dropbox_login_in_dialog_email(email_address)
            smart_tasks_screen.input_dropbox_login_in_dialog_password(password)
            smart_tasks_screen.click_dropbox_login_in_dialog_sign_in_btn()
        smart_tasks_screen.wait_for_sign_in_progressing_ring_disappear(60)
        smart_tasks_screen.click_create_smart_tasks_done_btn()
        if smart_tasks_screen.wait_for_saved_dialog(timeout=60, raise_e=False):
            smart_tasks_screen.verify_saved_dialog()
            smart_tasks_screen.click_saved_dialog_back_to_smart_tasks_btn()
        else:
            smart_tasks_screen.verify_you_just_created_a_smart_task_dialog()
            smart_tasks_screen.click_you_just_created_a_smart_task_dialog_ok_btn()
        smart_tasks_screen.verify_my_smart_tasks_screen()

    def create_fixed_smart_tasks_flow(self, st_name, email_address, password):
        '''
        This is a flow to create a print smart task with default settings.
        :parameter: st_name - a smart tasks name
        :return:
        '''
        smart_tasks_screen = SmartTasks(self.driver)
        smart_tasks_screen.wait_for_create_smart_tasks_screen()
        smart_tasks_screen.input_smart_tasks_name(st_name)
        smart_tasks_screen.click_create_smart_tasks_print_destination()
        smart_tasks_screen.click_print_destination_on_toggle_btn()
        sleep(1)
        smart_tasks_screen.click_create_smart_tasks_email_destination()
        smart_tasks_screen.click_email_destination_on_toggle_btn()
        smart_tasks_screen.input_email_recipients(email_address)
        sleep(1)
        smart_tasks_screen.click_create_smart_tasks_save_to_destination()
        smart_tasks_screen.click_create_smart_tasks_save_to_destination()
        smart_tasks_screen.click_save_to_destination_dropbox_on_toggle_btn()
        if smart_tasks_screen.wait_for_dropbox_login_dialog_load(60, raise_e=False):
            smart_tasks_screen.input_dropbox_login_in_dialog_email(email_address)
            smart_tasks_screen.input_dropbox_login_in_dialog_password(password)
            smart_tasks_screen.click_dropbox_login_in_dialog_sign_in_btn()
        smart_tasks_screen.wait_for_sign_in_progressing_ring_disappear(60)
        smart_tasks_screen.click_create_smart_tasks_done_btn()
        if smart_tasks_screen.wait_for_saved_dialog(timeout=60, raise_e=False):
            smart_tasks_screen.verify_saved_dialog()
            smart_tasks_screen.click_saved_dialog_back_to_smart_tasks_btn()
        else:
            smart_tasks_screen.verify_you_just_created_a_smart_task_dialog()
            smart_tasks_screen.click_you_just_created_a_smart_task_dialog_ok_btn()
        smart_tasks_screen.verify_my_smart_tasks_screen()

    def execute_a_smart_task_flow_from_smart_tasks_home_screen(self):
        '''
        This is a flow to execute a smart task from Smart Tasks Home screen.
        :parameter:
        :return:
        '''
        smart_tasks_screen = SmartTasks(self.driver)
        smart_tasks_screen.wait_for_my_smart_tasks_screen()
        smart_tasks_screen.select_the_first_smart_task_item()
        smart_tasks_screen.click_my_smart_tasks_start_btn()
        self.go_through_start_smart_tasks_flow()

    def execute_a_smart_task_flow_from_scan_result_screen(self):
        '''
        This is a flow to execute a smart task from Scan Result screen.
        :parameter:
        :return:
        '''
        scan_result_screen = ScanResult(self.driver)
        scan_result_screen.wait_for_screen_load()
        scan_result_screen.click_smart_tasks_btn()
        scan_result_screen.verify_smart_tasks_flyout()
        scan_result_screen.click_smart_tasks_flyout_first_st_start_btn()
        scan_result_screen.verify_your_smart_task_is_on_its_way_dialog()
        scan_result_screen.click_your_smart_task_is_on_its_way_dialog_home_btn()
        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load()

    def go_to_diagnose_and_fix_screen_from_printer_menu(self):
        '''
        This is a flow to go to Diagnose and Fix screen by clicking Diagnose and Fix item from Printer menu .
        :parameter:
        :return:
        '''
        menu_bar = MenuBar(self.driver)
        menu_bar.click_menubar_printers()
        menu_bar.click_diagnose_fix()
        diagnose_and_fix_screen = DiagnoseFix(self.driver)
        diagnose_and_fix_screen.click_diagnose_and_fix_screen_start_btn()

    def set_up_printer_on_main_page(self):
        '''
        This is a flow to set up printer on main ui.
        :parameter:
        :return:
        '''
        main_screen = MainUI(self.driver)
        main_screen.click_set_up_btn()
        connected_printing_services = ConnectedPrintingServices(self.driver)
        connected_printing_services.wait_for_screen_load(timeout=300)
        sleep(3)
        connected_printing_services.click_connected_printing_sevices_continue_btn()
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(timeout=60)
        tool_bar = ToolBar(self.driver)
        tool_bar.click_home_btn()
        printer_setup = PrinterSetupIncompleteDialog(self.driver)
        printer_setup.wait_for_screen_load()
        printer_setup.click_ok_btn()
        main_screen.wait_for_screen_load(120)
        