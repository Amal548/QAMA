import logging
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
class AndroidFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "android"

    def __init__(self, driver):
        super(AndroidFlow, self).__init__(driver)
        self.load_android_system_ui()

    def load_android_system_ui(self):
        ui_map = self.load_ui_map(system="ANDROID", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True
        
    def check_run_time_permission(self, accept=True, ga=False, timeout=5):
        """
        Allow App Permission alert if it displays on the screen for Marshmallow or N device
        """
        permission_popup ={False: ["_system_app_permission_popup", "_system_app_permission_allow_btn", "_system_app_permission_deny_btn"],
                           True: ["_system_app_permission_popup_ga", "_system_app_permission_allow_btn_ga", "_system_app_permission_deny_btn_ga"]}

        if self.driver.wait_for_object(permission_popup[ga][0], timeout=timeout, interval=1, raise_e=False):
            logging.info(
                "Permission popup found with text: " + self.driver.find_object("_system_app_permission_popup").text)
            if accept:
                self.driver.click(permission_popup[ga][1])
            else:
                self.driver.click(permission_popup[ga][2])


    def is_app_permission_popup(self):
        try:
            self.driver.wait_for_object("_system_app_permission_popup", timeout=5)
            is_displayed = True
        except (TimeoutException, NoSuchElementException):
            is_displayed = False
            logging.info("Popup about App Permission is not displayed")
        return is_displayed        

class android_system_ui_flow(AndroidFlow):
    project="system"
    flow_name = "system_ui"
