# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on Connect printer to WiFi screen.

@author: ten
@create_date: July 25, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens


class ConnectPrintertoWiFi(SmartScreens):
    folder_name = "oobe"
    flow_name = "connect_printer_to_wifi"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(ConnectPrintertoWiFi, self).__init__(driver)

# -------------------------------Operate Elements--------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("change_network_link", timeout=timeout, raise_e=raise_e)

    def wait_for_access_wifi_password_dialog_load(self, timeout=30, raise_e=True):
        '''
        Wait for screen marker.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[wait_for_access_wifi_password_dialog_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("access_wifi_password_dialog_title", timeout=timeout, raise_e=raise_e)

    def click_info_btn(self):
        '''
        This is a method to click Info button on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_info_btn]-Click info button... ")

        self.driver.click("info_btn")

    def click_change_network_link(self):
        '''
        This is a method to click Change Network link on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_change_network_link]-Click Change Network link... ")

        self.driver.click("change_network_link", is_native_event=True)

    def click_access_my_wifi_password_automatically_link(self):
        '''
        This is a method to click Access my WiFi password automatically link on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_access_my_wifi_password_automatically_link]-Click Access my WiFi password automatically link... ")

        self.driver.click("access_my_wifi_password_automatically_link", is_native_event=True)

    def click_connect_btn(self):
        '''
        This is a method to click Connect button on Connect printer to WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_continue_btn]-Click Continue button... ")

        self.driver.click("connect_btn")

    def click_no_thanks_btn_on_access_wifi_password(self):
        '''
        This is a method to click "No, thanks" button on Access WiFi Password for... dialog
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_no_thanks_btn_on_access_wifi_password]-Click No thanks button... ")

        self.driver.click("access_wifi_password_dialog_no_thanks_btn")

    def click_continue_btn_on_access_wifi_password(self):
        '''
        This is a method to click "Continue" button on Access WiFi Password for... dialog
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[click_continue_btn_on_access_wifi_password]-Click continue button... ")

        self.driver.click("access_wifi_password_dialog_continue_btn")

    def input_enter_wifi_password_box(self, contents):
        '''
        input enter contents in password box
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[enter_wifi_password_box]input-enter_wifi_password_box... ")

        self.driver.send_keys("enter_wifi_password_box", contents, press_enter=True)

    def clear_enter_wifi_password_box(self):
        '''
        clear enter contents in password box
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[enter_wifi_password_box]clear-enter_wifi_password_box... ")

        self.driver.clear_text("enter_wifi_password_box")

    def get_value_of_connect_printer_to_wifi_title(self):
        '''
        This is a method to get the value of Connect Printer to WiFi title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_title]-Get the contents of Connect Printer to WiFi title...  ")

        return self.driver.get_value("connect_printer_to_wifi_title")

    def get_value_of_connect_printer_to_wifi_printer_name(self):
        '''
        This is a method to get the value of Printer Name on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_printer_to_wifi_printer_name]-Get the contents of Printer Name...  ")

        return self.driver.get_value("connect_printer_to_wifi_printer_name")

    def get_value_of_wifi_network_text(self):
        '''
        This is a method to get the value of WiFi Network text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_wifi_network_text]-Get the contents of WiFi Network text...  ")

        return self.driver.get_value("wifi_network_text")

    def get_value_of_router_name_text(self):
        '''
        This is a method to get the value of Router Name on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_router_name_text]-Get the contents of Router Name...  ")

        return self.driver.get_value("router_name_text")

    def get_value_of_change_network_link(self):
        '''
        This is a method to get the value of Change Network link on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_change_network_link]-Get the contents of Change Network link...  ")

        return self.driver.get_value("change_network_link")

    def get_value_of_enter_wifi_password_text(self):
        '''
        This is a method to get the value of Enter WiFi Password text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_enter_wifi_password_text]-Get the contents of Enter WiFi Password text...  ")

        return self.driver.get_value("enter_wifi_password_text")

    def get_value_of_access_my_wifi_password_automatically_link(self):
        '''
        This is a method to get the value of Access my WiFi password automatically link on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_my_wifi_password_automatically_link]-Get the contents of Access my WiFi password automatically link...  ")

        return self.driver.get_value("access_my_wifi_password_automatically_link")

    def get_value_of_connect_btn(self):
        '''
        This is a method to get the value of Connect button on Connect Printer to WiFi screen
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_connect_btn]-Get the contents of Connect button...  ")

        return self.driver.get_title("connect_btn")

    def get_value_of_incorrect_password_text(self):
        '''
        This is a method to get the value of Incorrect password text on Connect Printer to WiFi screen
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_incorrect_password_text]-Get the contents of incorrectpassword_text ...  ")

        return self.driver.get_value("incorrect_pw_text")

    def get_value_of_access_wifi_password_dialog_title(self):
        '''
        This is a method to get the value of Access WiFi Password dialog title
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_title]-Get the contents of access_wifi_password_dialog_title...  ")

        return self.driver.get_value("access_wifi_password_dialog_title")

    def get_value_of_access_wifi_password_dialog_content_1(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 1
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_1]-Get the contents of access_wifi_password_dialog_content_1...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_1")

    def get_value_of_access_wifi_password_dialog_content_2(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 2
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_2]-Get the contents of access_wifi_password_dialog_content_2...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_2")

    def get_value_of_access_wifi_password_dialog_content_3(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 3
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_3]-Get the contents of access_wifi_password_dialog_content_3...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_3")

    def get_value_of_access_wifi_password_dialog_content_4(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Content - 4
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_content_4]-Get the contents of access_wifi_password_dialog_content_4...  ")

        return self.driver.get_value("access_wifi_password_dialog_content_4")

    def get_value_of_access_wifi_password_dialog_no_thanks_btn(self):
        '''
        This is a method to get the value of Access WiFi Password dialog No thanks button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_no_thanks_btn]-Get the contents of No thanks button...  ")

        return self.driver.get_title("access_wifi_password_dialog_no_thanks_btn")

    def get_value_of_access_wifi_password_dialog_continue_btn(self):
        '''
        This is a method to get the value of Access WiFi Password dialog Continue button
        :parameter:
        :return:
        '''
        logging.debug("[ConnectPrintertoWiFi]:[get_value_of_access_wifi_password_dialog_continue_btn]-Get the contents of Continue button...  ")

        return self.driver.get_title("access_wifi_password_dialog_continue_btn")

# -------------------------------Verification Methods------------------------
    def verify_access_wifi_password_dialog(self):
        '''
        This is a verification method to check UI strings of Access WiFi Password dialog.
        :parameter:
        :return:
        '''
        self.wait_for_access_wifi_password_dialog_load()
        logging.debug("Start to verify UI string of Access WiFi Password dialog")
#         assert self.get_value_of_access_wifi_password_dialog_title() == u""
#         assert self.get_value_of_access_wifi_password_dialog_content_1() == u""
#         assert self.get_value_of_access_wifi_password_dialog_content_2() == u""
#         assert self.get_value_of_access_wifi_password_dialog_content_3() == u""
#         assert self.get_value_of_access_wifi_password_dialog_content_4() == u""
#         assert self.get_value_of_access_wifi_password_dialog_no_thanks_btn() == u""
#         assert self.get_value_of_access_wifi_password_dialog_continue_btn() == u""

    def verify_connect_printer_to_wifi_screen(self):
        '''
        This is a verification method to check UI strings of Connect Printer To WiFi screen.
        :parameter:
        :return:
        '''
        self.verify_access_wifi_password_dialog()
        self.click_no_thanks_btn_on_access_wifi_password()

        self.wait_for_screen_load()
        self.driver.wait_for_object("info_btn", timeout=30, raise_e=True)
        self.driver.wait_for_object("enable_diable_show_password_btn", timeout=30, raise_e=True)

        logging.debug("Start to verify UI string of Connect Printer To WiFi screen")
#         assert self.get_value_of_connect_printer_to_wifi_title() == u""
#         assert self.get_value_of_connect_printer_to_wifi_printer_name() == u""
#         assert self.get_value_of_wifi_network_text() == u""
#         assert self.get_value_of_router_name_text() == u""
#         assert self.get_value_of_change_network_link() == u""
#         assert self.get_value_of_enter_wifi_password_text() == u""
#         assert self.get_value_of_access_my_wifi_password_automatically_link() == u""
#         assert self.get_value_of_connect_btn() == u""

    def verify_incorrect_password_waring(self):
        '''
        This is a verification method to check UI strings of Incorrect password after input a incorrect password on Connect Printer To WiFi screen.
        :parameter:
        :return:
        '''
        self.driver.wait_for_object("incorrect_pw_text", timeout=30, raise_e=True)
#        assert self.get_value_of_incorrect_password_text() == u"Incorrect password. Try entering it again."

    def verify_connect_printer_to_wifi_incorrect_password(self, pw):
        '''
        This is a verification method to check the incorrect password warning shows on Connect Printer to WiFi screen after input a wrong password.
        :parameter:
        :return:
        '''
        self.input_enter_wifi_password_box(pw)
        self.click_connect_btn()
        self.verify_incorrect_password_waring()
