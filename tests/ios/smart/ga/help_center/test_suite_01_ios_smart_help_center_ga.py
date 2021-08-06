import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
pytest.app_info = "SMART"


class Test_suite_01_ios_smart_help_center_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)

        cls.fc.go_home(verify_ga=True)

    def test_01_help_center_max_ga(self):


        self.fc.go_app_settings_screen_from_home()
        self.fc.fd["app_settings"].select_help_center()
        self.fc.fd["help_center"].verify_help_center_screen()
        self.fc.fd["help_center"].get_started()
        self.fc.fd["help_center"].how_to_use_the_app()
        self.fc.fd["help_center"].legal()