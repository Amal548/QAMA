import os
import sys
import uuid
import logging
import requests
import xml.etree.ElementTree as ET


from time import sleep
from SAF.misc import saf_misc
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
from requests.exceptions import InvalidURL
from MobileApps.libs.ma_misc import ma_misc

from MobileApps.libs.app_package.db_utils import DBUtils
from MobileApps.libs.app_package.github_api import github_api_factory

if sys.version_info <= (3, 0):
    input = raw_input

class CannotFindArtifact(Exception):
    pass

class BaseClass(object):
    __metaclass__ = ABCMeta

    def __init__(self, couchdb_info=None):
        if couchdb_info is not None:
            self.db_utils = DBUtils(couchdb_info)
        if self.location.upper() == "GITHUB":
            #Grabbing builds from github will require a database
            self.github_api = github_api_factory(self.platform, self.project_name, self.db_utils)

    def get_file_from_github_artifact(self):
        pass


    def get_file_from_jenkins_artifact(self,page_source, apk_type):
        soup = BeautifulSoup(page_source, 'html.parser')
        links = soup.find_all('a', href=True)
        for i in links:
            if apk_type == "ga":
                if "analytics" in i["href"]:
                    return i["href"]
            elif apk_type == "release":
                if "release" in i["href"] and "debug" not in i["href"]:
                    return i["href"]
            elif apk_type == "debug":
                if "debug" in i["href"] and "analytics" not in i["href"] and "debuggable-release" not in i["href"]:
                    return i["href"]
            elif apk_type == "debuggable":
                if "debuggable" in i["href"]:
                    return i["href"]
        raise CannotFindArtifact("Cannot find artifact of apk_type: " + apk_type)

    def get_file_from_nexus_artifact(self, project_name, app_version=None):
        rd_jenkins_paths = saf_misc.load_json(ma_misc.get_abs_path("libs/app_package/data/rd_jenkins_paths.json"))
        try:
            root_url = next(i for i in rd_jenkins_paths["NEXUS"]["nexus_root"] if project_name in i["projects"])["url"]
            repo_url = next(i for i in rd_jenkins_paths["NEXUS"]["repo_name"] if project_name in i["projects"])["url"]
            group_url = next(i for i in rd_jenkins_paths["NEXUS"]["group_id"] if project_name in i["projects"])["url"]
            pkg_ext = next(i for i in rd_jenkins_paths["NEXUS"]["pkg_ext"] if project_name in i["projects"])["ext"]
            project_url = root_url + repo_url + "content" + group_url + project_name
        except KeyError:
            logging.error("Does not know how to find nexus url for: '" + project_name)
            sys.exit()

        if app_version is None:
            req = requests.get(project_url+"/maven-metadata.xml")
            if req.status_code != 200:
                raise InvalidURL("The URL: " + project_url+ "/maven-metadata.xml" + " returned: " + str(req.status_code))
            tree = ET.fromstring(req.text)
            app_version = tree.findall(".//release")[0].text
        req = requests.get(project_url+"/" + app_version)
        if req.status_code !=200:
            raise InvalidURL("The URL: " + project_url+"/" + app_version + " returned: " + str(req.status_code))            
        pkg_xml = ET.fromstring(req.text)
        return next(i.text for i in pkg_xml.findall(".//resourceURI") if i.text.split(".")[-1] == pkg_ext)

    @abstractmethod
    def get_build_url(self):
        raise NotImplementedError("Please Implement this method")

class LocalBuild(BaseClass):

    platform = "ANY"
    project_name = "ANY"
    location= "local"
    def __init__(self, couch_info):
        if couch_info is None:
            raise RuntimeError("LocalBuild app_module requires couch_info to be not None")
        super(LocalBuild, self).__init__(couch_info)

    def get_build_url(self, file_path):
        if not os.path.isfile(file_path):
            raise IOError("File path: " + file_path + " is not a valid path")
        
        file_name = file_path.split("/")[-1]
        doc = {"file_name": file_name}
        pre_existing_build = self.db_utils.check_build_in_database(file_name, "local_builds", "view_by_file_name")
        if pre_existing_build:
            return pre_existing_build
        else:
            return self.db_utils.upload_build_to_database(doc, file_path)

    def upload_local_build(self, build_path):
        _os = input("For what platform is this build for?: ")
        if _os.lower() == "ios":
            build_type = input("Build type: ")
            build_version = input("Build version: ")
            daily_version = input("Daily version: ")
            doc = {"build_type": build_type, "build_version": build_version, "daily_version": daily_version, "os": _os.upper()}
            self.db_utils.upload_build_to_database(doc, build_path)
        else:
            print ("Currently this method only supports IOS") 