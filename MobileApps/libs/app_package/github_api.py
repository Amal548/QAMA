import os
import re
import sys
import abc
import json
import uuid
import shutil
import zipfile
import logging
import requests
from io import BytesIO
from SAF.misc import saf_misc
from SAF.misc.factory_util import *
from MobileApps.libs.ma_misc import ma_misc

class PkgSearchException(Exception):
    pass

class BadBuildVersionException(PkgSearchException):
    pass


def github_api_factory(platform, project_name, db_utils):
    for _cls in all_subclasses(GithubAPI):
        if is_abstract(_cls) or not getattr(_cls, "platform", False):
            continue

        if _cls.platform.upper() == platform.upper() and project_name.upper() in _cls.project_name:
            return _cls(platform, project_name, db_utils)
    
    logging.error("Cannot satisfy module type: " + platform + " for project: " + project_name)
    sys.exit()

class GithubAPI(abc.ABC):
    def __init__(self, platform, project_name, db_utils):
        self.db_utils = db_utils
        self.system_config = ma_misc.load_system_config_file()
        rd_jenkins_paths = saf_misc.load_json(ma_misc.get_abs_path("libs/app_package/data/rd_jenkins_paths.json"))

        self.project_name = project_name
        self.platform = platform

        token_name = next(i for i in rd_jenkins_paths["GITHUB"]["token_name"] if platform == i["platform"] and project_name in i["projects"])["name"]
        self.root_url = next(i for i in rd_jenkins_paths["GITHUB"]["github_root"] if platform == i["platform"] and project_name in i["projects"])["url"]
        self.releases_api_url = next(i for i in rd_jenkins_paths["GITHUB"]["release_url"] if platform == i["platform"] and project_name in i["projects"])["url"]
        self.build_type_dict = next(i for i in rd_jenkins_paths["GITHUB"]["build_type_dict"] if platform == i["platform"] and project_name in i["projects"])["build_type_dict"]

        self.access_token = self.system_config[token_name]

        self.request_paging = "?page=1&per_page=20"
        self.tag_api_url = "/tags/{}"
        self.auth_header = {"Authorization": "token " + self.access_token}
        #During transition I'll keep this the same
        self.db_view_section = "IOS_view"
        self.db_view_doc = self.platform.lower() + "_package_view"

    def download_build(self,build_type=None, build_version=None, build_number=None, release_type=None, save_location="./"):
        url, _, _ = self.find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        self.download_build_to_local(url, save_path=save_location)

    def get_build_url(self, build_type=None, build_version=None, build_number=None, release_type=None):
        """
        Params: build_type: The type of build (adhoc (ios), debug(android), loggable, ga, etc)
                build_version: The major version of the app (8.6.1, 8.7.0, etc)
                build_number: The build number of that major version (25, 8695, etc)
                release_type: Android HP Smart/HPPS specific (consists of daily or stable builds)
        """
        #look for it in the database
        match_key = [self.project_name, build_type, build_version, build_number, release_type]    
        database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc)
        if database_url:
            return database_url

        url, actual_build_version, actual_daily_version = self.find_build(build_type=build_type, build_version=build_version, build_number=build_number, release_type=release_type)
        match_key = [self.project_name, build_type, actual_build_version, actual_daily_version, release_type]
        database_url = self.db_utils.check_build_in_database(match_key, self.db_view_section, self.db_view_doc)
        if database_url:
            return database_url

        doc = {"build_type": build_type,
                "os": self.platform,
                "build_version": actual_build_version,
                "daily_version": actual_daily_version,
                "project": self.project_name,
                "release_type": release_type
                }
        unique_id = uuid.uuid4().hex
        unique_folder_path = "./" + unique_id
        fname = self.download_build_to_local(url, save_path=unique_folder_path)
        if fname.endswith(".zip"):
            unique_file_path = "./" + unique_id + "/" + os.listdir(unique_folder_path)[0]
        else:
            unique_file_path = "./" + unique_id + "/" + fname
        attachment_url = self.db_utils.upload_build_to_database(doc, unique_file_path)
        shutil.rmtree("./" + unique_id)
        return attachment_url

    @abc.abstractmethod
    def find_build(self, build_type=None, build_version=None, build_number=None, release_type=None):
        if build_number is not None and build_version is None:
            raise ValueError("You cannot only use build_number, you also need to pass in build_version")
        if build_version is not None:
            if len(build_version.split(".")) != 3:
                raise BadBuildVersionException("Build version needs 3 numbers sample: 8.5.0. This is what's passed in:" + str(build_version))
        

    def get_all_releases(self):
        req = requests.get(self.root_url + self.releases_api_url + self.request_paging, headers=self.auth_header)
        if req.status_code != 200:
            req.raise_for_status() 
        return json.loads(req.text)

    def download_build_to_local(self, url, save_path="./"):
        ma_misc.create_dir(save_path)
        logging.debug('Downloading...')
        stream_header = self.auth_header.copy()
        stream_header["Accept"] = "application/octet-stream"
        req = requests.get(url, headers=stream_header)
        fname = re.findall("filename=(.+)", req.headers['content-disposition'])[0]
        if fname.endswith(".zip"):
            z = zipfile.ZipFile(BytesIO(req.content))
            z.extractall(save_path)
            logging.debug('Downloading and extracting Completed')
        else:
            with open(save_path + "/" + fname, "wb") as fh:
                fh.write(req.content)
        return fname

    def all_releases_find_build(self, build_type, build_version=None, build_number=None, prerelease_only=True):
        desired_release = None
        if build_version and build_number:
            search_version = ".".join([build_version,build_number])
        else:
            search_version = None

        all_release = self.get_all_releases()
        for release in all_release:
            if prerelease_only is not release.get("prerelease", True):
                continue

            if search_version: 
                if self.clean_release_name(release["name"]) != search_version:
                    continue
            elif build_version:
                release_build_version = ".".join(self.clean_release_name(release["name"]).split(".")[:-1])
                if build_version != release_build_version:
                    continue
            if desired_release is None:
                desired_release = release
            else:
                if int(self.clean_release_name(release["name"]).replace(".", "")) > int(self.clean_release_name(desired_release["name"]).replace(".", "")):
                    desired_release = release

        if desired_release is None or desired_release.get("message", None) == "Not Found":
            raise PkgSearchException("Cannot locate release for build_version: "  + str(build_version) + " build_number: " + str(build_number))
        return self.find_asset(desired_release, build_type)

    def find_asset(self, desired_release, build_type):
        actual_build_version = ".".join(self.clean_release_name(desired_release["name"]).split(".")[:-1])
        actual_daily_version = self.clean_release_name(desired_release["name"]).split(".")[-1]
        for asset in desired_release["assets"]:
            if bool(re.search(self.build_type_dict[build_type], asset["name"])):
                return asset["url"], actual_build_version, actual_daily_version
        raise PkgSearchException("Somehow the asset was not found :( build_type: " + build_type)

    def clean_release_name(self, release_name):
        if release_name[0]=="v":
            return release_name[1:]
        else:
            return release_name

class AndroidGithubAPI(GithubAPI):
    platform = "ANDROID"
    project_name = ["SMART", "HPPS"]
    def find_build(self, build_type="debug", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type="build_type", build_version=build_version, build_number=build_number, release_type=release_type)
        if release_type=="daily":
            return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number)
        elif release_type=="stable":
            #This API returns the latest "Released" build which is the stable branch build
            if not build_version:
                return self.find_asset(json.loads((requests.get(self.root_url + self.releases_api_url + "/latest", headers=self.auth_header).text)), build_type)
            else:
                return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number, prerelease_only=False)


class IOSHPGithubAPI(GithubAPI):
    platform = "IOS"
    project_name = ["SMART"]
    def find_build(self, build_type="adhoc", build_version=None, build_number=None, release_type=None):
        super().find_build(build_type="build_type", build_version=build_version, build_number=build_number, release_type=release_type)
        return self.all_releases_find_build(build_type, build_version=build_version, build_number=build_number)

        