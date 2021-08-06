import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_01_HPID_IOS(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, record_testsuite_property):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]
        cls.app_settings = cls.fc.fd["app_settings"]
        cls.stack = request.config.getoption("--stack")
        record_testsuite_property("suite_test_category", "HPID")

    def test_01_hpid_sign_in(self):
        self.fc.go_home(stack=self.stack)

    def test_02_hpid_sign_out(self):
        self.home.select_app_settings()
        self.app_settings.sign_out_from_hpc()

    def test_03_hpid_sign_up(self):
        self.fc.go_home(stack=self.stack, reset=True, create_account=True)