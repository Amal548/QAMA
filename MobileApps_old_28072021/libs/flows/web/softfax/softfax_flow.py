from abc import ABCMeta
from MobileApps.libs.flows.web.web_flow import WebFlow
from selenium.webdriver.common.keys import Keys
import time
import pytest


class NotSwitchToSoftfaxWebViewException(Exception):
    pass

class SoftFaxFlow(WebFlow):
    __metaclass__ = ABCMeta
    project = "softfax"
    #context = "WEBVIEW_com.hp.printercontrol.debug"
    
    def __init__(self, driver, context=None):
        super(SoftFaxFlow, self).__init__(driver, context=context)
        self.func_ignore_methods.append("load_softfax_shared_ui")
        self.load_softfax_shared_ui()

    def load_softfax_shared_ui(self):
        ui_map = self.load_ui_map(system="web", project="softfax", flow_name="shared_obj")
        self.driver.load_ui_map("softfax", "shared_obj", ui_map)
        return True

    def click_back(self):
        """
        Click on Back button
        """
        self.driver.click("_shared_back_btn")
