import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.web.const import HPCONNECT as URL

pytest.app_info = "SMART"


class Test_Suite_04_MOOBE_WAC(object):

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
 
    @pytest.fixture(scope="function", autouse="true")
    def go_home(self):
        self.fc.go_home(verify_home=False)

    def test_01_wac_from_first_launch(self):
        """
        C16977263 WAC via tap here to get started
        """
        self.fc.moobe_wac(self.bonjour_name, self.ssid)

    def test_02_wac_from_printer_screen(self):
        """
        C17013729 WAC via add printer
        """
        self.fc.moobe_wac(self.bonjour_name, self.ssid, dismiss_popup=True)

    def test_03_cancel_automatic_setup(self):
        """
        C17013730 Select cancel button on automatic network setup screen, verify redirect to printer list screen
        """
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer()
        self.fc.fd["printers"].select_moobe_printer_from_list(self.bonjour_name)
        self.fc.fd["printers"].verify_automatically_put_device_on_network()
        self.fc.fd["printers"].select_cancel()
        self.fc.fd['printers'].verify_printers_nav()

    def test_04_cancel_accessory_setup(self):
        """
        C17013731 Select cancel button on accessory setup screen, verify redirect to printer list screen
        """
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer()
        self.fc.fd["printers"].select_moobe_printer_from_list(self.bonjour_name)
        self.fc.fd["printers"].verify_automatically_put_device_on_network()
        self.fc.fd["printers"].select_yes()
        self.fc.fd["moobe_wac"].verify_accessory_setup(ssid=self.ssid, accessory_name=self.bonjour_name)
        self.fc.fd["printers"].select_cancel()
        self.fc.fd['printers'].verify_printers_nav()
    