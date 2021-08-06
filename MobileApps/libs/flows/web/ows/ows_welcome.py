import logging

from selenium.webdriver.support.ui import Select
from SAF.decorator.saf_decorator import native_context
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from SAF.decorator.saf_decorator import screenshot_compare

class OWSWelcome(OWSFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "ows_welcome"
    
    def verify_welcome_screen(self):
        return self.driver.wait_for_object("page_title")
    
    @screenshot_compare()
    def click_continue(self):
        return self.driver.click("continue_btn")

    @native_context
    def select_more_options(self):
        self.driver.click("more_option")

    @native_context
    def select_skip_option(self):
        self.driver.click("skip_menu_item")

    @native_context
    def select_yes_popup_option(self):
        self.driver.click("skip_popup_yes_btn")