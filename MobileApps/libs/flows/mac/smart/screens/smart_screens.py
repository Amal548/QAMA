from abc import ABCMeta, abstractmethod

from MobileApps.libs.flows.mac.mac_flow import MACFlow


class SmartScreens(MACFlow):
    __metaclass__ = ABCMeta
    project = "smart"

    def __init__(self, driver):
        super(SmartScreens, self).__init__(driver)
        self.load_smart_app_shared_ui()

    def load_smart_app_shared_ui(self):
        ui_map = self.load_ui_map(
            system="MAC", project="smart", flow_name="shared_obj", folder_name=None)
        self.driver.load_ui_map("smart", "shared_obj", ui_map)
        return True

    @abstractmethod
    def wait_for_screen_load(self):
        raise NotImplementedError("Please Implement this method")
