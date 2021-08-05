import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Compose_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.fax_history = cls.fc.fd["softfax_fax_history"]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.add_mobile_fax_tile()
        self.home.select_tile_by_name(HOME_TILES.TILE_MOBILE_FAX)

    def test_01_load_compose_fax_by_creating_new_account(self):
        """
        Load compose fax screen by creating Mobile Fax screen
        """
        self.fc.create_account_from_tile()
        self.fc.verify_fax_welcome_screens_and_nav_compose_fax()

    def test_02_load_fax_history_screen_via_fax_tile_login(self):
        """
        Load to Compose fax screen by sign in through Fax tile - C13920028
        """
        self.fc.login_value_prop_screen(tile=True, stack=self.stack)
        self.driver.wait_for_context(WEBVIEW_URL.SOFTFAX, timeout=30)
        self.fax_history.verify_fax_history_screen(timeout=20)