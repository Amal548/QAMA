import os
import pytest
import traceback

from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc


pytest.platform = "WINDOWS"

# ----------------      FUNCTION     ---------------------------

@pytest.fixture(scope="session")
def windows_test_setup(request, session_setup, require_driver_session):

    try:
        system_config = ma_misc.load_system_config_file()
        driver = require_driver_session
    except:
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/windows_test_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "windows_test_setup_failed_page_source.txt")
        traceback.print_exc()
        driver.close()
        raise
    return driver
