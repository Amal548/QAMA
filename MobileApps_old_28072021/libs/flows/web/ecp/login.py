import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class Login(ECPFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "login"

    def verify_ecp_login(self):
        return self.driver.wait_for_object("email_txt_box")

    def enter_email_address(self, email):
        return self.driver.send_keys("email_txt_box", email)
    
    def click_next_btn(self):
        return self.driver.click("next_btn")

    def enter_email_login(self, email):
        self.verify_ecp_login()
        self.enter_email_address(email)
        self.click_next_btn()