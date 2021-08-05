import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*

pytest.app_info = "SMART"


class Test_Suite_01_Ios_Mobile_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()

    def test_01_app_settings_mobile_fax(self):
        """
        C25430555 
        """
        self.fc.go_home(button_index=2)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_mobile_fax()
        # AIOI-10891 user onboarding should display here instead of softfax get started screen
        self.driver.wait_for_context(WEBVIEW_URL.VALUE_PROP, timeout=60)
        self.fc.fd["ows_value_prop"].verify_ows_value_prop_screen(tile=True, timeout=60)
