import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.resources.const.web.const import HPCONNECT as URL

pytest.app_info = "SMART"


class Test_Suite_01_MOOBE_AWC(object):

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

    def test_01_awc_via_add_printer_from_home(self):
        self.fc.setup_moobe_awc_wifi(self.p, stack=self.stack)
        self.fc.moobe_connect_printer_to_wifi(ssid_name=self.ssid, wifi_password=self.password)

    def test_02_awc_via_app_settings(self):

        self.fc.setup_moobe_awc_wifi(self.p, app_settings=True, stack=self.stack)
        self.fc.moobe_connect_printer_to_wifi(ssid_name=self.ssid, wifi_password=self.password)

    def test_03_verify_location_popup(self):
        """
        Fresh install, AWC setup mode, iOS 13+
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.fd["home"].select_get_started_by_adding_a_printer()
        self.fc.fd["printers"].select_add_printer()
        self.fc.fd["printers"].select_set_up_a_new_printer()
        self.fc.fd["printers"].verify_allow_once()
        self.fc.fd["printers"].verify_allow_while_using_app()
        self.fc.fd["printers"].verify_dont_allow()
    
    def test_04_dont_allow_location(self):
        """
        C17028899 Fresh install, AWC setup mode, iOS 13+
        Press the + sign on home, set up a new printer, tap don't allow on location popup
        """
        self.fc.go_home(reset=True, stack=self.stack)
        self.fc.fd["home"].select_get_started_by_adding_a_printer()
        self.fc.fd["printers"].select_add_printer()
        self.fc.fd["printers"].select_set_up_a_new_printer()
        self.fc.fd["printers"].handle_location_popup(selection="allow")
        # TODO: verify location message
