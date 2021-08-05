import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.web.const import HPCONNECT as URL
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.ios.const import TEST_DATA
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.ows_printer import OWSSplPrinter
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory

pytest.app_info = "SMART"


class Test_Suite_06_WAC_E2E(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.stack = request.config.getoption("--stack")
        cls.stack_link = URL.STAGE1_URL if cls.stack == "stage" else URL.PIE_URL
        cls.ssid, cls.password = get_wifi_info(request)
        cls.bonjour_name = cls.p.get_printer_information()['bonjour name']
        cls.hpid_account = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]
        cls.ows_printer = OWSSplPrinter(cls.p)
        cls.ows_fc = ows_fc_factory(cls.driver, cls.ows_printer)

    @pytest.fixture(scope="function", autouse="true")
    def go_home(self):
        self.fc.go_home(verify_home=False)

    def test_01_wac_ows(self):
        """
        pre-sign into HPID with app settings and navigate OWS 
        """
        self.fc.fd["ios_system"].clear_safari_cache()
        self.fc.change_stack(self.stack)
        self.fc.fd["home"].select_app_settings()
        self.fc.fd["app_settings"].select_sign_in_option()
        self.fc.fd["app_settings"].select_continue()
        self.fc.fd["hpid"].verify_hp_id_sign_in()
        self.fc.fd["hpid"].login(self.hpid_account["username"], self.hpid_account["password"]) 
        self.fc.go_to_home_screen() 
        self.fc.moobe_wac(self.bonjour_name, self.ssid, dismiss_popup=True)
        self.fc.fd["moobe_wac"].select_done()
        self.ows_fc.navigate_ows(self.ows_printer)
        # TODO: instant ink