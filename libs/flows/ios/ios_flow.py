import logging
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class IOSFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "ios"

    def __init__(self, driver):
        super(IOSFlow, self).__init__(driver)
        self.load_ios_system_ui()

    def load_ios_system_ui(self):
        ui_map = self.load_ui_map(system="IOS", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True

    '''
    def check_run_time_permssion(self, accept=True):
        """
        Allow App Permission alert if it displays on the screen for Marshmallow or N device

        """

        if int(self.driver.driver_info["platformVersion"][0]) < 6:
            logging.info("Device's OS Version(" + self.driver.driver_info[
                "platformVersion"] + ") does NOT have run time permission")
            return True

        while self.driver.wait_for_object("_system_app_permission_popup", timeout=5, interval=1, raise_e=False):
            logging.info(
                "Permission popup found with text: " + self.driver.find_object("_system_app_permission_popup").text)
            self.driver.click("_system_app_permission_allow_btn")

    def is_app_permission_popup(self):
        try:
            self.driver.wait_for_object("_system_app_permission_popup", timeout=5)
            is_displayed = True
        except (TimeoutException, NoSuchElementException):
            is_displayed = False
            logging.info("Popup about App Permission is not displayed")
        return is_displayed
    '''

    def click_visit_website_button(self):
        """
        clicks visit website button
        """
        if self.driver.wait_for_object("_system_visit_website_pop_up_button", timeout=10, raise_e=False):
            self.driver.click("_system_visit_website_pop_up_button")
        else:
            logging.debug("visit website button not found")

    def click_continue_button(self):
        """
        select continue button during the sign in
        """
        if self.driver.wait_for_object("_system_continue_button", raise_e=False):
            self.driver.click("_system_continue_button", raise_e=False)
        else:
            logging.debug("continue button not found")