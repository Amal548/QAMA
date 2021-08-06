from MobileApps.libs.flows.web.ows.flow_container_base import BaseFlowContainer

class LiveUI_n_1_fc(BaseFlowContainer):
    #List of printers that have this flow
    liveui_version = -1
    def __init__(self, driver, p_obj, context=None, url=None):
        super(LiveUI_n_1_fc, self).__init__(driver, p_obj, context=context, url=url)