import logging
import time
import datetime
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory
from MobileApps.libs.flows.android.google_chrome.google_chrome import GoogleChrome
from MobileApps.libs.flows.android.google_drive.google_drive import GoogleDrive
from MobileApps.libs.flows.android.hpps.hp_print_service import HP_Print_Service
from MobileApps.libs.flows.android.hpps.job_notification import Job_Notification
from MobileApps.libs.flows.android.hpps.trap_door import Trap_Door
from MobileApps.libs.flows.android.hpps.hpps_settings import HPPS_Settings
from MobileApps.libs.flows.android.smart.about import About
from MobileApps.libs.flows.android.smart.app_settings import AppSettings
from MobileApps.libs.flows.android.smart.camera_scan import CameraScan
from MobileApps.libs.flows.android.smart.digital_copy import DigitalCopy
from MobileApps.libs.flows.android.smart.debug_settings import DebugSettings
from MobileApps.libs.flows.android.smart.file_photos import FilePhotos
from MobileApps.libs.flows.android.smart.local_files import LocalFiles
from MobileApps.libs.flows.android.smart.gmail import Gmail
from MobileApps.libs.flows.android.smart.home import Home
from MobileApps.libs.flows.android.smart.how_to_print import HowToPrint
from MobileApps.libs.flows.android.smart.preview import Preview
from MobileApps.libs.flows.android.smart.moobe_awc import MoobeAWC
from MobileApps.libs.flows.android.smart.moobe_ows import MoobeOWS
from MobileApps.libs.flows.android.smart.moobe_setup_complete import MoobeSetupComplete
from MobileApps.libs.flows.android.smart.online_documents import OnlineDocuments
from MobileApps.libs.flows.android.smart.online_photos import OnlinePhotos
from MobileApps.libs.flows.android.smart.personalize import Personalize
from MobileApps.libs.flows.android.smart.local_photos import LocalPhotos
from MobileApps.libs.flows.android.smart.print_preference import PrintPreference
from MobileApps.libs.flows.android.smart.printer_settings import PrinterSettings
from MobileApps.libs.flows.android.smart.printers import Printers
from MobileApps.libs.flows.android.smart.scan import Scan
from MobileApps.libs.flows.android.smart.dev_settings import DevSettings
from MobileApps.libs.flows.android.smart.photo_books import PhotoBooks
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.libs.flows.web.hp_id.hp_id import MobileHPID
from MobileApps.libs.flows.web.softfax.softfax_offer import SoftfaxOffer
from MobileApps.libs.flows.web.softfax.compose_fax import MobileComposeFax
from MobileApps.libs.flows.web.softfax.contacts import MobileContacts
from MobileApps.libs.flows.web.softfax.send_fax_details import SendFaxDetails
from MobileApps.libs.flows.web.softfax.softfax_welcome import MobileSoftfaxWelcome
from MobileApps.libs.flows.web.softfax.fax_history import MobileFaxHistory
from MobileApps.libs.flows.web.softfax.fax_settings import FaxSettings
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.smart.smart_welcome import AndroidSmartWelcome
from MobileApps.libs.flows.web.smart.privacy_preferences import PrivacyPreferences
from MobileApps.libs.flows.web.ows.value_prop import OWSValueProp
from MobileApps.libs.flows.android.system_flows.sys_flow_factory import system_flow_factory
from MobileApps.libs.flows.android.dropbox.dropbox import Dropbox
from MobileApps.libs.flows.android.smart.smart_tasks import SmartTasks
from MobileApps.libs.flows.common.edit.edit import AndroidEdit
from MobileApps.libs.flows.android.smart.notification import Notification
from MobileApps.libs.flows.web.smart.smart_printer_consent import SmartPrinterConsent
from MobileApps.libs.flows.web.instant_ink.offers import Offers
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from MobileApps.libs.flows.web.hp_connect.hp_connect_basic_account import HPConnectBasicAccount
from MobileApps.libs.flows.web.hp_connect.help_center import HelpCenter
from MobileApps.libs.flows.web.hp_connect.account import Account
from MobileApps.libs.flows.web.hp_connect.features import Features
from MobileApps.libs.flows.web.hp_connect.printers_users import PrintersUsers
from MobileApps.libs.flows.web.hp_connect.hp_instant_ink import HPInstantInk
from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.resources.const.android.const import *
from SPL.decorator import SPL_decorator
from SPL.driver.reg_printer import PrinterNotReady
from SAF.misc import saf_misc
import socket
from retry import retry


class HPIDLoginFail(Exception):
    pass

class HPIDCreateFail(Exception):
    pass

class NotFoundMOOBEConnectWifiType(Exception):
    pass

class FLOW_NAMES():
    ABOUT = "about"
    CAMERA_SCAN = "camera_scan"
    DEBUG_SETTINGS = "debug_settings"
    LOCAL_FILES = "files"
    GMAIL = "gmail"
    HELP_SUPPORT = "help_support"
    HOME = "home"
    HOW_PRINT = "how_to_print"
    PREVIEW = "preview"
    MOOBE = "moobe"
    ONLINE_DOCS = "online_documents"
    ONLINE_PHOTOS = "online_photos"
    PERSONALIZE = "personalize"
    LOCAL_PHOTOS = "photos"
    PRINT_PREFERENCE = "print_preference"
    PRINTER_SETTINGS = "printer_settings"
    PRINTERS = "printers"
    SCAN = "scan"
    DIGITAL_COPY = "digital_copy"
    MOOBE_AWC = "moobe_awc"
    MOOBE_OWS = "moobe_ows"
    MOOBE_SETUP_COMPLETE = "moobe_setup_complete"
    APP_SETTINGS = "app_settings"
    FILES_PHOTOS = "file_photos"
    SMART_TASKS = "smart_tasks"
    DEV_SETTINGS = "Dev Settings"
    PHOTO_BOOKS = "photo_books"
    EDIT = "edit"
    NOTIFICATION = "notification"
    # From another apps
    GMAIL_API = "gmail_api"
    HPPS_TRAPDOOR = "hpps_tradoor"
    HPPS_JOB_NOTIFICATION = "hpps_job_notification"
    HPPS = "hp_print_service"
    HPPS_SETTINGS = "hpps_settings"
    GOOGLE_DRIVE = "google_drive"
    GOOGLE_CHROME = "google_chrome"
    HPID = "hpid"
    GOOGLE_CHROME = "google_chrome"
    SYSTEM_FLOW = "system_flow"
    DROPBOX = "dropbox"
    SOFTFAX_OFFER = "softfax_offer"
    COMPOSE_FAX = "compose_fax"
    SEND_FAX_DETAILS = "send_fax_details"
    SOFTFAX_WELCOME = "softfax_welcome"
    SOFTFAX_FAX_HISTORY = "fax_history"
    SOFTFAX_CONTACTS = "softfax_contacts"
    SOFTFAX_FAX_SETTINGS = "fax_settings"
    UCDE_PRIVACY = "ucde_privacy"
    ANDROID_SETTINGS = "android_settings"
    WEB_SMART_WELCOME = "web_smart_welcome"
    PRIVACY_PREFERENCES = "privacy_preferences"
    OWS_VALUE_PROP = "value_prop"
    PRIVACY_SETTINGS = "privacy_settings"
    SMART_PRINTER_CONSENT = "smart_printer_consent"
    INSTANT_INK_OFFERS = "instant_ink_offer"
    HP_CONNECT = "hp_connect"
    HP_CONNECT_BASIC_ACCOUNT = "hp_connect_basic_account"
    HELP_CENTER = "help_center"
    HP_CONNECT_ACCOUNT = "account"
    HP_CONNECT_FEATURES = "features"
    HP_CONNECT_PRINTERS_USERS = "printers_users"
    HP_CONNECT_HP_INSTANT_INK = "hp_instant_ink"
    INSTANT_INK_VALUE_PROPOSITION = "instant_ink_value_proposition"
    YETI_FLOW_CONTAINER = "yeti_flow_container"


class TILE_NAMES():
    PRINT_PHOTOS = "_shared_print_photos_tile"
    PRINT_DOCUMENTS = "_shared_print_documents_tile"
    HELP_SUPPORT = "_shared_help_support_tile"
    PRINTER_SCAN = "_shared_printer_scan_tile"
    CAMERA_SCAN = "_shared_camera_scan_tile"
    COPY = "_shared_copy_tile"
    SMART_TASKS = "shared_smart_tasks_tile"
    GET_INK = "_shared_get_ink_tile"
    FAX = "_shared_fax_tile"
    CREATE_PHOTO_BOOKS = "_shared_create_photo_books_tile"


class FlowContainer(object):
    def __init__(self, driver, hpid_type="basic", hpid_claimable=False):
        self.driver = driver
        self.hpid_username, self.hpid_password = None, None
        self.set_hpid_account(hpid_type, hpid_claimable)
        self.fd = {
            FLOW_NAMES.ABOUT: About(driver),
            FLOW_NAMES.CAMERA_SCAN: CameraScan(driver),
            FLOW_NAMES.DEBUG_SETTINGS: DebugSettings(driver),
            FLOW_NAMES.APP_SETTINGS: AppSettings(driver),
            FLOW_NAMES.FILES_PHOTOS:FilePhotos(driver),
            FLOW_NAMES.LOCAL_FILES: LocalFiles(driver),
            FLOW_NAMES.GMAIL: Gmail(driver),
            FLOW_NAMES.HOME: Home(driver),
            FLOW_NAMES.HOW_PRINT: HowToPrint(driver),
            FLOW_NAMES.PREVIEW: Preview(driver),
            FLOW_NAMES.ONLINE_DOCS: OnlineDocuments(driver),
            FLOW_NAMES.ONLINE_PHOTOS: OnlinePhotos(driver),
            FLOW_NAMES.PERSONALIZE: Personalize(driver),
            FLOW_NAMES.LOCAL_PHOTOS: LocalPhotos(driver),
            FLOW_NAMES.PRINT_PREFERENCE: PrintPreference(driver),
            FLOW_NAMES.PRINTER_SETTINGS: PrinterSettings(driver),
            FLOW_NAMES.PRINTERS: Printers(driver),
            FLOW_NAMES.SCAN: Scan(driver),
            FLOW_NAMES.DIGITAL_COPY: DigitalCopy(driver),
            FLOW_NAMES.MOOBE_AWC: MoobeAWC(driver),
            FLOW_NAMES.MOOBE_OWS: MoobeOWS(driver),
            FLOW_NAMES.MOOBE_SETUP_COMPLETE: MoobeSetupComplete(driver),
            FLOW_NAMES.SMART_TASKS: SmartTasks(driver),
            FLOW_NAMES.DEV_SETTINGS: DevSettings(driver),
            FLOW_NAMES.PHOTO_BOOKS: PhotoBooks(driver),
            FLOW_NAMES.EDIT: AndroidEdit(driver),
            FLOW_NAMES.NOTIFICATION: Notification(driver),
            # Third party apps
            FLOW_NAMES.ANDROID_SETTINGS: android_system_flow_factory(driver),
            FLOW_NAMES.GMAIL_API: GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH),
            FLOW_NAMES.HPPS_TRAPDOOR: Trap_Door(driver),
            FLOW_NAMES.HPPS_JOB_NOTIFICATION: Job_Notification(driver),
            FLOW_NAMES.HPPS: HP_Print_Service(driver),
            FLOW_NAMES.HPPS_SETTINGS: HPPS_Settings(driver),
            FLOW_NAMES.GOOGLE_DRIVE: GoogleDrive(driver),
            FLOW_NAMES.HPID: MobileHPID(driver, context=WEBVIEW_CONTEXT.CHROME),
            FLOW_NAMES.GOOGLE_CHROME: GoogleChrome(driver),
            FLOW_NAMES.SYSTEM_FLOW: system_flow_factory(driver),
            FLOW_NAMES.DROPBOX: Dropbox(driver),
            FLOW_NAMES.SOFTFAX_OFFER: SoftfaxOffer(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.COMPOSE_FAX: MobileComposeFax(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SEND_FAX_DETAILS:SendFaxDetails(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SOFTFAX_WELCOME: MobileSoftfaxWelcome(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SOFTFAX_FAX_HISTORY: MobileFaxHistory(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SOFTFAX_CONTACTS: MobileContacts(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SOFTFAX_FAX_SETTINGS: FaxSettings(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.UCDE_PRIVACY: UCDEPrivacy(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.WEB_SMART_WELCOME: AndroidSmartWelcome(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.PRIVACY_PREFERENCES:PrivacyPreferences(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.OWS_VALUE_PROP: OWSValueProp(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.SMART_PRINTER_CONSENT: SmartPrinterConsent(driver, context={"url": WEBVIEW_URL.PRINTER_CONSENT}),
            FLOW_NAMES.INSTANT_INK_OFFERS: Offers(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT: HPConnect(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT_BASIC_ACCOUNT:HPConnectBasicAccount(driver, context={"url": WEBVIEW_URL.HP_CONNECT_BASIC_ACCOUNT}),
            FLOW_NAMES.HELP_CENTER: HelpCenter(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT_ACCOUNT: Account(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT_FEATURES: Features(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.YETI_FLOW_CONTAINER: YetiFlowContainer(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT_PRINTERS_USERS: PrintersUsers(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK:HPInstantInk(driver, context=WEBVIEW_CONTEXT.SMART),
            FLOW_NAMES.INSTANT_INK_VALUE_PROPOSITION: ValueProposition(driver, context=WEBVIEW_CONTEXT.SMART)
        }

    @property
    def flow(self):
        return self.fd

    def set_hpid_account(self, a_type, claimable=True, ii_status=False):
        """
        Set value for hpid account properties
        """
        account = ma_misc.get_hpid_account_info(self.driver.session_data["request"].config.getoption("--stack"), 
                                                a_type=a_type, 
                                                claimable=claimable, II=ii_status)
        logging.info("HPID account is: {}".format(account))
        self.hpid_username = account["email"]
        self.hpid_password = account["password"]
        self.hpid_account_type = a_type
        self.hpid_ii_status = ii_status

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         GENERAL FUNCTIONS       ---------------------
    # They are used by multiple flows
    def select_back(self):
        """
        Click on Back button of app
        """
        self.driver.click("_share_back_btn")

    def clean_up_download_and_pictures_folders(self):
        """
        Clean up Download and Pictures folders
        """
        folders= [TEST_DATA.MOBILE_DOWNLOAD, TEST_DATA.MOBILE_PICTURES]
        for folder in folders:
            if self.verify_existed_file("{}/*".format(folder)):
                self.driver.clean_up_device_folder(folder)

    def reset_app(self):
        """
        Reset Android Smart app:
            - Clear cache of Android Smart app
            because after clearing cache, the options in Dev Settings are setup back to default server, so:
                - Setup stack server
                - Turn off Detect leaks
        """
        pkg_name = PACKAGE.SMART.get(self.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        self.driver.clear_app_cache(pkg_name)
        self.flow_home_change_stack_server(self.driver.session_data["request"].config.getoption("--stack"))
        self.fd[FLOW_NAMES.DEV_SETTINGS].open_select_settings_page()
        self.fd[FLOW_NAMES.DEV_SETTINGS].toggle_detect_leaks_switch(on=False)

    def run_app_background(self, timeout=1):
        """
        Put app in background for sleep time. Then, launch app again at the same screen
        Note: Cannot use background_app() function from appium 
              because it launches to Home screen instead of the screen before putting app in background
        """
        self.driver.wdvr.background_app(-1)  # put app in background without launching again
        time.sleep(timeout)
        self.driver.press_key_switch_app()
        self.driver.click("_share_application_name")
    
    #   -----------------------         FROM WELCOME       -----------------------------
    def load_manage_options(self):
        """
        Load Privacy Preferences screen using Manage Options button in Welcome flow
        """
        pkg_name = PACKAGE.SMART.get(self.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        self.driver.wdvr.start_activity(pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART)
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen()
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_manage_options()
        
    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self, skip_value_prop=False, create_acc=False):
        """
        Load to Home screen:
            - Start base activity or launch app
            - If current screen is not Home screen, then it is Welcome screen
                + Skip it

        @param skip_value_prop: skip Value Prop screen or not
        @param create_acc: create new acc or sign in into an account
        @return: username, password: parameter's value for skip_value_prop = True
        """
        # Make sure current screen is not in customTabActivity of Chrome
        terminated_apps = [PACKAGE.GOOGLE_CHROME, PACKAGE.GOOGLE_PHOTOS, PACKAGE.HPPS, PACKAGE.SETTINGS]
        for terminated_app in terminated_apps:
            self.driver.terminate_app(terminated_app)
        # Make sure current screen is on mobile device home screen
        self.driver.press_key_home()
        pkg_name = PACKAGE.SMART.get(self.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        self.driver.wdvr.start_activity(pkg_name, LAUNCH_ACTIVITY.SMART)
        # After start activity, current screen is not Home screen -> Welcome screen -> skip it
        if not self.fd[FLOW_NAMES.HOME].verify_home_nav(raise_e=False):
            # Clear all data from Google Chrome for clearing HPID token which haven't been logged out.
            self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
            self.driver.wdvr.start_activity(pkg_name, LAUNCH_ACTIVITY.SMART)
            # Start skipping welcome screen
            username, password = self.skip_welcome_screen(skip_value_prop=skip_value_prop, create_acc=create_acc)
            # From user onboarding to Home screen will take to 40s-50s. And has CR GDG-1768 for tracking this issue
            self.fd[FLOW_NAMES.HOME].verify_home_nav(timeout=50)
            self.driver.performance.stop_timer("hpid_login", raise_e=False)
            return username, password

    def skip_welcome_screen(self, skip_value_prop=False, create_acc=False):
        """
        Skip Welcome screen
                + Click on Accept All button
                + On Value Prop screen: based on parameter, there are 3 options
                    + Skip this screen -> skip_value_prop = True
                    + (default) Sign in  -> skip_value_prop = False and create_acc = False 
                    + Create Account -> -> skip_value_prop = False and create_acc = True 
        @param skip_value_prop: skip Value Prop screen or not
        @param create_acc: create new acc or sign in into an account
        @return: username, password: value from creating acc. Otherwise, value from hpid account instant
        """
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART)
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].verify_welcome_screen()
        self.fd[FLOW_NAMES.WEB_SMART_WELCOME].click_accept_all_btn(change_check={"wait_obj": "accept_all_btn", "invisible": True, "timeout": 5, "context_change": {"webview_name": WEBVIEW_CONTEXT.SMART}})
        #Currently HPID take 30-40ss to load to value prop screen.
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=40)
        self.fd[FLOW_NAMES.OWS_VALUE_PROP].verify_ows_value_prop_screen(timeout=30)
        username, password = self.hpid_username, self.hpid_password
        if skip_value_prop:
            self.driver.press_key_back()
            self.fd[FLOW_NAMES.HOME].skip_are_you_sure_popup()
        else:
            self.fd[FLOW_NAMES.OWS_VALUE_PROP].select_value_prop_buttons(index=1)
            # Handle for welcome screen of Google Chrome
            self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
            self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
            self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
            if create_acc:
                self.fd[FLOW_NAMES.HPID].click_create_account_link()
                username, password = self.fd[FLOW_NAMES.HPID].create_account()
                self.driver.wait_for_context(WEBVIEW_URL.UCDE_PRIVACY, timeout=30)
                self.fd[FLOW_NAMES.UCDE_PRIVACY].verify_ucde_privacy_screen(timeout=10,raise_e=True)
                self.driver.performance.stop_timer("hpid_create_account")
                self.fd[FLOW_NAMES.UCDE_PRIVACY].skip_ucde_privacy_screen()
            else:
                self.fd[FLOW_NAMES.HPID].login(self.hpid_username, self.hpid_password, change_check={"wait_obj": "sign_in_button", "invisible": True})
        return username, password

    def flow_home_sign_in_hpid_account(self, create_acc=False):
        """
        At Home screen, sign in/ create HPID account
            - Go to App Settings
            - Sign in or create HPID account
        End of flow: App Settings screen
        :param create_acc: sign in or create account
        :param username: use for sign in (creat_acc = False)
        :param password: use for sign in (create_acc = False)
        """
        self.flow_load_home_screen(skip_value_prop=True)
        self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
        if create_acc:
            self.flow_app_settings_create_hpid()
        else:
            self.flow_app_settings_sign_in_hpid()

    def flow_home_verify_smart_app_on_userboarding(self, create_acc=False):
        """
        Make sure Android Smart on useronboarding.
        If not, sign in to default account
        """
        if self.fd[FLOW_NAMES.HOME].verify_bottom_nav_btn(self.fd[FLOW_NAMES.HOME]. NAV_PRINTER_SCAN_BTN, invisible=True, raise_e=False):
            self.flow_home_sign_in_hpid_account(create_acc=create_acc)
            self.flow_load_home_screen()

    def flow_home_verify_ready_printer(self, printer_bonjour):
        """
        Verify connected printer ready via:
            - Ready status icon on Home screen
            - if status icon is invisible, go to printer setting for checking
        :param printer_bonjour: bonjour name of printer
        :return:
        """
        if not self.fd[FLOW_NAMES.HOME].verify_ready_printer_status(raise_e=False):
            self.fd[FLOW_NAMES.HOME].load_printer_info()
            self.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_my_printer(printer_bonjour)
            self.fd[FLOW_NAMES.PRINTER_SETTINGS].verify_ready_status()
            self.select_back()

    def flow_home_select_network_printer(self, printer_obj, is_searched=False, is_loaded=True):
        """
        At Home screen, select target printer and return its status
            - Click on Printer icon on navigation bar
            - At printer screen search for the printer's ip
            - Click printer ip
            - Verify Home screen with target printer
            - If printer already selected nothing happens
        :param printer_obj: SPL printer
        :param is_searched: select printer via searching or not.
        :param is_loaded: check whether printer is loaded at the end of flow at home screen
        :param stack: stack server
        :param username: hpid username for logging in. Default: HPID Account in constant of HPID account
        :param password: hpid password for logging in. Default: HPID Account in constant of HPID account
        """
        self.fd[FLOW_NAMES.HOME].load_printer_selection()
        self.fd[FLOW_NAMES.PRINTERS].select_printer(printer_obj.p_obj.ipAddress, wifi_direct=False,
                                                    is_searched=is_searched,
                                                    keyword=printer_obj.p_obj.ipAddress)
        if self.fd[FLOW_NAMES.HOME].verify_feature_popup(raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_feature_popup_close()
        self.fd[FLOW_NAMES.HOME].verify_home_nav()
        if printer_obj.p_obj.projectName.split("_")[0] == "malbec":
            self.flow_home_verify_smart_app_on_userboarding()
            self.flow_home_set_up_printer(printer_obj)
        if is_loaded:
            if not self.fd[FLOW_NAMES.HOME].verify_loaded_printer(raise_e=False):
                logging.info("Printer is connected to Wifi: {} ".format(printer_obj.is_connected_to_wifi()))

    def flow_home_set_up_printer(self, printer_obj):
        """
        Use to set up a selected printer which hasn't been completed MOOBE successfully.
        This OWS flow is handled on App side only.
        Note: Currently, It is tested on Malbec which is cleaned up via SPL.exit_oobe()
        """
        if self.fd[FLOW_NAMES.HOME].verify_setup_btn(invisible=False, raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_set_up()
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_checking_printer_status_screen(invisible=False)
            self.fd[FLOW_NAMES.MOOBE_OWS].verify_checking_printer_status_screen(invisible=True)
            self.fd[FLOW_NAMES.MOOBE_OWS].skip_enjoy_hp_account_benefit_screen()
            if self.fd[FLOW_NAMES.MOOBE_OWS].verify_hp_instant_ink_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_OWS].skip_moobe_ows()
            if self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].verify_setup_complete_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].select_setup_complete_not_now()
            if self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].verify_print_other_devices_screen(raise_e=False):
                self.fd[FLOW_NAMES.MOOBE_SETUP_COMPLETE].select_not_right_now()
            self.flow_load_home_screen()
        else:
            logging.info("Printer ({}) is set up completely".format(printer_obj.p_obj.ipAddress))

    def flow_home_load_scan_screen(self, printer_obj, from_tile=True):
        """
        From Home screen, load to Scan screen
            - Select target printer
            - Verify ready printer at Home screen
            - Click on Printer Scan for scanning
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Scan icon on navigation bar
        """
        self.flow_home_verify_smart_app_on_userboarding()
        self.flow_home_select_network_printer(printer_obj)
        self.flow_home_verify_ready_printer(printer_obj.get_printer_information()["bonjour name"])
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.PRINTER_SCAN))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_PRINTER_SCAN_BTN)
        # Verify scan screen to make sure that printer is connected successfully by visible page size
        self.fd[FLOW_NAMES.SCAN].verify_scan_screen()
    
    def flow_home_load_photo_screen(self, printer_obj, from_tile=True):
        """
        From Home screen, load to My Photo screen
            - Select target printer
            - Verify ready printer at Home screen
            - Click on Print photos tile
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Files & Photos icon on navigation bar
        """
        self.flow_home_select_network_printer(printer_obj)
        self.flow_home_verify_ready_printer(printer_obj.get_printer_information()["bonjour name"])
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        # Verify scan screen to make sure that printer is connected successfully by visible page size
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].MY_PHOTOS_TXT)

    def flow_home_scan_single_page(self, printer_obj, from_tile=True):
        """
        At Home screen, scan a single_page via a scan tile buttons (Scan, Scan to Email, Scan to Cloud)
            - Select  target network printer via Printer button on navigation bar
            - Verify Home screen with ready target printer
            - Click on a scan tile button on Home screen button.
                Dismiss App Permission if mobile device are Android 6.0 or newer
            - Wait until Scan button is able to click.
                Select Scan button.
            - Verify scan is successful
        :param printer_obj:
        :param from_tile: True -> click on Tile. False -> click on Scan icon on navigation bar
        """
        self.flow_home_load_scan_screen(printer_obj, from_tile=from_tile)
        if self.is_printer_ready(printer_obj):
            self.fd[FLOW_NAMES.SCAN].select_scan()
            self.fd[FLOW_NAMES.SCAN].verify_successful_scan_job()

    def flow_home_camera_scan_pages(self, from_tile=True, number_pages=1):
        """
        Create pages via Camera Scan from Home screen (from tiles or bottom navigation bar)
        Steps:
            - From Home screen, load Camera screen from tile or button on bottom naviation bar
            - Select Batch mode
            - Capture photo for number_pages
            - Click on Done button
        :param from_tile: True -> click on Tile. False -> click on Camera icon on navigation bar
        :param number_pages: number of pages are captured
        """
        self.flow_home_verify_smart_app_on_userboarding()
        if from_tile:
            self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        else:
            self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_CAMERA_SCAN_BTN)
        self.fd[FLOW_NAMES.CAMERA_SCAN].capture_photo(mode=self.fd[FLOW_NAMES.CAMERA_SCAN].BATCH_MODE, number_pages=number_pages, manual=True)

    def flow_home_load_smart_task_screen(self, create_acc=False, printer_obj=None):
        """
        - Load to Home screen
        - Login in HPID in App Settings
        - Click on Smart Tasks tile on Home screen (Enable Smart Task file from Personalize if Smart Tasks tile not on Home screen)
        :param printer_ip
        :param is_searched: True or False (depends on need connect printer or not)
        :param create_acc: True or False
        :param smart_task_name
        """
        self.flow_home_sign_in_hpid_account(create_acc=create_acc)
        self.select_back()
        if printer_obj:
            self.flow_home_select_network_printer(printer_obj, is_searched=True)
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.SMART_TASKS))
        try:
            self.fd[FLOW_NAMES.SMART_TASKS].dismiss_smart_task_skip_btn()
        except (TimeoutException, NoSuchElementException):
            logging.info("There is no 'skip button'")
        self.fd[FLOW_NAMES.SMART_TASKS].verify_smart_tasks_screen()

    def flow_home_delete_all_smart_tasks(self):
        """
        - Load to Smart Tasks with HPID account login
        - Delete Smart Task on Smart Tasks list
        """
        self.flow_home_load_smart_task_screen()
        self.fd[FLOW_NAMES.SMART_TASKS].delete_all_smart_tasks()

    def flow_home_enable_softfax_tile(self):
        """
        Enable SoftFax tile if it is not on Home screen
            - Go to Debug Setting -> enable Softfax
            - Kill app
            - Go to Personalize -> enable Send Fax
            - Go back Home screen and verify this tile display
        :return:
        """
        if self.fd[FLOW_NAMES.HOME].verify_tile(self.driver.return_str_id_value(TILE_NAMES.FAX), invisible=True, raise_e=False):
            self.fd[FLOW_NAMES.HOME].select_personalize_tiles()
            self.fd[FLOW_NAMES.PERSONALIZE].toggle_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX), on=True)
            self.fd[FLOW_NAMES.PERSONALIZE].select_back()
            self.fd[FLOW_NAMES.HOME].verify_tile(self.driver.return_str_id_value(TILE_NAMES.FAX), invisible=False,
                                                 raise_e=True)
        else:
            logging.info("Send Fax is enable")

    def flow_home_change_stack_server(self, stack):
        """
        Change Stack server in DEV Settings
            - Load Select Setting Page
            - Click on HPC Settings
            - Change Stack
        :param stack:
        """
        stacks = {"stage": self.fd[FLOW_NAMES.DEV_SETTINGS].STAGE_STACK,
                  "pie": self.fd[FLOW_NAMES.DEV_SETTINGS].PIE_STACK}
        self.fd[FLOW_NAMES.DEV_SETTINGS].open_select_settings_page()
        self.fd[FLOW_NAMES.DEV_SETTINGS].change_stack_server(stacks[stack])

    def flow_home_load_compose_fax_screen(self, create_acc=False, check_onboarding=False):
        """
        From Home, load Compose Fax screen via login/create acc at App Settings.
            - Go To App Settings -> log out acc if there is any acc
            - Set condition for Fax
            - Sign In or create a new acc -> Go back to Home screen
            - Click on Fax tile
            - Verify Compose Fax screen
        :param create_acc: create acc or sign in
        :param check_onboarding: False: go to App Settings for login/create account every time,
                                 True: if app is on user-onboarding, don't need to login/create account from app settings
        """
        if check_onboarding:
            self.flow_load_home_screen(skip_value_prop=True)
            self.flow_home_verify_smart_app_on_userboarding(create_acc=create_acc)
        else:
            self.flow_home_sign_in_hpid_account(create_acc=create_acc)
            self.select_back()
        self.flow_home_enable_softfax_tile()
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX), is_permission=True)
        # Wait for context of webview is visible in list before switching to webview
        if create_acc:
            self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX_OFFER, timeout=30)
            if self.fd[FLOW_NAMES.SOFTFAX_OFFER].verify_get_started_screen(raise_e=False):
                self.fd[FLOW_NAMES.SOFTFAX_OFFER].skip_get_started_screen()
            if self.fd[FLOW_NAMES.SOFTFAX_WELCOME].verify_welcome_screen(raise_e=False):
                self.fd[FLOW_NAMES.SOFTFAX_WELCOME].skip_welcome_screen()
        else:
            #During HPID login process, take 30-45s to laod to Fax hisotry screen or compose fax screen. And has CR GDG-1768 for tracking this issue
            self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=40)
            self.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].verify_fax_history_screen(invisible=False, timeout=10)
            self.fd[FLOW_NAMES.SOFTFAX_FAX_HISTORY].click_compose_new_fax()
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=40)
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_compose_fax_screen(timeout=10)

    def flow_home_log_out_hpid_from_app_settings(self):
        """
        Log out HPID on App Settings if an account is logged in
        """
        self.flow_load_home_screen(skip_value_prop=True)
        self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
        # if an HPID account is logged in, sign out
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(timeout=10, raise_e=False):
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()

    def flow_home_log_out_cloud_account (self, cloud_names):
        """
        Log out if the cloud account is logged in before
        From Home screen:
            - Click on file icon on bottom navigation bar
            - Long press on cloud name
            - Click on logout button
        :param cloud_names: element is constant variable of file and photos flow
                    - GOOGLE_DRIVE_TXT
                    - DROPBOX_TXT
                    - FACEBOOK_TXT
                    - INSTAGRAM_TXT
                    - GOOGLE_PHOTOS_TXT
        """
        if isinstance(cloud_names, str):
            cloud_names = [cloud_names]
        self.flow_load_home_screen()
        self.flow_home_verify_smart_app_on_userboarding()
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_VIEW_PRINT_BTN)
        for cloud in cloud_names:
            if not self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_not_login(cloud, raise_e=False):
                self.fd[FLOW_NAMES.FILES_PHOTOS].load_logout_popup(cloud)
                self.fd[FLOW_NAMES.FILES_PHOTOS].logout_cloud_item(cloud)
                self.fd[FLOW_NAMES.FILES_PHOTOS].verify_cloud_not_login(cloud)

    def flow_home_load_digital_copy_single_page(self, printer_obj):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
                  otherwise clicking on small "+" button on Home screen
        - click on Copy tile on Home screen
        - Allow access to camera
        - Click on Capture button with manual mode
        """
        self.flow_load_home_screen()
        self.flow_home_verify_smart_app_on_userboarding()
        self.flow_home_select_network_printer(printer_obj, is_searched=True)
        self.flow_home_verify_ready_printer(printer_obj.get_printer_information()["bonjour name"])
        self.fd[FLOW_NAMES.HOME].select_tile_by_name(self.fd[FLOW_NAMES.HOME].get_text_from_str_id(TILE_NAMES.COPY))
        self.fd[FLOW_NAMES.CAMERA_SCAN].capture_photo(mode=self.fd[FLOW_NAMES.CAMERA_SCAN].BATCH_MODE,
                                                      is_copy=True)

    #   -----------------------         FROM PREVIEW       -----------------------------
    def flow_preview_share_via_gmail(self, to_email, subject, content="", from_email=""):
        """
        From Sharing Using popup, share via gmail:
            - Click on Gmail button on Sharing Using popup
            - At compose Gmail, enter all information
            - Verify that email is sent successfully
        :param from_email:
        :param to_email:
        :param subject:
        :param content:
        """
        #Change subject to separated value for multiple execution parallel
        self.fd[FLOW_NAMES.SYSTEM_FLOW].select_app(self.driver.return_str_id_value("share_gmail_btn", project="smart", flow="preview"))
        self.flow_gmail_send_email(to_email, subject, content, from_email=from_email)

    def flow_preview_make_printing_job(self, printer_obj, jobs=1, is_edit = True):
        """
        At Preview screen:
            - Click on Print button
            - Check printing job with HPPS
        :param printer_obj:
        :param jobs:
        """
        self.fd[FLOW_NAMES.PREVIEW].verify_preview_nav(is_edit=is_edit)
        self.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn(self.fd[FLOW_NAMES.PREVIEW].PRINT_BTN)
        if self.fd[FLOW_NAMES.HPPS].agree_and_accept_terms_and_condition_if_present():
            self.fd[FLOW_NAMES.HPPS].check_run_time_permission()
        if self.fd[FLOW_NAMES.HPPS].dismiss_file_not_available_popup():
            self.driver.press_key_back()
            self.fd[FLOW_NAMES.PREVIEW].verify_preview_nav(is_edit=is_edit)
            self.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn(self.fd[FLOW_NAMES.PREVIEW].PRINT_BTN)
        self.flow_hpps_make_print_job_via_trapdoor_ui(printer_obj, jobs=jobs, skip_agreement=False)

    #   -----------------------         FROM GMAIL Compose       -----------------------------
    def flow_gmail_send_email(self, to_email, subject, content="", from_email=None):
        """
        At Compose screen, send an email:
            - Enter valid information into From, To, Subject, and Content
            - Click on Send button
            - Verify that email is sent successfully
        :param from_email:
        :param to_email:
        :param subject:
        :param content:
        :return:
        """
        subject = "{}_{}".format(subject, self.driver.driver_info["desired"]["udid"])
        # Delete the email from previous execution
        try:
            msg_id = self.fd[FLOW_NAMES.GMAIL_API].search_for_messages(q_from=from_email,
                                                                       q_to=to_email,
                                                                       q_unread=False,
                                                                       q_subject=subject,
                                                                       q_content=content,
                                                                       timeout=30)
            self.fd[FLOW_NAMES.GMAIL_API].delete_email(msg_id)
        except TimeoutException:
            logging.info("Email is not existed or already deleted")
        except socket.timeout:
            logging.info("Session of Gmail Timeout")
        # Start to test Gmail
        try:
            f_email = self.fd[FLOW_NAMES.GMAIL].compose_email(to_email=to_email,
                                                          subject_text=subject,
                                                          body_text=content)

            msg_id = self.fd[FLOW_NAMES.GMAIL_API].search_for_messages(q_from=f_email,
                                                                       q_to=to_email,
                                                                       q_unread=True,
                                                                       q_subject=subject,
                                                                       q_content=content,
                                                                       timeout=120)
            self.fd[FLOW_NAMES.GMAIL_API].delete_email(msg_id)
        except TimeoutException as ex:
            logging.warning(ex.msg)

    #   -----------------------         FROM HPPS APP       -----------------------------
    @SPL_decorator.print_job_decorator()
    def flow_hpps_make_print_job_via_trapdoor_ui(self, printer_obj, jobs=1, skip_agreement=True):
        """
        - Make print job via trap door ui
        - Verify print job on printer and HPPS app
        :param printer_obj: instance GenericPrinter.
        :param file_name:
        :param is_document:
        :return:
        """
        if skip_agreement and self.fd[FLOW_NAMES.HPPS].agree_and_accept_terms_and_condition_if_present():
            self.fd[FLOW_NAMES.HPPS].check_run_time_permission()
        if self.is_printer_ready(printer_obj):
            self.fd[FLOW_NAMES.HPPS_TRAPDOOR].verify_printer_preview_screen()
            self.fd[FLOW_NAMES.HPPS_TRAPDOOR].select_print()
            self.driver.wdvr.open_notifications()
            bonjour_name = printer_obj.get_printer_information()['bonjour name']
            bonjour_name = bonjour_name[bonjour_name.find("HP ") + 3:bonjour_name.find("series") - 1]  # remove HP and series out of string
            self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].select_print_notification_by_printer_name(bonjour_name)
            self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].verify_print_jobs_screen()
            for i in range(jobs):
                self.fd[FLOW_NAMES.HPPS_JOB_NOTIFICATION].get_printing_results_trap_door(timeout=150)
        else:
            raise PrinterNotReady("Printer is not ready for printing job")

    #   -----------------------         FROM Smart Task       -------------------------------
    def flow_smart_task_load_smart_task_create_screen(self, smart_task_name):
        """
        1. Click CREATE NEW SMART button on smart task screen
        2. Input smart task name
        :param smart_task_name:
        """
        self.fd[FLOW_NAMES.SMART_TASKS].load_smart_task_create_screen()
        self.fd[FLOW_NAMES.SMART_TASKS].input_smart_task_name(smart_task_name)

    # Currently this function only verify Smart Task can direct into Print Preview screen, Skip for verifying printing job on printer success or not as defect INOS-3861 and IN0S-4117
    def flow_smart_task_make_printing_job(self, smart_task_name, printer_obj, jobs=1):
        """
        At Smart Task Preview screen:
            - Select a Smart Task
            - Click on Print button
            - Check printing job with HPPS
        :param smart_task_name
        :param printer_obj
        :param jobs:
        """
        self.fd[FLOW_NAMES.SMART_TASKS].check_run_time_permission()
        self.fd[FLOW_NAMES.SMART_TASKS].verify_smart_tasks_list_screen(is_empty=False)
        self.fd[FLOW_NAMES.SMART_TASKS].select_smart_task_from_preview_screen(smart_task_name)
        if self.fd[FLOW_NAMES.HPPS].agree_and_accept_terms_and_condition_if_present():
            self.fd[FLOW_NAMES.HPPS].check_run_time_permission()
        if self.fd[FLOW_NAMES.HPPS].dismiss_file_not_available_popup():
            self.driver.press_key_back()
            self.driver.press_key_back()
            self.fd[FLOW_NAMES.PREVIEW].verify_bottom_nav_btn(self.fd[FLOW_NAMES.PREVIEW].PRINT_BTN, invisible=False)
            self.fd[FLOW_NAMES.PREVIEW].select_bottom_nav_btn(self.fd[FLOW_NAMES.PREVIEW].PRINT_BTN)
        self.fd[FLOW_NAMES.HPPS_TRAPDOOR].verify_printer_preview_screen()
        # self.flow_hpps_make_print_job_via_trapdoor_ui(printer_obj, jobs=jobs, skip_agreement=False)
        #Make sure app will go back to Home screen as we skip printing function based on INOS-3861
        self.flow_load_home_screen()

    #   -----------------------         FROM Digital Copy       -----------------------------
    # Currently this function only verify Copy send success on App side, Skip for verifying printing job on printer success or not as defect INOS-3861
    def flow_digital_copy_make_copy_job(self, printer_obj, is_color_copy):
        """
        - Make copy job via trap door ui
        - Verify print job on printer and HPPS app
        :param printer_obj: instance GenericPrinter.
        :param is_color_copy: True: Color copy, False: Black copy
        :param printer_obj:
        :param jobs:
        :return:
        """
        if self.is_printer_ready(printer_obj):
            # current_job_id = printer_obj.get_newest_job_id()
            if is_color_copy:
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_color_copy_btn()
            else:
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_black_copy_btn()
            if self.fd[FLOW_NAMES.DIGITAL_COPY].verify_paper_size_mismatch_popup(raise_e=False):
                self.fd[FLOW_NAMES.DIGITAL_COPY].select_ok_btn()
            try:
                self.fd[FLOW_NAMES.HPPS].agree_and_accept_terms_and_condition_if_present()
                self.fd[FLOW_NAMES.HPPS].check_run_time_permission()
            except TimeoutException:
                logging.info("There is no 'agree and accept terms'")
            self.fd[FLOW_NAMES.DIGITAL_COPY].verify_copy_job_finished_screen()
            return True
        raise PrinterNotReady("Current Printer status is {} and not ready for printing job".format(printer_obj.get_printer_status()))

    #   -----------------------         FROM Instagram       -----------------------------
    def flow_instagram_login(self, username, password):
        """
        Start at first screen of logging in Instagram account
        Log in to Instagram acc
        :param username:
        :param password:
        """
        if self.fd[FLOW_NAMES.ONLINE_PHOTOS].verify_instagram_login_screen(raise_e=False):
            self.fd[FLOW_NAMES.ONLINE_PHOTOS].instagram_login(username, password, self.fd[FLOW_NAMES.GMAIL_API])
        else:
            logging.info("Instagram is automatically logged in to {}".format(username))

    #   -----------------------         FROM APP SETTINGS       -----------------------------
    def flow_app_settings_sign_in_hpid(self):
        """
        From App Settings: Click on Sign out if an account is signed in
            - Click on Sign In button
            - Log in if HPID log in screen or
              Current account is not usrname, log out and login again
            - Verify App Settings with the same username
        """
        #If HPID is signed in with the expected username
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(self.hpid_username, raise_e=False):
            return True
        #Since HPID isn't signed in with the expected username
        #Check if HPID is signed in or not
        elif self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(raise_e=False):
            #Sign out of the existing account because it's signed in
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()

        # Avoid to automatically logged into HPID account. CLear cache Google Chrome
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)

        # For Android 7/8/9, somehow direct into mobile device home screen instead of app settings screen after clear cache for Google Chrome. 
        # We submitted CR AIOA-8868 for this issue. This is temporay fix until the CR get fixed
        if not self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_in_btn(invisible=False, raise_e=False):
            self.flow_load_home_screen(skip_value_prop=True)
            self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()

        self.fd[FLOW_NAMES.APP_SETTINGS].click_sign_in_btn()
        self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        #Should be a the sign in page now and continue signing in with the account i want
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()
        self.fd[FLOW_NAMES.HPID].login(self.hpid_username, self.hpid_password, change_check={"wait_obj": "sign_in_button", "invisible": True})
        self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(self.hpid_username, timeout=40, raise_e=True)
        return True

    def flow_app_settings_create_hpid(self):
        """
        From App Settings:
            - Sign out account if there is a logged in account
            - Clear cache of Google Chrome to avoid to automatically log in into a HPID account
            - Click on Sign In
            - At HPID's sign up screen, create a new hpid
        :return: credential of new hpid
        """
        # If an HPID account is logged in, click on sign out button
        if self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(timeout=10, raise_e=False):
            self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()
        # Make sure there is no saved HPID account in cache of Google Chrome which causes automatically logged in
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)

        # For Android 7/8/9, somehow direct into mobile device home screen instead of app settings screen after clear cache for Google Chrome
        if not self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_in_btn(invisible=False, raise_e=False):
            self.flow_load_home_screen(skip_value_prop=True)
            self.fd[FLOW_NAMES.HOME].select_more_options_app_settings()
            if self.fd[FLOW_NAMES.APP_SETTINGS].verify_sign_out_btn(timeout=5, raise_e=False):
                self.fd[FLOW_NAMES.APP_SETTINGS].sign_out_hpc_acc()

        self.fd[FLOW_NAMES.APP_SETTINGS].click_create_account_btn()
        hpid_username = self.hpid_username.split("@")
        hpid_username = "{}+{:%Y_%m_%d_%H_%M_%S}@{}".format(hpid_username[0], datetime.datetime.now(), hpid_username[1])
        # Handle for welcome screen of Google Chrome
        self.fd[FLOW_NAMES.GOOGLE_CHROME].handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.fd[FLOW_NAMES.HPID].verify_hp_id_sign_up()
        email, password = self.fd[FLOW_NAMES.HPID].create_account(email=hpid_username)
        # After creating new account, ucde privacy display in timeout=30 seconds
        #After clicking create account button, take sometime to load to UCDE privacy screen
        self.driver.wait_for_context(WEBVIEW_URL.UCDE_PRIVACY, timeout=40)
        #Todo: Skip UCDE screen take longer time, will update it after CR gdg-1768 get fixed
        self.fd[FLOW_NAMES.UCDE_PRIVACY].skip_ucde_privacy_screen(timeout=10)
        #Todo: Wait for designer's reply for updating timeout.
        self.fd[FLOW_NAMES.APP_SETTINGS].verify_app_settings_with_hpc_account(email, raise_e=False, timeout=40)
        return email, password
            
            
    #   -----------------------         FROM DROPBOX       -----------------------------
    def flow_dropbox_log_in(self, username, password):
        """
        If current screen is not Allow Permission of Dropbox, then:
            - Login to an account use Dropbox flow
            - Allow Permission
        :param username:
        :param password:
        """
        if self.fd[FLOW_NAMES.DROPBOX].verify_welcome_screen(raise_e=False):
            self.fd[FLOW_NAMES.DROPBOX].login(username, password)
        self.fd[FLOW_NAMES.DROPBOX].allow_account_access_dropbox(username)

    def flow_dropbox_logout(self):
        """
        Logout Dropbox account
        """
        self.fd[FLOW_NAMES.DROPBOX].load_app()
        # guard code for issue load dropbox. Sometimes will go to device home screen after load_app() function
        if self.driver.get_current_app_activity()[0] != PACKAGE.DROPBOX:
            self.fd[FLOW_NAMES.DROPBOX].load_app()
        if not self.fd[FLOW_NAMES.DROPBOX].verify_welcome_screen(raise_e=False):
            self.fd[FLOW_NAMES.DROPBOX].unlink_devices()
            self.fd[FLOW_NAMES.DROPBOX].skip_choose_dropbox_plan_screen()
            self.fd[FLOW_NAMES.DROPBOX].skip_connect_your_computer_screen()
            self.fd[FLOW_NAMES.DROPBOX].skip_how_to_backup_photos_screen()
            self.fd[FLOW_NAMES.DROPBOX].skip_access_computer_file_screen()
            self.fd[FLOW_NAMES.DROPBOX].logout()

    def get_dropbox_acc(self):
        """
        To avoid issue about limited number devices (max: 3 devices) in one dropbox account for parallel job,
        each platform will be assign its own dropbox account.

        Note: Android 7 and 11 use the same account since Android 7 will be dropped soon.
        """
        accounts = {"8": "android_smart_02", 
                    "9": "android_smart_03", 
                    "10": "android_smart_04",
                    "11": "android_smart_01"}
        current_os = self.driver.platform_version
        return saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"][accounts[current_os]]

    #   -----------------------         FROM Printer       -----------------------------
    def is_printer_ready(self, printer_obj):
        """
        Verify printer is ready for making any job:
            - Check printer assert -> reset printer
            - Check printer ready
        :param printer_obj: printer object (SPL)
        :return: True -> ready. False -> not ready
         """
        printer_obj.check_init_coredump()
        return printer_obj.is_printer_status_ready()

    def get_printer_oobe_name(self, printer_obj, is_ble=True):
        """
        Get Printer's OOBE name for selecting printer in MOOBE process
        Note: Android 10 -> using Wi-Fi Direct MAC address
              Otherwise: Wi-Fi Direct name
        :param printer_obj: SPL instance
        :param is_ble: suport ble or not
        """
        if is_ble and int(self.driver.platform_version) > 9:
            printer_obj.toggle_wifi_direct(on=True)
            mac_addrr = printer_obj.get_wifi_direct_information()["mac address"]
            printer_obj.toggle_wifi_direct(on=False)    #set printer back to beaconnning mode
            return ":".join([mac_addrr[i:i+2] for i in range(0, len(mac_addrr), 2)])
        else:
            return printer_obj.get_wifi_direct_information()["name"]

    def get_moobe_connect_wifi_type(self, printer_obj):
        """
        From printer object, confirm what connect Wi-Fi type of moobe is
        Note": This list of types is from list of printer in Chamber, update it when there is added new type printer.
        :param printer_obj: SPL instance
        :return "awc"/"awc_ble"/"secure_ble"
        """
        types = {"awc": ["naplesplus", "corfuplus", "naples", "naples_minus", "naples_super", "palermo_fast"],
                 "awc_ble": ["palermo_minus", "palermo_super", "verona_base", "malbec"],
                 "secure_ble": ["vasari_base", "vasari_plus", "taccola_plus"]}
        project_name = printer_obj.p_obj.projectName
        for key in types:
            if project_name[:project_name.rfind("_")] in types[key]:
                return key
        raise NotFoundMOOBEConnectWifiType("{} is not found in list of type".format(project_name))

    #   -----------------------         MOBILE DEVICE       -----------------------------
    def transfer_test_data_to_device(self, file_names):
        """
        Transfer test data (.pdf or .jpg files) to mobile device for testing
        :param file_names: list or str (1 file)
        """
        folder_path = {"pdf": TEST_DATA.DOCUMENTS_PDF_FOLDER,
                         "jpg": TEST_DATA.IMAGES_JPG_FOLDER}
        if isinstance(file_names, str):
            file_names = [file_names]
        for fn in file_names:
            file_ext = fn[fn.rfind(".") + 1: ]
            self.driver.wdvr.push_file("{}/{}".format(TEST_DATA.MOBILE_DOWNLOAD, fn), source_path=ma_misc.get_abs_path(os.path.join(folder_path[file_ext], fn)))
            logging.debug("Pushed file to /sdcard/Download/{}".format(fn))

    def verify_existed_file(self, file_path):
        """
        Verify a file is existed/non-existed via file_path
        :param file_path
        :return True -> exist. False -> non-exist
        """
        try:
            self.driver.wdvr.execute_script("mobile:shell", {"command": "ls {}".format(file_path)})
            return True
        except WebDriverException:
            return False

    #   -----------------------         SOFTFAX INFORMATION       -----------------------------
    def get_softfax_recipient_info(self):
        """
        To avoid multiple sending fax jobs on one phone number at the same time, each platform is assigned a fake fax number
        if it is not assigned from pytest argument
        """
        recipients = {"8": "recipient_03", 
                      "9": "recipient_04", 
                      "10": "recipient_05",
                      "11": "recipient_02"}
        current_os = self.driver.platform_version
        recipient_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"][recipients[current_os]]
        request = self.driver.session_data["request"]
        recipient_info["phone"] = request.config.getoption("--recipient-phone") if request.config.getoption("--recipient-phone") else recipient_info["phone"]
        recipient_info["code"] = request.config.getoption("--recipient-code") if request.config.getoption("--recipient-code") else recipient_info["code"]
        return recipient_info

    def make_send_fax_job(self, recipient_phone, sender_name, sender_phone):
        """
        Make Send Fax job (doesn't matter that it is successful or not)
        return: full phone number of recipient
        """
        self.fd[FLOW_NAMES.COMPOSE_FAX].enter_recipient_information(recipient_phone)
        phone, name, code = self.fd[FLOW_NAMES.COMPOSE_FAX].get_recipient_information()
        self.fd[FLOW_NAMES.COMPOSE_FAX].click_add_files_option_btn(self.fd[FLOW_NAMES.COMPOSE_FAX].FILES_PHOTOS_BTN)
        self.fd[FLOW_NAMES.FILES_PHOTOS].verify_files_photos_screen()
        self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].MY_PHOTOS_TXT)
        self.fd[FLOW_NAMES.LOCAL_PHOTOS].select_album_photo_by_index(GOOGLE_PHOTOS.JPG)
        self.fd[FLOW_NAMES.PREVIEW].select_next()
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_compose_fax_screen()
        # Confirmed with developer that 60s here is reasonable as decided by file size
        self.fd[FLOW_NAMES.COMPOSE_FAX].verify_uploaded_file(timeout=60)
        self.fd[FLOW_NAMES.COMPOSE_FAX].enter_sender_information(sender_name, sender_phone)
        self.fd[FLOW_NAMES.COMPOSE_FAX].click_send_fax()
        self.fd[FLOW_NAMES.SEND_FAX_DETAILS].verify_send_fax_detail_screen()
        return "{} {}".format(code, phone)

    #   -----------------------         MOOBE       -----------------------------
    def flow_home_moobe_connect_printer_to_wifi(self, printer_obj, ssid, password, is_ble=True, is_secure=False, create_acc=False):
        """
        This flow is used for AWC, BLE, and secure BLE printer (withou front panel)
        Start from Home screen to connect printer to Wi-Fi via MOOBE steps
        Steps:
            - Load Home screen
            - Load Printer screen from Home
            - CLick on Add Printer 
            - Select OOBE printer on Add Printer screen
            - At Connect Wi-fi screen, enter valid password of ssid and click on Continue button
                + To Android 7, 8, and 9, dismiss turn on bluetooth popup by deny/allow (via enable bluetooth)
            - Go through thermometer to connect printer to wifi
        Expected:
            - Connected screen displays
        
        :param printer_obj: SPL instance
        :param ssid: ssid of network
        :param password: password of ssid
        :param is_ble: Moobe BLE or not
        :param is_secure: True -> check Press button popup for secure BLE printer. False -> ignore this popup
        :param create_acc: signin/create new hpid account
        """
        # Select oobe printer from home screen
        self.flow_home_select_oobe_printer(printer_obj, ssid=ssid, is_ble=is_ble, create_acc=create_acc)

         # Start AWC process
        self.fd[FLOW_NAMES.MOOBE_AWC].connect_printer_to_wifi(ssid, password, is_secure=is_secure, printer_obj=printer_obj)

    def flow_home_select_oobe_printer(self, printer_obj, ssid, is_ble=True, create_acc=False):
        """
        Start from Home scfreen:
            - Go to Printer screen
            - Click on Add printer button on bottom
            - Select target oobe printer on Add Printer screen
        Expected:
            Connect to Wi-Fi screen
        
        :param printer_obj: SPL instance
        :param is_ble: Moobe BLE or not
        :param create_acc: signin/create new hpid account
        """
        self.flow_load_home_screen(create_acc=create_acc)
        self.fd[FLOW_NAMES.HOME].load_printer_selection()
        self.fd[FLOW_NAMES.PRINTERS].select_add()   
        self.fd[FLOW_NAMES.PRINTERS].select_search_printers_popup_continue(is_permission=True, raise_e=False)
        if not is_ble and int(self.driver.platform_version) > 9:
            self.fd[FLOW_NAMES.PRINTERS].select_oobe_awc_printer(self.get_printer_oobe_name(printer_obj, is_ble=is_ble), ssid)
        else:
            self.fd[FLOW_NAMES.PRINTERS].select_oobe_printer(self.get_printer_oobe_name(printer_obj, is_ble=is_ble))

    #   -----------------------      Smart Dashboard       -----------------------------
    def flow_home_smart_dashboard(self):
        """
        1. Load Smart app with hp+ account / ucde account / basic account
        2. Click on Account  button on Home screen
        3. Verify Account Summary screen
        :param account_type: ucde / hp+ / basic
        """
        self.flow_load_home_screen()
        self.fd[FLOW_NAMES.HOME].select_bottom_nav_btn(self.fd[FLOW_NAMES.HOME].NAV_CREATE_ACCOUNT_BTN)
        if self.hpid_account_type == "basic":
            self.driver.wait_for_context(WEBVIEW_URL.HP_CONNECT_BASIC_ACCOUNT, timeout=40)
            self.fd[FLOW_NAMES.HP_CONNECT_BASIC_ACCOUNT].verify_new_printer_page(timeout=10)
        else:
            self.driver.wait_for_context(WEBVIEW_URL.HP_CONNECT, timeout=40)
            self.fd[FLOW_NAMES.HP_CONNECT].accept_privacy_popup()
            if self.hpid_account_type == "hp+":
                self.fd[FLOW_NAMES.HP_CONNECT].verify_account_summary()
            else:
                self.fd[FLOW_NAMES.HP_CONNECT].verify_account_profile_screen()

    def flow_home_smart_dashboard_help_center(self):
        """
        1. Load Smart app with hp+ account
        2. Click on Account  button on Home screen
        3. Verify Account Summary screen
        4. Click on Toggle menu button
        5. Click on Help Center button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT].click_help_center_btn()
        if self.hpid_account_type == "hp+":
            self.fd[FLOW_NAMES.HELP_CENTER].verify_help_center_menu()
        else:
            self.fd[FLOW_NAMES.HELP_CENTER].verify_help_center_menu(invisible=True)

    def load_smart_dashboard_help_center_about_hp_smart(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on About HP Smart item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].ABOUT_HP_SMART)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_about_hp_smart()

    def load_smart_dashboard_help_center_hp_plus(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on HP+ item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].HP_PLUS)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_hp_plus()

    def load_smart_dashboard_help_center_print_scan_and_share(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Print, Scan, and Share item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].PRINT_SCAN_AND_SHARE)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_print_scan_and_share()

    def load_smart_dashboard_help_center_printer_and_connection_info(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Printer and Connection information item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].PRINTER_AND_CONNECTION)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_printer_and_connection_information()

    def load_smart_dashboard_help_center_additional_help_and_support(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard Help center screen
        2. Click on Additional help and support item
        """
        self.flow_home_smart_dashboard_help_center()
        self.fd[FLOW_NAMES.HELP_CENTER].click_link_on_help_center_screen(self.fd[FLOW_NAMES.HELP_CENTER].ADDITIONAL_HELP_AND_SUPPORT)
        self.fd[FLOW_NAMES.HELP_CENTER].verify_additional_help_and_support()

    def load_edit_screen_through_camera_scan(self):
        """
        1. Load app to camera scan screen
        2. Capture a picture, and lead to Preview screen
        3. Click on Page options button / Edit button
        """
        self.flow_load_home_screen()
        self.flow_home_camera_scan_pages()
        self.fd[FLOW_NAMES.PREVIEW].verify_preview_nav()
        self.fd[FLOW_NAMES.PREVIEW].select_preview_image_opts_btn(self.fd[FLOW_NAMES.PREVIEW].EDIT_BTN)
        self.fd[FLOW_NAMES.PREVIEW].check_run_time_permission()
        self.fd[FLOW_NAMES.EDIT].verify_edit_page_title()
    
    def flow_home_smart_dashboard_account_menu(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / Account button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT].click_account_btn()
        self.fd[FLOW_NAMES.HP_CONNECT_ACCOUNT].verify_account_menu_screen()
    
    def flow_home_smart_dashboard_features_menu(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / Features button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_FEATURES].click_features_btn()
        if self.hpid_account_type == "hp+":
            self.fd[FLOW_NAMES.HP_CONNECT_FEATURES].verify_features_screen(invisible=False)
        else:
            self.fd[FLOW_NAMES.HP_CONNECT_FEATURES].verify_features_screen(invisible=True)
    
    def flow_home_smart_dashboard_hp_instant_ink(self):
        """
        1. Load Smart app with hp+ account to Smart Dashboard
        2. Click on Toogl menu / HP Instant Ink button
        """
        self.flow_home_smart_dashboard()
        self.fd[FLOW_NAMES.HP_CONNECT].click_menu_toggle()
        self.fd[FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK].click_hp_instant_ink_btn()
        self.fd[FLOW_NAMES.HP_CONNECT_HP_INSTANT_INK].verify_hp_instant_ink_menu_screen()