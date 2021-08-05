# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the device picker screen.

@author: Sophia
@create_date: May 22, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class DevicePicker(SmartScreens):
    folder_name = "common"
    flow_name = "device_picker"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(DevicePicker, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait device picker screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("search_box", timeout=timeout, raise_e=raise_e)

    def wait_for_beaconing_printer_load(self, printer_name, timeout=30, raise_e=True):
        '''
        This is a method to wait beaconing printer screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_beaconing_printer_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("beaconing_printer_chose", format_specifier=[printer_name], timeout=timeout, raise_e=raise_e)

    def wait_for_first_searched_printer_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait the first searched printer screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_first_searched_printer_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("first_printer_item", timeout=timeout, raise_e=raise_e)

    def wait_for_trying_to_communicate_string_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Trying to communicate to printer string load.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_trying_to_communicate_string_load]-Wait for screen load... ")

        return self.driver.wait_for_object("trying_to_communicate_with_printer", timeout=timeout, raise_e=raise_e)

    def wait_for_trying_to_communicate_string_disappear(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Trying to communicate to printer string disappear.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_trying_to_communicate_string_disappear]-Wait for screen disappear... ")

        return self.driver.wait_for_object_disappear("trying_to_communicate_with_printer", timeout=timeout, raise_e=raise_e)

    def wait_for_busy_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait busy icon shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_busy_icon_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("busy_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_warning_icon_display(self, timeout=60, raise_e=True):
        '''
        This is a method to wait warning icon shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[wait_for_warning_icon_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("warning_icon", timeout=timeout, raise_e=raise_e)

    def click_search_box(self):
        '''
        This is a method to click search box.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[click_search_box]-Click search box... ")

        self.driver.click("search_box", is_native_event=True)

    def set_value_to_search_box(self, printer_name):
        '''
        This is a method to set value to the search box.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[set_value_to_search_box]-Set value to search box... ")

        self.driver.send_keys("search_box", printer_name, press_enter=True)

    def click_beaconing_printer_chose(self, printer_name):
        '''
        This is a method to click the beaconing name to select printer using name.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[click_beaconing_printer_chose]-click to select printer... ")

        self.driver.click("beaconing_printer_chose", format_specifier=[printer_name], is_native_event=True)

    def click_searched_printer(self):
        '''
        This is a method to click searched printer.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[click_searched_printer]-Click first searched printer... ")

        self.driver.click("first_printer_item", is_native_event=True)

    def click_remote_printer(self, printer_name):
        '''
        This is a method to select remote printer using name.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[click_remote_printer]-click to select printer... ")

        self.driver.click("remote_printer_item", format_specifier=[printer_name], is_native_event=True)

    def click_refresh_btn(self):
        '''
        This is a method to click refresh button.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_refresh_btn-Click 'refresh' button... ")

        self.driver.click("refresh_btn", is_native_event=True)

    def click_search_box_delete_btn(self):
        '''
        This is a method to delete button on the search box.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_search_box_delete_btn]-Click 'x' button... ")

        self.driver.click("search_box_delete_btn")

    def click_setup_new_printer_btn(self):
        '''
        This is a method to click setup new printer button.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_setup_new_printer_btn]-Click 'setup_new_printer' button... ")

        self.driver.click("setup_new_printer_btn", is_native_event=True)

    def click_set_up_text(self):
        '''
        This is a method to click setup words.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_set_up_text]-Click 'set_up_words' button... ")

        self.driver.click("set_up_words", is_native_event=True)

    def click_usb_text(self):
        '''
        This is a method to select a USB connected printer.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_usb_words]-Select a USB connected printer... ")

        self.driver.click("usb_text", format_specifier=['USB.3'], is_native_event=True)

    def choose_remote_printer(self):
        '''
        This is a method to click setup words.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_set_up_text]-Click 'set_up_words' button... ")

        self.driver.click("remote", is_native_event=True)

    def input_remote_to_search_box(self):
        '''
        This is a method to set value to the search box.
        :parameter:
        :return:
        '''
        logging.debug("[DevicePickerScreen]:[set_value_to_search_box]-Set value to search box... ")

        self.driver.send_keys("search_box", "Remote")

    def click_remote_text(self):
        '''
        This is a method to select a Remote printer.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[click_remote_text]-Select a Remote printer... ")

        self.driver.click("remote_text", format_specifier=['Remote'])

    def get_value_of_set_up_text(self):
        '''
        This is a method to get value of setup words.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_set_up_text]-Get the contents of set_up_words...  ")

        return self.driver.get_value("set_up_words")

    def get_value_of_setup_new_printer_btn(self):
        '''
        This is a method to get value of setup new printer button.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_setup_new_printer_btn]-Get the contents of setup_new_printer_btn...  ")

        return self.driver.get_title("setup_new_printer_btn")

    def get_value_of_refresh_btn(self):
        '''
        This is a method to get value of refresh button.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_refresh_btn]-Get the contents of refresh_btn...  ")

        return self.driver.get_title("refresh_btn")

    def get_value_of_device_picker_title(self):
        '''
        This is a method to get value of device picker title.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_device_picker_title]-Get the contents of device_picker_tittle...  ")

        return self.driver.get_value("device_picker_title")

    def get_value_of_no_printers_available(self):
        '''
        This is a method to get value of no printer available.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_no_printers_available]-Get the contents of no_printers_available...  ")

        return self.driver.get_value("no_printers_available")

    def get_value_of_no_printers_contents(self):
        '''
        This is a method to get contents of no printer available.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_no_printers_contents]-Get the contents of no_printers_contents...  ")

        return self.driver.get_value("no_printers_contents")

    def get_value_of_warning_message(self):
        '''
        This is a method to get contents of warning message.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_warning_message]-Get the contents of warning_message...  ")

        return self.driver.get_value("warning_message")

    def get_value_of_printer_name(self):
        '''
        This is a method to get value of printer name.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_printer_name]-Get the contents of printer_name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_printer_status(self):
        '''
        This is a method to get value of no printer status.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_printer_status]-Get the contents of printer_status...  ")

        return self.driver.get_value("printer_status")

    def get_value_of_device_picker_contents_1(self):
        '''
        This is a method to get value of device_picker_contents.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_device_picker_contents]-Get the contents of device_picker_contents..  ")

        return self.driver.get_value("device_picker_contents_1")

    def get_value_of_device_picker_contents_2(self):
        '''
        This is a method to get value of device_picker_contents.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_device_picker_contents]-Get the contents of device_picker_contents..  ")

        return self.driver.get_value("device_picker_contents_2")

    def get_value_of_device_picker_contents_3(self):
        '''
        This is a method to get value of device_picker_contents.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_device_picker_contents]-Get the contents of device_picker_contents..  ")

        return self.driver.get_value("device_picker_contents_3")

    def get_value_of_device_picker_contents_4(self):
        '''
        This is a method to get value of device_picker_contents.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_device_picker_contents]-Get the contents of device_picker_contents..  ")

        return self.driver.get_value("device_picker_contents_4")

    def get_value_of_printer_ip(self):
        '''
        This is a method to get value of no printer IP.
        :parameter:
        :return:
        '''
        logging.debug("[Device Picker]:[get_value_of_printer_ip]-Get the contents of printer_ip...  ")

        return self.driver.get_value("printer_ip")

# -------------------------------Verification Methods--------------------------
    def verify_device_picker_string(self):
        test_strings = smart_utility.get_local_strings_from_table(screen_name='device_picker')
#         self.driver.wait_for_object("usb_text", format_specifier=['USB.4'])
#         assert self.get_value_of_set_up_text() == test_strings['set_up_text']
        assert self.get_value_of_device_picker_title() == test_strings['device_picker_title']
        assert test_strings['setup_new_printer_btn'] in self.get_value_of_setup_new_printer_btn()
        assert test_strings['refresh_btn'] in self.get_value_of_refresh_btn()
        assert self.get_value_of_device_picker_contents_1() + self.get_value_of_device_picker_contents_2() + self.get_value_of_device_picker_contents_3() + self.get_value_of_device_picker_contents_4() == test_strings['device_picker_contents']

    def verify_no_printers_available_screen(self):
        logging.debug("Should say 'No printers available'and 'Please make sure that your printer is powered on and connected to the same network as this computer' string displayed in the Device Picker no result UI.")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='device_picker')
        assert self.get_value_of_no_printers_available() == test_strings['no_printers_available_title']
        assert self.get_value_of_no_printers_contents() == test_strings['no_printers_contents']

    def verify_beaconing_printer_initiate_oobe(self):
        logging.debug("Verify OOBE flow starts")
        self.driver.wait_for_object("oobe_flow_tittle_2")
#         assert self.get_value_of_oobe_flow_tittle_1()==u""

    def verify_warning_message_display(self):
        logging.debug("verify warning message string shows")
        self.wait_for_warning_icon_display()
        self.driver.wait_for_object("warning_message")

    def verify_printer_info(self, printerip):
        logging.debug("Should only display the following-Printer NameOnline or Offline StatusSource:Ethernet = ip address")
        self.driver.wait_for_object("printer_ip", format_specifier=[printerip])

    def verify_remote_printer_display(self):
        if not self.driver.wait_for_object("remote_txt", raise_e=False):
            raise UnexpectedItemPresentException("the remote printer not be found")
        return True

    def verify_printer_is_found(self):
        if self.driver.wait_for_object("warning_icon", raise_e=False):
            raise UnexpectedItemPresentException("the printer not be found")
        return True
