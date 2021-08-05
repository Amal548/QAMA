import pytest
import SPL.driver.driver_factory as p_driver_factory

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


@pytest.mark.usefixtures("require_driver")
class Test_suite_01_ios_smart_home_ga(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, require_driver):

        cls = cls.__class__
        # cls.driver = require_driver
        cls.fc = FlowContainer(cls.driver)

    # Initializing Printer1
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = p_driver_factory.get_printer(cls.sys_config["printer_power_config"])
        cls.p.set_mech_mode(mech=False)
        cls.printer_info = cls.p.get_printer_information()

    # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"])
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()

        # cls.ssid = pytest.config.getoption("--wifi-ssid") if pytest.config.getoption("--wifi-ssid") else \
        # cls.system_cfg["default_wifi"]["ssid"]
        # cls.passwd = pytest.config.getoption("--wifi-pass") if pytest.config.getoption("--wifi-pass") else \
        # cls.system_cfg["default_wifi"]["passwd"]
        # cls.p.connect_to_wifi(cls.ssid, cls.passwd)

    # Printer1 variables
        cls.printer_bonjour_name = cls.printer_info['bonjour name']
        cls.printer_ip = cls.printer_info['ip address']

    # Printer2 variables
        cls.printer_bonjour_name2 = cls.printer_info2['bonjour name']
        cls.printer_ip2 = cls.printer_info2['ip address']

    def test_01_home_max_ga(self):
        """

        :return:
        """

        self.fc.go_home(verify_ga=False)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.select_personalize_tile_enable_all_tiles_ga_purpose()
        self.fc.select_printer_from_topbar(printer_ip=self.printer_ip2)
        self.fc.fd["home"].printer_menu_options_ga_purpose()

    def test_02_home_coverage_flow1_ga(self):
        self.fc.go_home(verify_ga=True)
        self.fc.fd["home"].verification_of_clicks_on_menu_icons_ga_purpose()