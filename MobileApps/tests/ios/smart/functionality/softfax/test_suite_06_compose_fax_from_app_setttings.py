import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_06_COMPOSE_FAX_FROM_APP_SETTINGS(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_load_compose_fax_new_user_signin_app_settings(self):
        self.fc.go_home(stack=self.stack, button_index=2)
        self.email, self.password = self.fc.create_account_from_homepage()
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_mobile_fax()
        self.fc.login_value_prop_screen(tile=True, username=self.email, password=self.password)
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_02_load_compose_fax_create_user_app_settings(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_mobile_fax()
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_03_load_compose_fax_user_signin_app_settings(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_mobile_fax()
        self.fc.login_value_prop_screen(tile=True, stack=self.stack)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=20)
        self.fc.fd["fax_settings"].verify_fax_settings_screen()