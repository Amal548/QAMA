from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow
from MobileApps.libs.ma_misc import ma_misc
import logging


class SmartFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "smart"

    def __init__(self, driver):
        super(SmartFlow, self).__init__(driver)
        self.load_smart_app_shared_ui()
        self.load_file_handle_app_strings()
        self.remove_methods_out_func_ignored_method_list()

    def load_smart_app_shared_ui(self):
        ui_map = self.load_ui_map(system="ANDROID", project="smart", flow_name="shared_obj")
        self.driver.load_ui_map("smart", "shared_obj", ui_map)
        return True

    def load_file_handle_app_strings(self):
        """
        Add Files app string into string table of smart app
        """
        lang = self.driver.session_data["language"]
        locale = self.driver.session_data["locale"]
        self.driver.load_app_strings(self.project, ma_misc.get_apk_path("documentsui"), lang if locale is None else lang + "_" + locale, append=True)

    def remove_methods_out_func_ignored_method_list(self):
        """
        Remove some methods which are in function ignored method list
        """
        methods_list = ["check_run_time_permission", "is_app_permission_popup"]
        for m in methods_list:
            self.func_ignore_methods.remove(m)

    def check_run_time_permission_photo_ga(self, accept=True):
        """
        Allow App Permission alert if it displays on the screen for Marshmallow or N device
        """

        if int(self.driver.driver_info["platformVersion"][0]) < 6:
            logging.info("Device's OS Version(" + self.driver.driver_info["platformVersion"] + ") does NOT have run time permission")
            return True

        while self.driver.wait_for_object("_shared_photo_permission_popup_ga", timeout=5, interval = 1, raise_e=False):
            logging.info("Permission popup found with text: " + self.driver.find_object("_system_app_permission_popup").text)
            if accept:
                self.driver.click("_shared_photo_permission_allow_btn_ga")
            else:
                self.driver.click("_shared_photo_permission_deny_btn_ga")

    def skip_are_you_sure_popup(self, is_yes=True):
        """
        Skip Are you sure? popup when it displayed
        # This one is for click device back button on Welcome screen. Moved to SmartFlow which required by Jay
        """
        self.driver.wait_for_object("_shared_are_you_sure_popup_title")
        button = "_shared_are_you_sure_popup_yes_btn" if is_yes else "_shared_are_you_sure_popup_no_btn"
        self.driver.click(button)
        

