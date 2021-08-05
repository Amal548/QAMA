import json
from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class ServicePlugin(JwebFlow):
    flow_name="service_plugin"

    def select_get_services_test_btn(self):
        """
        Click the get services test btn
        """
        self.driver.click("get_services_test_button")

    def select_get_service_availability_test_btn(self):
        """
        Click the get services availability test btn
        """
        self.driver.click("get_service_availability_test_button")

    def select_launch_service_test_btn(self):
        """
        Click the launch services test btn
        """
        self.driver.click("launch_service_test_btn", timeout=8)

    def select_get_service_instance_test_btn(self):
        """
        Click the get service instance test btn
        """
        self.driver.click("get_service_instance_test_btn")

    def select_add_listener_test_btn(self):
        """
        Click the add listener test btn
        """
        self.driver.click("service_routing_add_listener")

    def select_event_close_button(self, index=0):
        """
        Click the event close btn of the toast notification pop up
        """
        el = self.driver.find_object(obj_name="add_listener_event_close_btn", index=index)
        el.click()

    def get_service_availability_result(self):
        """
        Return JSON data found after clicking get services availability test btn
        """
        return json.loads(self.driver.find_object("get_service_availability_result_txt").text)

    def get_services_result(self):
        """
        Return JSON data found after clicking get services test btn
        """
        return json.loads(self.driver.find_object("get_services_result_txt").text)

    def get_service_launch_result(self):
        """
        Return JSON data found after clicking get service availablity test btn
        """
        return json.loads(self.driver.find_object("service_launch_result_txt").text)

    def get_service_instance_result(self):
        """
        Return JSON data found after clicking the get service instance test btn
        """
        return json.loads(self.driver.find_object("get_service_instance_result_txt").text)

    def get_service_instance_svc_id(self):
        """
        Return value found inside of get_service_isntance_svc_id entry field 
        """
        return self.driver.get_attribute(obj_name="get_service_instance_svc_id", attribute="value")

    def enter_service_availability_id(self, text):
        """
        Enter text value into service availability id
        """
        self.driver.send_keys("service_availability_service_id", text)

    def enter_service_launch_data(self, text):
        """
        Enter text value into lanch data
        """
        self.driver.send_keys("service_launch_data", text)

    def enter_get_service_instance_svc_id(self, text):
        """
        Enter text value into sergive instance svc id field
        """
        self.driver.send_keys("get_service_instance_svc_id", text)