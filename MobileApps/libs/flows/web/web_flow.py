import types
import logging
import time
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow

class MissingWebDriver(Exception):
    pass

class UnexpectedURLError(Exception):
    pass

class WebFlow(BaseFlow, metaclass=ABCMeta):
    system = "web"

    def __init__(self, driver, context=None, url=None, window_name="main"):
        #Driver: Your appium/selenium driver object
        #Context: When using these are webview flows you should pass in what context
        #The flow should expect to be in 
        #url: The partial/full URL of the window you are expecting to be at after switching to the webivew (appium usages only)
        #Window_name: When using the flow in a multi window setup make sure you pass in the window name the flow is associated io
        super(WebFlow, self).__init__(driver)
        self.logging_ignore_methods.append("wrapper")
        self.wn = window_name
        self.load_web_system_ui()
        if context is not None:
            self.context = context
        self.url = url

    def load_web_system_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map, append=True)
        return True

    def dismiss_connection_not_private(self):
        if self.driver.wait_for_object("_system_chrome_not_private_advanced_btn", timeout=5, raise_e=False):
            self.driver.click("_system_chrome_not_private_advanced_btn")
            self.driver.click("_system_chrome_not_private_proceed_link")
        return True

    def verify_web_page(self, sub_url=None, timeout=60, raise_e=True):
        start_time = time.time()
        while time.time() - start_time <=timeout:
            for window in self.driver.wdvr.window_handles:
                self.driver.wdvr.switch_to.window(window)
                cur_url = self.driver.current_url
                sub_url = self.flow_url if sub_url is None else sub_url 
                if sub_url in cur_url.split("/"):
                    return True
            time.sleep(5)

        if raise_e:
            raise UnexpectedURLError("Expecting: " + self.flow_url + " got: " + cur_url)
        else:
            return False

    def verify_existed_context(self, context, timeout=10):
        """
        Verify a context in context list or not in timeout
        :return True -> existed. False -> unexisted.
        """
        timeout = time.time() + timeout
        while time.time() < timeout:
            if context in self.driver.wdvr.contexts:
                return True
        return False

    def dismiss_safari_connection_not_private(self):
        if self.driver.wait_for_object("_system_safari_not_private_show_details", timeout=5, raise_e=False):
            self.driver.click("_system_safari_not_private_show_details")
            self.driver.click("_system_safari_not_private_visit_this_website")
        return True
    
    def switch_to_window(self, url):
        """
        Using to switch to window which url is matched with the window
        It is only switched if there are multiple windows. Otherwise, do nothing
        """
        windows = self.driver.wdvr.window_handles
        if len(windows) > 1:
            for window in windows:
                self.driver.wdvr.switch_to.window(window)
                if url in self.driver.current_url:
                    break
        else:
            logging.info("There is only one window in this context")