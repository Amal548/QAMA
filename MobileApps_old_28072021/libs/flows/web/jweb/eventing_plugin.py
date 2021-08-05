from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
import json

class EventingPlugin(JwebFlow):
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

    def select_eventing_dispatch_open(self):
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
        self.driver.swipe(direction="up")
        self.driver.click("eventing_test_button")

    def eventing_test_result(self):
        """
        :return: eventing test result text
        """
        return self.driver.wait_for_object("eventing_test_result_txt").text

    def add_listener_multiple_event_results(self):
        """
        :return: add multiple event result text
        """
        return self.driver.wait_for_object("multiple_event_result_text").text

    def add_listener_event_result(self):
        """
        :return: add listener test result
        """
        return json.loads(self.driver.get_attribute(obj_name="add_listener_test_result_txt", attribute="value"))

    def add_listener_test_result(self):
        """
        :return: add listener test result text
        """
        self.driver.swipe(direction="down")
        return self.driver.wait_for_object("add_listener_test_result_text").text

    def select_add_listener_pop_up_close_btn(self):
        """
        clicks the add listener pop up close btn
        :return:
        """
        self.driver.click("add_listener_pop_up_close_btn")

    def get_add_listener_pop_up_toast_text(self):
        """
        :return: main and sub text found from the toast pop up notification
        """
        pop_up_toast_text = {}
        pop_up_toast_text['main_text'] = self.driver.wait_for_object("pop_up_toast_text", index=0).text
        pop_up_toast_text['sub_text'] = self.driver.wait_for_object("pop_up_toast_text", index=1).text
        return pop_up_toast_text

    def select_add_listener_test_btn(self):
        """
        clicks the add listener test btn
        :return:
        """
        self.driver.click("eventing_add_listener_btn")

    def enter_add_listener_event(self, option):
        """
        sends name of event listener in Eventing.addListener() tab
        :param option:
        :return:
        """
        self.driver.send_keys("eventing_native_element_listener_field", option)
  
    def enter_name_field(self,option):
        """
        sends the name field
        :param option:
        :return:
        """
        self.driver.send_keys("eventing_name_field", option)

    def enter_data_field(self,option):
        """
        sends the data field
        :param option:
        :return:
        """
        self.driver.send_keys("eventing_data_field", option)

    def select_jarvis_event_option_test(self):
        """
        clicks the send jarvis event test btn
        :return:
        """
        self.driver.click("eventing_send_jarvis_test_btn")

    def jarvis_event_option_test_result(self):
        """
        :return: text after clicking jarvis event option test btn
        """
        return self.driver.find_object("eventing_jarvis_options_test_result").text