import requests
import logging
import sys
from abc import ABCMeta, abstractmethod
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from requests.exceptions import InvalidURL

from MobileApps.libs.app_package.base_class import BaseClass
class AndroidApp(BaseClass):
    __metaclass__ = ABCMeta

    platform="ANDROID"

    def android_app_package_url(self, project_name, apk_type="debug", release_type="daily"):
        rd_jenkins_paths = saf_misc.load_json(ma_misc.get_abs_path("libs/app_package/data/rd_jenkins_paths.json"))
        try:
            root_url = rd_jenkins_paths[self.platform]["jenkins_root"]
            view = rd_jenkins_paths[self.platform][project_name]["view"]
            project_url = root_url + view + "/job"+ rd_jenkins_paths[self.platform][project_name][release_type]
        except KeyError:
            logging.error("Does not know how to find url for: '" + project_name + "' for '" + self.platform + "' system with a '"+ release_type + "' release")
            sys.exit()

        req = requests.get(project_url)
        if req.status_code != 200:
            raise InvalidURL("The URL: " + project_url + " returned: " + str(req.status_code))
        page_source = req.text
        root_url_page_type= rd_jenkins_paths[self.platform][project_name]["location"] 
        if root_url_page_type == "jenkins":
            return project_url + self.get_file_from_jenkins_artifact(page_source, apk_type)

    @abstractmethod
    def get_build_url(self):
        raise NotImplementedError("Please Implement this method")


class AndroidSmart(AndroidApp):
    location = "github"
    location_type = "server"
    project_name = "SMART"
    def __init__(self, couch_info):
        super(AndroidSmart, self).__init__(couch_info)

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)

class AndroidHPPS(AndroidApp):
    location = "github"
    location_type = "server"
    project_name = "HPPS"
    def __init__(self, couch_info):
        super(AndroidHPPS, self).__init__(couch_info)

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)

class AndroidJweb(AndroidApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB"
    
    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.get_file_from_nexus_artifact("jarvis_android_webview", app_version='0.2.33')

class AndroidJwebDataCollection(AndroidApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB_DATA_COLLECTION"

    def get_build_url(self, build_type="debug", build_version=None, build_number=None, release_type="daily"):
        return self.get_file_from_nexus_artifact("jarvis_android_data_collection", app_version=build_version)