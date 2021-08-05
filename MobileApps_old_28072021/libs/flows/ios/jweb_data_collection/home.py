from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow

class Home(JwebDataCollectionFlow):
    flow_name = "home"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_data_collection_item(self):
        """
        clicks the data collection button
        :return:
        """
        self.driver.click("data_collection_btn")

    def select_retargeting_data_item(self):
        """
        clicks the retargeting data button
        :return:
        """
        self.driver.click("retargeting_data_btn")

    def select_controlled_data_item(self):
        """
        clicks the controlled data button
        :return:
        """
        self.driver.click("controlled_data_btn")

    def select_weblet_item(self):
        """
        clicks the weblet button
        :return:
        """
        self.driver.click("weblet_btn")

########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################
