import io
import os
import sys
import json
import base64
import pytest
import logging
import zipfile
import requests

#Web imports 


from SAF.misc import saf_misc
from SAF.driver import driver_factory
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.app_package.app_class_factory import app_module_factory

#Appium platform consts
import MobileApps.resources.const.ios.const as i_const
import MobileApps.resources.const.mac.const as m_const
import MobileApps.resources.const.android.const as a_const
import MobileApps.resources.const.windows.const as w_const


class BadLocaleStrException(Exception):
    pass

class UnknownDefaultLocaleException(Exception):
    pass

class MissingWifiInfo(Exception):
    pass

#Default locales please reference this webpage 
#http://www.apps4android.org/?p=3695

default_locale= {"ar": "SA",
                 "en": "US",
                 "cs": "CZ",
                 "da": "DK",
                 "de": "DE",
                 "el": "GR",
                 "es": "ES",
                 "fi": "FI",
                 "he": "IL",
                 "hu": "HU",
                 "ja": "JP",
                 "ko": "KR",
                 "nb": "NO",
                 "pl": "PL",
                 "pt": "PT",
                 "ru": "RU",
                 "sv": "SE",
                 "tr": "TR",
                 "zh": "CN",
                 "nl": "NL",
                 "fr": "FR",
                 "it": "IT"}

def get_locale(request):
    locale_parts = request.config.getoption("--locale").split("_")
    if len(locale_parts) == 2:
        return locale_parts
    elif len(locale_parts) == 1:
        if default_locale.get(locale_parts[0], None) is None:
            raise UnknownDefaultLocaleException("Cannot find a default locale for the language: " + locale_parts[0] + " please append it to the default_locale dictionary in conftest_misc.py")
        return locale_parts[0], default_locale[locale_parts[0]]
    else:
        raise BadLocaleStrException("The locale format needs to be [language]_[region]. What was passed in is: " + request.config.getoption("--locale"))

def build_info_dict(request, _os=None):
    const = None
    system_config = ma_misc.load_system_config_file()
    try:
        project_name = pytest.app_info
    except AttributeError:
        logging.error("Please mark your class with the app you are testing ['SMART', 'HPPS', etc]")
        sys.exit()

    try:
        _os = _os if _os else pytest.platform
    except AttributeError:
        logging.error("Please mark test with a platform ['ANDROID', 'IOS', etc]")
        sys.exit()        

    lang, locale = get_locale(request)
    executor_url = system_config["executor_url"] if not request.config.getoption("--executor-url") else request.config.getoption("--executor-url")
    executor_port =  system_config["executor_port"] if not request.config.getoption("--executor-port") else request.config.getoption("--executor-port")

    info_dict = {"server": {"url": executor_url,
                                "port": executor_port},
                     "dc":{"platformName": _os.upper(),
                           "platform": _os.upper(),
                           "clearSystemFiles": True, 
                           "language": lang
                           }}

    info_dict["ga"] =request.config.getoption("--ga")

    if _os.upper() == "ANDROID":
        const = a_const
        info_dict["dc"]["locale"] = locale
        info_dict["dc"]["remoteAppsCacheLimit"] = 0
        info_dict["dc"]["automationName"] = "uiautomator2"
        info_dict["dc"]["androidInstallPath"] = "/sdcard/Download/"
        info_dict["dc"]["androidScreenshotPath"] = "/sdcard/Screenshot/"
        info_dict["dc"]["uiautomator2ServerInstallTimeout"] = 60000
        info_dict["dc"]["androidInstallTimeout"] = 180000
        info_dict["dc"]["unicodeKeyboard"] = True
        info_dict["dc"]["recreateChromeDriverSessions"] = True

        if getattr(const.OPTIONAL_INTENT_ARGUMENTS, project_name.upper(), False):
            info_dict["dc"]["optionalIntentArguments"] = getattr(const.OPTIONAL_INTENT_ARGUMENTS,
                                                                 project_name.upper())
        info_dict["dc"]["resetKeyboard"] = True

        if getattr(const.ANDROID_PROCESS, project_name.upper(), False):
            info_dict["dc"]["chromeOptions"] = {}
            info_dict["dc"]["chromeOptions"]["androidProcess"] = getattr(const.ANDROID_PROCESS, project_name.upper())

        if getattr(const.CUSTOM_CHROME_DRIVER, project_name.upper(), False):
            info_dict["dc"]["chromedriverExecutable"] = getattr(const.CUSTOM_CHROME_DRIVER, project_name.upper())

    elif _os.upper() == "IOS":
        const = i_const
        info_dict["dc"]["locale"] = lang + "_" +locale
        info_dict["dc"]["automationName"] = "XCUITest"
        info_dict["dc"]["useNewWDA"] = False
        info_dict["dc"]["waitForQuiescence"] = True
        info_dict["dc"]["showXcodeLog"] = True
        # info_dict["dc"]["webviewConnectTimeout"] = 30000
        # info_dict["dc"]["safariLogAllCommunication"] = True

    elif _os.upper() == 'MAC':
        const = m_const
        info_dict["dc"]["deviceName"] = "mac device"
        if request.config.getoption("--afm2"):
            info_dict["dc"]["automationName"] = "Mac2"
            info_dict["dc"]["showServerLogs"] = True
        else:
            info_dict["dc"]["automationName"] = "Mac"

    elif _os.upper() == "WINDOWS":
        const = w_const
        info_dict["dc"]["ms:experimental-webdriver"] = True

    if project_name.upper() not in const.NONE_THIRD_PARTY_APP.APP_LIST:
        if _os.upper() == "IOS":
            info_dict["dc"]["bundleId"] = eval("const.BUNDLE_ID." + project_name.upper())
        elif _os.upper() == "ANDROID":
            try:
                info_dict["dc"]["appWaitActivity"] = getattr(const.WAIT_ACTIVITY, project_name.upper())
            except AttributeError:
                logging.debug("Does not have a wait activity")
        info_dict["dc"]["noReset"] = True
    else:
        info_dict["dc"]["fullReset"] = True
        if _os.upper() not in ["WINDOWS", "MAC"]:
            #Adding for android and mac the ability to have package name/wait activty in a dictionary
            info_dict["dc"]["app"] = get_package_url(request, _os=_os)
            if _os.upper() == "ANDROID":
                pkg_name, act_name = get_pkg_activity_name_from_const(request, const, project_name)
                if pkg_name is not None:
                    info_dict["dc"]["appPackage"] = pkg_name
                if act_name is not None:
                    info_dict["dc"]["appActivity"] = act_name
        else:
            info_dict["dc"]["app"] = eval("const.APP_NAME." + project_name.upper())
        
    if request.config.getoption("--mobile-device") is not None:
        info_dict["dc"]["applicationName"] = request.config.getoption("--mobile-device")
    if request.config.getoption("--platform-version") is not None:
        info_dict["dc"]['platformVersion'] = request.config.getoption("--platform-version")

    info_dict["language"], info_dict["locale"] = get_locale(request)
    if request.config.getoption("--imagebank-path") is not None:
        info_dict["image_bank_root"] = request.config.getoption("--imagebank-path")
    else:
        info_dict["image_bank_root"] = system_config.get("image_bank_root")
    info_dict["bulk_image_root"]=system_config.get("bulk_image_root")
    info_dict["start_up_project"] = project_name
    info_dict["request"] = request

    return info_dict

def build_web_info_dict(request, browser_type):
    system_config = ma_misc.load_system_config_file()  
    executor_url = system_config["executor_url"] if not request.config.getoption("--executor-url") else request.config.getoption("--executor-url")
    executor_port =  system_config["executor_port"] if not request.config.getoption("--executor-port") else request.config.getoption("--executor-port")

    try:
        project_name = pytest.app_info
    except AttributeError:
        logging.error("Please mark your class with the app you are testing ['SMART', 'HPPS', etc]")
        sys.exit()
    info_dict = {"server": {"url": executor_url,
                                "port": executor_port},
                     "dc":{"platform": request.config.getoption("--platform") ,
                           }}
    info_dict["language"], info_dict["locale"] = get_locale(request)
    if request.config.getoption("--imagebank-path") is not None:
        info_dict["image_bank_root"] = request.config.getoption("--imagebank-path")
    else:
        info_dict["image_bank_root"] = system_config.get("image_bank_root")
    info_dict["bulk_image_root"]=system_config.get("bulk_image_root")
    info_dict["request"] = request
    if pytest.app_info == "ECP":
        info_dict["proxy"] = "web-proxy.austin.hpicorp.net:8080"
    return info_dict

def create_driver(request, _os):
    info_dict = build_info_dict(request, _os)
    return driver_factory.web_driver_factory(_os, info_dict)

def utility_web_driver(browser_type="chrome"):
    system_config = ma_misc.load_system_config_file()
    info_dict = {"server": {"url": system_config["web_executor_url"], "port": system_config["web_executor_port"]},
                            "dc": {"platform": "ANY"}}
    return driver_factory.web_driver_factory(browser_type, info_dict)

def create_web_driver(request):
    browser_type = request.config.getoption("--browser-type")
    info_dict = build_web_info_dict(request, browser_type)
    return driver_factory.web_driver_factory(browser_type, info_dict)

def get_package_url(request, _os=None, project=None, app_type=None,  app_build=None, app_release=None):
    system_config = ma_misc.load_system_config_file()
    custom_location = request.config.getoption("--app-location")
    if custom_location is not None:
        if ma_misc.validate_url(custom_location) or os.path.isfile(custom_location):
            if system_config.get("database_info", None) is not None:
                #If database then cache it
                app_obj = app_module_factory("ANY", "ANY", system_config["database_info"])
                return app_obj.get_build_url(custom_location)
            #If the build is local and there is no database_info then return the location
            return custom_location
        else:
            raise RuntimeError("App Location: " + custom_location + " is not a valid location")

    actual_os = _os if _os is not None else pytest.platform
    actual_project = project if project is not None else pytest.app_info
    app_obj = app_module_factory(actual_os, actual_project, system_config.get("database_info", None))

    if _os.lower() == "ANDROID".lower():
        app_type = app_type if app_type is not None else request.config.getoption("--app-type")
        app_version = request.config.getoption("--app-version")
        app_build = app_build if app_build is not None else request.config.getoption("--app-build")
        app_release = app_release if app_release is not None else  request.config.getoption("--app-release")
        return app_obj.get_build_url(build_type=app_type, build_version=app_version, build_number=app_build, release_type=app_release)


    elif _os.lower() == "IOS".lower():
        app_type = request.config.getoption("--app-type")
        app_version = request.config.getoption("--app-version")
        app_build = app_build if app_build is not None else request.config.getoption("--app-build")
        return app_obj.get_build_url(build_type=app_type, build_version=app_version, build_number=app_build)

    elif _os.lower() == "WINDOWS".lower():
        app_version = request.config.getoption("--app-version")
        return app_obj.get_build_url(build_version=app_version)

def get_session_result_folder_path(driver):
    info = driver.driver_info
    root_path = ma_misc.get_abs_path("/results", False)
    if info.get("desired", False):
        device_name = info["desired"]["deviceName"].replace(" ", "_")
    else:
        device_name = info["deviceName"].replace(" ", "_")
    dir_path = str("{}/{}/{}_{}/".format(root_path, info["platformName"].lower(),
            device_name, info.get("CONFIG_UUID", info.get("udid"))))
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return dir_path    

def get_web_session_result_folder_path(request):
    root_path = ma_misc.get_abs_path("/results", False)
    return "{}/{}/{}/{}/".format(root_path, "web", request.config.getoption("--browser-type"), request.config.getoption("--uuid"))


def get_test_result_folder_path(session_result_folder, test_class_name):
    dir_path = session_result_folder + test_class_name + "/"
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    return dir_path

def get_attachment_folder():
    #This function only works after the class scope
    path = pytest.test_result_folder + "attachment/"
    if not os.path.isdir(path):
        os.makedirs(path)
    return path

def save_printer_fp_and_publish(p, file_path):
    try:
        p.printer_screen_shot(file_path)
    except: 
        logging.warning("Could not take screenshot of printer: " + file_path)
        return False
    ma_misc.publish_to_junit(file_path)    

def save_mem_stat_and_publish(driver, root_path, file_name=None):
    data = driver.wdvr.execute_script("mobile: shell", {"command": "cat", "args":["/proc/meminfo"]})
    if file_name is None:
        file_name = "mem_stat.txt"
    file_path = root_path + file_name
    with open(file_path, "w+", encoding="utf-8") as f:
        f.write(data)
    ma_misc.publish_to_junit(file_path)

def save_screenshot_and_publish(driver, file_path):
    """
    Get screen-shot of mobile device
    :param driver:
    :param file_path:
    :return:
    """
    # This is currently not proper location need to fix later
    driver.wdvr.get_screenshot_as_file(file_path)
    ma_misc.publish_to_junit(file_path)

def save_source_and_publish(driver, root_path, file_name=None):
    if file_name is None:
        file_name = "page_source.txt"
    file_path = root_path + file_name
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(driver.wdvr.page_source)
    ma_misc.publish_to_junit(file_path)


def save_log_and_publish(driver, root_path, node_name):
    """
    Get logcat of device and save to file_path
    :param driver:
    :param root_path:
    :param node_name:
    :return:
    """
    save_file_path = "{}{}_log.txt".format(root_path, node_name)
    driver.return_device_log(save_file_path)
    ma_misc.publish_to_junit(save_file_path)

def save_app_log_and_publish(project, driver, root_path, node_name):
    try:
        zipfile = base64.b64decode(driver.wdvr.pull_folder(eval("a_const.TEST_DATA." + project + "_APP_LOG_PATH")))
        fh = open(root_path + node_name + "_app_log" + ".zip", "wb")
        fh.write(zipfile)
        fh.close()
        #Publish to junit
        ma_misc.publish_to_junit(os.path.realpath(fh.name))
    except:
        logging.warning("Unable to capture app log")

def save_ios_app_log_and_publish(fc, driver, root_path, node_name):
    try:
        zipfile = base64.b64decode(driver.wdvr.pull_folder("@com.hp.printer.control.dev:documents/" + "Logs"))
        fh = open(root_path + node_name + "_app_log" + ".zip", "wb")
        fh.write(zipfile)
        fh.close()
        ma_misc.publish_to_junit(os.path.realpath(fh.name))
    except:
        logging.warning("Unable to capture app log")

def save_video_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".mp4"
    fh = open(file_path, "wb+")
    data = driver.wdvr.stop_recording_screen()
    fh.write(base64.b64decode(data))
    fh.close()
    ma_misc.publish_to_junit(file_path)

def save_cms_results_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".json"
    if driver.session_data["context_manager_mode"] != "verify":
        logging.info("Context manager verify not activated nothing to save")
        return True
    with open(file_path, "w+", encoding="utf-8") as fh:
        json.dump(driver.session_data["context_manager_results"], fh)
    ma_misc.publish_to_junit(file_path)

def save_cms_failed_images_and_publish(driver, root_path, file_name):
    file_path = root_path + file_name + ".zip"
    file_list = []
    for key, value in driver.session_data["context_manager_failed_images"].items():
        img_file = key.replace("/", "_") + ".png"
        content = base64.b64decode(value)
        file_list.append(tuple([img_file, content]))
    if file_list == []:
        #If no failures don't post a zip file
        return True
    in_memory_zip(file_path, file_list)
    ma_misc.publish_to_junit(file_path)

def in_memory_zip(zip_file_path, content):
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
        for file_name, data in content:
            zip_file.writestr(file_name, io.BytesIO(data).getvalue())
    with open(zip_file_path, "wb") as f:
        f.write(zip_buffer.getvalue())

def get_wifi_info(request, raise_e=True):
    system_cfg = ma_misc.load_system_config_file()
    if not system_cfg.get("default_wifi", False):
        ssid = request.config.getoption("--wifi-ssid")
        password = request.config.getoption("--wifi-pass")
    else:
        ssid = request.config.getoption("--wifi-ssid") if request.config.getoption("--wifi-ssid") else system_cfg["default_wifi"]["ssid"]
        password = request.config.getoption("--wifi-pass") if request.config.getoption("--wifi-pass") else system_cfg["default_wifi"]["passwd"]

    if ssid is None or password is None:
        if raise_e:
            raise MissingWifiInfo("System config file is missing 'default_wifi' info and it's not passed in")
        else:
            return None, None

    return ssid, password

def get_pkg_activity_name_from_const(request,const, project_name):
    pkg_name = getattr(const.PACKAGE, project_name.upper())
    act_name = getattr(const.LAUNCH_ACTIVITY, project_name.upper())
    pkg_type = request.config.getoption("--app-build")
    if type(pkg_name) == dict:
        pkg_name= pkg_name.get(pkg_type, pkg_name["default"])
    if type(act_name) == dict:
        act_name= act_name.get(pkg_type, act_name["default"])
    return pkg_name, act_name

if __name__ == "__main__":
    pass