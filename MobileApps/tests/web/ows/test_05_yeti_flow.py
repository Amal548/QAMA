import os
import time
import pytest
import traceback

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.web.ows.yeti_flow_container import YetiFlowContainer
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

pytest.app_info = "OWS"

class Test_OWS_Yeti(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, web_session_setup, request):
        self = self.__class__
        self.driver = web_session_setup
        self.driver.set_size("max")
        self.fc = YetiFlowContainer(self.driver)
        self.profile =  request.config.getoption("--printer-profile")
        self.biz_model = request.config.getoption("--printer-biz-model")
        self.stack = request.config.getoption("--stack")
        self.driver.set_global_cms_sys_arg(["--printer-profile", "--printer-biz-model", "--emu-platform"])
        try:
            ows_status, self.access_token, self.id_token = self.fc.emulator_start_yeti(self.stack, self.profile, self.biz_model)
            self.driver.wait_for_new_window(timeout=15)
            self.driver.add_window("OWSEmuPrinter")
            self.ows_printer = OWSEmuPrinter(self.fc.get_printer_name_from_profile(self.profile), self.driver, 2, ows_status, window_name="OWSEmuPrinter")  
        except:
            session_attachment = pytest.session_result_folder + "session_attachment"
            os.makedirs(session_attachment)
            c_misc.save_screenshot_and_publish(self.driver, session_attachment + "/ows_yeti_setup_failure.png")
            c_misc.save_source_and_publish(self.driver,  session_attachment+ "/", file_name = "ows_yeti_setup_failure.txt")
            traceback.print_exc()
            raise

    def test_01_verify_printer_data_page(self):
        self.fc.flow["smart_printer_consent"].verify_printer_consent_screen()
        self.fc.flow["smart_printer_consent"].click_accept_all()
    
    def test_02_navigate_offer(self):
        self.fc.navigate_yeti(self.profile, self.biz_model)

    def test_04_complete_activation(self):
        self.ows_printer.login(self.access_token, self.id_token)
        redirect_url = self.ows_printer.get_console_data("GET - SignInHp")["params"]["continuationUrl"] + "&completionCode=0"
        self.driver.switch_window()
        self.driver.navigate(redirect_url)
        time.sleep(10)
        self.ows_printer.click_enable_ws()

    def test_05_verify_ucde_privacy(self):
        self.fc.flow["ucde_privacy"].skip_ucde_privacy_screen(timeout=20)

    def test_06_verify_ucde_activation(self):
        self.fc.flow["ucde_activation_success"].verify_ucde_activation_success(timeout=120)
        self.fc.flow["ucde_activation_success"].click_continue(raise_e=False)
    
    def test_07_verify_flow_complete(self):
        self.fc.flow["value_proposition"].verify_value_proposition_page(timeout=40)