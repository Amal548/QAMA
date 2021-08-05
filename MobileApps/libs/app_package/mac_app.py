from abc import ABCMeta, abstractmethod
from MobileApps.libs.app_package.base_class import BaseClass

class MACApp(BaseClass):
    __metaclass__ = ABCMeta

    platform = "MAC"

    @abstractmethod
    def get_build_url(self, *args, **kwarg):
        raise NotImplementedError("Please Implement this method")


class MACJweb(MACApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB"

    def get_build_url(self, app_version=None, *args, **kwarg):
        return self.get_file_from_nexus_artifact("jarvis_mac_webview", app_version=app_version)

class MACJwebDataCollection(MACApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB_DATA_COLLECTION"

    def get_build_url(self, app_version=None, *args, **kwarg):
        return self.get_file_from_nexus_artifact("jarvis_mac_data_collection", app_version=app_version)