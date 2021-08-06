import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_factory import moobe_ows_flow_container_factory
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.libs.ma_misc.ma_misc import truncate_printer_model_name
from MobileApps.resources.const.web.const import HPCONNECT as URL

pytest.app_info = "SMART"


class Test_Suite_05_Secure_BLE(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.ssid, cls.password = get_wifi_info(request)
        cls.ows_fc = moobe_ows_flow_container_factory(cls.driver, cls.p, cls.fc.fd["moobe_ows"])

    @pytest.fixture(scope="function", autouse=True)
    def secure_ble(self):
        printer_name = truncate_printer_model_name(self.p.get_printer_information()['model name'])
        self.fc.moobe_secure_ble(printer_name, self.ssid, self.password)
        self.fc.fd["moobe_awc"].verify_information_security_popup()

    def test_01_push_info_btn_without_fp(self):
        """
        C17047530 printer without front panel (Taccola)
        """
        self.p.press_info_btn()
        self.fc.fd["moobe_awc"].verify_printer_connected_screen()

    def test_02_verify_timeout_ui(self):
        """
        C17464746
        """
        self.fc.fd["moobe_awc"].verify_try_again_ui()

    def test_03_verify_try_again_functionality(self):
        """
        C17466138
        """
        for _ in range(5):
            self.fc.fd["moobe_awc"].verify_try_again_ui()
            self.fc.fd["moobe_awc"].select_try_again()
            self.fc.fd["moobe_awc"].verify_information_security_popup()

    def test_04_cancel_setup_ui(self):
        """
        C17464782 Verify the 'Are you sure you want to cancel?' popup
        """
        self.p.press_cancel_btn()
        self.fc.fd["moobe_awc"].verify_cancel_setup_popup()

    def test_05_cancel_and_exit_setup(self):
        """
        C17466132 Printer's Cancel Button-> Click exit setup-> click Continue -> verify home page
        """
        self.p.press_cancel_btn()
        self.fc.fd["moobe_awc"].select_exit_setup_btn()
        self.fc.fd["moobe_awc"].verify_exit_setup_ui()
        self.fc.fd["moobe_awc"].select_continue()
        self.fc.fd["home"].verify_home()
        assert self.p.is_oobe_mode() is True

    def test_06_cancel_and_try_again(self):
        """
        C17466134 Verify cancel button-> Click Try again-> verify Push i Button popup
        """
        self.p.press_cancel_btn()
        self.fc.fd["moobe_awc"].select_try_again()
        self.fc.fd["moobe_awc"].verify_information_security_popup()


