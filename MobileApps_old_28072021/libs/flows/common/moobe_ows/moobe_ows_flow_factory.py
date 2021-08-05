from SAF.misc import saf_misc
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import *
from MobileApps.libs.flows.common.moobe_ows.verona_moobe_ows_flow import *
from MobileApps.libs.flows.common.moobe_ows.palermo_moobe_ows_flow import *
from MobileApps.libs.flows.common.moobe_ows.infinity_moobe_ows_flow import *
from MobileApps.libs.flows.common.moobe_ows.malbec_moobe_ows_flow import *
from MobileApps.libs.flows.common.moobe_ows.vasari_moobe_ows_flow import *
from MobileApps.libs.flows.common.moobe_ows.moobe_ows_flow_container import *


class MoobeOWSSubClassNotImplimented(Exception):
    pass


def return_firmware_type(printer_obj):
    if printer_obj.p_obj.isSOL:
        return "sol"
    else:
        return "sirius"

def moobe_ows_flow_container_factory(driver, printer_obj, ows_flow):
    printer_name = printer_obj.p_obj.projectName.split("_")
    project_name = printer_name[0]
    project_sub_name = printer_name[1]
    is_sol = return_firmware_type(printer_obj)

    firmware_type_class = None
    for cls in saf_misc.all_subclasses(BaseMoobeOWSFlowContainer):
        if saf_misc.is_abstract(cls) and not getattr(cls, "firmware", False):
            continue

        cls_is_sol = getattr(cls, "firmware", None)
        cls_project_name = getattr(cls, "project", None)
        cls_project_sub_name = getattr(cls, "sub_name", None)

        if cls_project_name is not None and cls_project_name.lower() == project_name.lower():
            if cls_project_sub_name is not None and cls_project_sub_name.lower() == project_sub_name.lower():
                return cls(driver, printer_obj, ows_flow)
            elif cls_project_sub_name is None:
                firmware_type_class = cls
        elif cls_project_name is None and cls_is_sol.lower() == is_sol.lower():
            firmware_type_class = cls
    if firmware_type_class is None:
        raise MoobeOWSSubClassNotImplimented("Cannot satisfy: " + project_name + " " + is_sol)

    return firmware_type_class(driver, printer_obj, ows_flow)