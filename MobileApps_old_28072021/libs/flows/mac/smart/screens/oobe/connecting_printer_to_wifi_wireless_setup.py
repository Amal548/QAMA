# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connecting printer to WiFi... screen
@author: ten
@create_date: Aug 21, 2019
'''

import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectingPrintertoWiFiSetup(SmartScreens):

    folder_name = "oobe"
    flow_name = "connecting_printer_to_wifi_wireless_setup"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectingPrintertoWiFiSetup, self).__init__(driver)

# -------------------------------Operate Elements-------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("yes_opt", timeout=timeout, raise_e=raise_e)

    def wait_for_screen_load_after_select_yes_opt(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectingPrintertoWiFi]:[wait_for_screen_load_after_select_yes_opt]-Wait for screen loading... ")

        return self.driver.wait_for_object("select_yes_opt_content_4_3", timeout=timeout, raise_e=raise_e)

    def click_yes_opt(self):
        '''
        This is a method to select Yes opt on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[click_yes_opt]-Select Yes opt.. ")

        self.driver.click("yes_opt")

    def click_no_opt(self):
        '''
        This is a method to select No opt on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[click_no_opt]-Select No opt.. ")

        self.driver.click("no_opt")

    def click_back_btn(self):
        '''
        This is a method to click Back button on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[click_back_btn]-Click Back button.. ")

        self.driver.click("back_btn")

    def click_connect_printer_btn(self):
        '''
        This is a method to click Connect printer button on Connecting printer to WiFi... screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[click_continue_btn]-Click Connect printer button.. ")

        self.driver.click("connect_printer_btn")

    def click_click_here_link(self):
        '''
        This is a method to click Click Here link on Connecting printer to WiFi... screen after select yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[click_click_here_link]-Click click_here_link.. ")

        self.driver.click("select_yes_opt_content_4_3")

    def get_value_of_screen_title(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen title.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_screen_title]-Get the contents of Connecting printer to WiFi... screen title..  ")

        return self.driver.get_value("screen_title")

    def get_value_of_contents(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen contents.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_contents]-Get the contents of Connecting printer to WiFi... screen contents..  ")

        return self.driver.get_value("contents")

    def get_value_of_yes_opt(self):
        '''
        This is a method to get the value of Yes opt on Connecting printer to WiFi... screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_yes_opt]-Get the contents of Yes opt..  ")

        return self.driver.get_title("yes_opt")

    def get_value_of_no_opt(self):
        '''
        This is a method to get the value of No opt on Connecting printer to WiFi... screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_no_opt]-Get the contents of No opt..  ")

        return self.driver.get_title("no_opt")

    def get_value_of_select_yes_opt_content_1_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 1-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_1_1]-Get the content of 1-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_1_1")

    def get_value_of_select_yes_opt_content_1_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 1-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_1_2]-Get the content of 1-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_1_2")

    def get_value_of_select_yes_opt_content_2_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_2_1]-Get the content of 2-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_1")

    def get_value_of_select_yes_opt_content_2_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_2_2]-Get the content of 2-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_2")

    def get_value_of_select_yes_opt_content_2_3(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-3 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_2_3]-Get the content of 2-3 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_3")

    def get_value_of_select_yes_opt_content_2_4(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-4 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_2_4]-Get the content of 2-4 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_4")

    def get_value_of_select_yes_opt_content_2_5(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 2-5 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_2_5]-Get the content of 2-5 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_2_5")

    def get_value_of_select_yes_opt_content_3_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_3_1]-Get the content of 3-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_1")

    def get_value_of_select_yes_opt_content_3_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_3_2]-Get the content of 3-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_2")

    def get_value_of_select_yes_opt_content_3_3(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 3-3 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_3_3]-Get the content of 3-3 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_3_3")

    def get_value_of_select_yes_opt_content_4_1(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 4-1 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_4_1]-Get the content of 4-1 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_4_1")

    def get_value_of_select_yes_opt_content_4_2(self):
        '''
        This is a method to get the value of Connecting printer to WiFi... screen content 4-2 after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_select_yes_opt_content_4_2]-Get the content of 4-2 after select Yes opt..  ")

        return self.driver.get_value("select_yes_opt_content_4_2")

    def get_value_of_click_here_link(self):
        '''
        This is a method to get the value of Click here link on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_click_here_link]-Get the content of Click here link..  ")

        return self.driver.get_value("click_here_link")

    def get_value_of_back_btn(self):
        '''
        This is a method to get the value of Back button on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_back_btn]-Get the content of Back button..  ")

        return self.driver.get_title("back_btn")

    def get_value_of_connect_printer_btn(self):
        '''
        This is a method to get the value of Connect printer button on Connecting printer to WiFi... screen after select Yes opt.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectComputerToWiFi]:[get_value_of_connect_printer_btn]-Get the content of Connect printer button..  ")

        return self.driver.get_title("connect_printer_btn")

# -------------------------------Verification Methods---------------------------------------------
    def verify_connecting_printer_to_wifi_wireless_setup_screen(self):
        '''
        This is a verification method to check UI strings of Connecting printer to WiFi screen.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Connecting printer to WiFi screen")
#         assert self.get_value_of_screen_title() == u""
#         assert self.get_value_of_contents() == u""
#         assert self.get_value_of_yes_opt() == u""
#         assert self.get_value_of_no_opt() == u""
#         assert self.get_value_of_back_btn() == u""

    def verify_connecting_printer_to_wifi_wireless_setup_screen_select_yes_opt(self):
        '''
        This is a verification method to check UI strings of Connecting printer to WiFi screen after select Yes opt.
        :parameter:
        :return:
        '''
        self.click_yes_opt()
        self.wait_for_screen_load_after_select_yes_opt()
        logging.debug("Start to check UI strings of Connecting printer to WiFi screen after select Yes opt")
#         assert self.get_value_of_screen_title() == u""
#         assert self.get_value_of_contents() == u""
#         assert self.get_value_of_select_yes_opt_content_1_1() == u""
#         assert self.get_value_of_select_yes_opt_content_1_2() == u""
#         assert self.get_value_of_select_yes_opt_content_2_1() == u""
#         assert self.get_value_of_select_yes_opt_content_2_2() == u""
#         assert self.get_value_of_select_yes_opt_content_2_3() == u""
#         assert self.get_value_of_select_yes_opt_content_2_4() == u""
#         assert self.get_value_of_select_yes_opt_content_2_5() == u""
#         assert self.get_value_of_select_yes_opt_content_3_1() == u""
#         assert self.get_value_of_select_yes_opt_content_3_2() == u""
#         assert self.get_value_of_select_yes_opt_content_3_3() == u""
#         assert self.get_value_of_select_yes_opt_content_4_1() == u""
#         assert self.get_value_of_select_yes_opt_content_4_2() == u""
#         assert self.get_value_of_click_here_link() == u""
#         assert self.get_value_of_back_btn() == u""
#         assert self.get_value_of_connect_printer_btn() == u""
