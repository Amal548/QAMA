import pytest
import time
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
pytest.app_info = "SMART"

class Test_Suite_01_Notification_And_Privacy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.fd["home"]
        cls.preview = cls.fc.fd["preview"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_ui_notification_privacy_creen(self):
        """
        C27654979 - Verify UI for Notification & Privacy Screen
        """
        # go to home screen without login
        self.fc.go_home(button_index=2, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.verify_promotional_message_switch()
        assert self.app_settings.get_switch_status(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH) == 0
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 0
    
    def test_02_verify_supply_status_n_promotional_message_switcher(self):
        """
        C27654978 - Verify supply status switcher
        C27654983 - Verify Promotional Messaging switcher
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.verify_promotional_message_switch()
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 1
        self.app_settings.toggle_switch(self.app_settings.SUPPLY_STATUS_SWITCH, uncheck=True)
        assert self.app_settings.get_switch_status(self.app_settings.SUPPLY_STATUS_SWITCH) == 0
        # C27654983
        assert self.app_settings.get_switch_status(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH) == 0
        self.app_settings.toggle_switch(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH, uncheck=False)
        assert self.app_settings.get_switch_status(self.app_settings.PROMOTIONAL_MESSAGE_SWITCH) == 1

    def test_03_verify_data_collection_notice_link(self):
        """
         C27992764 - Redirection by tapping on "Data Collection Notice" hyperlink
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_data_collection_notice_link()
        self.app_settings.select_i_accept_btn(timeout=10)
        self.app_settings.verify_data_collection_notice_page()
    
    def test_04_verify_hp_privacy_hyperlink(self):
        """
        C27992765 - Redirection by tapping on "HP Privacy Statement" hyperlink
        """
        self.fc.go_to_home_screen()
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_hp_privacy_statement()
        self.fc.fd["privacy_statement"].verify_our_approach_to_privacy()
    
    def test_05_verify_links_on_notifications_n_privacy_screen(self):
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        # EULA link
        self.app_settings.select_eula_link() 
        self.app_settings.select_i_accept_btn(timeout=10)
        self.app_settings.verify_eula_page()
        self.app_settings.select_navigate_back()
        # Terms of Use link
        self.app_settings.select_terms_of_use_link()
        self.app_settings.verify_terms_of_use_page()
        self.app_settings.select_navigate_back()
        # Google Analytics policy link
        self.app_settings.select_google_analytics_privacy_policy_link()
        self.app_settings.verify_google_analytics_privacy_policy_page()
        self.app_settings.select_navigate_back()
        # Adobe privacy policy link
        self.app_settings.select_adobe_privacy_link()
        self.app_settings.verify_adobe_privacy_policy_page()
        self.app_settings.select_navigate_back()
        # Optimizely privacy link
        self.app_settings.select_optimizely_link()
        self.app_settings.verify_optimizely_page()
    
    def test_06_verify_manage_my_privacy_settings(self):
        """
        C28873941 - Verify "Manage my Privacy Settings" page if not all options has been enabled
        C28873934 - Verify "Manage my Privacy Settings" behavior
        """
        stack = self.stack.lower()
        self.driver.reset(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].clear_safari_cache()
        if stack != "pie":  # pie stack is default server on iOS HP Smart
            self.fc.change_stack(stack)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)
        self.fc.fd["welcome_web"].verify_welcome_screen()
        if self.fc.fd["welcome_web"].verify_manage_options(raise_e=False) is False:
            pytest.skip('Skipped because of old welcome screen')
        self.fc.fd["welcome_web"].click_manage_options()
        self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=False)
        self.privacy_preferences.click_continue()
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        self.fc.login_value_prop_screen(tile=False)
        time.sleep(1)
        self.fc.clear_popups_on_first_login()
        self.fc.fd["home"].verify_home()
        if self.driver.platform_version == '14':
            self.fc.fd["ios_system"].dismiss_hp_local_network_alert(timeout=10)
        time.sleep(2)
        self.fc.remove_default_paired_printer()
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_manage_privacy_settings_option()
        time.sleep(10)
        self.privacy_preferences.verify_privacy_preference_screen()
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=False) is True
    
    def test_07_verify_change_n_back_on_privacy_settings(self):
        """
        C28873936 - Verify change and Save on "Manage my Privacy Settings" page
        C28873937 - Verify change and Back on "Manage my Privacy Settings" page
        C28873938 - Verify "Save" button on "Manage my Privacy Settings" page
        C28873940 - Verify "Back" button on "Manage my Privacy Settings" page
        """
        self.fc.go_home(reset=True, button_index=1, stack=self.stack)
        self.navigate_to_notification_n_privacy_settings()
        self.app_settings.select_manage_privacy_settings_option()
        time.sleep(10)
        self.privacy_preferences.verify_privacy_preference_screen()
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=True) is True
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.ADVERTISING, state=True) is True
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.PERSONALIZED_SUGGESTIONS, state=True) is True
        self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=False)
        self.privacy_preferences.click_back_btn()
        self.app_settings.select_manage_privacy_settings_option()
        time.sleep(10)
        self.privacy_preferences.verify_privacy_preference_screen()
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=True) is True
        self.privacy_preferences.toggle_switch(self.privacy_preferences.APP_ANALYTICS, uncheck=True)
        self.privacy_preferences.click_continue()
        self.app_settings.select_manage_privacy_settings_option()
        time.sleep(10)
        self.privacy_preferences.verify_privacy_preference_screen()
        assert self.privacy_preferences.get_switch_status(self.privacy_preferences.APP_ANALYTICS, state=False) is True
    
    def navigate_to_notification_n_privacy_settings(self):
        self.home.select_app_settings()
        self.app_settings.select_notification_n_privacy_option()
