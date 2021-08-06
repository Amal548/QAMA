import logging
from SAF.misc import saf_misc

from MobileApps.libs.flows.web.ows.sub_flow.osprey import *
from MobileApps.libs.flows.web.ows.sub_flow.load_ink import *
from MobileApps.libs.flows.web.ows.sub_flow.load_paper import *
from MobileApps.libs.flows.web.ows.sub_flow.calibration import *
from MobileApps.libs.flows.web.ows.sub_flow.remove_wrap import *
from MobileApps.libs.flows.web.ows.sub_flow.country_language import *
from MobileApps.libs.flows.web.ows.sub_flow.semi_calibration_scan import *
from MobileApps.libs.flows.web.ows.sub_flow.semi_calibration_print import *
from MobileApps.libs.flows.web.ows.sub_flow.remove_protective_sheet import *


class SubFlowNotImplimented(Exception):
    pass

def sub_flow_factory(driver, flow_name, context=None, url=None):
    try:
        base_class = eval(flow_name)
    except NameError:
        raise SubFlowNotImplimented("Subflow: " + flow_name + " is either not imported or does not exist")

    for cls in saf_misc.all_subclasses(base_class):
        if hasattr(cls, "platform") and driver.driver_type in cls.platform:
            return cls(driver, context=context, url=url)

    logging.warning("Subflow: " + flow_name + " does not have child class for platform " + driver.driver_type)
    return base_class(driver, context=context, url=url)