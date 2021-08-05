from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
import json

class DevicePlugin(JwebFlow):
    flow_name = "device_plugin"

    def press_device_info_test_btn(self):
        """
        presses the test button under Device.getInfo()
        :return:
        """
        self.driver.click("device_info_test_btn")

    def return_device_info(self):
        """
        :return: text result text under Device.getInfo() 
        """
        return json.loads(self.driver.wait_for_object("device_info_test_result").text)

    def press_language_test_btn(self):
        """
        presses the test button under Device.getLanguageCode()
        :return:
        """
        self.driver.click("language_code_test_btn")

    def return_language_test_result(self):
        """
        :return: text result text under Device.getLanguageCode() 
        """
        return json.loads(self.driver.wait_for_object("language_test_result").text)
