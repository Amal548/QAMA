import sys
import inspect
import logging
from MobileApps.libs.flows.android.system_flows.base_system import *
from MobileApps.libs.flows.android.system_flows.samsung_system import *
from MobileApps.libs.flows.android.system_flows.nexus_system import *
from MobileApps.libs.flows.android.system_flows.pixel_system import *

def all_subclasses(cls):
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in all_subclasses(s)]


def is_abstract(cls):
    return inspect.isabstract(cls)


def system_flow_factory(driver):
    manufacture = driver.driver_info["deviceManufacturer"].lower()
    android_version = driver.driver_info["platformVersion"].split(".")[0]

    default = None
    for cls in all_subclasses(BaseSystem):
        if is_abstract(cls) and not getattr(cls, "manufacture", False):
            continue
        if manufacture in cls.manufacture and not getattr(cls, "version", False):
            default = cls
        if manufacture in cls.manufacture and (getattr(cls, "version", False) and android_version in cls.version):
            return cls(driver)

    if default is not None:
        return default(driver)
    else:
        logging.warning("Cannot satisfy manufacture: {} android_version: {}".format(manufacture,android_version))
        logging.warning("Returning default driver (Note if this doesn't work please overload method with child class)")
        return BaseSystem(driver)