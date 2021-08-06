from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class MoobeWac(SmartFlow):
    flow_name = "moobe_wac"

    def verify_accessory_setup(self, ssid, accessory_name, timeout=60):
        self.driver.wait_for_object("selected_network_name", format_specifier=[ssid], timeout=timeout)
        self.driver.wait_for_object("accessory_name_textfield", format_specifier=[accessory_name], timeout=timeout)

    def verify_setup_complete(self, timeout=60):
        self.driver.wait_for_object("setup_complete_title", timeout=timeout)
        self.driver.wait_for_object("_shared_done", clickable=True)

    def select_next(self, timeout=60):
        self.driver.wait_for_object("next_button", timeout=timeout).click()
