import time
import pytest
import logging
import SPL.driver.driver_factory as p_driver_factory
from SPL.driver.reg_printer import PrinterNotReady
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import moobe_ows_flow_container_factory
from MobileApps.libs.flows.web.hp_connect.hp_connect import HPConnect
from selenium.common.exceptions import NoSuchElementException, TimeoutException


from MobileApps.resources.const.ios.const import *


pytest.app_info = "SMART"

#@pytest.mark.app_info("SMART")
@pytest.mark.usefixtures("require_driver", "load_flows")
class Test_Class(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, require_driver):
        self= self.__class__
        self.stack = pytest.config.getoption("--stack")
        self.fc = FlowContainer(self.driver)
        # # Initializing Printer
        self.sys_config = ma_misc.load_system_config_file()
        self.wifi_info = self.sys_config["default_wifi"]
        self.p = p_driver_factory.get_printer(self.sys_config["printer_power_config"],printer_serial="TH74K1Y01F")
        self.p.set_mech_mode(mech=False)
        self.p.send_secure_cfg(self.stack)
        self.p.connect_to_wifi(self.wifi_info["ssid"], self.wifi_info["passwd"])
        self.printer_info = self.p.get_printer_information()
        pytest.printer_serial =self.printer_info["serial number"]
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']
        logging.info(self.p.p_obj.serialNumber)
        self.fc.flow["ios_system"].switch_wifi(self.wifi_info["ssid"], self.wifi_info["passwd"])
        self.fc.change_stack(self.stack)

        logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")        
        if self.p.printer_is_hpc_associated(self.stack):
            hp_connect = HPConnect(self.sys_config, stack=self.stack)
            account = self.p.printer_hp_id_account(self.stack)
            hp_connect.sign_in_from_home_page(account[0], account[1])
            hp_connect.delete_printer(self.printer_info["serial number"], self.stack)                    



        def hp_connect_clean_up():
            try:
                pytest.hp_id_email
            except AttributeError:
                return True

            try:
                pytest.require_clean_up
            except AttributeError:
                return True
            sys_config = ma_misc.load_system_config_file()
            stack = pytest.config.getoption("--stack")
            hp_connect = HPConnect(sys_config, stack=stack)
            hp_connect.sign_in_from_home_page(pytest.hp_id_email, pytest.hp_id_password)
            hp_connect.delete_printer(pytest.printer_serial, stack)        
        request.addfinalizer(hp_connect_clean_up)


    def test_01_home_full_ga(self):
        self.fc.go_home()
        self.fc.add_printer_by_ip(self.printer_ip)

    def test_02_scan_a_file(self):

        self.fc.flow["home"].select_scan_icon()
        self.fc.flow["camera"].select_camera_option_to_scan()
        self.fc.flow["camera"].select_camera_option_to_scan()
        self.fc.flow["camera"].select_allow_camera_if_popup_visible()

        self.fc.flow["camera"].select_capture_btn()
        self.fc.flow["camera"].verify_adjust_boundaries_nav()
        self.fc.flow["camera"].select_adjust_boundaries_next()
        self.fc.flow["preview"].verify_preview_screen()
        self.fc.flow["preview"].save_scan_result("test_file")
        self.fc.flow["preview"].select_save_to_hp_smart_btn()
        self.fc.flow["preview"].verify_print_success_sent_screen()
        self.fc.flow["preview"].select_sent_home()
        time.sleep(2)
        self.driver.wdvr.find_element_by_name("Not Now").click()

    def test_03_create_hpc_account(self):
        self.fc.flow["home"].select_app_settings()
        if self.fc.flow["app_settings"].verify_successfull_sign_in_screen(raise_e=False):
            self.fc.flow["app_settings"].sign_out_from_hpc()
        self.fc.flow["app_settings"].select_sign_in_option()
        if self.fc.flow["app_settings"].verify_successfull_sign_in_screen(raise_e=False):
            self.fc.flow["app_settings"].sign_out_from_hpc()        
            self.fc.flow["app_settings"].select_sign_in_option()

        pytest.hp_id_email, pytest.hp_id_password=self.fc.flow["hp_id_hybrid"].create_account(self.printer_info["serial number"], self.stack)
        self.fc.flow["app_settings"].verify_app_settings_screen_via_top_nav_bar()
        self.fc.flow["home"].select_home_icon()

    def test_04_active_print_anywhere(self):
        self.fc.flow["home"].select_carousel()
        self.fc.flow["printer_settings"].verify_printer_settings_screen(ga=False)
        self.fc.flow["printer_settings"].select_print_anywhere()
        self.fc.flow["printer_settings"].verify_print_anywhere_screen()
        self.fc.flow["printer_settings"].select_enable_in_print_anywhere_screen()
        self.fc.flow["printer_settings"].verify_print_anywhere_enabled_screen(self.printer_info["serial number"], self.stack)
        pytest.require_clean_up=True
        self.fc.flow["printer_settings"].select_navigate_back()
        self.fc.flow["printer_settings"].verify_print_anywhere_menu_item()
        self.fc.flow["printer_settings"].select_navigate_back()

    def test_05_switch_wifi_network(self):
        self.fc.flow["ios_system"].switch_wifi("rdfishbowl50", "adgkmadgkm")
        self.driver.launch_app("com.hp.printer.control")
        time.sleep(20)

    

    def test_06_print_scanned_file(self):
        self.fc.flow["home"].select_documents_icon()
        self.fc.flow["files"].verify_files_screen()
        self.fc.flow["files"].select_hp_smart_files()
        self.fc.flow["files"].verify_hp_smart_files_home_screen()
        self.driver.wdvr.find_element_by_name("test_file.jpeg").click()
        time.sleep(2)
        self.fc.flow["photos"].select_album_details_print()
        self.fc.flow["photos"].verify_photos_edit_screen()
        time.sleep(10)
        self.driver.wdvr.find_element_by_name("Home").click()


