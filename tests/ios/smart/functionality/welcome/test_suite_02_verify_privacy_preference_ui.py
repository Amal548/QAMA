import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*


pytest.app_info = "SMART"


class Test_Suite_02_Verify_Privacy_Preference_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.driver.reset(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].dismiss_software_update_if_visible()
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        self.fc.fd["ios_system"].clear_safari_cache()
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)
    
    @pytest.mark.parametrize('accept', [True, False])
    def test_01_verify_behavior_tapping_accept_all_btn(self,accept):
        """
        C28862781 - [8.5.1] Verify new Welcome screen
        C28862784 - [8.5.1] Verify behavior by tapping "Accept All"
        C28862788 - [8.5.1] Verify behavior by tapping "Allow Tracking"
        C28862789 - [8.5.1] Verify behavior by tapping "Ask App Not to Track"
        """
        self.welcome_web.verify_welcome_screen()
        self.welcome_web.click_accept_all_btn()
        if self.driver.platform_version == '14':
            self.fc.fd["ios_system"].handle_allow_tracking_popup(option=accept, raise_e=True)
            self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        if self.driver.platform_version == '13':
            self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
            if self.fc.fd["welcome"].verify_an_element_and_click("share_usage_data_title", click=False, raise_e=False) is \
            not False:
                self.fc.fd["welcome"].swipe_down_scrollview()
                self.fc.fd["welcome"].select_yes()
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
    
    def test_02_verify_behavior_tapping_manage_options_and_selecting_different_privacy_preferences(self):
        """
        C28862785 - [8.5.1] Verify behavior by tapping "Manage Options"
        C28862786 - [8.5.1] Verify behavior by tapping on "Continue" button
        C28862787 - [8.5.1] Verify behavior by tapping on "Back" button
        C28862790 - [8.5.1] Verify behavior after enabling "App Analytics" option
        C28862791 - [8.5.1] Verify behavior after enabling "Advertising" option
        C28862792 - [8.5.1] Verify behavior after enabling "Personalized Suggestions" option
        C28862793 - [8.5.1] Verify behavior after enabling all options
        """
        self.welcome_web.verify_welcome_screen()
        if self.welcome_web.verify_manage_options(raise_e=False) is False:
            pytest.skip('Skipped because of old welcome screen')
        self.welcome_web.click_manage_options()
        self.privacy_preferences.click_back_btn()
        self.welcome_web.click_manage_options()
        self.privacy_preferences.toggle_switch(self.welcome_web.APP_ANALYTICS, uncheck=False)
        self.privacy_preferences.toggle_switch(self.welcome_web.ADVERTISING, uncheck=False)
        self.privacy_preferences.toggle_switch(self.welcome_web.PERSONALIZED_SUGGESTIONS, uncheck=False)
        self.privacy_preferences.click_continue()
        if self.driver.platform_version == '14':
            self.fc.fd["ios_system"].handle_allow_tracking_popup(option=True, raise_e=True)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)