from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import NoSuchWindowException, TimeoutException
import logging

pytest.app_info = "SMART"

class Test_Suite_01_User_Onboarding(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.ucde_privacy = cls.fc.flow[FLOW_NAMES.UCDE_PRIVACY]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.fax_history =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.privacy_preferences = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]

        # Define the variable
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])

    @pytest.mark.parametrize("sign_type",["new_account", "existed_account"])
    def test_01_create_account_sign_in(self, sign_type):
        """
        Description: C28073477, C28073476
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on Account button
         3. If sign_type == "existed_account": then Sign In an HPID account
            If sign_type == "new_account", then Login with a new HPID account
        Expected Result:
         3. Verify HPID create new account screen:
         3. Verify Home screen with account login success:
            - Buttons on navigation bar are visible: Printer Scan / Camera Scan / View & Print
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_CREATE_ACCOUNT_BTN)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_up()
        if sign_type == "existed_account":
            self.hpid.click_sign_in_link_from_create_account()
            self.hpid.verify_hp_id_sign_in()
            self.hpid.login(self.fc.hpid_username, self.fc.hpid_password, change_check={"wait_obj": "sign_in_button", "invisible": True})
        else:
            self.hpid.create_account()
            self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
            #Todo: Skip UCDE screen take longer time, will update it after CR gdg-1768 get fixed
            self.ucde_privacy.skip_ucde_privacy_screen(timeout=10)
        #After UCDE privacy screen, app still will take some time to load to HPID information before go to next screen
        self.home.verify_bottom_nav_btn(btn=self.home.NAV_PRINTER_SCAN_BTN, timeout=20)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
       
    def test_02_sign_in_from_app_settings(self):
        """
        Description: C27212800
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on App Settings
         3. Click on Sign In button
         4. Login an HPID account
         5. Click on Back button from App Settings
        Expected Result:
         5. Verify Home screen with account login success:
            - Buttons on navigation bar are visible: Printer Scan / Camera Scan / View & Print
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_home_sign_in_hpid_account()
        self.fc.select_back()
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN)
        self.home.verify_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
    
    def test_03_user_onboarding_not_offered_again(self):
        """
        Description: C27212766
         1. Load Home screen with user onboarding account login
         2. Click on Print Photos tile
         
        Expected Result:
         2. Verify View & Print screen
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.file_photos.verify_files_photos_screen()

    @pytest.mark.parametrize("from_source",["shortcuts", "mobile_fax"])
    def test_04_notification_mobile_fax(self, from_source):
        """
        Description: C27864739, C27735802
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on notification button
         3. If from_source == "mobile_fax" then, Click on Mobile Fax
            If from_source == "shortcuts" then, Click on Shortcuts
         4. Login HPID
        Expected Result:
         3. Verify ows value prop screen-
         4. Make sure HPID login success
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_notifications_icon()
        self.home.verify_notification_screen()
        if from_source == "shortcuts":
            self.notification.select_shortcuts()
        else:
            self.notification.select_mobile_fax()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=30)
        # Currently HPID take 10-20s to load to value prop screen.
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
        self.ows_value_prop.select_value_prop_buttons(index=1)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context("WEBVIEW_chrome")
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.fc.hpid_username, self.fc.hpid_password, change_check={"wait_obj": "sign_in_button", "invisible": True})
        if from_source == "mobile_fax":
            #After HPID login, app will take some time direct into next screen for loading HPID account information
            self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=20)
            try:
                self.fax_history.verify_fax_history_screen(invisible=False, timeout=10)
            except NoSuchWindowException:
                logging.info("Window is close. Try to connect window again and rerun verification")
                self.driver.wdvr.switch_to.window(self.driver.wdvr.window_handles[0])
                self.fax_history.verify_fax_history_screen(invisible=False)

    def test_05_personalized_promotions(self):
        """
        Description: C27891989
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on App Settings
         3. Click on Notification and Privacy
         4. Click on Manage my Personalized Promotions consent
         5. Click on Sign In button
         6. Login with an HPID account
        Expected Result:
         5. Verify HPID create new account screen
         6. Verify Privacy Setting screen with webview mode
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_app_settings()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.MANAGEMENT_MY_PERSONALIZED_PROMOTIONS)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=15)
        self.privacy_preferences.verify_privacy_preference_screen(timeout=15)

    @pytest.mark.parametrize("btn_name", ["yes", "no"])
    def test_06_ucde_privacy_are_you_sure_popup(self, btn_name):
        """
        Description: C27735807
         1. Load to UCDE privacy screen through app settings
         2. Click on Back button from Mobile device
         3. If btn name == yes, then Click on Yes button
            If btn_name == no, then click on No button
         
        Expected Result:
         2. Verify Are you sure? popup
         3. If btn name == yes, then verify app settings screen
            If btn_name == no, then verify UCDE Privacy screen
        """
        self.__load_ucde_privacy_screen_through_app_settings()
        self.driver.press_key_back()
        self.app_settings.skip_are_you_sure_popup(is_yes=True if btn_name == "yes" else False)
        if btn_name == "no":
            self.ucde_privacy.verify_ucde_privacy_screen(timeout=10)
        else:
            self.app_settings.verify_app_settings()

    def test_07_ucde_privacy_learn_more(self):
        """
        Description: C27735807
         1. Load to UCDE privacy screen through app settings
         2. Click on Learn More link from UCDE Privacy screen

        Expected Result:
         2. Verify HP Print Account Data Usage Notice screen
        """
        self.__load_ucde_privacy_screen_through_app_settings()
        self.ucde_privacy.select_learn_more_link()
        if self.ucde_privacy.verify_your_privacy_screen(raise_e=False):
            self.ucde_privacy.select_i_accept_btn()
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_08_user_onboarding_close(self):
        """
        Description: C28073479
         1. Load Home screen without user onboarding account login (make sure app is the clear one)
         2. Click on Print Photo tile
         3. Click on Close button
         
        Expected Result:
         2. Verify value prop screen
         3. Verify Home screen without HPID account login
        """
        # Add clear cache here to make sure HPID isn't login from previous test
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=30)
        # Currently HPID take 10-20s to load to value prop screen.
        try:
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
        except TimeoutException:
            # work around for some devices being brought to chrome
            self.google_chrome.handle_welcome_screen_if_present()
            self.driver.press_key_back()
            self.home.verify_home_nav()
            self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
            self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
        self.ows_value_prop.select_value_prop_buttons(index=2)
        #After close HPID page, app need take some time to load to previous screen
        self.home.verify_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN, timeout=15, invisible=True)
        self.home.verify_bottom_nav_btn(self.home.NAV_CAMERA_SCAN_BTN, invisible=True)
    
    def test_09_login_from_shortcuts_tile_when_consent_not_accept_from_app_settings(self):
        """
        Description: C28183360
         1. Load to UCDE privacy screen through app settings
         2. Close the app
         3. Launch app again, and lead App to Home screen
         4. Click on Smart Tasks tile

        Expected Result:
         4. Verify value ows prop screen
        """
        self.__load_ucde_privacy_screen_through_app_settings()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.home.verify_home_nav()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.shortcuts))
        self.fc.verify_invisible_transition_screen()
        self.driver.wait_for_context(WEBVIEW_URL.OWS_VALUE_PROP)
        # Currently HPID take 10-20s to load to value prop screen.
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
    
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_ucde_privacy_screen_through_app_settings(self):
        """
        1. Load Home screen without user onboarding account login (make sure app is the clear one)
        2. Click on App Settings
        3. Click on Sign In button
        4. Fill all account information, anc click CREATE ACCOUNT button
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_app_settings()
        self.app_settings.click_create_account_btn()
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_up()
        self.hpid.create_account()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=30)
        self.ucde_privacy.verify_ucde_privacy_screen(timeout=10)
