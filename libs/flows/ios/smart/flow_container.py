import random
import string

from selenium.common.exceptions import *
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.app_settings import AppSettings
from MobileApps.libs.flows.ios.smart.box import Box
from MobileApps.libs.flows.ios.smart.camera import Camera
from MobileApps.libs.flows.ios.smart.copy import Copy
from MobileApps.libs.flows.ios.smart.clouds import Clouds
from MobileApps.libs.flows.ios.smart.dropbox import Dropbox
from MobileApps.libs.flows.ios.smart.facebook import Facebook
from MobileApps.libs.flows.ios.smart.files import Files
from MobileApps.libs.flows.ios.smart.gmail import Gmail
from MobileApps.libs.flows.ios.smart.google_drive import GoogleDrive
from MobileApps.libs.flows.ios.smart.safari import Safari
from MobileApps.libs.flows.ios.smart.home import Home
from MobileApps.libs.flows.ios.smart.message import Message
from MobileApps.libs.flows.ios.smart.moobe_awc import MoobeAwc
from MobileApps.libs.flows.ios.smart.moobe_setup_complete import MoobeSetupComplete
from MobileApps.libs.flows.ios.smart.moobe_ows import MoobeOws
from MobileApps.libs.flows.ios.smart.moobe_wac import MoobeWac
from MobileApps.libs.flows.ios.smart.notifications import Notifications
from MobileApps.libs.flows.ios.smart.personalize import Personalize
from MobileApps.libs.flows.ios.smart.photo_books import Photo_Books
from MobileApps.libs.flows.ios.smart.photos import Photos
from MobileApps.libs.flows.ios.smart.preview import Preview
from MobileApps.libs.flows.ios.smart.printer_settings import PrinterSettings
from MobileApps.libs.flows.ios.smart.printers import Printers
from MobileApps.libs.flows.ios.smart.scan import Scan
from MobileApps.libs.flows.ios.smart.share import ios_share_flow_factory
from MobileApps.libs.flows.ios.smart.welcome import Welcome
from MobileApps.libs.flows.web.softfax.softfax_offer import SoftfaxOffer
from MobileApps.libs.flows.web.softfax.softfax_welcome import MobileSoftfaxWelcome
from MobileApps.libs.flows.web.softfax.compose_fax import MobileComposeFax
from MobileApps.libs.flows.web.softfax.contacts import MobileContacts
from MobileApps.libs.flows.web.softfax.fax_history import MobileFaxHistory
from MobileApps.libs.flows.web.softfax.fax_settings import FaxSettings
from MobileApps.libs.flows.web.softfax.send_fax_details import SendFaxDetails
from MobileApps.libs.flows.web.help_center.help_center import IOSHelpCenter
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.common.edit.edit import IOSEdit
from MobileApps.libs.flows.web.privacy_statement.privacy_central import PrivacyCentral
from MobileApps.libs.flows.web.hp_id.hp_id import MobileHPID
from MobileApps.libs.flows.web.ows.value_prop import MobileValueProp
from MobileApps.libs.flows.web.smart.smart_welcome import SmartWelcome
from MobileApps.libs.flows.web.smart.privacy_preferences import PrivacyPreferences
from MobileApps.libs.flows.web.ows.ucde_privacy import MobileUCDEPrivacy
from MobileApps.libs.flows.ios.smart.smart_tasks import SmartTasks
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from MobileApps.libs.flows.web.hp_connect.printers_users import IOSPrintersUsers

from ios_settings.src.libs.ios_system_flow_factory import ios_system_flow_factory
from SAF.misc import saf_misc

from SPL.decorator import SPL_decorator
from SPL.driver.reg_printer import *

import pytest
import os

class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver

        self.fd = {"app_settings": AppSettings(driver),
                   "box": Box(driver),
                   "camera": Camera(driver),
                   "copy": Copy(driver),
                   "clouds": Clouds(driver),
                   "dropbox": Dropbox(driver),
                   "facebook": Facebook(driver),
                   "files": Files(driver),
                   "gmail": Gmail(driver),
                   "google_drive": GoogleDrive(driver),
                   "home": Home(driver),
                   "message": Message(driver),
                   "moobe_awc": MoobeAwc(driver),
                   "moobe_setup_complete": MoobeSetupComplete(driver),
                   "moobe_ows": MoobeOws(driver),
                   "moobe_wac": MoobeWac(driver),
                   "notifications": Notifications(driver),
                   "personalize": Personalize(driver),
                   "photos": Photos(driver),
                   "photo_books": Photo_Books(driver),
                   "preview": Preview(driver),
                   "printer_settings": PrinterSettings(driver),
                   "printers": Printers(driver),
                   "scan": Scan(driver),
                   "share": ios_share_flow_factory(driver),
                   "welcome": Welcome(driver),
                   "ios_system": ios_system_flow_factory(driver),
                   "hpid": MobileHPID(driver, context=-1),
                   "gmail_api": GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH),
                   "edit": IOSEdit(driver),
                   "softfax_offer": SoftfaxOffer(driver, context={"url": WEBVIEW_URL.SOFTFAX_OFFER}),
                   "softfax_welcome": MobileSoftfaxWelcome(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "softfax_compose_fax": MobileComposeFax(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "softfax_fax_history": MobileFaxHistory(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "fax_settings": FaxSettings(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "send_fax_details": SendFaxDetails(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "softfax_contacts": MobileContacts(driver, context={"url": WEBVIEW_URL.SOFTFAX}),
                   "help_center": IOSHelpCenter(driver, context=-1),
                   "safari": Safari(driver),
                   "ows_welcome": OWSWelcome(driver, context=-1),
                   "privacy_statement": PrivacyCentral(driver, context=-1),                   
                   "ows_value_prop": MobileValueProp(driver, context={"url": WEBVIEW_URL.VALUE_PROP}),
                   "welcome_web": SmartWelcome(driver, context={"url": WEBVIEW_URL.SMART_WELCOME}),
                   "privacy_preferences": PrivacyPreferences(driver, context={"url": WEBVIEW_URL.SMART_WELCOME}),
                   "ucde_privacy": MobileUCDEPrivacy(driver, context=-1),
                   "smart_tasks": SmartTasks(driver),
                   "hp_connect": HPConnect(driver, context={"url": WEBVIEW_URL.HP_CONNECT}),
                   "hpc_printers_users": IOSPrintersUsers(driver, context={"url": WEBVIEW_URL.HP_CONNECT}),
                   }

    @property
    def flow(self):
        return self.fd

    def change_stack(self, stack):
        self.driver.terminate_app(BUNDLE_ID.SMART)
        self.flow["ios_system"].switch_smart_app_stack(stack)
        self.driver.launch_app(BUNDLE_ID.SMART)

    ###############################################################################################################
    #
    #                               HOME // WELCOME(moobe) included
    #
    ##############################################################################################################

    def go_home(self, reset=False, stack="pie", button_index=1, username="", password="", create_account=False,
                share_usage_data=True, remove_default_printer=True):
        """
         @param button_index: int between 0-2 for the position of the ows value prop button
            - 0: setup printer
            - 1: use hp smart/sign in
            - 2: explore hp smart/skip now
        - From fresh installed app
        - navigate welcome screens
        - navigate ows value prop
        - Verify home
        - remove_default_printer: is default set to True, change to False for HP+ or other test accounts
                   wit printer paired
        """
        stack = stack.lower()
        if reset:
            self.driver.reset(BUNDLE_ID.SMART)
        self.fd["ios_system"].clear_safari_cache()
        if stack != "pie":  # pie stack is default server on iOS HP Smart
            self.change_stack(stack)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)
        self.fd["welcome_web"].verify_welcome_screen()
        # Click on Accept all button
        self.fd["welcome_web"].click_accept_all_btn()
        self.fd["ios_system"].handle_allow_tracking_popup(raise_e=False)
        # This change is for the issue AIOI-12918, where old welcome screen is showing up
        if self.driver.platform_version == '13':
            self.fd["welcome"].allow_notifications_popup(raise_e=False)
            if self.fd["welcome"].verify_an_element_and_click("share_usage_data_title", click=False, raise_e=False) is \
                    not False:
                self.fd["welcome"].swipe_down_scrollview()
                if share_usage_data:
                    self.fd["welcome"].select_yes()
                else:
                    self.fd["welcome"].select_no_option()

        # TODO: waiting on specs for webview timeout GDG-1768
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        if button_index == 1:
            # TODO: longer wait times in below method are due to existing issue- GDG-1768
            if not create_account:
                cc = {"wait_obj": "sign_in_button", "invisible": True, "timeout": 10}
            else:
                cc = {"wait_obj": "sign_up_form_create_account_button", "invisible": True, "timeout": 10}
            self.login_value_prop_screen(tile=False, stack=stack, username=username, password=password,
                                         create_account=create_account,
                                         change_check=cc)
            sleep(1)
            self.clear_popups_on_first_login()
            self.fd["home"].verify_home()
        else:
            self.fd["ows_value_prop"].select_value_prop_buttons(button_index)
            if self.driver.platform_version == '14':
                self.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)
        sleep(2)
        if remove_default_printer:
            self.remove_default_paired_printer()

    def clear_popups_on_first_login(self, timeout=15, smart_task=False, coachmark=True):
        sleep(2)
        self.fd["home"].allow_notifications_popup(timeout=timeout, raise_e=False)
        if self.driver.platform_version == '14':
            self.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)
        if smart_task:
            self.fd["home"].close_smart_task_awareness_popup()
        if coachmark:
            self.fd["home"].dismiss_tap_account_coachmark()

    # TODO: longer wait times in below method are due to existing issue- GDG-1768
    def login_value_prop_screen(self, tile=False, stack="pie", username="", password="", change_check=None,
                                create_account=False, webview=True,
                                timeout=60):
        if not (username and password) and not create_account:
            login_info = ma_misc.get_hpid_account_info(stack=stack, a_type="basic", claimable=False)
            username, password = login_info["email"], login_info["password"]
        if webview:
            self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=timeout)
            self.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=tile, timeout=timeout)
            self.fd["ows_value_prop"].select_value_prop_buttons(1)
        else:
            self.fd["ows_value_prop"].verify_native_value_prop_screen()
            self.fd["ows_value_prop"].select_native_value_prop_buttons(1)
        # TODO: longer wait times in below method are due to existing issue- GDG-1768
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=45)
        self.fd["hpid"].verify_hp_id_sign_in()
        
        if not create_account:
            self.fd["hpid"].login(username, password, change_check=change_check)
        else:
            self.fd["hpid"].click_create_account_link()
            self.create_new_user_account()

    def login_from_home_screen(self, stack="pie", username="", password="", change_check=""):
        if not (username and password):
            login_info = ma_misc.get_hpid_account_info(stack=stack, a_type="basic", claimable=False)
            username, password = login_info["email"], login_info["password"]
        self.fd["home"].select_create_account_icon()
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=30)
        self.fd["hpid"].click_sign_in_link_from_create_account()
        self.fd["hpid"].verify_hp_id_sign_in()
        self.fd["hpid"].login(username, password, change_check=change_check)

    def go_to_home_screen(self):
        if self.fd["home"].verify_home(raise_e=False) is False:
            self.driver.restart_app(BUNDLE_ID.SMART)
        if self.fd["home"].verify_home(raise_e=False) is False:
            self.fd["ios_system"].dismiss_software_update_if_visible()
            self.fd["home"].verify_home_tile(raise_e=True)

    def dismiss_tap_here_to_start(self):
        if self.fd["home"].verify_tap_here_to_start():
            self.fd["home"].select_tap_here_to_start()
            if self.driver.wait_for_object("_shared_cancel", raise_e=False) is not False:
                self.fd["home"].select_cancel()
            else:
                self.fd["home"].select_navigate_back()
            self.fd["home"].close_smart_task_awareness_popup()

    def setup_moobe_awc_ble(self, printer_name):
        """
        starts from 'Welcome' screen, ends on 'Connect to Printer Network' screen
        :param printer_name: shortened model name of the printer. i.e. "ENVY 5000 series"
        """
        self.go_home(verify_home=False)
        self.dismiss_tap_here_to_start()
        self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_moobe_printer_from_list(printer_name)
        self.fd["moobe_awc"].pass_weak_bluetooth_connection(timeout=20)

    def setup_moobe_awc_wifi(self, p_obj, app_settings=False, stack="pie"):
        """
        starts from 'Welcome' screen, ends on 'Connect to Printer Network' screen
        :param p_obj: Printer object from SPL. i.e. RegPrinter()
        :param app_settings: default False, set True to go through wifi setup through App Settings tab
        """
        self.go_home(reset=True, stack=stack)
        if app_settings:
            self.fd["home"].select_app_settings()
            self.fd["app_settings"].select_set_up_new_printer_cell()
            self.fd["printers"].handle_bluetooth_popup()
        else:
            self.dismiss_tap_here_to_start()
            self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_add_printer()
        self.fd["printers"].select_set_up_a_new_printer()
        self.fd["printers"].handle_location_popup(selection="allow")
        self.fd["app_settings"].verify_set_up_new_printer_ui_elements()
        self.fd["ios_system"].launch_ios_settings()
        self.fd["ios_system"].select_wifi_menu_item()
        beacon_ssid = p_obj.get_wifi_direct_information()['name']
        self.fd["ios_system"].select_wifi_by_ssid(beacon_ssid, None, security_type="None")
        self.driver.activate_app(BUNDLE_ID.SMART)

    def moobe_secure_ble(self, printer_name: str, ssid: str, password: str):
        """
        starts from 'Welcome' screen and performs secure BLE steps up to putting printer onto the network
        """
        self.go_home(verify_home=False)
        self.dismiss_tap_here_to_start()
        self.fd["home"].select_get_started_by_adding_a_printer()
        self.fd["printers"].select_moobe_printer_from_list(printer_name)
        self.fd["moobe_awc"].handle_location_popup(selection="allow")
        self.fd["moobe_awc"].connect_printer_to_network(ssid)
        self.fd["moobe_awc"].verify_network_loaded(ssid)
        self.fd["moobe_awc"].enter_wifi_pwd(password, press_enter=True)

    def moobe_wac(self, bonjour_name, ssid, dismiss_popup=False):
        """
        starts from 'Welcome' screen and performs WAC steps to connect device to printer
        if the path does not matter, set dismiss_popup to True for better reliability
        :param dismiss_popup: bool True to perform WAC via 'tap here to start' flow, False to go through printer screen
        :param bonjour_name: str printer bonjour name
        :param ssid: str network name 
        """
        if dismiss_popup:
            self.dismiss_tap_here_to_start()
            self.fd["home"].select_get_started_by_adding_a_printer()
            self.fd["printers"].select_moobe_printer_from_list(bonjour_name)
        else:
            self.fd["home"].select_tap_here_to_start()
            if self.fd['printers'].verify_printers_nav(raise_e=False):
                # if there are multiple WAC supported printers in moobe mode
                self.fd["printers"].select_moobe_printer_from_list(bonjour_name)
            else:
                # could fail here if requested printer connection is lost
                self.fd["printers"].verify_found_printer_for_setup(bonjour_name)
                self.fd["printers"].select_continue()
        self.fd["printers"].verify_automatically_put_device_on_network()
        self.fd["printers"].select_yes()
        self.fd["moobe_wac"].verify_accessory_setup(ssid=ssid, accessory_name=bonjour_name)
        self.fd["moobe_wac"].select_next()
        self.fd["moobe_wac"].verify_setup_complete()

    def moobe_connect_printer_to_wifi(self, ssid_name="rd", wifi_password="1213141567890"):
        """
        Starts on 'Connect to Printer Network' screen, ends on "Printer Connected screen" signaling end of AWC
        :param ssid_name: name of the ssid
        :param wifi_password: password for specified ssid:
        """
        self.fd["moobe_awc"].verify_network_loaded(ssid_name)
        self.fd["moobe_awc"].enter_wifi_pwd(wifi_password, press_enter=True)
        self.fd["moobe_awc"].verify_connecting_to_printer()
        retry = False
        try:
            self.fd["moobe_awc"].select_retry_button(timeout=120)
            retry = True
        except TimeoutException:
            logging.info("Retry popup did not occur")
        if retry:
            try:
                self.fd["moobe_awc"].verify_network_loaded(ssid_name)
                self.fd["moobe_awc"].enter_wifi_pwd(wifi_password, press_enter=True)
            except TimeoutException:
                logging.info("Retry button didn't go back to input Wi-Fi password screen")
        if self.fd["moobe_awc"].verify_reconnect_your_device_title():
            self.fd["ios_system"].launch_ios_settings()
            self.fd["ios_system"].select_wifi_menu_item()
            wpa = "WPA2" if self.driver.driver_info['platformVersion'].split(".")[0] == '12' else "WPA2/WPA3"
            self.fd["ios_system"].select_wifi_by_ssid(ssid_name, wifi_password, security_type=wpa)
            self.driver.activate_app(BUNDLE_ID.SMART)
        self.fd["moobe_awc"].verify_printer_connected_screen(timeout=60)

    def add_printer_by_ip(self, printer_ip, verify_ga=False):
        """
            - Warning: Starts from Home but does not count initial Home GA. (above go_home(self):is counting GA)
            select
        :return:
        """
        self.fd["home"].close_smart_task_awareness_popup()
        self.fd["home"].select_get_started_by_adding_a_printer()
        if self.fd["printers"].verify_bluetooth_popup(raise_e=False):
            self.fd["printers"].handle_bluetooth_popup()
        self.fd["printers"].add_printer_ip(printer_ip)
        self.fd["home"].handle_location_pop()
        self.fd["home"].close_smart_task_awareness_popup()
        self.fd["home"].verify_home()

    def remove_default_paired_printer(self):
        self.fd["home"].allow_notifications_popup(raise_e=False)
        self.fd["home"].handle_location_pop()
        if self.fd["home"].verify_add_your_first_printer(raise_e=False) is False:
            try:
                self.fd["home"].remove_printer()
            except NoSuchElementException:
                self.fd["home"].hide_printer()

    def select_printer_from_topbar(self, printer_ip, verify_ga=False):
        self.fd["home"].select_printer_plus_button_from_topbar()
        self.fd["printers"].verify_printers_nav()
        self.fd["printers"].select_add_printer()
        self.fd["printers"].verify_add_printer_screen()
        self.fd["printers"].select_add_printer_using_ip()
        self.fd["printers"].verify_connect_the_printer_screen()
        self.fd["printers"].search_for_printer_directly_using_ip(printer_ip)
        self.fd["printers"].select_is_this_your_printer()
        self.fd["home"].verify_home(ga=verify_ga)

    def create_account_from_homepage(self):
        self.fd["home"].select_create_account_icon()
        return self.create_new_user_account()

    def create_new_user_account(self, timeout=10, coachmark=True):
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=timeout)
        email, password = self.fd["hpid"].create_account()
        try:
            self.fd["home"].select_continue()
        except NoSuchElementException:
            self.fd["ucde_privacy"].skip_ucde_privacy_screen()
        self.clear_popups_on_first_login(coachmark=coachmark)
        return email, password

    def create_account_from_tile(self):
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=45)
        self.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=30)
        self.fd["ows_value_prop"].select_value_prop_buttons(0)
        return self.create_new_user_account(timeout=15)

    def create_account_from_app_settings(self):
        self.fd["home"].select_app_settings()
        self.fd['app_settings'].select_sign_in_option()
        self.create_new_user_account(timeout=15)

    ###############################################################################################################
    #
    #                               APP Settings
    #
    ##############################################################################################################

    def go_app_settings_screen_from_home(self):

        if not self.fd["app_settings"].verify_app_settings_screen(raise_e=False):
            self.fd["home"].select_settings_icon()

    ################################################################################################################
    #
    #                               Digital COPY
    #
    ###############################################################################################################

    def go_copy_screen_from_home(self):

        self.fd["home"].select_tile_by_name("_shared_str_copy_tile")
        self.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fd["copy"].verify_copy_screen()

    ###############################################################################################################
    #
    #                                   Print Photo
    #
    ##############################################################################################################
    def go_photos_screen_from_home(self, select_photo_tile=True):
        if self.fd["photos"].verify_photos_screen() is not False:
            return True
        else:
            self.go_to_home_screen()
            if select_photo_tile:
                self.fd["home"].select_tile_by_name(HOME_TILES.TILE_PRINT_PHOTOS)
            else:
                self.fd["home"].select_documents_icon()
            self.fd["photos"].select_allow_access_to_photos_popup()
            self.fd["photos"].select_my_photos()
            self.fd["photos"].verify_my_photos_screen()
            self.fd["photos"].select_recents_or_first_option()
            self.fd["photos"].verify_photos_screen()

    def select_multiple_photos_to_preview(self, select_tile=False, no_of_photos=2):
        self.go_photos_screen_from_home(select_photo_tile=select_tile)
        self.fd["photos"].select_multiple_photos(end=no_of_photos)
        self.fd["photos"].verify_multi_selected_photos_screen()
        self.fd["photos"].select_next_button()
        sleep(2)
        self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)

    def navigate_to_transform_screen(self):
        self.fd["preview"].go_to_print_preview_pan_view(pan_view=False)
        self.fd["preview"].select_transform_options(Preview.TRANSFORM_TXT)

    ###############################################################################################################
    #
    #                                          FILES // DOCUMENTS
    #
    ###############################################################################################################

    def go_hp_smart_files_screen_from_home(self, select_tile=False):
        if self.fd["files"].verify_hp_smart_files_screen(raise_e=False) is not False:
            return True
        else:
            self.go_to_home_screen()
            if select_tile is not False:
                self.fd["home"].select_tile_by_name(HOME_TILES.TILE_PRINT_DOCUMENTS)
            else:
                self.fd["home"].select_documents_icon()
            self.fd["photos"].select_allow_access_to_photos_popup()
            self.fd["files"].verify_files_screen()
            self.fd["files"].select_hp_smart_files_folder_icon()
            self.fd["files"].verify_hp_smart_files_screen()

    def go_hp_smart_files_and_delete_all_files(self):
        if not self.fd["files"].verify_hp_smart_files_screen(raise_e=False):
            self.go_hp_smart_files_screen_from_home()
        self.fd["files"].delete_all_hp_smart_files()

    def scan_and_save_file_in_hp_smart_files(self, printer_obj, file_name, no_of_pages=2, file_type="PDF",
                                             go_home=True):
        self.go_scan_screen_from_home(printer_obj)
        self.add_multi_pages_scan(no_of_pages)
        self.save_file_to_hp_smart_files_and_go_home(file_name, Preview.SHARE_AND_SAVE_BTN, file_type, go_home=go_home)

    ###############################################################################################################
    #
    #                              SCANNER  //  PREVIEW
    #
    ###############################################################################################################

    def go_scan_screen_from_home(self, printer_obj):
        """
        :param printer_obj: Printer object to connect
        :param select_scan_tile: Default is False, Set to True to select Scan Tile
        :return:
        """
        p = printer_obj.get_printer_information()

        if self.fd["scan"].verify_preview_button_on_scan_screen(raise_e=False):
            return True
        else:
            self.go_to_home_screen()
            if self.fd["home"].verify_printer_added() is False:
                self.add_printer_by_ip(printer_ip=p["ip address"])
            sleep(2)
            self.fd["home"].select_tile_by_name(HOME_TILES.TILE_SCAN)
            # close coach marks
            if self.fd["scan"].verify_second_close_btn() is not False:
                self.fd["scan"].select_second_close_btn()
            self.fd["scan"].verify_scanner_screen()

    def send_and_verify_email(self, from_email_id, to_email_id, subject="", content=""):

        subject = "{}_{}".format(subject, self.driver.driver_info["udid"])
        self.fd["gmail"].compose_and_send_email(to_email=to_email_id, subject_text=subject)
        time.sleep(5)
        msg_id = self.fd["gmail_api"].search_for_messages(q_from=from_email_id, q_to=to_email_id, q_unread=True,
                                                          q_subject=subject, q_content=content, timeout=300)
        msg = self.fd["gmail_api"].gmail.get_message(msg_id[0]['id'])
        self.fd["gmail_api"].delete_email(msg_id)
        return msg

    def add_multi_pages_scan(self, no_of_pages):
        for page in range(1, no_of_pages + 1):
            self.fd["scan"].select_scan_job()
            sleep(1)
            self.fd["preview"].nav_detect_edges_screen()
            self.fd["preview"].verify_preview_screen()
            if page == no_of_pages:
                break
            else:
                self.fd["preview"].select_add_page()

    def create_and_save_file_using_camera_scan_and_go_home(self, file_name):
        self.go_camera_screen_from_home(tile=False)
        self.multiple_manual_camera_capture(1)
        self.fd["preview"].verify_preview_screen()
        self.save_file_to_hp_smart_files_and_go_home(file_name, Preview.SHARE_AND_SAVE_BTN, file_type="jpg")

    # ------------------------------------------------------CAMERA---------------------------------------------------- #

    def go_camera_screen_from_home(self, tile=False, camera=True):
        if self.fd["home"].verify_home_tile() is False:
            self.go_to_home_screen()
        if tile:
            self.fd["home"].select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        else:
            self.fd["home"].select_scan_icon()
        self.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fd["camera"].select_popup_option(camera=camera)
        if self.fd["camera"].verify_second_close_btn() is not False:
            self.fd["camera"].select_second_close_btn()
        self.fd["camera"].verify_camera_screen()

    def multiple_manual_camera_capture(self, number, flash_option=FLASH_MODE.FLASH_OFF):
        """
        Precondition: start on the Camera flow
        :param number: number of images to take
        :param flash_option: flash mode for the camera
        :return: None
        """
        self.fd["camera"].capture_manual_photo_by_camera(flash_option)
        for _ in range(number - 1):
            self.fd["preview"].select_add_page()
            self.fd["camera"].capture_manual_photo_by_camera(flash_option)
        self.fd["preview"].dismiss_feedback_pop_up()

    ###############################################################################################################
    #
    #                              SHARE  //  SAVE //
    #
    ###############################################################################################################

    def save_file_to_hp_smart_files_and_go_home(self, file_name, option, file_type="jpg", go_home=True):
        """
        :param file_name: File name to rename file
        :param option:Select Save or Share option from tool bar and corresponding button
        :return:
        """
        if not self.fd["preview"].verify_preview_screen_title(Preview.SHARE_AND_SAVE_TEXT):
            self.fd["preview"].select_toolbar_icon(option)
        self.fd["preview"].dismiss_new_file_types_coachmark()
        self.fd["preview"].rename_file(file_name)
        self.fd["preview"].select_file_type(file_type)
        self.fd["preview"].select_navigate_back()
        self.fd["preview"].verify_file_type_selected(file_type, raise_e=True)
        self.fd["preview"].select_button(option)
        self.fd["share"].select_save_to_hp_smart()
        self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        if go_home:
            self.fd["preview"].go_home_from_preview_screen()
            self.fd["home"].close_print_anywhere_pop_up()
            self.fd["home"].verify_home_tile()

    ###############################################################################################################
    #
    #                             Print// Print Settings
    #
    ###############################################################################################################

    def select_a_file_and_go_to_print_preview(self, file_name, select_tile=True):
        self.go_hp_smart_files_screen_from_home(select_tile)
        self.fd["files"].select_a_file("{}.pdf".format(file_name))
        self.fd["preview"].go_to_print_preview_pan_view()

    def select_a_google_drive_file_and_go_to_print_preview(self, file_type="pdf", file_name="4pages"):
        self.navigate_to_google_drive_in_files()
        self.select_file_in_google_drive(file_type=file_type, file_name=file_name)
        self.fd["preview"].go_to_print_preview_pan_view()

    def scan_and_go_to_print_preview_pan_view(self, printer_obj):
        self.go_scan_screen_from_home(printer_obj)
        # Close the coach marks to capture scan
        if self.fd["scan"].verify_second_close_btn() is not False:
            self.fd["scan"].select_second_close_btn()
        self.fd["scan"].select_scan_job_button()
        self.fd["preview"].nav_detect_edges_screen()
        self.fd["preview"].verify_preview_screen()
        self.fd["preview"].go_to_print_preview_pan_view()

    @SPL_decorator.print_job_decorator()
    # Long wait time is to verify print job completion
    def select_print_button_and_verify_print_job(self, printer_obj, timeout=60):
        """
        On Print Preview Page, press print button and verify print success on HP smart and printer
        :param printer_obj:
        :return:
        """
        printer_status = printer_obj.get_printer_status()
        if printer_obj.is_printer_status_ready():
            if not self.fd["preview"].verify_button(Preview.PRINT):
                self.fd["preview"].select_toolbar_icon(Preview.PRINT)
            self.fd["preview"].dismiss_print_preview_coach_mark()
            self.fd["preview"].select_button(Preview.PRINT)
            self.fd["preview"].verify_job_sent_and_reprint_buttons_on_print_preview(timeout=timeout)
        else:
            raise PrinterNotReady("Printer is NOT ready. Printer Status is: {}".format(printer_status))

    def select_and_get_print_option_value(self, print_option, value):
        self.fd["preview"].verify_an_element_and_click(print_option)
        self.fd["preview"].select_static_text(value)
        self.fd["preview"].select_navigate_back()
        self.fd["preview"].verify_button(Preview.PRINT)
        return self.fd["preview"].get_option_selected_value(print_option)

    def get_latest_job_status(self, printer_obj, previous_job_id, timeout=10, raise_e=True):
        timeout = time.time() + timeout
        if printer_obj.get_newest_job_id() > previous_job_id:
            while time.time() < timeout:
                if printer_obj.get_newest_job_state() == 'Processing':
                    time.sleep(5)
                else:
                    break
            return printer_obj.get_newest_job_state()
        else:
            if raise_e:
                raise PrinterJobIdNotIncremented("Print job not incremented")
            else:
                logging.info("Print job not incremented")
                return False

    ###############################################################################################################
    #
    #                              Printer Settings screen
    #
    ###############################################################################################################

    def go_to_printer_settings_screen(self, printer_obj):

        p = printer_obj.get_printer_information()
        if self.fd["printer_settings"].verify_printer_settings_screen(raise_e=False):
            return True
        else:
            self.go_to_home_screen()
            if self.fd["home"].verify_printer_added() is False:
                self.add_printer_by_ip(printer_ip=p["ip address"])
            self.fd["home"].close_smart_task_awareness_popup()
            # Tap printer icon and go to printer settings screen
            self.fd["home"].click_on_printer_icon()
            self.fd["printer_settings"].verify_printer_settings_screen(raise_e=True)

    ###############################################################################################################
    #
    #                                     Edit Feature
    #
    ###############################################################################################################

    def go_to_edit_screen_with_printer_scan_image(self, printer_obj):
        if self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE) is False:
            self.go_scan_screen_from_home(printer_obj)
            self.fd["scan"].select_scan_job_button()
            sleep(2)
            self.fd["preview"].nav_detect_edges_screen()
            self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    def go_to_edit_screen_with_camera_scan_image(self, no_of_images=1):
        if self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE) is False:
            self.go_camera_screen_from_home(tile=True)
            self.multiple_manual_camera_capture(no_of_images)
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    def get_preview_img_and_go_to_edit_screen(self):
        self.select_multiple_photos_to_preview(no_of_photos=1)
        preview_image = self.fd["preview"].preview_img_screenshot()
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()
        return preview_image

    def go_to_edit_screen_with_selected_photo(self, no_of_photos=1):
        if self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE) is False:
            self.select_multiple_photos_to_preview(no_of_photos=no_of_photos)
        self.fd["preview"].select_edit()
        self.fd["edit"].verify_edit_page_title()

    ###############################################################################################################
    #
    #                                     Preview Landing screen
    #
    ###############################################################################################################

    def verify_preview_screen_and_go_home(self):
        self.fd["edit"].select_edit_done()
        self.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fd["preview"].select_navigate_back()
        self.fd["preview"].select_yes_go_home_btn()

    def select_a_file_and_go_to_preview_screen(self, file_name, file_type, select_tile=False):
        self.go_hp_smart_files_screen_from_home(select_tile)
        self.fd["files"].select_a_file("{}".format(file_name + file_type))

    ###############################################################################################################
    #
    #                                     Soft Fax
    #
    ###############################################################################################################

    def add_mobile_fax_tile(self):
        self.fd["home"].select_personalize_btn()
        self.fd["personalize"].verify_personalize_screen()
        self.fd["personalize"].toggle_switch_by_name(self.fd["personalize"].MOBILE_FAX_SWITCH, on=True)
        self.fd["personalize"].select_done()
        self.fd["home"].close_smart_task_awareness_popup()
        self.dismiss_tap_here_to_start()
        self.fd["home"].verify_home()

    def nav_to_compose_fax(self, new_user=False, stack="pie"):
        if self.fd["home"].verify_home(raise_e=False) is False:
            self.go_to_home_screen()
        if self.fd["home"].verify_tile_displayed(HOME_TILES.TILE_MOBILE_FAX) is False:
            self.add_mobile_fax_tile()
        self.fd["home"].select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)
        # long wait time is due soft fax webview loading time similar to GDG-1768
        login_screen, _ = self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=30, raise_e=False)
        if login_screen is not None:
            self.login_value_prop_screen(tile=True, stack=stack)
        if new_user:
            self.verify_fax_welcome_screens_and_nav_compose_fax()
        else:
            self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=30)
            self.fd["softfax_fax_history"].verify_fax_history_screen()
            self.fd["softfax_fax_history"].click_compose_new_fax()
            sleep(2)
            self.fd["softfax_compose_fax"].verify_compose_fax_screen()

    def recipient_info_for_os(self):
        """
        Assigning recipient for iOS version to avoid over stepping
        """
        recipients = {"12": "recipient_04",
                      "13": "recipient_05",
                      "14": "recipient_06"}
        device_os = self.driver.platform_version
        recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"][
            recipients[device_os]]
        return recipient_info

    def select_file_from_hp_smart_files(self, file_name):
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["files"].verify_files_screen()
        self.fd["files"].select_hp_smart_files_folder_icon()
        self.fd["files"].verify_hp_smart_files_screen()
        self.fd["files"].select_a_file("{}.pdf".format(file_name))

    def select_photo_from_my_photos(self, no_of_photos=1):
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["photos"].select_my_photos()
        self.fd["photos"].verify_my_photos_screen()
        self.fd["photos"].select_recents_or_first_option()
        self.fd["photos"].verify_photos_screen()
        self.fd["photos"].select_multiple_photos(end=no_of_photos)
        self.fd["photos"].select_next_button()

    def verify_fax_welcome_screens_and_nav_compose_fax(self):
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX_OFFER)
        self.fd["softfax_offer"].verify_get_started_screen()
        self.fd["softfax_offer"].skip_get_started_screen()
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX)
        self.fd["softfax_welcome"].verify_welcome_screen()
        self.fd["softfax_welcome"].skip_welcome_screen()
        self.fd["softfax_compose_fax"].verify_compose_fax_screen()

    def delete_contact(self, is_deleted=True):
        self.fd["softfax_contacts"].click_edit_contact_delete()
        self.fd["softfax_contacts"].verify_edit_delete_confirmation_popup()
        self.fd["softfax_contacts"].dismiss_edit_delete_confirmation_popup(is_deleted=is_deleted)

    def delete_all_contacts(self):
        contacts_list = self.fd["softfax_contacts"].get_contact_list()
        if contacts_list is False:
            logging.info("Contact list is empty")
        else:
            for _ in range(len(contacts_list)):
                contact = self.fd["softfax_contacts"].get_contact_list(multiple=False)
                self.fd["softfax_contacts"].select_info_icon(contact)
                self.delete_contact()

    def nav_to_contacts_screen(self):
        if self.fd["softfax_contacts"].verify_contact_screen_title() is False:
            self.fd["softfax_compose_fax"].click_contacts_icon()
            self.fd["softfax_contacts"].verify_contact_screen_title()

    def nav_to_fax_settings_screen(self, fax_settings_option=None):
        if not self.fd["softfax_compose_fax"].verify_compose_fax_screen(raise_e=False):
            self.nav_to_compose_fax()
        self.fd["softfax_compose_fax"].click_menu_option_btn(self.fd["softfax_compose_fax"].MENU_FAX_SETTINGS_BTN)
        self.fd["softfax_compose_fax"].dismiss_save_as_draft_popup()
        self.fd["fax_settings"].verify_fax_settings_screen()
        if fax_settings_option is not None:
            self.fd["fax_settings"].click_fax_settings_option(fax_settings_option)

    ###############################################################################################################
    #
    #                                     Google Drive
    #
    ###############################################################################################################

    def navigate_to_google_drive_in_files(self, email="", password=""):
        if not (email and password):
            login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]
            email, password = login_info["username"], login_info["password"]
        sleep(2)
        if self.fd["home"].verify_home_tile() is False:
            self.go_to_home_screen()
        self.fd["home"].verify_bottom_navigation_bar()
        self.fd["home"].select_documents_icon()
        self.fd["photos"].select_allow_access_to_photos_popup()
        self.fd["files"].select_google_drive_image()
        if self.fd["files"].verify_continue_popup() is not False:
            self.fd["files"].select_continue()
        if self.fd["google_drive"].verify_google_drive_login_screen(raise_e=False) is not False:
            self.fd["google_drive"].sign_in_to_google_drive(email, password)

    def select_google_drive_folder(self, email="", password=""):
        if not (email and password):
            login_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"]
            email, password = login_info["username"], login_info["password"]
        sleep(2)
        self.fd["files"].select_google_drive_image()
        if self.fd["files"].verify_continue_popup() is not False:
            self.fd["files"].select_continue()
        if self.fd["google_drive"].verify_google_drive_login_screen(raise_e=False) is not False:
            self.fd["google_drive"].sign_in_to_google_drive(email, password)

    def select_file_in_google_drive(self, file_type, file_name):
        self.fd["google_drive"].go_to_a_folder_in_test_data_folder(file_type=file_type)
        self.fd["files"].select_a_file("{}.".format(file_name) + file_type)

    # Random utility to generate string
    @staticmethod
    def get_random_str(length=4):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def navigate_to_smart_dashboard(self, account_type):
        self.fd["home"].select_account_icon()
        self.driver.wait_for_context(WEBVIEW_URL.HP_CONNECT)
        self.fd["hp_connect"].accept_privacy_popup()
        if account_type == "hp+":
            # TODO: needs verification
            self.fd["hp_connect"].verify_account_summary()
        elif account_type == "ucde":
            self.fd["hp_connect"].verify_account_profile_screen()
        else:
            # TODO: needs verification
            self.fd["hp_connect"].verify_new_printer_page(timeout=40)
    
    def export_app_log_to_files(self, export_method="files"):
        self.go_to_home_screen()
        self.fd["home"].select_app_settings()
        self.fd["app_settings"].select_share_logs()
        if export_method == "files":
            path = pytest.test_result_folder
            _ ,tail = os.path.split(os.path.split(path)[0])
            self.fd["app_settings"].verify_an_element_and_click("save_to_files", raise_e=True)
            self.fd["app_settings"].verify_an_element_and_click("logs_option", raise_e=True)
            file_name = "Logs_" + tail
            self.fd["app_settings"].rename_file("folder_name", file_name=file_name)
            self.fd["app_settings"].verify_an_element_and_click("done_btn", raise_e=True)
            # self.fd["app_settings"].verify_an_element_and_click("hp_smart_files_option", raise_e=True)
            self.fd["app_settings"].verify_an_element_and_click("save_btn", raise_e=True)
            # Pull file from iOS Files application
            zip = self.driver.wdvr.pull_file("@com.hp.printer.control.dev:documents/" + file_name + ".zip")
            return zip
        else:
            login_info = ma_misc.get_hpid_account_info(stack=self.stack, a_type="basic", claimable=False)
            receiver_email = login_info["email"]
            path = pytest.test_result_folder
            _ ,tail = os.path.split(os.path.split(path)[0])
            subject = "Logs_" + tail
            self.fd["app_settings"].send_app_logs_via_email(email=receiver_email, subject=subject)

