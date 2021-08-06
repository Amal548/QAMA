# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on WiFi network problem dialog

@author: Ivan
@create_date: Aug 28, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class WiFiNetworkProblemDialog(SmartScreens):

    folder_name = "oobe"
    flow_name = "wifi_network_problem_dialog"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(WiFiNetworkProblemDialog, self).__init__(driver)

# -------------------------------Operate Elements----------------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait welcome screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("you_are_connected_to_content", timeout=timeout, raise_e=raise_e)

    def click_network_btn(self):
        '''
        This is a method to click network button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_network_btn]-Click network_btn.. ")

        self.driver.click("network_btn")

    def click_change_connection_btn(self):
        '''
        This is a method to click change connection button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_change_connection_btn]-Click change_connection_btn.. ")

        self.driver.click("change_connection_btn")

    def click_continue_btn(self):
        '''
        This is a method to click continue button.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[click_continue_btn]-Click continue_btn.. ")

        self.driver.click("continue_btn")

    def get_value_of_title(self):
        '''
        This is a method to get the value of dialog title.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_title]-Get the value of title...  ")

        return self.driver.get_value("wifi_network_problem_title")

    def get_value_of_you_are_connected_to_content(self):
        '''
        This is a method to get the value of you_are_connected_to_content.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_you_are_connected_to_content]-Get the contents of you_are_connected_to_content...  ")

        return self.driver.get_value("you_are_connected_to_content")

    def get_value_of_wifi_network_problem_content_1_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_1.
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_1]-Get the contents of wifi_network_problem_content_1_1...  ")

        return self.driver.get_value("wifi_network_problem_content_1_1")

    def get_value_of_wifi_network_problem_content_1_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_2]-Get the contents of wifi_network_problem_content_1_2...  ")

        return self.driver.get_value("wifi_network_problem_content_1_2")

    def get_value_of_wifi_network_problem_content_1_3(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_3
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_3]-Get the contents of wifi_network_problem_content_1_3...  ")

        return self.driver.get_value("wifi_network_problem_content_1_3")

    def get_value_of_wifi_network_problem_content_1_4(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_4
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_4]-Get the contents of wifi_network_problem_content_1_4...  ")

        return self.driver.get_value("wifi_network_problem_content_1_4")

    def get_value_of_wifi_network_problem_content_1_5(self):
        '''
        This is a method to get the value of wifi_network_problem_content_1_5
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_1_5]-Get the contents of wifi_network_problem_content_1_5...  ")

        return self.driver.get_value("wifi_network_problem_content_1_5")

    def get_value_of_network_btn(self):
        '''
        This is a method to get the value of network_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_network_btn]-Get the contents of network_btn...  ")

        return self.driver.get_title("network_btn")

    def get_value_of_or_content(self):
        '''
        This is a method to get the value of or_content
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_or_content]-Get the contents of or_content...  ")

        return self.driver.get_value("or_content")

    def get_value_of_wifi_network_problem_content_2_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_1
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_1]-Get the contents of wifi_network_problem_content_2_1...  ")

        return self.driver.get_value("wifi_network_problem_content_2_1")

    def get_value_of_wifi_network_problem_content_2_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_2]-Get the contents of wifi_network_problem_content_2_2...  ")

        return self.driver.get_value("wifi_network_problem_content_2_2")

    def get_value_of_wifi_network_problem_content_2_3(self):
        '''
        This is a method to get the value of wifi_network_problem_content_2_3
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_2_3]-Get the contents of wifi_network_problem_content_2_3...  ")

        return self.driver.get_value("wifi_network_problem_content_2_3")

    def get_value_of_change_connection_btn(self):
        '''
        This is a method to get the value of change_connection_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_change_connection_btn]-Get the contents of change_connection_btn...  ")

        return self.driver.get_title("change_connection_btn")

    def get_value_of_wifi_network_problem_content_3_1(self):
        '''
        This is a method to get the value of wifi_network_problem_content_3_1
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_3_1]-Get the contents of wifi_network_problem_content_3_1...  ")

        return self.driver.get_value("wifi_network_problem_content_3_1")

    def get_value_of_wifi_network_problem_content_3_2(self):
        '''
        This is a method to get the value of wifi_network_problem_content_3_2
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_wifi_network_problem_content_3_2]-Get the contents of wifi_network_problem_content_3_2...  ")

        return self.driver.get_value("wifi_network_problem_content_3_2")

    def get_value_of_continue_btn(self):
        '''
        This is a method to get the value of continue_btn
        :parameter:
        :return:
        '''
        logging.debug("[WiFiNetworkProblemDialog]:[get_value_of_continue_btn]-Get the contents of continue_btn...  ")

        return self.driver.get_title("continue_btn")

#  -------------------------------Verification Methods------------------------
    def verify_wifi_network_problem_ui_string(self):
        '''
        verify_ui_string
        :parameter:
        :return:
        '''
        logging.debug("Verify strings are translated correctly and matching string table.")
#         assert self.get_value_of_contents_1() == u''
#         assert self.get_value_of_contents_3() == u''
#         assert self.get_value_of_contents_4() == u''
#         assert self.get_value_of_contents_5() == u''
#         assert self.get_value_of_contents_6() == u''
#         assert self.get_value_of_contents_7() == u''
