import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
from time import sleep


pytest.app_info = "SMART"


class Test_Suite_03_Ios_14_Local_Network(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.welcome_web = cls.fc.fd["welcome_web"]
        cls.privacy_preferences = cls.fc.fd["privacy_preferences"]
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def fresh_install(self, index=2):
        self.driver.reset(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].dismiss_software_update_if_visible()
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        self.fc.fd["ios_system"].clear_safari_cache()
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)
        self.fc.fd["welcome_web"].verify_welcome_screen()
        self.fc.fd["welcome_web"].click_accept_all_btn()
        self.fc.fd["ios_system"].handle_allow_tracking_popup(raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        if index == 2:
            self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
            self.fc.fd["ows_value_prop"].select_value_prop_buttons(index=index)
        elif index == 1:
            sleep(5)
            self.fc.login_value_prop_screen(tile=False, stack=self.stack, timeout=60)
            sleep(5)
            self.fc.fd["home"].allow_notifications_popup(timeout=15, raise_e=False)
            self.fc.fd["home"].close_smart_task_awareness_popup()
            self.fc.fd["home"].dismiss_tap_account_coachmark()

    def test_01_dont_allow_network(self):

        '''
            C28270924: local network popup message(don't allow)
            C28270932: restart app
            C28270926: don't enable get back
        '''
        if not self.driver.platform_version == '14':
            pytest.skip("popup only shows in iOS 14")
        self.fresh_install()
        self.fc.fd["ios_system"].dismiss_hp_local_network_alert(allow=False, timeout=10)
        self.fc.fd["ios_system"].verify_local_network_screen()
        self.fc.fd["ios_system"].select_enable_permissions()
        self.fc.fd["ios_system"].verify_hp_smart_title()
        # do not enable and get back
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].verify_local_network_screen()
        # do not enable and restart
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].verify_local_network_screen()

    def test_02_permit_local_network(self):
        '''
            C28270925: tapping enable permission
        '''
        if not self.driver.platform_version == '14':
            pytest.skip("popup only shows in iOS 14")
        self.fresh_install()
        self.dismiss_popup_and_enable_local_network()
        self.fc.fd["ios_system"].switch_smart_app_local_network(on=True)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["home"].verify_home()
        
    def test_03_permit_and_deny_add_printer_local_network(self):
        '''
            C28387081: "No Local Network" on Add Printer flow
        '''
        if not self.driver.platform_version == '14':
            pytest.skip("popup only shows in iOS 14")
        self.fresh_install(index=1)
        self.dismiss_popup_and_enable_local_network()
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["home"].verify_home()
        self.fc.fd["home"].select_settings_icon()
        self.fc.fd["ios_system"].switch_smart_app_local_network(on=False)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.fc.fd["home"].select_home_icon()
        self.fc.fd["home"].select_add_your_first_printer()
        self.fc.fd["home"].verify_bluetooth_popup()
        self.fc.fd["home"].handle_bluetooth_popup(allow=True)
        self.fc.fd["home"].select_navigate_back()
        self.fc.fd["home"].select_printer_plus_button_from_topbar()
        self.fc.fd["ios_system"].verify_add_printer_local_network_screen()

    def dismiss_popup_and_enable_local_network(self):
        self.fc.fd["ios_system"].dismiss_hp_local_network_alert(allow=False, timeout=10)
        self.fc.fd["ios_system"].verify_local_network_screen()
        self.fc.fd["ios_system"].select_enable_permissions()
        self.fc.fd["ios_system"].verify_hp_smart_title()
        self.fc.fd["ios_system"].toggle_local_network_switch(on=True)
