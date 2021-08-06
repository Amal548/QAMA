import pytest
import time
import json
import datetime
import SPL.driver.driver_factory as p_driver_factory
from SPL.driver.reg_printer import PrinterNotReady
from SPL.driver.driver_factory import printer_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer


from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

# @pytest.mark.app_info("SMART")

@pytest.mark.usefixtures("require_driver")
class Test_Class(object):

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


    def test_01_digital_copy_data_flow1(self):
        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()

        # its not necessary but still we are keeping this file locally to make sure if they ask results we can attach
        time.sleep(5)
        ga_result = 'ga_data_{}.json'.format(str(datetime.datetime.now()))
        with open(ga_result, 'w') as outfile:
            json.dump(self.driver.ga_container.ga_data, outfile)

    def test_02_digital_copy_data_flow2(self):

        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_object_size(object_size=OBJECT_SIZE.SIZE_US_LEGAL)
        self.fc.fd["copy"].select_flash_button()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()

        time.sleep(5)
        ga_result = 'ga_data_{}.json'.format(str(datetime.datetime.now()))
        with open(ga_result, 'w') as outfile:
            json.dump(self.driver.ga_container.ga_data, outfile)


    def test_03_digital_copy_data_flow3(self):

        self.fc.go_home(verify_ga=True)

        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_object_size(object_size=OBJECT_SIZE.SIZE_DRIVER_LICENSE)
        self.fc.fd["copy"].select_flash_button()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()

        self.fc.fd["copy"].select_add_more_pages()
        self.fc.fd["copy"].verify_copy_screen()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_number_of_copies(change_copies=1)
        self.fc.fd["copy"].select_resize_in_digital_copy(resize=RESIZE.RESIZE_FILL_PAGE)
        self.fc.fd["copy"].select_start_color()

        time.sleep(5)
        ga_result = 'ga_data_{}.json'.format(str(datetime.datetime.now()))
        with open(ga_result, 'w') as outfile:
            json.dump(self.driver.ga_container.ga_data, outfile)
