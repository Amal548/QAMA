import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_01_Home_Bottom_Navigation_Bar(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")

    @pytest.mark.parametrize('sign_in', [(1,True), (2,False)])
    def test_01_verify_toolbar(self, sign_in):
        """
        @param sign_in: tuple (int, bool)
        C27654945 Sign in on value prop, verify: Home, Scan, View & Print, Settings, Account
        C27725932 Explore HP Smart on value prop, verify: Home, Create Account, Settings icons
        """
        self.fc.go_home(reset=True, button_index=sign_in[0], stack=self.stack)
        self.home.verify_bottom_navigation_bar()
        self.home.verify_bottom_navigation_bar_icons(signed_in=sign_in[1])

    def test_02_verify_toolbar_after_sign_out(self):
        """
        C27725933 Sign in on value prop, go home, and sign out in app settings
        verify: Home, Create Account, Settings icons
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.home.verify_bottom_navigation_bar()
        self.home.verify_bottom_navigation_bar_icons(signed_in=True)
        self.home.select_app_settings()
        self.fc.fd["app_settings"].select_sign_out_hpc()
        self.fc.fd["app_settings"].select_sign_out_on_popup()
        self.fc.fd["app_settings"].select_continue_to_allow_hp_com_signin()
        self.home.select_home_icon()
        self.home.close_smart_task_awareness_popup()
        self.home.verify_bottom_navigation_bar_icons(signed_in=False)
