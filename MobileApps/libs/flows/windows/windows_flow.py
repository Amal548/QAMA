import logging
from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.base_flow import BaseFlow

class WindowsFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "windows"

    def __init__(self, driver):
        super(WindowsFlow, self).__init__(driver)
        self.load_windows_system_ui()

    def load_windows_system_ui(self):
        ui_map = self.load_ui_map(system="WINDOWS", project="system", flow_name="system_ui")
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True
        