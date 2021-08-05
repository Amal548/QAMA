from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow


class DataCollectionSettings(JwebDataCollectionFlow):
    flow_name = "data_collection_settings"

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def toggle_allow_tracking_btn(self, disable):
        """
        clicks the allow tracking button
        :return:
        """
        self.driver.check_box("allow_tracking_switch", uncheck=disable)

    def select_allow_btn(self):
        """
        clicks the allow button
        """
        if self.driver.wait_for_object("allow_btn", raise_e=False):
            self.driver.click("allow_btn")

    def toggle_printer_uuid_custom_btn(self, disable):
        """
        clicks the printer uuid custom button
        :return:
        """
        self.driver.check_box("printer_uuid_custom_switch", uncheck=disable)

    def toggle_app_instance_id_custom_btn(self, disable):
        """
        clicks the app instance id custom button
        :return:
        """
        self.driver.check_box("app_instance_id_custom_switch", uncheck=disable)

    def select_data_ingress_stack(self):
        """
        clicks the data ingress stack
        :return:
        """
        self.driver.click("data_ingress_stack_select")

    def select_pie_stack(self):
        """
        clicks the pie stack
        :return:
        """
        self.driver.click("stack_pie_select")

    def select_dev_stack(self):
        """
        clicks the dev stack
        :return:
        """
        self.driver.click("stack_dev_select")

    def select_data_collection_settings(self):
        """
        clicks the data collections settings
        :return:
        """
        self.driver.click("data_collection_settings")

    def enter_custom_printer_uuid(self, option="11111111-0000-0000-0000-000000000001"):
        """
        enters the printer custom uuid
        """
        self.driver.send_keys("printer_uuid_custom_txt_box",content=option)

    def enter_custom_app_instance_id(self, option="22222222-0000-0000-0000-000000000001"):
        """
        enters the app instance custom id
        """
        self.driver.send_keys("app_instance_id_custom_txt_box",content=option)



