'''
Created on May 8, 2019
@author: Sophia
'''
import pytest
import os
import logging
import traceback

import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import TEST_DATA
from MobileApps.libs.flows.mac.smart.flows.flows_common import CommonFlows
from MobileApps.libs.flows.mac.system.flows.flows_system import SystemFlows


@pytest.fixture(scope="session", autouse=True)
def mac_smart_setup(mac_test_setup):
    """
    This fixture is for Mac HP Smart set up :
        - Get driver instance
        - Get Common_Flows instance
        - Clean up HP Smart folder
        - Install latest App
    :param mac_test_setup:
    :return:
    """
    try:
        driver = mac_test_setup
        common_flows = CommonFlows(driver)

        # Clean up hp smart folder
        file_path = ma_misc.load_json_file(TEST_DATA.MAC_SMART_APP_INFO)["mac_smart"]["app_log_file"]["file_path"]
        smart_utility.delete_all_files(os.path.expanduser(file_path))

        # Clean up and delete all installed printers
        system_flows = SystemFlows(driver)
        system_flows.delete_all_printers_and_fax()

        # Install App

    except:
        logging.error("MAC_SMART_SETUP FAILED!")
        session_attachment = pytest.session_result_folder + "session_attachment"
        os.makedirs(session_attachment)
        c_misc.save_screenshot_and_publish(driver, session_attachment+ "/mac_smart_setup_failed.png")
        c_misc.save_source_and_publish(driver,  session_attachment+ "/", file_name = "mac_smart_setup_failed_page_source.txt")
        driver.close()
        traceback.print_exc()

    return driver, common_flows, system_flows
