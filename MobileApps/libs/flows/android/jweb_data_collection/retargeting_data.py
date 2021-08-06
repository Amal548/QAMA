from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

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

    def select_open_ads_settings_item(self):
        """
        clicks the open ads settings button
        :return:
        """
        self.driver.click("open_ads_settings_btn")

    def select_reset_adv_id_btn(self, index=1):
        """
        clicks the reset adv id button
        :return:
        """
        self.driver.click("reset_advertising_id_btn")

    def select_navigate_up_btn(self):
        """
        clicks the nav up button
        :return:
        """
        self.driver.click("navigate_up_btn")

    def select_ok_pop_btn(self):
        """
        clicks the ok pop up button
        :return:
        """
        if self.driver.wait_for_object("ok_pop_up_btn", raise_e=False):
            self.driver.click("ok_pop_up_btn")

    def toggle_opt_out_ads_switch(self, disable):
        """
        clicks the pop up button
        :return:
        """
        self.driver.check_box("opt_out_ads_personalization_switch", uncheck=disable)
        self.select_ok_pop_btn()

    def client_id_availability_response(self):
        """
        clicks the application settings button
        :return:
        """
        el = self.driver.wait_for_object("client_id_availability_response")
        return el.text