import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, PACKAGE, LAUNCH_ACTIVITY


pytest.app_info = "SMART"

class Test_suite_01_home_nav_notification(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.notification = cls.fc.flow[FLOW_NAMES.NOTIFICATION]
        cls.hpps = cls.fc.flow[FLOW_NAMES.HPPS]
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.fax_welcome = cls.fc.flow[FLOW_NAMES.SOFTFAX_WELCOME]
    
    def test_01_home_nav_notifications_btn(self):
        """
        Verify Mobile Fax and Smart Tasks options can be seen in notification screen from HP Smart home.
        C13266447
        Step:
        1. Tap on bell icon from Home page to go to Notification page

        Expected Results:
        1.Verify notification page
        2.Verify "Mobile Fax" and "Smart Task" options under Activity tab
        3. When logged in verify "Supplies" and "Account" options under Activity tab
        """        
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.verify_mobile_fax_option()
        self.notification.verify_shortcuts_option()
        self.notification.verify_supplies_option()
        self.notification.verify_account_option()
    
    def test_02_popup_under_inbox_on_notification_screen(self):
        """
        C27761736
        Verify a popup appears when clicking on inbox on notification screen for first time after user login
        Pre-condition & Steps:
        1.Freshly install the app/ Upgrade the App
        2.Launch the App
        3.Navigate to Home Page
        4.Make sure "Inbox" has never been clicked before using the HPID User Account that is used to login.
        5.Tap on Notification bell icon
        6.Tap on "Inbox"
        
        Expected Results:
        1)Verify a Popup Screen with a 'Yes' or 'No' option
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_inbox()
        self.notification.verify_welcome_popup()
    
    def test_03_verify_no_option_welcome_inbox_screen_popup(self):
        """
        C17466847
        Verify NO option on Welcome to HP inbox screen popup
        Steps:
        1.Freshly install the app/ Upgrade the App
        2.Launch the App
        3.Navigate to Home Page
        4.Make sure "Inbox" has never been clicked before using the HPID User Account (used to login)
        5.Tap on Notification bell icon
        6.Tap on "Inbox" under "Notification" screen
        7.Verify a Popup Screen with a 'Yes' or 'No' option
        8.Tap on 'NO' from the Pop-up screen
        9.Relaunch the App and verify that the Pop up is no longer displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_inbox()
        self.notification.verify_welcome_popup()
        self.hpps.check_run_time_permission()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_inbox()
        self.notification.verify_inbox_screen()
        
    def test_04_verify_yes_option_welcome_inbox_screen_popup(self):
        """
        C17466850
        Verify YES option on Welcome to HP inbox screen popup
        Steps:
        1.Freshly install the app/ Upgrade the App
        2.Launch the App
        3.Navigate to Home Page
        4.Make sure "Inbox" has never been clicked before using the HPID User Account (used to login)
        5.Tap on Notification bell icon
        6.Tap on "Inbox" under "Notification" screen
        7.Verify a Popup Screen with a 'Yes' or 'No' option
        8.Tap on 'YES' from the Pop-up screen
        9.Relaunch the App and verify that the Pop up is no longer displayed
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_inbox()
        self.notification.verify_welcome_popup()
        self.hpps.check_run_time_permission(accept=True)
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_inbox()
        self.notification.verify_inbox_screen()
        
    def test_05_verify_mobile_fax_activity_user_logged_out(self):
        """
        C19536556
        Verify Mobile Fax behaviour under activity tab whrn user is looged in then loggs out
        Steps:
        1.Install and launch app.
        2.Add printer to the carousel
        3.Make sure user is logged in into App settings (HPID) 
        4.Tap on bell icon from Home page to go to Notification page
        5.Tap on "Mobile Fax" option under "Activity" tab
        6.Now go to App Settings and Log out
        7.Tap on the bell icon from Home page to go to Notification page
        8.Tap on "Mobile Fax" option under "Activity" Tab
        
        Expected Results:
        1)The Fax history page should be displayed.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_log_out_hpid_from_app_settings()
        self.driver.back()
        self.home.select_notifications_icon()
        self.notification.select_mobile_fax()
        self.fax_welcome.verify_welcome_screen()

    def test_06_verify_mobile_fax_user_logged_in(self):
        """
        C19536556
        Verify the Mobile Fax Behavior under Activity Tab when the user is LOGGED IN
        Steps:
        1.Tap on bell icon from Home page to go to Notification page
        2.Tap on "Mobile Fax" option under "Activity" tab
        
        Expected Results:
        1) Verify fax history page
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.home.select_notifications_icon()
        self.notification.select_mobile_fax()
        self.fax_history.verify_fax_history_screen()