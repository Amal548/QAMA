import os
import pytest
import logging
import traceback
from MobileApps.resources.const.android import const

import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.tests.android.conftest import android_test_setup
from MobileApps.libs.ma_misc.ma_misc import return_apk_cache_path
from MobileApps.libs.ma_misc.conftest_misc import get_package_url
from MobileApps.libs.flows.android.hpps.flow_container import Flow_Container

def pytest_addoption(parser):
    hpps_argument_group = parser.getgroup('HPPS Test Parameters')
    hpps_argument_group.addoption("--hpps-app-build", action = "store", default="debug", help="Which hpps build to use")

    hpps_argument_group.addoption("--hpps-app-release", action = "store", default="daily", help="Which hpps release to use")

    hpps_argument_group.addoption("--hpps-protocol", action = "store", default="Default", help="hpps protocol parameter")
    hpps_argument_group.addoption("--hpps-copies", action = "store", default="Default", help="hpps copies parameter")
    hpps_argument_group.addoption("--hpps-color", action = "store", default="Default", help="hpps color parameter")
    #Not added in jenkins
    hpps_argument_group.addoption("--hpps-paper-size", action = "store", default="Default", help="hpps pclm compress parameter")
    hpps_argument_group.addoption("--hpps-orientation", action = "store", default="Default", help="hpps orientation parameter")
    hpps_argument_group.addoption("--hpps-two-sided", action = "store", default="Default", help="hpps two sided parameter")
    hpps_argument_group.addoption("--hpps-quality", action = "store", default="Default", help="hpps quality parameter")
    hpps_argument_group.addoption("--hpps-scaling", action = "store", default="Default", help="hpps scaling parameter")
    #Not added in jenkins
    hpps_argument_group.addoption("--hpps-file-size", action = "store", default="Default", help="hpps file size parameter")
    hpps_argument_group.addoption("--hpps-borderless", action = "store", default="Default", help="hpps borderless parameter")
    hpps_argument_group.addoption("--hpps-PCLm-compress", action = "store", default="Default", help="hpps pclm compress parameter")
    # For generating specific test cases
    hpps_argument_group.addoption("--hpps-document-type", action = "store", default="Random", help="hpps non-pdf file format parameter")
    hpps_argument_group.addoption("--hpps-image-type", action = "store", default="Random", help="hpps image file format parameter")


@pytest.fixture(scope="session", autouse=True)
def hpps_setup(request, android_test_setup, require_driver_session):
    try:
        driver = require_driver_session
        driver.session_data["test_params"] = request.config.option
        driver.clear_app_cache("com.android.printspooler")

        hpps_build = request.config.getoption("--hpps-app-build")
        hpps_release = request.config.getoption("--hpps-app-release")
        driver.install_app(get_package_url(request, _os="ANDROID", project="HPPS", app_type=hpps_build, app_release= hpps_release), "HPPS", const.PACKAGE.HPPS, uninstall=True)
        driver.load_app_strings("hpps", driver.pull_package_from_device("com.android.printspooler"), driver.session_data["language"], append=True, add_array=True) 
        fc = Flow_Container(driver)
        driver.terminate_app(const.PACKAGE.SETTINGS)        
        fc.turn_on_hpps()
        fc.set_protocol()
        fc.flow["android_system"].clear_notifications()
    except:
        logging.error("HPPS_SETUP FAILED!")
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_app_log_and_publish("SMART",driver, session_attachment, request.node.name)  
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/hpps_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "hpps_setup_failed_page_source.txt")
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("HPPS_SETUP FAILED!")

    return driver, fc

# Customized parametrize based on the command line option
def pytest_generate_tests(metafunc):
    if "non_pdf_file_format" in metafunc.fixturenames:
        metafunc.parametrize("non_pdf_file_format", metafunc.config.getoption("hpps_document_type").split('+'))
    if "photo_file_format" in metafunc.fixturenames: 
        metafunc.parametrize("photo_file_format", metafunc.config.getoption("hpps_image_type").split('+'))

@pytest.fixture(scope="function", autouse=True)
def android_smart_get_app_log(request):
    driver = request.cls.driver 
    def get_app_log():
        attachment_root_path = c_misc.get_attachment_folder()
        c_misc.save_app_log_and_publish("HPPS", driver, attachment_root_path, request.node.name)  
        #Delete the folder for next test
        try:
            driver.wdvr.execute_script('mobile: shell', {'command': 'rm', 'args': ["-r", TEST_DATA.APP_LOG_PATH],'includeStderr': True})
        except Exception:
            logging.error("Cannot delete log folder for some reason !!!!")
    request.addfinalizer(get_app_log)
