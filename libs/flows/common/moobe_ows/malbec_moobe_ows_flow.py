from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import Gen2MoobeOWSFlowContainer


class MalbecMoobeOWSFlow(Gen2MoobeOWSFlowContainer):
    project = "malbec"

    def __init__(self, driver, printer_obj, ows_flow):
        super(MalbecMoobeOWSFlow, self).__init__(driver, printer_obj, ows_flow)
        self.fp_elements = {"cartridge_error": ["fl_devstatus::st_devsts_error_message", "fb_action"],
                            "home_screen": "flow_home::state_home"
                            }