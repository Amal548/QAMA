import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY, WEBVIEW_CONTEXT, WEBVIEW_URL


pytest.app_info = "SMART"

class Test_suite_02_Value_Prop(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.web_welcome = cls.fc.flow[FLOW_NAMES.WEB_SMART_WELCOME]
        cls.value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        #Defind variable
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])

    def test_01_value_prop_screen(self):
        """
        Description:
         1. Click on Yes/No button on Analytics Consent screen

        Expected Result:
         1. Value Prop screen
        """
        self.__load_value_prop_from_welcome()

    def test_02_set_up_new_printer(self):
        """
        Description:
         1. Load Value Prop screen on Welcome flow
         2. Click on Set up a New Printer

        Expected Result:
         2. Printers screen
        """
        self.__load_value_prop_from_welcome()
        self.value_prop.select_value_prop_buttons(index=0)
        self.printers.verify_printers_screen()

    def test_03_sign_in(self):
        """
        Description:
         1. Load Value Prop screen on Welcome flow
         2. Click on Sign In

        Expected Result:
         2. Sign IN screen of HPID
        """
        self.__load_value_prop_from_welcome()
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        self.value_prop.select_value_prop_buttons(index=1)
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_in()

    def test_04_skip_for_now(self):
        """
        Description:
         1. Load Value Prop screen on Welcome flow
         2. Click on Skip for Now

        Expected Result:
         2. Home screen of Android Smart app
        """
        self.__load_value_prop_from_welcome()
        self.value_prop.select_value_prop_buttons(index=2)
        self.home.verify_home_nav()

    def test_05_relaunch_app(self):
        """
        Description:
         1. Load Value Prop screen on Welcome flow
         2. Relaunch app

        Expected Result:
         2. Home screen of Android Smart app
        """
        self.__load_value_prop_from_welcome()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.home.verify_home_nav()

    @pytest.mark.parametrize("confirm", ["yes", "no"])
    def test_06_press_mobile_back_btn(self, confirm):
        """
        Description:
         1. Load Value Prop screen on Welcome flow
         2. Press Mobile back key button
         3. CLick on Yes/No of "Are you sure?" popup

        Expected Result:
         2. Are you sure popup
         3. No: Value Prop screen
            Yes: Home screen
        """
        self.__load_value_prop_from_welcome()
        self.driver.press_key_back()
        is_yes = True if confirm == "yes" else False
        self.home.skip_are_you_sure_popup(is_yes=is_yes)
        if confirm == "yes":
            self.home.verify_home_nav()
        else:
            self.value_prop.verify_ows_value_prop_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_value_prop_from_welcome(self):
        """
        - Reset app to launch app as first time
        - Launch app
        - Click on Continue button
        - Skipp Share Uage screen with Yes button
        - Verify Value Prop screen
        """
        self.fc.reset_app()
        self.driver.wdvr.start_activity(self.pkg_name, LAUNCH_ACTIVITY.SMART)
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.web_welcome.verify_welcome_screen()
        self.web_welcome.click_accept_all_btn()
        self.driver.switch_to_webview(webview_name='NATIVE_APP')
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        # Currently HPID take 10-20s to load to value prop screen.
        self.value_prop.verify_ows_value_prop_screen()