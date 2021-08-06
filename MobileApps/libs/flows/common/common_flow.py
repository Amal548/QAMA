from MobileApps.libs.flows.base_flow import BaseFlow

class CommonFlow(BaseFlow):
    system = "common"

    def __init__(self, driver):
        super(CommonFlow, self).__init__(driver)
        if getattr(self, "platform", None) is not None:
            self.ui_map = self.load_ui_map(system=self.system, project=self.project,
                                           flow_name=self.flow_name + "_" + self.platform, folder_name=self.folder_name)
            self.driver.load_ui_map(self.project, self.flow_name, self.ui_map, append=True)
