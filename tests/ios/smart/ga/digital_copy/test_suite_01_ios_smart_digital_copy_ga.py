import pytest

import SPL.driver.driver_factory as p_driver_factory
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer


from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

@pytest.mark.usefixtures("require_driver")
class Test_suite_01_ios_smart_digital_copy_ga(object):

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

    def test_01_digital_copy_max_ga(self):

        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_object_size(object_size=OBJECT_SIZE.SIZE_US_LEGAL)
        self.fc.fd["copy"].select_flash_button()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_add_more_pages()
        self.fc.fd["copy"].verify_copy_screen()
        self.fc.fd["copy"].select_capture_button()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_number_of_copies(change_copies=4)
        self.fc.fd["copy"].select_resize_in_digital_copy(resize=RESIZE.RESIZE_FIT_TO_PAGE)
        self.fc.fd["copy"].select_start_color()

    def test_02_digital_copy_coverage_flow1(self):

        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.fd["home"].select_tile_by_name(HOME_TILES.TILE_COPY)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=False)
        self.fc.fd["copy"].verify_enable_access_to_camera_screen()
        self.fc.fd["copy"].select_enable_access_to_camera_link_text()
        self.fc.fd["copy"].enable_camera_access_toggle_in_settings()

        # TODO: still working to get something more better
        # import pdb
        # pdb.set_trace()
        # # self.fc.fd["app_settings"].select_browser_back_to_hp_smart()
        # self.fc.fd["copy"].select_settings()
        # self.fc.fd["app_settings"].select_browser_back_to_hp_smart()

    def test_03_digital_copy_coverage_flow2(self):

        self.fc.go_home(verify_ga=True)
        self.fc.add_printer_by_ip(printer_ip=self.printer_ip)
        self.fc.go_copy_screen_from_home()
        self.fc.fd["copy"].select_flash_button()
        self.fc.fd["copy"].select_object_size(object_size=OBJECT_SIZE.SIZE_DRIVER_LICENSE)
        self.fc.fd["copy"].select_auto_capture()
        self.fc.fd["copy"].verify_copy_preview_screen()
        self.fc.fd["copy"].select_number_of_copies(change_copies=1)
        self.fc.fd["copy"].select_resize_in_digital_copy(resize=RESIZE.RESIZE_FILL_PAGE)
        self.fc.fd["copy"].select_start_black()

