import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*

pytest.app_info = "SMART"


class Test_Suite_01_Ios_Smart_Help_Center(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_help_center(self):
        """
        C27655428, C27654976
        """
        self.fc.go_home(stack=self.stack)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_help_center()
        self.fc.fd["help_center"].verify_help_center_screen()
