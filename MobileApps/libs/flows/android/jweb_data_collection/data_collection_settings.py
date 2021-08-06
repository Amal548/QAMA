from MobileApps.libs.flows.android.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow


class DataCollectionSettings(JwebDataCollectionFlow):
    flow_name = "data_collection_settings"

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def select_reset_btn(self):
        """
        clicks the reset button
        """
        self.driver.click("reset_btn")

    def select_save_btn(self):
        """
        clicks the save button
        """
        self.driver.click("save_btn")

    def enter_custom_printer_uuid(self, option="11111111-0000-0000-0000-000000000001"):
        """
        enters the printer custom uuid
        """
        self.driver.send_keys("printer_uuid_custom_txt_box", content=option)

    def enter_custom_app_instance_id(self, option="22222222-0000-0000-0000-000000000001"):
        """
        enters the app instance custom id
        """
        self.driver.send_keys("app_instance_id_custom_txt_box", content=option)
