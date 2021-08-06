import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import*
from selenium.webdriver.support.ui import WebDriverWait

pytest.app_info = "SMART"

class Test_Suite_02_About_Screen(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

    def test_01_verify_about_screen_ui(self):
        """
        C27654992
        Verify all the UI elements on the About screen
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].verify_about_ui_elements()

    def test_02_verify_back_button_functionality(self):
        """
        C27654992
        Verify clicking back button on About screen goes back to App Settings screen
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_navigate_back()
        self.fc.fd["app_settings"].verify_app_settings_screen()

    def test_03_verify_rate_us_button_functionality(self):
        """
        C27654993
        Verify clicking rate us button redirects to app store
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_rate_us_button()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.AppStore") == 4)

    def test_04_verify_privacy_link_functionality(self):
        """
        C27654994
        Verify clicking HP privacy link redirects to browser link
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_hp_privacy_link()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)

    def test_05_verify_eula_link_functionality(self):
        """
        C27654994
        Verify clicking EULA agreement link redirects to browser link
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_eula_link()
        assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)

    def test_06_verify_legal_info_link_functionality(self):
        """
        C27654994
        Verify clicking Legal Information link opens up legal info screen
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_legal_info_link()
        self.fc.fd["app_settings"].verify_legal_information_ui_elements()

    def test_07_verify_legal_info_back_button(self):
        """
        Verify clicking back button on legal information screen goes back to about screen
        """
        self.go_to_about_screen()
        self.fc.fd["app_settings"].select_legal_info_link()
        self.fc.fd["app_settings"].verify_legal_information_ui_elements()
        self.fc.fd["app_settings"].select_navigate_back()
        self.fc.fd["app_settings"].verify_about_ui_elements()

    def go_to_about_screen(self):
        self.fc.go_home(reset=True, stack=self.stack, button_index=2)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_about_cell()
