from MobileApps.libs.flows.mac.jweb.jweb_flow import JwebFlow

class EventingPlugin(JwebFlow):
    project = "jweb"
    flow_name = "eventing_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_eventing_dispatch_open(self):
        """
        clicks the eventing dispatch open item
        :return:
        """
        self.driver.click("eventing_dispatch_open_item")

    def select_eventing_dispatch_close(self):
        """
        clicks the eventing dispatch close item
        :return:
        """
        self.driver.click("eventing_dispatch_close_item")

    def select_eventing_plugin_test(self):
        """
        clicks the eventing plugin test button
        :return:
        """
        self.driver.click("eventing_test_button")

    def eventing_test_result(self):
        """
        returns the eventing test result
        :return:
        """
        json_data = self.driver.find_object("eventing_test_result_txt")
        return json_data.text

    def enter_name_field(self,option):
        """
        sends the name field
        :param option:
        :return:
        """
        self.driver.send_keys("eventing_name_field", clear_text=True, content=option)

    def enter_data_field(self,option):
        """
        sends the data field
        :param option:
        :return:
        """
        self.driver.send_keys("eventing_data_field", clear_text=True, content=option)

    def verify_eventing_plugin_test(self):
        """
        verifies eventing plugin test button
        :return:
        """
        return self.driver.wait_for_object("eventing_test_button", raise_e=False)