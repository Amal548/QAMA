import uuid
import json
import shutil
import logging
from lxml import html
from MobileApps.libs.ma_misc import ma_misc
import requests, zipfile,os
from abc import ABCMeta, abstractmethod
from MobileApps.libs.app_package.base_class import BaseClass
from io import BytesIO

class IOSApp(BaseClass):
    __metaclass__ = ABCMeta

    platform="IOS"
    @abstractmethod
    def get_build_url(self):
        raise NotImplementedError("Please Implement this method")

class IOSSmart(IOSApp):
    location = "github"
    location_type = "server"
    project_name = "SMART"
    def __init__(self, couch_info):
        #Due to where the IOS Smart app is located a couchdb is required to automate this
        if couch_info is None:
            raise RuntimeError("IOSSmart app_module requires couch_info to be not None")
        super(IOSApp, self).__init__(couch_info)

    def get_build_url(self, build_type="adhoc", build_version=None, build_number=None):
        return self.github_api.get_build_url(build_type=build_type, build_version=build_version, build_number=build_number)

class IOSAuth(IOSApp):
    location = "nexus"
    location_type = "server"
    project_name = "JAUTH"
    def get_build_url(self, build_number=None):
        return self.get_file_from_nexus_artifact("jarvis_ios_auth", build_number=build_number)

class IOSJweb(IOSApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB"
    def get_build_url(self, build_type="debug", build_version=None, build_number=None):
        return self.get_file_from_nexus_artifact("jarvis_ios_webview", app_version=None)

class IOSJwebDataCollection(IOSApp):
    location = "nexus"
    location_type = "server"
    project_name = "JWEB_DATA_COLLECTION"
    def get_build_url(self, build_number=None):
        return self.get_file_from_nexus_artifact("jarvis_ios_data_collection", build_number=build_number)