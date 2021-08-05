import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_factory import moobe_ows_flow_container_factory
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc.conftest_misc import get_wifi_info
from MobileApps.libs.ma_misc.ma_misc import truncate_printer_model_name
from MobileApps.resources.const.web.const import HPCONNECT as URL

pytest.app_info = "SMART"


class Test_Suite_03_MOOBE_BLE(object):

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
        cls.ows_fc = moobe_ows_flow_container_factory(cls.driver, cls.p, cls.fc.fd["moobe_ows"])

    def test_01_ble_via_add_printer(self):
        """
        C17013719 Preconditions: Printer supports BLE and is in oobe mode, only one BLE printer in moobe nearby
        Complete AWC via BLE from home screen using + printer button
        """
        printer_name = truncate_printer_model_name(self.p.get_printer_information()['model name'])
        self.fc.setup_moobe_awc_ble(printer_name=printer_name)
        self.fc.moobe_connect_printer_to_wifi(ssid_name=self.ssid, wifi_password=self.password)
    
    def test_02_ble_printer_not_discovered(self):
        """
        C17023816 Preconditions: BLE Printer in Setup mode, bluetooth on
        Launch the app, go past welcome screen and navigate home. Verify that there's no BLE printers in setup mode
        """
        self.fc.go_home()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].verify_add_your_first_printer()
    
    @pytest.mark.parametrize('allow_bluetooth', [True, False])
    def test_03_bluetooth_popup(self, allow_bluetooth):
        """
        C17019669 Preconditions: BLE printer in Setup mode, iOS 13
        """
        if self.driver.driver_info["platformVersion"].split(".")[0]=='12':
            pytest.skip('iOS 13+ specific test')
        self.fc.go_home()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer(handle_popup=False)
        self.fc.fd["printers"].verify_bluetooth_popup_ui()
        self.fc.fd["printers"].handle_bluetooth_popup(allow=allow_bluetooth)
        printer_name = truncate_printer_model_name(self.p.get_printer_information()['model name'])
        self.fc.fd["printers"].find_printer_using_search_bar(printer_name)
        if allow_bluetooth:
            self.fc.fd["printers"].verify_printer_in_list(printer_name, timeout=30)
        else:
             assert self.fc.fd["printers"].verify_printer_in_list(printer_name, timeout=30, raise_e=False) is False

    def test_04_bluetooth_popup_appears_only_once(self):
        """
        C17023843 Preconditions: Fresh install, BLE printer, iOS 13
        Go home, tap on + icon, verify bluetooth popup, go home and tap + icon again 
        verify bluetooth popup does not appear again
        """
        if self.driver.driver_info["platformVersion"].split(".")[0]=='12':
            pytest.skip('iOS 13+ specific test')
        self.fc.go_home()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer(handle_popup=True)
        self.fc.go_to_home_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer(handle_popup=False)
        assert not any(self.fc.fd["printers"].verify_bluetooth_popup_ui(raise_e=False)) 
    
    def test_05_location_popup_dont_allow(self):
        """
        C17463991 Fresh Install, BLE printer, iOS 13
        Go home, tap on + icon, accept Bluetooth popup, tap BLE printer in setup mode
        verify location popup and press don't allow, verify user is redirected to list of available networks
        repeat previous steps to ensure location popup doesn't appear again
        """
        if self.driver.driver_info["platformVersion"].split(".")[0]=='12':
            pytest.skip('iOS 13+ specific test')
        self.fc.go_home()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer(handle_popup=True)
        printer_name = truncate_printer_model_name(self.p.get_printer_information()['model name'])
        self.fc.fd["printers"].select_moobe_printer_from_list(printer_name)
        self.fc.fd["moobe_awc"].handle_location_popup(selection="dont_allow")
        self.fc.fd["moobe_awc"].verify_connect_printer_to_network_screen()
        self.fc.go_to_home_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.dismiss_tap_here_to_start()
        self.fc.fd["home"].select_get_started_by_adding_a_printer(handle_popup=False)
        self.fc.fd["printers"].select_moobe_printer_from_list(printer_name)
        assert self.fc.fd["moobe_awc"].verify_allow_while_using_app(raise_e=False) is False
        assert self.fc.fd["moobe_awc"].verify_allow_once(raise_e=False) is False
        assert self.fc.fd["moobe_awc"].verify_dont_allow(raise_e=False) is False
        self.fc.fd["moobe_awc"].verify_connect_printer_to_network_screen()