import time
from time import sleep
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.web.web_flow import WebFlow
import logging
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.ma_misc import ma_misc

class ConnectWebServices(WebFlow):
    project = "instant_ink"
    flow_name="connect_web_services"

    
    def __init__(self,driver):
        super(ConnectWebServices, self).__init__(driver)

    def finish_connection(self, p_object, stack="pie"):
        self.verify_connect_web_services_page()
        if not self.check_connect_path():
            self.driver.click("continue_btn")
            sleep(1)
            self.driver.click("continue_btn")
            sleep(1)
            self.driver.click("continue_btn")
            self.driver.wdvr.switch_to.context(self.driver.wdvr.contexts[-1])
            self.verify_enter_code()
            self.driver.send_keys("enter_code_txt", p_object.get_claim_code(stack))
            self.driver.click("apply_btn")

    def verify_enter_code(self, timeout=60):
        self.driver.wait_for_object("enter_code_txt")

    def verify_connect_web_services_page(self):
        self.driver.wdvr.switch_to.context(self.driver.wdvr.contexts[-1])
        sleep(1)
        self.driver.wait_for_object("connect_web_services_title", timeout=20)
        self.driver.wdvr.switch_to.context("NATIVE_APP")
        sleep(1)

    def check_connect_path(self, timeout=180):
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                self.driver.find_object("couldn't_connect_automatically_txt")
                return False
            except NoSuchElementException:
                sleep(5)
        raise TimeoutException("Neither path showed up")