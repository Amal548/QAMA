import pytest
import logging
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES


pytest.app_info = "SMART"
class Test_Suite_08_Home_UI_toolbar(object):
    @pytest.fixture(scope="class",autouse="true")
    def class_setup(cls,android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        #define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
    
    @pytest.mark.capture_screen
    def test_01_signin_btn_validation(self):
        """
        Test Case: C28370572
        Description:
        1.Freshly Install the App
        2.Launch the App
        3.Accept all the consents
        4.Use the back button on phone to go to home screen.
        5.Tap on the "Sign In" Button

        Expected Result:
        The "Sign In" button is available in the Home screen toolbar when user is not logged in.
        Tapping on the "Sign In" button launches Signin screen
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_SIGN_IN_BTN)
        self.google_chrome.handle_welcome_screen_if_present()
        self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_in()

    @pytest.mark.capture_screen
    def test_02_create_account_btn_validation(self):
        """
        Test Case: C28370571
        Description:
        1.Freshly Install the App
        2.Launch the App
        3.Accept all the consents
        4.Use the back button on phone to go to Home screen.
        5.Tap on App settings
        6.Tap on the "Create Account" Button
        
        Expected Result:
        Tapping on the button launches User Onboarding
        with no value prop and goes to the HPID Create Account screen
        """

        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_bottom_nav_btn(self.home.NAV_APP_SETTINGS_BTN)
        self.app_settings.click_create_account_btn()
        self.google_chrome.handle_welcome_screen_if_present()
        self.fc.fd[FLOW_NAMES.HPID].verify_hp_id_sign_up()

    def test_03_verify_logo_on_home_screen(self):
        """
        Pre-condition:
        1.Clear Cache, Clear Storage of the previous App from the Phone Settings
        Steps:
        1.Install Latest App
        2.Follow the Welcome Flow with all options from UCDE & App Value prop Screen
        3.Verify Home Screen is displayed
        Expected Result:
        1.Verify the Logo on the top left corner of the Home Screen.
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen(skip_value_prop=False)
        self.home.verify_hp_logo()
