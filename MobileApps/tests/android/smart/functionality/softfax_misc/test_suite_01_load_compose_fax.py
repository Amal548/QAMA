import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import PACKAGE, WEBVIEW_CONTEXT, WEBVIEW_URL

pytest.app_info = "SMART"


class Test_Suite_01_Load_Compose_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.softfax_welcome = cls.fc.flow[FLOW_NAMES.SOFTFAX_WELCOME]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.vallue_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.ucde = cls.fc.flow[FLOW_NAMES.UCDE_PRIVACY]
        cls.chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]
        cls.fax_history =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.softfax_offer = cls.fc.flow[FLOW_NAMES.SOFTFAX_OFFER]


    def test_01_load_compose_fax_by_login_via_tile(self):
        """
        Precondition: App is not login to any accounts
        Description:
            1/ Enable Mobile Fax tile
            2/ Click on Mobile Fax at Home screen
            3/ Click on Sign In button on Value Prop screen
            4/ Log in into a HPID account
            5/ Dismiss App Permision
            6/ Load Home screen again-> go to App Settings.        
        Expected Result:
            4/ App Permission display
            5/ Compose Fax screen
            6/ HPID is logged in
        """
        self.fc.flow_home_log_out_hpid_from_app_settings()
        # Remove HPID in cached of Google Chrome -> avoid to automatically log in
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        #Load home screen again instead of clicking Back button as defect AIOA-8868. Will use click back button function after AIOA-8868 get fixed
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_enable_softfax_tile()
        self.home.select_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX))
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.vallue_prop.verify_ows_value_prop_screen(tile=True)
        self.vallue_prop.select_secondary_btn(change_check=True, timeout=10)
        self.chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context("WEBVIEW_chrome")
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.fc.hpid_username, self.fc.hpid_password,
                        change_check={"wait_obj": "sign_in_button", "invisible": True})
        #Todo: wait for designer's reply on timeout after signing into HPID account
        self.home.check_run_time_permission(accept=True, timeout=10)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=30)
        self.fax_history.verify_fax_history_screen()
        self.fc.flow_load_home_screen()
        self.home.select_more_options_app_settings()
        self.app_settings.verify_app_settings_with_hpc_account(self.fc.hpid_username)

    def test_02_load_compose_fax_by_login_via_app_settings(self):
        """
            Description:
                1/ Enable Mobile Fax tile
                2/ Login to HPID in App Settings
                3/ Click on Send Fax tile on Home screen
            Expected Result:
                3/ Compose Fax screen display
        """
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)

    def test_03_load_compose_fax_by_creating_account_via_tile(self):
        """
        Precondition: App is not login to any accounts
        Description:
            1/ Enable Mobile Fax tile
            2/ Click on Mobile Fax tile
            3/ Click on Create Account on Value Prop screen
            4/ Process for creating a new HPID account
            5/ Dismiss App Permission by clicking Allow
            6/ Skip Get Start and Welcome screen of Softfax

        Expected Result:
            6/ Compose Fax screen display
        """
        self.fc.reset_app()
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_enable_softfax_tile()
        self.home.select_tile_by_name(self.driver.return_str_id_value(TILE_NAMES.FAX))
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        # Currently HPID take 10-20s to load to value prop screen.
        self.vallue_prop.verify_ows_value_prop_screen(tile=True)
        self.vallue_prop.select_primary_btn(change_check=False, timeout=10)
        self.chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.CHROME)
        self.hpid.verify_hp_id_sign_up()
        self.hpid.create_account()
        # After clicking create account button, it take some time to load to uCDE Privacy screen
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=30)
        #Todo: Skip UCDE screen take longer time, will update it after CR gdg-1768 get fixed
        self.ucde.skip_ucde_privacy_screen(timeout=10)
        self.home.check_run_time_permission(accept=True, timeout=10)
        #There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        if self.softfax_offer.verify_get_started_screen(raise_e=False):
            self.softfax_offer.skip_get_started_screen()
        if self.softfax_welcome.verify_welcome_screen(raise_e=False):
            self.softfax_welcome.skip_welcome_screen()
        self.compose_fax.verify_compose_fax_screen()

    def test_04_load_compose_fax_by_creating_account_via_app_settings(self):
        """
            Description:
                1/ Enable Send Fax tile and Change stack
                2/ Create a HPID account in App Settings
                3/ Click on Send Fax tile on Home screen
            Expected Result:
                3/ Compose Fax screen display
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)