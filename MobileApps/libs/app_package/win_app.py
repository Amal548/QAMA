from abc import ABCMeta, abstractmethod
from MobileApps.libs.app_package.base_class import BaseClass

class WINAppException(Exception):
    pass

class WINApp(BaseClass):
    __metaclass__ = ABCMeta

    platform = "WINDOWS"

    @abstractmethod
    def get_build_url(self, *args, **kwarg):
        raise NotImplementedError("Please Implement this method")


class WINJweb(WINApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB"

    def get_build_url(self, app_version=None, *args, **kwarg):
        return self.get_file_from_nexus_artifact("jarvis_windows_webview", app_version=app_version)

class WinSmart(WINApp):
    location = "nexus"
    location_type = "server"
    project_name = "SMART"

    def get_build_url(self, build_version=None, *args, **kwarg):
        return self.get_file_from_nexus_artifact("GothamUltron", build_version=app_version)

class WINJwebDataCollection(WINApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB_DATA_COLLECTION"

    def get_build_url(self, app_version=None, *args, **kwarg):
        return self.get_file_from_nexus_artifact("jarvis_windows_data_collection", app_version=app_version)
