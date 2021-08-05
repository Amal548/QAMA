from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class RetargetingData(JwebDataCollectionFlow):
    flow_name = "retargeting_data"

    def select_client_id_availability_item(self):
        """
        clicks the client advertising id availability button
        :return:
        """
        self.driver.click("get_client_advertising_id_availability_btn")

    def select_request_client_id_access_item(self):
        """
        clicks the request client id access button
        :return:
        """
        self.driver.click("request_client_advertising_id_access_btn")

    def select_goto_application_settings_item(self):
        """
        clicks the application settings button
        :return:
        """
        self.driver.click("go_to_application_settings_btn")

    def client_id_availability_response(self, index=1):
        """
        clicks the application settings button
        :return:
        """
        el = self.driver.wait_for_object("client_id_availability_response", index=2)
        return el.text

    def select_ok_pop_up_item(self):
        """
        clicks the pop up button
        :return:
        """
        if self.driver.wait_for_object("retargeting_data_ok_pop_up_btn", raise_e=False):
            self.driver.click("retargeting_data_ok_pop_up_btn")