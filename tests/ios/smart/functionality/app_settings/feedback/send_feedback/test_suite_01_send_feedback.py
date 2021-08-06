import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
import re

pytest.app_info = "SMART"

class Test_Suite_01_Ios_Smart_Send_Feedback(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()

    @pytest.fixture(scope="function", autouse="true")
    def fresh_install(self):
        self.driver.wdvr.reset()

    def test_01_verify_medallia_sendfeedback(self):
        """
        C17128623
        """
        self.fc.go_home()
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_send_feedback_cell()
        self.fc.fd["app_settings"].verify_medallia_page()
        self.fc.fd["app_settings"].select_navigate_back()
        self.fc.fd["app_settings"].verify_app_settings_screen()
        self.fc.fd["app_settings"].select_send_feedback_cell()
        self.fc.fd["app_settings"].verify_medallia_page()
        self.fc.fd["app_settings"].select_stars()
        stars = self.fc.fd["app_settings"].verify_star_slider().get_attribute("value")
        if stars:
            assert int(float(stars)) == 3
        else:
            pattern = re.compile(r'type=\"XCUIElementTypeSlider\" value=\"(\d*\.\d+|\d)\"')
            assert int(re.search(pattern, self.driver.wdvr.page_source).group(1)) == 3
        self.fc.fd["app_settings"].select_submit_btn()
        self.fc.fd["app_settings"].verify_feedback_submission_popup()
        self.fc.fd["app_settings"].select_ok()
        self.fc.fd["app_settings"].verify_app_settings_screen()
