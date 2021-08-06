import os
import re
import sys
import time
import json
import shutil
import logging
import requests
from SAF.misc import saf_misc
from requests.exceptions import InvalidURL

class SystemConfigFileMissing(Exception):
    pass

class CannotSatisfyAccount(Exception):
    pass

def get_abs_path(relative_path=None, file_check=False):
    """
    Description: Find the absolute path from a relative path 
    Param:
    relative_path -- The relative path from the repo to the file
    file_check -- if set true the method will throw an exception if file does not exist

    NOTE: Due to how the __file__ works this method cannot be moved outside of the repo
          A copy in each repo is REQUIRED 
    """
    path = "/".join(os.path.abspath(os.path.dirname(__file__)).split("/")[:-2])
    if relative_path is not None:
        if type(relative_path) != str:
            raise TypeError("relative_path must be type str")
        if relative_path[0] != "/":
            path = path + "/"
        path = path + relative_path

        if file_check and not os.path.isfile(path) and not os.path.isdir(path):
            raise IOError("The path: " + path + " is not a file or directory")

    return path

def return_apk_cache_path(apk_name):
    return get_abs_path("/resources/apk_cache/" + apk_name)

def create_dir(directory):
    """
    Create a directory
    :param directory: path of directory
    :return: absolute path of directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.debug("{} is created successfully!".format(directory))
    else:
        logging.debug("{} is already existed!".format(directory))
    return os.path.abspath(directory)

def create_file(file_path, write_mode='w', content=""):
    """
    Create a file with a content
    :param file_path: file's path
    :param write_mode: writing mode
    :param content: content in file
    """
    if not os.path.exists(file_path):
        if file_path.rfind("/") > 0:
            create_dir(file_path[:file_path.rfind("/")])
        with open(file_path, write_mode) as fi:
            fi.write(content)
    else:
        logging.debug("'{}' is already created".format(file_path))

def load_system_config_file(relative_path="config/system_config.json"):
    try:
        get_abs_path(relative_path, file_check=True)
        return load_json_file(relative_path)
    except IOError:
        logging.info("Could not find system_config.json in MobileApps, trying system path")
        if not os.path.isfile("/work/ma_config/system_config.json"):
            raise SystemConfigFileMissing("No system_config.json file in MobileApps or the system path (/work/ma_config/system_config.json)")
        else:
            return load_json_file("/work/ma_config/system_config.json")

def load_json_file(relative_path):
    file_path = get_abs_path(relative_path)
    return saf_misc.load_json(file_path)

def get_apk_path(apk_name):
    """
    Get absolute path of apk file via apk name
    :param apk_name: name of apk file. For example: google_drive
    :return paths: list of paths based on keyword, apk_name"
    """
    apk_folder = get_abs_path("resources/test_data/apk_files")
    for file in os.listdir(apk_folder):
        if apk_name in file:
            return os.path.join(apk_folder, file)
    raise IOError ("There is no apk file for {}".format(apk_name))


def prep_base_url(url):
    if url[-1] != "/":
        url = url + "/"

    return url

def validate_url(_str):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, _str) is not None

def delete_content_of_folder(path, time_delta=None, everything=True, recreate=True):
    #Delete folder and remake it if time_stamp is None
    #If there is a time stamp only delete anything older than the time specified
    if not os.path.isdir(path):
        logging.debug("Folder: " + path + " does not exist returning True")
        return True

    if time_delta is None:
        if os.path.isdir(path):
            shutil.rmtree(path)
    else:
        if everything and os.path.getctime(path) < (time.time() - time_delta.total_seconds()):
            shutil.rmtree(path)
        if not everything:
            content = os.listdir(path)
            for item in content:
                child_path = path+'/' + item
                if os.path.getctime(child_path) < (time.time() - time_delta.total_seconds()):
                    shutil.rmtree(child_path)

    if recreate:
        os.makedirs(path)

def publish_to_junit(path):
    sys.stderr.write("\n[[ATTACHMENT|{}]]".format(path))

def truncate_printer_model_name(name, case_sensitive=True):
    """
    https://github-partner.azc.ext.hp.com/HPSmartiOS/dociOS/wiki/02.8.-%5bHome%5d-Device-Model-Name-shortening
    shortening model name for iOS app
    :param case_sensitive: bool
    """
    removed_list = [
        "Hewlett-Packard",
        "e-All-in-One",
        "All-in-One",
        "AIO",
        "Ink Advantage Ultra",
        "Ink Advantage",
        "Advantage",
        "Postscript",
        "Flowmfp",
        "Flow",
        "ePrinter",
        "Printer",
        "Series",
        "ColorMFP",
        "Color",
        "MFP",
        "Professional",
        "Premium",
        "Prem"
    ]
    if not case_sensitive:
        removed_list = [word.lower() for word in removed_list]
        name = name.lower()
    for i in removed_list:
        name = name.replace(i,"").strip()
    name = re.sub(r'\[.*?\]', "", name)
    return " ".join(name.split())

def get_subfolder_path(file_path, relative_root):
    path_list = os.path.abspath(os.path.dirname(file_path)).split("/")
    return "/".join(path_list[path_list.index(relative_root)+1:])

def _launch_driver(self, browser_type="chrome"):
    info_dict = {"server": {"url": self.system_config["web_executor_url"], "port": self.system_config["web_executor_port"]},
                            "dc": {"platform": "ANY"}}
    return driver_factory.web_driver_factory(browser_type, info_dict)

def is_int(check_str):
    try:
        int(check_str)
        return True
    except ValueError:
        return False

def poll(method, timeout=10, frequency=.5, *args, **kwargs) -> bool:
    """
    Continuously poll a method until it returns True or timeout has been reached
    :param method: function obj that returns a bool
    :param timeout: int or float
    :param frequency: int or float. how often to poll
    :param args: args for method
    :param kwargs: keyword args for method
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        if method(*args, **kwargs):
            return True
        time.sleep(frequency)
    return False

def get_hpid_account_info(stack, a_type, claimable=True, II=False):
    f = saf_misc.load_json(get_abs_path("/resources/test_data/hpid/test_accounts.json"))
    try:
        account_info = f[stack][a_type]
    except KeyError:
        raise
    for account in account_info:
        if (II and not account.get("instant_ink", False)) or (not II and account.get("instant_ink", False)):
            continue

        if account["claimable"] == claimable:
            return account
            
    raise CannotSatisfyAccount("No account for: stack=" + stack + " type="+ a_type + " claimable=" + str(claimable))

def get_ecp_account_info(stack):
    f = saf_misc.load_json(get_abs_path("/resources/test_data/ecp/accounts.json"))
    try:
        return f[stack]
    except KeyError:
        raise CannotSatisfyAccount("No account for: stack=" + stack)    
            

#Test code for debugging
if __name__ == "__main__":
    pass