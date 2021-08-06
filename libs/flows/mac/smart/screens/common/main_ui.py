# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the main UI screen.

@author: Sophia
@create_date: May 9, 2019
'''

import logging
from time import sleep

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class MainUI(SmartScreens):
    folder_name = "common"
    flow_name = "main_ui"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(MainUI, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("scan_tile", format_specifier=['Scan'], timeout=timeout, raise_e=raise_e)

    def wait_for_ready_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait main UI screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_ready_status_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("printer_status_text", format_specifier=['Ready'], timeout=timeout, raise_e=raise_e)

    def wait_for_mobile_fax_tile_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Tile load on main UI screen correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_mobile_fax_tile_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("mobile_fax_tile", format_specifier=['Mobile Fax'], timeout=timeout, raise_e=raise_e)

    def wait_for_smart_tasks_tile_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Smart Tasks tile load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_smart_tasks_tile_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("smart_tasks_tile", format_specifier=['Smart Tasks'], timeout=timeout, raise_e=raise_e)

    def wait_for_printer_status_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for printer status load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for printer_status loading... ")

        return self.driver.wait_for_object("printer_status", timeout=timeout, raise_e=raise_e)

    def wait_for_set_up_btn_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait for printer status load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_screen_load]-Wait for set_up_btn loading... ")

        return self.driver.wait_for_object("set_up_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_app_windows(self, timeout=30, raise_e=True):
        '''
        This is a method to wait app windows shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_app_windows]-Wait for screen loading... ")

        return self.driver.wait_for_object("app_window", timeout=timeout, raise_e=raise_e)

    def wait_for_find_printer_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait find printer icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_find_printer_icon]-Wait for screen loading... ")

        return self.driver.wait_for_object("add_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_smart_tasks_awareness_modal_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Smart TaskS Awareness modal shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_smart_tasks_awareness_modal_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("smart_task_dialog_get_started_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_mobile_fax_awareness_modal_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile Fax Awareness modal shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_mobile_fax_awareness_modal_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("mobile_fax_awareness_content_1", timeout=timeout, raise_e=raise_e)

    def wait_for_forget_printer_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait forget printer screen load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_forget_printer_btn_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_forget_this_printer_btn_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait forget this printer button load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_forget_this_printer_btn_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("forget_this_printer_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_left_arrow_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait left arrow icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_left_arrow_icon_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("left_arrow_icon", timeout=timeout, raise_e=raise_e)

    def wait_for_right_arrow_icon_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait right arrow icon load correctly.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_right_arrow_icon_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("right_arrow_icon", timeout=timeout, raise_e=raise_e)

    def click_left_arrow_icon(self):
        '''
        This is a method to click left arrow icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_left_arrow_icon]-Click left arrow icon... ")

        self.driver.click("left_arrow_icon", is_native_event=True)

    def click_right_arrow_icon(self):
        '''
        This is a method to click right arrow icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_right_arrow_icon]-Click right arrow icon... ")

        self.driver.click("right_arrow_icon", is_native_event=True)

    def click_set_up_btn(self):
        '''
        This is a method to click right arrow icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_right_arrow_icon]-Click right arrow icon... ")

        self.driver.click("set_up_btn", is_native_event=True)

    def click_close_btn_on_smart_tasks_awareness_modal(self):
        '''
        This is a method to click close icon on Smart Tasks Awareness Modal.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_close_btn_on_smart_tasks_awareness_modal]-Click close icon... ")

        self.driver.click("smart_task_dialog_close_btn", is_native_event=True)

    def click_close_btn_on_mobile_fax_awareness_modal(self):
        '''
        This is a method to click close icon on Mobile Fax Awareness Modal.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_close_btn_on_mobile_fax_awareness_modal]-Click close icon... ")

        self.driver.click("mobile_fax_awareness_close_btn", is_native_event=True)

    def click_learn_more_btn_on_mobile_fax_awareness_modal(self):
        '''
        This is a method to click Learn Mode button on Mobile Fax Awareness Modal.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_learn_more_btn_on_mobile_fax_awareness_modal]-Click Learn More button... ")

        self.driver.click("mobile_fax_awareness_learn_more_btn", is_native_event=True)

    def click_get_ink_tile(self):
        '''
        This is a method to click Get Ink tile or Get Supplies tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_get_ink_tile]-Click 'Get Ink Tile' or 'Get Supplies tile'... ")

        self.driver.click("get_ink_tile", is_native_event=True)  # format_specifier=['Get Ink']

    def click_smart_tasks_tile(self):
        '''
        This is a method to click Smart Tasks tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_smart_tasks_tile]-Click Smart Tasks tile... ")

        self.driver.click("smart_tasks_tile", format_specifier=['Smart Tasks'], is_native_event=True)

    def click_scan_tile(self):
        '''
        This is a method to click scan tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_scan_tile]-Click 'Scan Tile' button... ")

        self.driver.click("scan_tile", format_specifier=['Scan'], is_native_event=True)

    def click_print_document_tile(self):
        '''
        This is a method to click print document tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_print_document_tile]-Click 'Print Document Tile' button... ")

        self.driver.click("print_document_tile", format_specifier=['Print Documents'], is_native_event=True)

    def click_print_photo_tile(self):
        '''
        This is a method to click print photo tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_print_photo_tile]-Click 'Print Photo Tile' button... ")

        self.driver.click("print_photo_tile", format_specifier=['Print Photos'], is_native_event=True)

    def click_mobile_fax_tile(self):
        '''
        This is a method to click Mobile Fax tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_mobile_fax_tile]-Click 'Mobile Fax Tile' button... ")

        self.driver.click("mobile_fax_tile", format_specifier=['Mobile Fax'], is_native_event=True)

    def click_help_center_tile(self):
        '''
        This is a method to click help_center_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_help_center_tile]-Click 'Help Center Tile' button... ")

        self.driver.click("help_center_tile", format_specifier=['Help & Support'], is_native_event=True)

    def click_printables_tile(self):
        '''
        This is a method to click printables_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printables_tile]-Click 'printables_tile' button... ")

        self.driver.click("printables_tile", format_specifier=['Printables'], is_native_event=True)

    def click_printer_settings_tile(self):
        '''
        This is a method to click printer_settings_tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_settings_tile]-Click 'Printer Settings Tile' button... ")

        self.driver.click("printer_settings_tile", format_specifier=['Printer Settings'], is_native_event=True)

    def click_printer_image(self):
        '''
        This is a method to click Printer Image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_image]-Click Printer Image... ")

        self.driver.click("printer_image", is_native_event=True)

    def click_printer_status_image(self):
        '''
        This is a method to click Printer Status Image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_printer_status_image]-Click Printer Status Image... ")

        self.driver.click("printer_status_image", is_native_event=True)

    def click_find_printer_icon(self):
        '''
        This is a method to click find printer icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_find_printer_icon]-Click 'find_printer' icon... ")

        self.driver.click("add_printer_btn")

    def right_click_find_printer_icon(self):
        '''
        This is a method to right click find printer icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_find_printer_icon]-Click 'find_printer' icon... ")

        self.driver.context_click("add_printer_btn")

    def right_click_printer_image_by_id(self):
        '''
        This is a method to right click printer image on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[right_click_printer_image_by_id]-Click 'print_image' icon... ")

        self.driver.context_click("printer_image")

    def right_click_printer_image_by_coordinates(self):
        '''
        This is a method to select file.
        :parameter:
        :return:
        '''
        position = self.driver.get_location("printer_status")
        x_position = position['x'] - 1300
        y_position = position['y'] - 300

        sleep(2)
        self.driver.click("printer_status", is_native_event=True)
        self.driver.context_click_by_coordinates(x=x_position, y=y_position)
        return True

    def click_outside_of_forget_this_printer_btn(self):
        '''
        This is a method to click outside of Forget this printer btn on Main UI.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_outside_of_forget_this_printer_btn]-Click outside of Forget this printer btn... ")

        self.driver.click("right_arrow_icon", is_native_event=True)
#         position = self.driver.get_location("printer_status")
#         x_position = position['x'] - 1400
#         y_position = position['y'] - 400
#         logging.debug(position)
# 
#         sleep(2)
#         self.driver.click_by_coordinates(x=x_position, y=y_position)
#         return True

    def click_forget_this_printer_btn(self):
        '''
        This is a method to click forget printer button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_find_printer_icon]-Click 'forget_printer' btn... ")

        self.driver.click("forget_this_printer_btn")

    def click_smart_task_dialog_get_started_btn(self):
        '''
        This is a method to click get started button on smart tasks welcome modal.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_get_started_btn]-Click get started button... ")

        self.driver.click("smart_task_dialog_get_started_btn", is_native_event=True)

    def click_already_have_smart_tasks_link(self):
        '''
        This is a method to click already have smart tasks sign in link.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[click_already_have_smart_tasks_link]-Click already have smart tasks sign in link... ")

        self.driver.click("smart_task_dialog_sign_in_link", is_native_event=True)

    def get_value_of_printer_name(self):
        '''
        This is a method to get value of printer name.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_name]-Get printer name...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_printer_status(self):
        '''
        This is a method to get value of printer_status.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_status]-Get printer_status...  ")

        return self.driver.get_value("printer_status_text")

    def get_value_of_get_ink_tile(self):
        '''
        This is a method to get value of Get Ink Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_get_ink_tile]-Get value of Get Ink Tile...  ")

        return self.driver.get_value("get_ink_tile_text")

    def get_value_of_smart_tasks_tile(self):
        '''
        This is a method to get value of Smart Tasks Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_smart_tasks_tile]-Get value of Smart Tasks Tile...  ")

        return self.driver.get_value("smart_tasks_tile_text")

    def get_value_of_scan_tile(self):
        '''
        This is a method to get value of Scan Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_scan_tile]-Get value of Scan Tile...  ")

        return self.driver.get_value("scan_tile_text")

    def get_value_of_print_documents_tile(self):
        '''
        This is a method to get value of Print Documents Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_print_documents_tile]-Get value of Print Documents Tile...  ")

        return self.driver.get_value("print_document_tile_text")

    def get_value_of_print_photos_tile(self):
        '''
        This is a method to get value of Print Photos Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_print_photos_tile]-Get value of Print Photos Tile...  ")

        return self.driver.get_value("print_photo_tile_text")

    def get_value_of_mobile_fax_tile(self):
        '''
        This is a method to get value of Mobile Fax Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_mobile_fax_tile]-Get value of Mobile Fax Tile...  ")

        return self.driver.get_value("mobile_fax_tile_text")

    def get_value_of_help_support_tile(self, is_malbec_taccola_vasari=False):
        '''
        This is a method to get value of Help Support Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_help_support_tile]-Get value of Help Support Tile...  ")

        if not is_malbec_taccola_vasari:
            return self.driver.get_value("help_center_tile_text")
        else:
            return self.driver.get_value("7_help_center_tile_text")

    def get_value_of_printer_settings_tile(self, is_malbec_taccola_vasari=False):
        '''
        This is a method to get value of Printer Settings Tile.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_printer_settings_tile]-Get value of Printer Settings Tile...  ")

        if not is_malbec_taccola_vasari:
            return self.driver.get_value("printer_settings_tile_text")
        else:
            return self.driver.get_value("8_printer_settings_tile_text")

    def get_value_of_mobile_fax_awareness_content_1(self):
        '''
        This is a method to get value of Mobile Fax Awareness modal content - 1.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_mobile_fax_awareness_content_1]-Get value of Mobile Fax Awareness modal content - 1...  ")

        return self.driver.get_value("mobile_fax_awareness_content_1")

    def get_value_of_mobile_fax_awareness_content_2(self):
        '''
        This is a method to get value of Mobile Fax Awareness modal content - 2.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_mobile_fax_awareness_content_2]-Get value of Mobile Fax Awareness modal content - 2...  ")

        return self.driver.get_value("mobile_fax_awareness_content_2")

    def get_value_of_mobile_fax_awareness_learn_more_btn(self):
        '''
        This is a method to get value of Mobile Fax Awareness modal Learn More button.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[get_value_of_mobile_fax_awareness_learn_more_btn]-Get value of Mobile Fax Awareness modal Learn More button...  ")

        return self.driver.get_title("mobile_fax_awareness_learn_more_btn")

# -------------------------------Verification Methods--------------------------
    def verify_printer_name_main_ui(self, printer_name):
        logging.debug("[MainUIScreen]:[verify_printer_name_main_ui]-Verify printer name on the main page... ")

        assert self.get_value_of_printer_name() == printer_name

    def verify_main_ui_with_installed_printer(self, printer_info):
        logging.debug("[MainUIScreen]:[verify_main_ui_with_installed_printer]-Verify Main page with Installed printer... ")

        self.verify_printer_name_main_ui(printer_info["printerName"])

    def verify_forget_this_printer_btn_notdisplay(self, timeout=1):
        '''
        verify_forget_this_printer_btn_notdisplay
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("forget_this_printer_btn", timeout=timeout, raise_e=False)

    def verify_instant_ink_tile(self, support=True):
        '''
        check Instant Ink tile on Main UI
        :parameter:
        :return:
        '''
        if(support):
            assert self.get_value_of_get_ink_tile() == ""
        else:
            assert self.get_value_of_get_ink_tile() == "Get Supplies"

    def verify_gothamappwindow_minimized(self):
        '''
        Verify gotham app was minimized
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("scan_tile", raise_e=False):
            raise UnexpectedItemPresentException("the screen still exists")
        return True

    def check_printer_added(self):
        '''
        check printer added on main ui
        :parameter:
        :return:
        '''
        if self.driver.wait_for_object("add_printer_btn", raise_e=False):
            raise UnexpectedItemPresentException("the printer will not be added")
        return True

    def verify_mobile_fax_awareness_modal(self):
        '''
        This is a verification method to check UI strings of Mobile Fax Awareness modal.
        :parameter:
        :return:
        '''
        self.wait_for_mobile_fax_awareness_modal_display()

        logging.debug("Start to check UI strings of Mobile Fax Awareness modal")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='mobile_fax_awareness_modal')
        assert self.get_value_of_mobile_fax_awareness_content_1() == test_strings['modern_faxing_text']
        assert self.get_value_of_mobile_fax_awareness_content_2() == test_strings['its_easy_to_send_text']
        assert self.get_value_of_mobile_fax_awareness_learn_more_btn() == test_strings['learn_more_btn']

    def verify_mobile_fax_awareness_modal_disappear(self, timeout=3):
        '''
        This is a verification method to verify Mobile Fax Awareness modal disappear after clicking close button.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("mobile_fax_awareness_content_1", timeout=timeout, raise_e=False)

    def verify_smart_tasks_tile_hidden(self, timeout=5):
        '''
        This is a verification method to verify Smart Tasks tile is hidden on Main page.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("smart_tasks_tile", format_specifier=['Smart Tasks'], timeout=timeout, raise_e=False)

    def verify_mobile_fax_tile_hidden(self, timeout=5):
        '''
        This is a verification method to verify Mobile Fax tile is hidden on Main page.
        :parameter:
        :return:
        '''
        assert not self.driver.wait_for_object("mobile_fax_tile", format_specifier=['Mobile Fax'], timeout=timeout, raise_e=False)

    def verify_printer_status(self, status):
        '''
        This is a verification method to check UI strings of printer_stauts.
        :parameter:
        :return:
        '''
        assert self.get_value_of_printer_status() == status

    def verify_printer_status_is_ready(self):
        '''
        This is a verification method to check UI strings of printer_stauts.
        :parameter:
        :return:
        '''
        assert self.get_value_of_printer_status() == "Ready"

    def verify_printer_status_is_offline(self):
        '''
        This is a verification method to check UI strings of printer_stauts.
        :parameter:
        :return:
        '''
        test_strings = smart_utility.get_local_strings_from_table(screen_name='main_ui')
        assert self.get_value_of_printer_status() == test_strings['offline_text']
