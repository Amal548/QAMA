import sys
import inspect
import logging
from SAF.misc.factory_util import *
from MobileApps.libs.app_package.base_class import BaseClass
from MobileApps.libs.app_package.android_app import *
from MobileApps.libs.app_package.ios_app import *
from MobileApps.libs.app_package.mac_app import *
from MobileApps.libs.app_package.win_app import *

def app_module_factory(platform, app_name, couchdb_info=None):

    for _cls in all_subclasses(BaseClass):
        if is_abstract(_cls) or not getattr(_cls, "project_name", False):
            continue

        if _cls.platform.lower() == platform.lower() and _cls.project_name.lower() == app_name.lower():
            return _cls(couchdb_info)

    logging.error("Cannot satisfy module type: " + platform + " for project: " + app_name)
    sys.exit()


if __name__ == "__main__":
    pass
    #couchdb_info = {"url": "https://saldb06.vcs.rd.hpicorp.net/", "user":"service", "password":"service"}
    #app_obj = app_module_factory("IOS", "SMART", couchdb_info)
    #url = app_obj.get_build_url(build_type="adhoc", build_version="6.0")
    #app_obj = app_module_factory("ANDROID", "HPPS", couchdb_info)
    #url = app_obj.get_build_url("debug", "daily")
