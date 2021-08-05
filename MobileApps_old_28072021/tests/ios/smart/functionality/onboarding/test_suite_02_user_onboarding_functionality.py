from inspect import stack
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.resources.const.ios.const import HOME_TILES
from SAF.misc import saf_misc
from time import sleep

pytest.app_info = "SMART"


class Test_Suite_02_User_Onboarding_Functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        
    def test_01_notification_onboarding(self):
        self.fc.go_home(stack=self.stack, button_index=2)
        self.fc.fd["home"].verify_notification_bell()
        self.fc.fd["home"].select_notification_bell()
        self.fc.fd["home"].verify_notification_screen()
        for tab in self.fc.fd["home"].ACTIVITY_TABS:
            sleep(5)
            self.fc.fd["home"].verify_an_element_and_click(tab)
            self.fc.fd["ows_value_prop"].verify_native_value_prop_screen()
            self.fc.fd["ows_value_prop"].select_native_value_prop_buttons(index=2)
            
    def test_02_create_account_app_settings(self):
        '''
            C28370571: create account button under app settings
            skip value prop screen
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.go_app_settings_screen_from_home()
        assert self.fc.fd["app_settings"].verify_create_account_btn() is True
        self.fc.fd["app_settings"].select_create_account_btn()
        sleep(5)
        self.fc.fd["hpid"].handle_privacy_popup()
        assert self.fc.fd["hpid"].verify_create_an_account_page() is True

    def test_03_signin_btn_validation(self):
        '''
            C28370572: signin btn is available under bottom nav bar if not signed in
            should skip value prop screen
            C28800002: signin screen
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        assert self.fc.fd["home"].verify_sign_in_icon() is not False
        self.fc.fd["home"].select_sign_in_icon()
        self.fc.fd["hpid"].handle_privacy_popup()
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=60)

    def test_04_onboarding_personalize_promotion_link(self):
        '''
            C28873934: Manage my Privacy Settings
            C27891989: user onboarding personalize promotion link
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.go_app_settings_screen_from_home()
        self.fc.fd["app_settings"].select_notification_n_privacy_option()
        self.fc.fd["app_settings"].select_manage_privacy_settings_option()
        self.fc.fd["privacy_preferences"].verify_privacy_preference_screen()
        
    def test_05_cancel_onboarding_app_settings(self):
        '''
            C27735800: cancel onboarding to UCDE
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.go_app_settings_screen_from_home()
        assert self.fc.fd["app_settings"].verify_sign_in_option() is True
        self.fc.fd["app_settings"].select_sign_in_option()
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.fc.go_app_settings_screen_from_home()
        assert self.fc.fd["app_settings"].verify_sign_in_option() is True

    def test_06_ucde_learn_more(self):
        '''
            C28073476: verify ucde privacy
            C28510827: ucde learn more
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].verify_bottom_navigation_bar_icons(signed_in=False) 
        self.fc.fd["home"].select_create_account_icon()
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=10)
        sleep(5)
        email, password = self.fc.fd["hpid"].create_account()
        sleep(5)
        self.fc.fd["ucde_privacy"].verify_ucde_privacy_screen()
        self.fc.fd["ucde_privacy"].select_learn_more_link_native()
        sleep(5)
        self.fc.fd["ucde_privacy"].select_i_accept_btn_native()
        self.fc.fd["ucde_privacy"].verify_account_data_usage_title()

    def test_07_ucde_exit(self):
        '''
            C27764946: not accepting ucde with force exit
        '''
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].verify_bottom_navigation_bar_icons(signed_in=False) 
        self.fc.fd["home"].select_create_account_icon()
        self.driver.wait_for_context(WEBVIEW_URL.HPID, timeout=10)
        sleep(5)
        email, password = self.fc.fd["hpid"].create_account()
        sleep(5)
        self.fc.fd["ucde_privacy"].verify_ucde_privacy_screen()
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.fc.go_app_settings_screen_from_home()
        # TODO: https://hp-jira.external.hp.com/browse/AIOI-13600 
        # defect: the user will be automatically signed in after kill the app
        # self.fc.fd["app_settings"].select_sign_in_option()
        # self.fc.fd["ucde_privacy"].skip_ucde_privacy_screen()


