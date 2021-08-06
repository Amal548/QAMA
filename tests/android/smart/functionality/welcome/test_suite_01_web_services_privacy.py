import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, PACKAGE, LAUNCH_ACTIVITY
from MobileApps.resources.const.android.const import WEBVIEW_URL, WEBVIEW_CONTEXT


pytest.app_info = "SMART"

class Test_suite_01_Web_Service_Privacy(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.privacy_preference = cls.fc.flow[FLOW_NAMES.PRIVACY_PREFERENCES]

        #Defind variable
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
    
    def test_01_web_services_privacy_with_relaunch_app(self):
        """
        Description:
         1. Start app as first launch
         2. Relaunch app

        Expected Result:
         1. Webservice privacy of welcome screen
         2. Webservice privacy of welcome screen
                + There are 3 links
        """
        self.__load_app_first_screen_welcome()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        # Switch back to native app, so that next line of code actually switch into webview after relaunching app
        # because after relaunching the app, the previous webview context is refreshed; 
        # however switch_to_webview() cannot force to switch to webview again
        self.driver.switch_to_webview(webview_name='NATIVE_APP')
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.web_welcome.verify_welcome_screen()
        self.web_welcome.verify_click_btn()
        self.web_welcome.verify_manage_options()

    def test_03_term_of_use_link(self):
        """
        Description:
         1. Start app as first launch
         2. Click on HP Smart term of Usage link
        
        Expected Result:
         2. "Term of Use - Worldwide" screen
            https://www.hpsmart.com/us/en/tou
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_link(self.web_welcome.TERM_USE_LINK)
        self.web_welcome.verify_terms_of_use_page()

    def test_04_end_user_license_agreement(self):
        """
        Description:
         1. Start app as first launch
         2. Click on End User License Agreement link

        Expected Result:
         2. "Select a location" popup of End User License Agreement
            https://support.hp.com/us-en/document/c00581401?openCLC=true
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_link(self.web_welcome.EULA_LINK)
        self.web_welcome.verify_eula_page()

    def test_05_press_mobile_back_btn(self):
        """
        Description:
         1. Start app as first launch
         2. Press Back button of mobile device
         3. Launch app again
         
        Expected Result:
         2. Exit Android Smart app
         3.  Webservice privacy of welcome screen
        """
        self.__load_app_first_screen_welcome()
        self.driver.press_key_back()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        # switching to native app force implemnting of switch to webview for next line of code
        # due to issue like above.
        self.driver.switch_to_webview(webview_name='NATIVE_APP')
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.web_welcome.verify_welcome_screen()
    
    def test_06_verify_all_btn(self):
        """
        Verify the buttons
        Description:
        1. Launch the App
        2.HP Smart Suite and Web services (Privacy) screen is launched.
        3.Tap on "Accept All" Button
        4.Observe
        5.Tap on "More Options" Button
        6.Observe
        Expected Results:
        1) Verify tapping on "Accept All" Button should launch the OWS Value Prop Screen.
        2) Verify Tapping on "More Options" should launch "Manage Privacy Preferences" screen. 
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_accept_all_btn()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=40)
        self.value_prop.verify_ows_value_prop_screen(timeout=20)
        self.__load_app_first_screen_welcome()
        self.web_welcome.verify_manage_options()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen() 

    def test_07_privacy_preference_screen(self):
        """
        Verify Privacy preference screen UI
        Description:
        1.Launch the App
        2.Verify Smart Suite and Web services (Privacy) screen.
        3.Tap on "More Options"
        4."Manage Privacy Preferences" screen is launched
        5.Observe the UI of the screen 
        
        Verify the screen looks as shown in the image below:
        1) Verify privacy preference screen
        2) Verify 4 Toggle Switches "Required", "Analytics", "Advertising", "Personalized".
        3) Verify there are two buttons "Continue" and "Back".
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen()
        self.privacy_preference.verify_toggles(self.privacy_preference.APP_ANALYTICS)
        self.privacy_preference.verify_toggles(self.privacy_preference.ADVERTISING)
        self.privacy_preference.verify_toggles(self.privacy_preference.PERSONALIZED_SUGGESTIONS)
        self.privacy_preference.verify_continue_btn()
        self.privacy_preference.verify_back_btn()
    
    def test_09_verify_continue_btn(self):
        """ 
        Verify continue button launches OWS value Prop screen
        Description:
        1.Launch the App
        2.Verify Smart Suite and Web services (Privacy) screen.
        3.Tap on "More Options"
        4."Manage Privacy Preferences" screen is launched
        5.Enable and Disable the switches
        6.Tap on "Continue" Button
        7.Observe
        
        Verify Tapping on "Continue" Button Launches OWS Value Prop screen
        """
        self.__load_app_first_screen_welcome()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen()
        self.privacy_preference.toggle_privacy_options(self.privacy_preference.APP_ANALYTICS, state =False)
        self.privacy_preference.toggle_privacy_options(self.privacy_preference.ADVERTISING, state =True)
        self.privacy_preference.toggle_privacy_options(self.privacy_preference.PERSONALIZED_SUGGESTIONS, state =False)
        self.privacy_preference.click_continue()
        self.driver.switch_to_webview(webview_name='NATIVE_APP')
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.value_prop.verify_ows_value_prop_screen()

    def test_10_verify_back_btn(self):
        """ Verify clicking back button launches welcome screen
        Description:
        1.Launch the App
        2.Verify Smart Suite and Web services (Privacy) screen.
        3.Tap on "More Options"
        4."Manage Privacy Preferences" screen is launched
        5.Tap on "Back" Button
        6.Observe 
        Verify Tapping on "Back" Button relaunches the Welcome Screen"""

        self.__load_app_first_screen_welcome()
        self.web_welcome.click_manage_options()
        self.privacy_preference.verify_privacy_preference_screen()
        self.privacy_preference.click_back_btn()
        self.web_welcome.verify_welcome_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_app_first_screen_welcome(self):
        """
        Load first screen of Welcome
        """
        self.fc.reset_app()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.web_welcome.verify_welcome_screen()
