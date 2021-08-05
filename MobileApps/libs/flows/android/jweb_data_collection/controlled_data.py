from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
from time import sleep

class ControlledData(JwebDataCollectionFlow):
    flow_name = "controlled_data"

    def select_data_refresh_button(self):
        """
        clicks the data refresh button
        :return:
        """
        self.driver.click("controlled_data_refresh_btn")
        sleep(4)

    def select_printer_warning_button(self):
        """
        clicks the controlled_data_warning_btn
        :return:
        """
        self.driver.click("controlled_data_warning_btn")

    def get_printer_id(self):
        """
        :return the printer id result
        """
        return self.driver.get_attribute("printer_id", "text")

    def get_application_id(self):
        """
        :return the printer id result
        """
        return self.driver.get_attribute("application_id", "text")

    def get_associated_device_product_number(self):
        """
        :return the associated_device_product_number
        """
        return self.driver.get_attribute("associated_device_product_number", "text")

    def get_associated_device_uuid(self):
        """
        :return the associated_device_uuid
        """
        return self.driver.get_attribute("associated_device_uuid", "text")

    def get_associated_stratus_user_uuid(self):
        """
        :return the associated_stratus_user_uuid
        """
        return self.driver.get_attribute("associated_stratus_user_uuid", "text")

    def get_app_caid(self):
        """
        :return the app_caid
        """
        return self.driver.get_attribute("app_caid", "text")

    def get_app_name(self):
        """
        :return the app_name
        """
        return self.driver.get_attribute("app_name", "text")

    def get_app_package_deployed_uuid(self):
        """
        :return the app_package_deployed_uuid
        """
        return self.driver.get_attribute("app_package_deployed_uuid", "text")

    def get_app_package_id(self):
        """
        :return the printer id result
        """
        return self.driver.get_attribute("app_package_id", "text")

    def get_behavior_click(self):
        """
        :return the behavior_click
        """
        return self.driver.get_attribute("behavior_click", "text")

    def get_app_version(self):
        """
        :return the app_version
        """
        return self.driver.get_attribute("app_version", "text")

    def get_os_architecture(self):
        """
        :return the os_architecture
        """
        return self.driver.get_attribute("os_architecture", "text")

    def get_os_country_region(self):
        """
        :return the os_country_region
        """
        return self.driver.get_attribute("os_country_region", "text")

    def get_printer_id_result(self):
        """
        :return the printer id result
        """
        return self.driver.get_attribute("printer_id", "text")

    def get_os_language(self):
        """
        :return the os_language
        """
        return self.driver.get_attribute("os_language", "text")

    def get_os_name(self):
        """
        :return the os_name
        """
        return self.driver.get_attribute("os_name", "text")

    def get_os_platform(self):
        """
        :return the os_platform
        """
        return self.driver.get_attribute("os_platform", "text")

    def get_os_screen_resolution(self):
        """
        :return the os_screen_resolution
        """
        return self.driver.get_attribute("os_screen_resolution", "text")

    def get_os_version(self):
        """
        :return the printer id result
        """
        return self.driver.get_attribute("os_version", "text")

    def get_sys_architecture(self):
        """
        :return the sys_architecture
        """
        return self.driver.get_attribute("sys_architecture", "text")

    def get_sys_battery_enabled(self):
        """
        :return the sys_battery_enabled
        """
        return self.driver.get_attribute("sys_battery_enabled", "text")

    def get_sys_category(self):
        """
        :return the sys_category
        """
        return self.driver.get_attribute("sys_category", "text")

    def get_sys_manufacturer(self):
        """
        :return the sys_manufacturer
        """
        return self.driver.get_attribute("sys_manufacturer", "text")

    def get_sys_model_name(self):
        """
        :return the sys_model_name
        """
        return self.driver.get_attribute("sys_model_name", "text")

    def get_sys_sku(self):
        """
        :return the sys_sku
        """
        return self.driver.get_attribute("sys_sku", "text")

    def get_sys_touch_enabled(self):
        """
        :return the sys_touch_enabled
        """
        return self.driver.get_attribute("sys_touch_enabled", "text")

    def get_sysUuid(self):
        """
        :return the sysUuid
        """
        return self.driver.get_attribute("sysUuid", "text")

    def verify_printer_warning_button(self):
        """
        verifies the controlled_data_warning_btn
        :return:
        """
        return self.driver.wait_for_object("controlled_data_warning_btn", raise_e=False)