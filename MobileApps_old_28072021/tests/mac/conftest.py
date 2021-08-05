import os
import pytest
import traceback

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc


pytest.platform = "MAC"
pytest.mac_os_version = os.popen("sw_vers -productVersion").read(5)


def pytest_addoption(parser):
    mac_argument_group = parser.getgroup('Mac Test Parameters')
    mac_argument_group.addoption("--mac-app-build", action="store", default="debug", help="Which app build to use [debug, release, ga] NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--mac-app-release", action="store", default="daily", help="Which app relese to use [daily, weekly] NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--afm2", action="store_true", default=False, help="Run with the afm2 driver")


# ----------------      FUNCTION     ---------------------------
@pytest.fixture(scope="session")
def mac_test_setup(request, session_setup, require_driver_session):
    """
    Test general precondition for Mac test
        + Create log file which store log of test script
        + Updating list when adding new precondition into this fixture
        + Change language

    :param request:
    """
    try:
        system_config = ma_misc.load_system_config_file()
        driver = require_driver_session

        # Change OS language and region
        # lang = request.config.getoption("--lang")

    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment + "/mac_test_setup_failed.png")
        c_misc.save_source_and_publish(driver, session_attachment + "/", file_name="mac_test_setup_failed_page_source.txt")
        traceback.print_exc()
        raise

    return driver
