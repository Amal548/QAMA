import pytest
import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer

from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

@pytest.mark.usefixtures("require_driver")
class Test_suite_01_ios_smart_digital_copy_functionality(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, require_driver):

        cls = cls.__class__
        #cls.driver = require_driver
        cls.fc = FlowContainer(cls.driver)

    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], printer_serial="TH84U13238")
        cls.p.set_mech_mode(mech=False)
        cls.printer_info = cls.p.get_printer_information()

    # Printer variables
        cls.printer_bonjour_name = cls.printer_info['bonjour name']
        cls.printer_ip = cls.printer_info['ip address']

    def test_01_digital_copy_default_job_black(self):

        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_start_black()

    def test_02_digital_copy_default_job_color(self):
        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_start_color()
