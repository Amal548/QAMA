import time
import pytest
from MobileApps.libs.flows.web.web_flow import WebFlow


class HelpCenter(WebFlow):
    project = "help_center"
    flow_name = "help_center"

    def verify_help_center_screen(self, timeout=30):
        """
        Verifying Help Center screen via title: "Welcome to HP Smart App Help and Support"
        """
        self.driver.wait_for_object("help_center_title", timeout=timeout)

    def select_chat_with_virtual_agent(self):
        self.driver.click("chat_with_virtual_agent_btn")

    def select_accept_cookies(self):
        self.driver.click("accept_cookies_btn")


class IOSHelpCenter(HelpCenter):
    context = "NATIVE_APP"

    def native_verify_help_center_screen(self, timeout=30):
        """
        Verifying Help Center screen via title: "Welcome to HP Smart App Help and Support"
        """
        self.driver.wait_for_object("help_center_title", timeout=timeout)

    def native_select_chat_with_virtual_agent(self):
        self.driver.click("chat_with_virtual_agent_btn")

    def native_select_accept_cookies(self):
        self.driver.click("accept_cookies_btn")
      
    def verify_virtual_agent(self):
        """
        verifies virtual agent in safari
        """
        self.driver.wait_for_object("virtual_agent", timeout=30)
