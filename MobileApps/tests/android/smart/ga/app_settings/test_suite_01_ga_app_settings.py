from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
from SAF.misc import saf_misc
import pytest
import time
import logging

pytest.app_info = "SMART"

class Test_Suite_01_GA_App_Settings(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hpid = HPID(driver=cls.driver)
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"][
            "username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"][
            "password"]


    def test_01_ga_app_settings(self):
        """
        Preconditions:
        - Make sure the printer connected to stage stack
        - Make sure our App is on Stage stack

        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from search icon)
        - Verify Home Screen with printer connected
        - Click on More Option ico (3 dots)
        - Click on App Settings
        - Verify App Settings screen
        - Click on Sign in button
        - Type HPC account with username and password
        - Click on Sign In button
        - Verify App Settings screen with HPC account sign in success

        # Currently Sign Out event haven't been automated since Appium issue about login from Website
        - Click on Sign Out button
        - Click on SIGN OUT button
        - Verify App Setting screen
        - Click on Sign In button
        - Type HPC account with username and password
        - Click on Sign In button
        - Verify App settings screen with HPC account sign in success
        - Click on Offer to reduce size
        - Verify Offer to reduce size screen
        - Click on switch button to Off
        - Click on Back button
        - Verify App Settings screen with HPC account sign in success
        - Verify Home screen with connected printer
        - Click on Printer Image on Home screen
        - Verify My Printer screen
        - Click on Print Anywhere
        - Verify Print Anywhere without sign in screen
        - Close App
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_more_options_app_settings()
        self.app_settings.verify_app_settings()
        self.app_settings.click_sign_in_btn()

        # Login HPC account
        if self.hpid.verify_hp_id_sign_in():
            self.driver.swipe()
            self.hpid.login(self.hpid_username, self.hpid_pwd)
        else:
            logging.info("App is already signed to an HPID account")
        time.sleep(10)
        self.app_settings.verify_app_settings_with_hpc_account(username=self.hpid_username)
        self.app_settings.click_file_size_reduction()
        self.app_settings.verify_file_size_reduction()
        self.fc.select_back()
        self.app_settings.verify_app_settings_with_hpc_account(username=self.hpid_username)
        self.app_settings.click_sign_out_btn(ga=False)
        self.app_settings.click_sign_out_btn(ga=True)
        self.app_settings.verify_app_settings()

        #Click Print anywhere when printer supported this feature
        self.fc.select_back()
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SETTINGS), is_permission=False)
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])
        self.printer_settings.select_print_anywhere()
        self.printer_settings.verify_print_anywhere_before_enabled()
