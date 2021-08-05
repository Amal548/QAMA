from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from MobileApps.resources.const.android.const import PACKAGE, LAUNCH_ACTIVITY


class DevSettings(SmartFlow):
    flow_name = "dev_settings"

    PIE_STACK = "pie_stack_cb"
    STAGE_STACK = "stage_stack_cb"
    PRODUCTION_STACK = "production_stack_cb"
    DEV_SETTINGS_TITLE = "dev_settings_title"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def open_select_settings_page(self):
        """
        Launch Select Settings Page Screen
        """
        package_name = PACKAGE.SMART.get(self.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        self.driver.start_activity(package_name, LAUNCH_ACTIVITY.SMART_DEV_SETTINGS)

    def change_stack_server(self, stack_name):
        """
        change stack server in HPC Settings
        :param stack_name: using class constant
                    - PIE_STACK
                    - STAGE_STACK
                    - PRODUCTION_STACK
        """
        self.driver.scroll("server_stack_cell", 
                            format_specifier=[self.driver.return_str_id_value("server_stack_txt")],
                            click_obj=True)
        self.driver.click(stack_name)

    def toggle_detect_leaks_switch(self, on=True):
        """
        toggle switch of Detect leaks option 
        """
        self.driver.scroll("detect_leaks_txt")
        self.driver.check_box("toggle_switch", 
                              format_specifier=[self.driver.return_str_id_value("detect_leaks_txt")],
                              uncheck= not on)

    # *********************************************************************************
    #                                VERIFY FLOWS                                     *
    # *********************************************************************************
    def verify_dev_settings_page(self,raise_e=True):
        """
        Verify the Developer settings page using page title
        """
        return self.driver.wait_for_object("dev_settings_title",raise_e=raise_e)
