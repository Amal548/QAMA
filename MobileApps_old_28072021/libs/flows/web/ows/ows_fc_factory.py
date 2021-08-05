import re
import logging
from SAF.misc import saf_misc
from MobileApps.libs.flows.web.ows.live_ui_n_1 import *
from MobileApps.libs.flows.web.ows.live_ui_1_0 import *
from MobileApps.libs.flows.web.ows.live_ui_2_0 import *
from MobileApps.libs.flows.web.ows.flow_container_base import BaseFlowContainer

class LiveUIFlowNotImplemented(Exception):
    pass
class BadLiveUIVersion(Exception):
    pass


def ows_fc_factory(driver, ows_p_obj, context=None, url=None):
    """
        Factory method for live ui flow classes: -1, 1.0, 2.0
        Determined by the printer name.
    """
    #Make sure the sub class printer list is all in lower case
    printer_live_ui_version = ows_p_obj.get_liveui_version()
    if type(printer_live_ui_version) != int:
        raise BadLiveUIVersion("Getting a bad live ui version num: " + str(printer_live_ui_version))
    
    default_liveui = None
    for cls in saf_misc.all_subclasses(BaseFlowContainer):
        if saf_misc.is_abstract(cls) and not getattr(cls, "liveui_version", False):
            continue
        #All sub flow containers need to have a printer_list 
        liveui_version = getattr(cls, "liveui_version")
        platform = getattr(cls, "platform", None)
        logging.debug("Looking for liveui_version: " + str(liveui_version))
        if liveui_version == printer_live_ui_version:
            if platform and driver.driver_type == platform:
                return cls(driver, ows_p_obj, context=context, url=url)
            elif not platform:
                default_liveui = cls
    if default_liveui:
        return default_liveui(driver, ows_p_obj, context=context, url=url)
    raise LiveUIFlowNotImplemented("Unable to find flow container for printer: " + str(ows_p_obj.project_name))