from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.wprint_debug_enabler.wprint_debug_enabler_flow import WPrintDebugEnablerFlow


class WPrintDebugEnabler(WPrintDebugEnablerFlow):
    flow_name="wprint_debug_enabler"

    def __init__(self, driver):
        super(WPrintDebugEnabler, self).__init__(driver)

    def launch_wprint_debug_enabler(self):
        self.driver.wdvr.start_activity(const.PACKAGE.WPRINT_DEBUG, const.LAUNCH_ACTIVITY.WPRINT_DEBUG)
        self.allow_access_alert()

    def enable_hp_print_service_plugin(self):
        """Enable HP Print Service Plugin"""
        self.driver.click("hp_print_service_plugin")

    def enable_wprint_test_app(self):
        """Enable wPrintTestApp"""
        self.driver.click("wprint_test_app")

    def allow_access_alert(self):
        """Allow wPrint Debug to access photos, media, and files on your device"""
        if self.driver.wait_for_object("permission_message", timeout=5, raise_e=False) is not False:
            self.driver.click("permission_allow_button")