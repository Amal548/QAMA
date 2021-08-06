import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*


pytest.app_info = "SMART"


class Test_Suite_01_Ios_Smart_Welcome_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.welcome_web = cls.fc.fd["welcome_web"]

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.driver.reset(BUNDLE_ID.SMART)
        self.fc.fd["ios_system"].dismiss_software_update_if_visible()
        if self.stack != "pie":
            self.fc.change_stack(self.stack)
        self.driver.launch_app(BUNDLE_ID.SMART)
        self.driver.wait_for_context(WEBVIEW_URL.SMART_WELCOME, timeout=30)

    def test_01_verify_terms_and_conditions_screen(self):
        """
        C27796362 Precondition: fresh install
        """
        self.fc.fd["welcome_web"].verify_welcome_screen()
        self.check_if_old_screen_welcome_screen_visible()
        self.fc.fd["welcome_web"].verify_click_btn()
        # Added raise_e False due to issue HPC3-5646
        self.fc.fd["welcome_web"].verify_hp_privacy_statement_link(raise_e=False)
        self.fc.fd["welcome_web"].verify_terms_of_use_link()
        self.fc.fd["welcome_web"].verify_eula_link()

    @pytest.mark.parametrize('allow', [True, False])
    def test_02_setup_new_printer(self, allow):
        """
        C27803200, C28496244
        """
        self.fc.fd["welcome_web"].verify_welcome_screen()
        self.check_if_old_screen_welcome_screen_visible()
        self.fc.fd["welcome_web"].click_accept_all_btn()
        self.fc.fd["ios_system"].handle_allow_tracking_popup(option=True, raise_e=False)
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(timeout=60)
        self.fc.fd["ows_value_prop"].select_value_prop_buttons(0)
        if self.fc.fd["printers"].verify_bluetooth_popup(raise_e=False):
            self.fc.fd["printers"].handle_bluetooth_popup()
        if self.driver.platform_version == '14':
            self.fc.fd["ios_system"].dismiss_hp_local_network_alert(allow=allow)
            if allow is True:
                self.fc.fd["printers"].verify_printers_list()
            else:
                self.fc.fd["printers"].verify_enable_local_network_permission_blocker_screen()
        
    def check_if_old_screen_welcome_screen_visible(self):
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        if self.welcome_web.verify_manage_options(raise_e=False) is False:
            pytest.skip("old welcome screen")