import os
import sys
import uuid
import json
import base64
import shutil
import pytest
import traceback
import logging
import logging.config

from time import sleep
from SAF.misc import saf_misc
from SPL.driver import driver_factory
from datetime import datetime, timedelta
from MobileApps.libs.ma_misc import ma_misc

from SPL.driver.reg_printer import PrinterNotReady
import MobileApps.libs.ma_misc.conftest_misc as c_misc
import MobileApps.resources.const.ios.const as i_const
from MobileApps.libs.ma_misc.conftest_exceptions import *
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.android.android_flow import android_system_ui_flow
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory

if (sys.version_info < (3, 0)):
     # Python 2 code in this block
    str = unicode

def pytest_addoption(parser):
    test_option = parser.getgroup("Test Parameters")
    test_option.addoption("--executor-url", action="store", default=False, help="Overload executor-url in system_config.json")
    test_option.addoption("--executor-port", action="store", default=False, help="Overload executor-port in system_config.json")
    test_option.addoption("--locale", action="store", default="en", help="Locale of the test")
    test_option.addoption("--stack", action="store", default="pie", help="Which stack to run the test on")
    test_option.addoption("--mobile-device", action="store", help="Which phone to test")
    test_option.addoption("--platform-version", action="store", help="Test on a specific platform version")
    test_option.addoption("--app-location", action="store", default=None, help="DEBUG PURPOSE ONLY pass in a file path to something local or an url")
    test_option.addoption("--printer-model", action="store", default=None, help="Which printer model to test with")   
    test_option.addoption("--printer-serial", action="store", default=None, help="Printer Serial Number (FOR DEBUGGING ONLY DO NOT USE FOR PRODUCTION CODE)")   
    test_option.addoption("--ga", action="store_true", default=False, help="Enable the GA module in SAF")
    test_option.addoption("--log-type", action="store", default=None, help="log type [debug/info/None] which will be displayed in log file")
    test_option.addoption("--wifi-ssid", action="store", default=None, help="The ssid used by the test")
    test_option.addoption("--wifi-pass", action="store", default=None, help="The password for the default ssid")
    test_option.addoption("--skip-power-cycle-printer", action="store_true", default=False, help="Whether to powercycle or not")
    test_option.addoption("--printer-mech", action="store_true", default=False, help="Set printer mech mode")
    test_option.addoption("--capture-video", action="store_true", default=False, help="Enable video capture")
    test_option.addoption("--context-manager", action="store", default=False, help="Options[False: disabled, 'gather': gather the ss, 'verify': validate screenshots against golden]")
    test_option.addoption("--ss-sequence", action="store_true", default=False, help="Adding a number sequence to the screenshot that is gathered by the context manager")
    test_option.addoption("--imagebank-path", action="store", default=None, help="Root path of image bank, should use system config as default")
    test_option.addoption("--email-verification", action="store_true", default=False, help="To toggle on/off email verification, default is off")
    test_option.addoption("--performance", action="store_true", default=False, help="To toggle on/off performance testing")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return

# ------------------------      SESSION SCOPE       ---------------------------------

@pytest.fixture(scope="session")
def require_driver_session(request, record_testsuite_property):

    #Fixture only for driver instantiation.
    #NOTHING ELSE GOES IN HERE
    try:
        os = pytest.platform
        driver = c_misc.create_driver(request, os)
        record_testsuite_property("suite_test_platform_version", driver.platform_version)
    except:
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("REQUIRE_DRIVER_SESSION FAILED")        
    return driver

@pytest.fixture(scope="session")
def require_web_session(request):
    try:
        driver = c_misc.create_web_driver(request)
    except:
        traceback.print_exc()
        raise
    return driver

@pytest.fixture(scope="session")
def load_printers_session(request):
    """
     Load printer object.
        - Power cycle printer for new execution of test if type is pdu
        - Check whether printer is ready for testing
        - Connect printer to target network (from argument or in system_config.json - default value)
    Note: in config/system_config.json, comment out the "printer_power_config" that are not used.
                                        pcs_url should be "pcs://<ip>:<port>"
    :param request:
     :return:
    """
    system_cfg = ma_misc.load_system_config_file()
    pp_info = system_cfg["printer_power_config"]
    if pp_info["type"] == "manual":
        if request.config.getoption("--printer-serial") is None:
            raise ManualPrinterError("You need to pass in --printer-serial parameter for manual printer power setup")
        p = driver_factory.printer_driver_factory("pcs://{}:8779/{}".format(pp_info["pcs_url"],
                                                                request.config.getoption("--printer-serial")),
                                                    pp_info,
                                                  queue_time=30,
                                                  mech=request.config.getoption("--printer-mech"),
                                                  power_cycle_printer= False)
    else:        
        db_info = system_cfg.get("database_info", None)
        if db_info is None:
            raise PDUPrinterError("You need the section 'database_info' in the system_cfg file for a PDU power setup")
        p = driver_factory.get_printer(pp_info,
                                       printer_serial=request.config.getoption("--printer-serial"),
                                       product_name=request.config.getoption("--printer-model"),
                                       printer_feature=getattr(pytest, "printer_feature", {}),
                                       db_info = db_info,
                                       mech=request.config.getoption("--printer-mech"),
                                       power_cycle_printer= not request.config.getoption("--skip-power-cycle-printer"))

    if not p.is_printer_status_ready(timeout=120):
        raise PrinterNotReady("Printer with serial: " + str(p.get_printer_information()["serial number"]) + " have status: " + str(p.get_printer_status()))
    p_info = p.get_printer_information()

    ssid, passwd = c_misc.get_wifi_info(request, raise_e=False)
    if ssid is None or passwd is None:
        logging.info("Wifi info was not provided skipping putting the printer on the wifi network")
        return p
    else:
        if not p.connect_to_wifi(ssid, passwd):
            raise PrinterNotReady("Print with Serial #: " + str(p_info["serial number"]) +  " cannot connect to wifi: " + ssid + " password: " + passwd)
        # Print printer information
        logging.info("Printer Information:\n {}".format(p_info))
        return p

@pytest.fixture(scope="session")
def prep_results_folder(request):
    if not os.path.isdir(ma_misc.get_abs_path("/results")):
        os.mkdir(ma_misc.get_abs_path("/results"))   
    return True

@pytest.fixture(scope="session")
def session_setup(request, prep_results_folder, require_driver_session):
    driver = require_driver_session
    pytest.session_result_folder = c_misc.get_session_result_folder_path(driver)
    ma_misc.delete_content_of_folder(pytest.session_result_folder)
    logging.info("Session Results Folder: " + pytest.session_result_folder)
    return driver

@pytest.fixture(scope="session")
def web_session_setup(request, prep_results_folder, require_web_session):
    driver = require_web_session
    pytest.session_result_folder = c_misc.get_web_session_result_folder_path(request)
    ma_misc.delete_content_of_folder(pytest.session_result_folder+".." , time_delta=timedelta(days=7), everything=False, recreate=False)
    ma_misc.create_dir(pytest.session_result_folder)
    return driver

# ------------------------ Class Scope --------------------------- #

@pytest.fixture(scope="class", autouse=True)
def global_class_setup(request):
    pytest.test_result_folder = test_result_folder = c_misc.get_test_result_folder_path(pytest.session_result_folder, request.cls.__name__)
    config_logging(request, test_result_folder)
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

# ------------------------      FUNCTION SCOPE      ---------------------------------
@pytest.fixture(scope="function", autouse=True)
def test_case_clean_up(request):
    driver = request.cls.driver
    if pytest.platform.lower() == "android":
        android_system_flow = android_system_ui_flow(driver)
        android_system_flow.check_run_time_permission(accept=False)
        driver.press_key_home()

    def clean_up():
        attachment_root_path = c_misc.get_attachment_folder()
        if request.node.rep_call.failed:
            logging.error("Test failed cleaning up...")
            sleep(1)
            try:
                p = request.cls.p
            except AttributeError:
                logging.warning("Cannot find printer object in class")
            else:
                logging.debug("Printer object found in class take printer front panel image")
                try:
                    c_misc.save_printer_fp_and_publish(p, attachment_root_path + "/" + p.get_printer_information()[
                        "serial number"] + "_front_panel" + ".png")
                except:
                    logging.warning("Printer front panel capture failed!")

            if pytest.platform.lower() == "web":
                driver.wdvr.switch_to.default_content()

            if driver.driver_class == "selenium":
                for window, _ in driver.session_data["window_table"].items():
                    driver.switch_window(window)
                    logging.debug("Window: " + str(window) + " URL: " + driver.current_url)
                    c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source_{}.txt".format(window))
                    c_misc.save_screenshot_and_publish(driver,
                                               "{}/screenshot_{}_{}.png".format(attachment_root_path, request.node.name, window))
            else:
                try:
                    c_misc.save_source_and_publish(driver, attachment_root_path)
                    c_misc.save_screenshot_and_publish(driver,
                                               "{}/screenshot_{}.png".format(attachment_root_path, request.node.name))
                except WebDriverException:
                    if driver.context != "NATIVE_APP":
                        logging.info("Webview teardown capture failed, switching to native")
                        driver.switch_to_webview(webview_name="NATIVE_APP")
                        c_misc.save_source_and_publish(driver, attachment_root_path)
                        c_misc.save_screenshot_and_publish(driver,
                                               "{}/screenshot_{}.png".format(attachment_root_path, request.node.name))                        

            if pytest.platform.lower() in ["android", "ios"]:
                driver.switch_to_webview(webview_name="NATIVE_APP")
                c_misc.save_log_and_publish(driver, attachment_root_path, request.node.name)

                # Dismiss app crash popup for android platform. It is in this fixture because it is following capturing screen-shot
                if pytest.platform.lower() == "android":
                    c_misc.save_mem_stat_and_publish(driver, attachment_root_path)
                    android_system = android_system_flow_factory(driver)
                    android_system.dismiss_app_crash_popup()
                    

    request.addfinalizer(clean_up)
    return True

@pytest.fixture(scope="class", autouse=True)
def save_cms_results(request):
    def save_results():
        driver = request.cls.driver
        if driver.session_data["context_manager_mode"] == "verify":
            attachment_root_path = c_misc.get_attachment_folder()
            c_misc.save_cms_results_and_publish(driver, attachment_root_path, "cms_results")
            c_misc.save_cms_failed_images_and_publish(driver, attachment_root_path, "cms_failed_img")
    request.addfinalizer(save_results)

@pytest.fixture(scope="function", autouse=True)
def capture_video(request):
    attachment_root_path = pytest.test_result_folder + "attachment/"
    if request.config.getoption("--capture-video"):
        request.cls.driver.wdvr.start_recording_screen(videoType="mpeg4", timeLimit=600)
        logging.debug("Started video record")
        def stop_video():
            if request._parent_request.scope == "session":
                file_name = request._parent_request.fixturename
            elif request._parent_request.scope == "function":
                file_name = request.node.name
            c_misc.save_video_and_publish(request.cls.driver, attachment_root_path, file_name)
            logging.debug("Stopped video record")
        request.addfinalizer(stop_video)

@pytest.fixture(scope="session", autouse=True)
def inject_data_to_junit(request, record_testsuite_property):
    record_testsuite_property("suite_test_stack", request.config.getoption("--stack"))
    record_testsuite_property("performance", request.config.getoption("--performance"))
    record_testsuite_property("suite_test_platform", pytest.platform)
    record_testsuite_property("suite_test_client", getattr(pytest, "app_info", None))

# ---------------------- Utility --------------------#
def config_logging(request, test_result_folder):
    if test_result_folder[-1] != "/":
        test_result_folder += "/"
    log_path = test_result_folder + "log/logging.log"

    if not os.path.isdir("/".join(log_path.split("/")[:-1])):
        os.makedirs("/".join(log_path.split("/")[:-1]))

    ma_misc.create_file(log_path)
    logging.config.fileConfig(ma_misc.get_abs_path("/config/logging.cfg"),
                              defaults={"log_file_name": log_path})
    log_types = {"debug": logging.DEBUG, "info": logging.INFO}
    log_type = request.config.getoption("--log-type")
    logging.getLogger().setLevel(log_types[log_type] if log_type else logging.NOTSET)