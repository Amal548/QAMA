from MobileApps.libs.flows.ios.jweb_data_collection.jweb_data_collection_flow import JwebDataCollectionFlow
import json


class DataCollection(JwebDataCollectionFlow):
    flow_name = "data_collection"

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def select_send_ui_event_item(self):
        """
        clicks the send ui event button
        :return:
        """
        self.driver.click("send_ui_event_btn")

    def select_send_sys_info_event_item(self):
        """
        clicks the send sys info event button
        :return:
        """
        self.driver.click("send_sys_info_event_btn")

    def toggle_activity_btn(self, disable):
        """
        clicks the activity toggle button
        :return:
        """
        self.driver.check_box("activity_toggle_btn", uncheck=disable)

    def toggle_screenpath_btn(self, disable):
        """
        clicks the screenpath toggle button
        :return:
        """
        self.driver.check_box("screenpath_toggle_btn", uncheck=disable)

    def toggle_screenmode_btn(self, disable):
        """
        clicks the activity toggle button
        :return:
        """
        self.driver.check_box("screenmode_toggle_btn", uncheck=disable)

    def toggle_control_name_btn(self, disable):
        """
        clicks the screenpath toggle button
        :return:
        """
        self.driver.check_box("control_name_toggle_btn", uncheck=disable)

    def toggle_control_detail_btn(self, disable):
        """
        clicks the activity toggle button
        :return:
        """
        self.driver.check_box("control_detail_toggle_btn", uncheck=disable)

    def select_send_item(self):
        """
        clicks the send button
        :return:
        """
        self.driver.click("send_btn")

    def select_share_item(self):
        """
        clicks the share button
        :return:
        """
        self.driver.click("share_btn")

    def select_data_collection_services_item(self):
        """
        clicks the data collection services button
        :return:
        """
        self.driver.click("data_collection_services_btn")

    def send_ui_event_result(self):
        """
        :return the send ui event result
        """
        el = self.driver.find_object("data_collection_send_ui_event_response")
        return json.loads(el.text)

    def send_ui_event_result_mim(self):
        """
        :return the send ui event result
        """
        return self.driver.get_attribute("data_collection_send_ui_event_response", "value")

    def send_sys_info_event_result(self):
        """
        :return the send sys info event result
        """
        return self.driver.get_attribute("data_collection_send_sys_info_event_response", "value")

    def enter_action_name(self, option):
        """
        sends the action name
        :param option:
        :return:
        """
        self.driver.send_keys("action_name_txt_bx", option)

    def enter_screen_name(self, option):
        """
        sends the screen name
        :param option:
        :return:
        """
        self.driver.send_keys("screen_name_txt_bx", option)

    def enter_activity_name(self, option):
        """
        sends the activity name
        :param option:
        :return:
        """
        self.driver.send_keys("activity_txt_bx", option)

    def enter_screen_path(self, option):
        """
        sends the screen path
        :param option:
        :return:
        """
        self.driver.send_keys("screenpath_txt_bx", option)

    def enter_screen_mode(self, option):
        """
        sends the screen mode
        :param option:
        :return:
        """
        self.driver.send_keys("screenmode_txt_bx", option)

    def enter_control_name(self, option):
        """
        sends the control name
        :param option:
        :return:
        """
        self.driver.send_keys("control_name_txt_bx", option)

    def enter_control_detail(self, option):
        """
        sends the control detail
        :param option:
        :return:
        """
        self.driver.send_keys("control_detail_txt_bx", option)
