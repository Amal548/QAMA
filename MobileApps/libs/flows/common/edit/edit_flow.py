from MobileApps.libs.flows.common.common_flow import CommonFlow 

class Edit_Flow(CommonFlow):
    #Base Flow for all involved platforms
    project = "smart"

    def __init__(self, driver):
        super(Edit_Flow, self).__init__(driver)
        # if needed to load a specific ui file, this is where it goes