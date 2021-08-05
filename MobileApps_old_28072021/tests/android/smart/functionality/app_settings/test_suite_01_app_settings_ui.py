from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *

pytest.app_info = "SMART"

class Test_Suite_01_App_Settings_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.about = cls.fc.flow[FLOW_NAMES.ABOUT]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.privacy_preferences = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]
        cls.smart_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]

    def test_01_app_settings_ui_without_sign_in(self):
        """
        Description:
         1. Load to Home screen (reset app to make sure not any hpc account logged in on App Settings screen)
         2. Click on 3 
         3. Click on App Settings
        Expected Result:
         3. Verify App Settings screen without hpc account logged in:
            + Title
            + Sign In button
        """
        self.__load_app_settings_screen()
        self.app_settings.verify_app_settings()
        self.app_settings.verify_sign_in_btn()

    def test_02_app_settings_help_center(self):
        """
        Description:
         1. Load Home screen
         2. Click on App Settings icon from navigation bar of Home screen
         3. Click on Help Center button
        Expected Result:
         3. Verify Welcome to HP Smart App Help and Support screen popup on chrome browser
        """
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.app_settings.select_app_settings_opt(self.app_settings.HELP_CENTER)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    @pytest.mark.parametrize("app_settings_opt", ["about", "use_5ghz_wifi", "notification_and_privacy"])
    def test_03_app_settings_opt_verify(self, app_settings_opt):
        """
        Description:
         1. Load Home screen
         2. Click on App Settings from more option screen
         3. Click on the item on App Settings screen:
            - About
            - Use 5GHz WiFi
            - Notifications and Privacy
        Expected Result:
         3. Verify each item screen
            - About screen
            - Use 5GHz WiFi screen
            - Notifications and Privacy screen
        """
        app_settings_opts = {"about": self.app_settings.ABOUT,
                             "use_5ghz_wifi": self.app_settings.USE_5GHZ_WIFI,
                             "notification_and_privacy": self.app_settings.NOTIFICATIONS_AND_PRIVACY,
                      }
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.app_settings.select_app_settings_opt(app_settings_opts[app_settings_opt])
        if app_settings_opt == "about":
            self.about.verify_about_screen()
        elif app_settings_opt == "use_5ghz_wifi":
            self.app_settings.verify_notification_privacy_opt_screen(self.app_settings.USE_5GHZ_WIFI)
            self.app_settings.toggle_on_off_btn(enable=True)
        else:
            self.app_settings.verify_notification_privacy_screen()

    @pytest.mark.parametrize("item_name", ["supply_status", "promotional_messaging"])
    def test_04_notification_and_pricy_opt_verify(self, item_name):
        """
        Description:
         1. Load to App Settings screen
         2. Click on Notifications and Privacy
         3. Click on each item on Notifications and Privacy screen:
            - Supply Status
            - Promotional Messaging
            - App Improvement
         4. - Turn on the switch icon for Promotional Messaging
            - Turn off the switch icon for Supply Status and App Improvement
        Expected Result:
         3. Verify each item's screen with below points:
            + Title
            + On/Off Switch icon
            + Message
         4. Verify each item's screen with:
            + Switch icon status is off
        :param item_name:
        """
        item_names = {"supply_status": self.app_settings.SUPPLY_STATUS,
                      "promotional_messaging": self.app_settings.PROMOTIONAL_MESSAGING,
                      }
        self.__load_app_settings_screen()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(item_names[item_name])
        self.app_settings.verify_notification_privacy_opt_screen(item_names[item_name])
        if item_name == "promotional_messaging":
            self.app_settings.toggle_on_off_btn(enable=True)
        else:
            self.app_settings.toggle_on_off_btn(enable=False)

    @pytest.mark.parametrize("opt_name", ["sign_out_success", "cancel_sign_out"])
    def test_05_app_settings_hpc_account_sign_out_options(self, opt_name):
        """
        Description:
         1. Load to App Settings screen with account signed in
         2. Click on Sign In button
         3. Enter account email and pwd
         4. Click on Sign Out button on App Settings screen
         5. Click on Sign Out button
        Expected Result:
         3. Verify App Settings screen with below points:
            + Title
            + Sign In button
            + Account Information
         5. Verify App Settings screen with below points:
            + Title
            + Sign In button
        """
        self.__load_app_settings_screen(is_nav_app_settings_btn=True)
        self.fc.flow_app_settings_sign_in_hpid()
        if opt_name == "sign_out_success":
            self.app_settings.sign_out_hpc_acc()
            self.app_settings.verify_app_settings()
        else:
            self.app_settings.click_sign_out_btn()
            self.app_settings.click_cancel_btn()
            self.app_settings.verify_app_settings_with_hpc_account(self.fc.hpid_username)

    def test_06_app_settings_hpc_account_sign_in_cancel(self):
        """
        Description:
         1. Load to App Settings screen without account sign in
         2. Click on Sign In button
         3. Click on Close button on Sign in page
        Expected Result:
         3. Verify App Settings screen with below points:
            + Title
            + Sign In button
        """
        self.fc.flow_home_log_out_hpid_from_app_settings()
        # Remove HPID in cached of Google Chrome -> avoid to automatically log in
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        # For Android 7/8/9, direct into mobile device home screen instead of app settings screen after clear cache for Google Chrome. We submitted CR AIOA-8868 for this issue. This is temporay fix until the CR get fixed
        if not self.app_settings.verify_sign_in_btn(invisible=False, raise_e=False):
            self.fc.flow_load_home_screen(skip_value_prop=True)
            self.home.select_more_options_app_settings()
        self.app_settings.click_sign_in_btn()
        self.chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_in()
        self.chrome.click_webview_close_btn()
        self.app_settings.verify_app_settings()
    
    def test_07_app_settings_compare_manage_privacy_preferences_with_welcome_flow(self):
        """
        Description:
        1. Launch the App and Tap on Manage Options
        2. From the Manage Privacy Preferences screen, Enable and Disable few switches to enable and disable few consents.
        3. Skip sign in and Navigate to Home screen
        4. Go to App Settings -> Notifications and Privacy ->Privacy
        5. Under Personalized Promotions section, Tap on "Manage my Privacy Settings" link.
        Expected Result:
        1. Verify the toggle switches enabled from the welcome flow are also enabled under App Setting.
        2. Verify user is able to enable and disable privacy preferences 
        by enabling and disabling the options under Manage my Privacy Settings
        """

        self.fc.reset_app()
        self.fc.load_manage_options()
        self.privacy_preferences.toggle_privacy_options(self.privacy_preferences.APP_ANALYTICS, state=True)
        self.privacy_preferences.click_continue()
        self.__load_app_settings_screen()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.MANAGEMENT_MY_PERSONALIZED_PROMOTIONS)
        self.privacy_preferences.toggle_privacy_options(self.privacy_preferences.APP_ANALYTICS, state=False)

    def test_07_app_settings_compare_manage_privacy_preferences_with_welcome_flow(self):
        """
        Description:
        1. Launch the App and Tap on Manage Options
        2. From the Manage Privacy Preferences screen, Enable and Disable few switches to enable and disable few consents.
        3. Skip sign in and Navigate to Home screen
        4. Go to App Settings -> Notifications and Privacy ->Privacy
        5. Under Personalized Promotions section, Tap on "Manage my Privacy Settings" link.
        Expected Result:
        1. Verify the toggle switches enabled from the welcome flow are also enabled under App Setting.
        2. Verify user is able to enable and disable privacy preferences 
        by enabling and disabling the options under Manage my Privacy Settings
        """

        self.fc.reset_app()
        self.fc.load_manage_options()
        self.privacy_preferences.toggle_privacy_options(self.privacy_preferences.APP_ANALYTICS, state=True)
        self.privacy_preferences.click_continue()
        self.__load_app_settings_screen()
        self.app_settings.select_app_settings_opt(self.app_settings.NOTIFICATIONS_AND_PRIVACY)
        self.app_settings.select_notification_privacy_opt(self.app_settings.MANAGEMENT_MY_PERSONALIZED_PROMOTIONS)
        self.privacy_preferences.toggle_privacy_options(self.privacy_preferences.APP_ANALYTICS, state=False)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_app_settings_screen(self, is_nav_app_settings_btn=False):
        """
        If current screen is not Home screen, load to Home screen.
        Click on 3 dots on Home screen
        Click on App Settings icon
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        if is_nav_app_settings_btn:
            self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN)
        else:
            self.home.select_more_options_app_settings()