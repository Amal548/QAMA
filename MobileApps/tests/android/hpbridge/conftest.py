import os
import pytest
import traceback
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.resources.const.android.const import LAUNCH_ACTIVITY
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.android.hpbridge.flows.flow_container import FlowContainer
from selenium.common.exceptions import NoSuchElementException



@pytest.fixture(scope="session")
def set_default_language(request):
    request.config.option.locale = "zh"

@pytest.fixture(scope="session")
def hpbridge_test_setup(request, set_default_language, hpbridge_android_setup):
    """
    This fixture is for Android HP Smart set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest HPPS app
    :param request:
    :param hpbridge_android_setup:
    :return:
    """

    system_config = ma_misc.load_system_config_file()
    driver = hpbridge_android_setup
    fc = FlowContainer(driver)
    # wechat was slow to launch
    driver.wdvr.wait_activity(LAUNCH_ACTIVITY.HPBRIDGE, 20)

    return driver, fc


@pytest.fixture(scope="session")
def hpbridge_android_setup(request, session_setup, require_driver_session):

    try:
        driver = require_driver_session

    except NoSuchElementException:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/android_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "android_test_setup_failed_page_source.txt")
        traceback.print_exc()
        driver.close()
        raise
        #This doesn't give any reporting
        #pytest.exit("ANDROID TEST SETUP FAILED")
    return driver

