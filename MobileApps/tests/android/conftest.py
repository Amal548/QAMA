import os
import pytest
import traceback

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.morelangs.morelangs import MoreLangs
from android_settings.src.libs.android_system_flow_factory import android_system_flow_factory


pytest.platform = "ANDROID"

def pytest_addoption(parser):
    android_argument_group = parser.getgroup('Android Test Parameters')
    android_argument_group.addoption("--app-type", action="store", default="debug", help="The type of app you would like to run")
    android_argument_group.addoption("--app-build", action="store", default=None, help="The build number of the app you would like to run")
    android_argument_group.addoption("--app-version", action="store", default=None, help="The app version you would like to run")
    android_argument_group.addoption("--app-release", action = "store", default="daily", help="Which app relese to use daily or stable")

# ----------------      FUNCTION     ---------------------------

@pytest.fixture(scope="session")
def android_test_setup(request, session_setup, require_driver_session):
    """
    Test general precondition for Android test
        + Create log file which store log of test script
        + Updating list when adding new precondition into this fixture
        + Change language
        + Change wifi to default wifi
        + Install and get string table of latest HPPS for Android SMART
    Test general post test for Android test:
        + Delete all Gmail from inbox
        + Updating list when adding new precondition into this fixture
    :param request:
    """
    try:
        system_config = ma_misc.load_system_config_file()
        driver = require_driver_session
        driver.press_key_home()

    # Change wifi
        ssid = request.config.getoption("--wifi-ssid") if request.config.getoption("--wifi-ssid") else system_config["default_wifi"]["ssid"]
        passwd = request.config.getoption("--wifi-pass") if request.config.getoption("--wifi-pass") else system_config["default_wifi"]["passwd"]
        android_system = android_system_flow_factory(driver)
        android_system.change_wifi(ssid, passwd, connect_timeout=60)
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/android_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "android_test_setup_failed_page_source.txt")
        traceback.print_exc()
        raise
        #This doesn't give any reporting
        #pytest.exit("ANDROID TEST SETUP FAILED")
    return driver

@pytest.fixture(scope="function", autouse=True)
def android_cleanup_popup(request):
    """
    Clean up all following popup before and after executing each test:
        - App crash
    """
    driver = request.cls.driver

    # Dismiss popups at setup
    android_system = android_system_flow_factory(driver)
    android_system.dismiss_app_crash_popup()