from MobileApps.libs.flows.android.wprint_test.wprint_test_flow import WPrintTestFlow
from MobileApps.resources.const.android import const
import time
from selenium.common.exceptions import NoSuchElementException

class WPrintTest(WPrintTestFlow):
    flow_name="wprint_test"

    def __init__(self, driver):
        super(WPrintTest, self).__init__(driver)


    def open_wprint_test(self):
        self.driver.wdvr.start_activity(const.PACKAGE.HPPS, const.LAUNCH_ACTIVITY.WPRINT_TEST)
        self.check_run_time_permission()
        self.verify_test_app_home()

    def select_print_document_via_print_system(self):
        self.driver.click("print_document_via_print_system_btn")

    def select_print_photo_via_print_system(self):
        self.driver.click("print_photo_via_print_system_btn")

    def select_print_document_via_backdoor(self):
        self.driver.click("print_document_via_backdoor_btn")

    def select_print_photo_via_backdoor(self):
        self.driver.click("print_photo_via_backdoor_btn")

    def verify_test_app_home(self):
        self.driver.wait_for_object("print_document_via_print_system_btn", timeout=10)