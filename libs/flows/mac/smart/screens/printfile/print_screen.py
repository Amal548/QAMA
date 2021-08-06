# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on
the print dialog.

@author: Sophia
@create_date: May 6,  2019
'''

import logging

import MobileApps.resources.const.mac.const as smart_const
from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import ItemNotFoundException


class PrintScreen(SmartScreens):
    folder_name = "printfile"
    flow_name = "print_screen"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PrintScreen, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait print dialog shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("scan_tile", timeout=timeout, raise_e=raise_e)

    def wait_for_support_sheet_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait support file type sheet shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[wait_for_support_sheet_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("ok_btn_sheet", timeout=timeout, raise_e=raise_e)

    def click_ok_support_file(self):
        '''
        This is a method to click OK button on the support file type sheet.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_ok_support_file]-Click 'OK' button on the Support file type sheet... ")

        self.driver.click("ok_btn_sheet")

    def click_print_btn(self):
        '''
        This is a method to click print button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_print_btn]-Click 'Print' button... ")

        self.driver.click("print_btn")

    def click_browser_btn(self):
        '''
        This is a method to click browser button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_browser_btn]-Click 'Browser' button... ")

        self.driver.click("browser_btn", is_native_event=True)

    def click_cancel_btn(self):
        '''
        This is a method to click cancel button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_cancel_btn]-Click 'Cancel' button... ")

        self.driver.click("cancel_btn")

    def click_cancel_btn_on_print_photo(self):
        '''
        This is a method to click cancel button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_cancel_btn_on_print_photo]-Click 'Cancel' button... ")

        self.driver.click("cancel_btn_print_photo")

    def click_show_details_btn(self):
        '''
        This is a method to click show details button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_show_details_btn]-Click 'Show Details' button... ")

        self.driver.click("show_detail_btn")

    def click_hide_details_btn(self):
        '''
        This is a method to click hide details button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_hide_details_btn]-Click 'Hide Details' button... ")

        self.driver.click("hide_detail_btn")

    def choose_presets(self, presets_value):
        '''
        This is a method to choose presets option.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[choose_presets]-Choose presets option... ")

        self.driver.choose_combo_box_options("presets", option_index=presets_value)

    def set_copy_value(self, copy_value):
        '''
        This is a method to set copies value.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[set_copy_value]-Set copy value... ")

        self.driver.send_keys("copy", copy_value)

    def check_black_and_white(self):
        '''
        This is a method to check blank and white check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[check_black_and_white]-Check black and white... ")

        self.driver.check_box("color_black")

    def uncheck_black_and_white(self):
        '''
        This is a method to uncheck blank and white check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[uncheck_black_and_white]-Uncheck black and white... ")

        self.driver.check_box("color_black", uncheck=True)

    def check_two_side(self):
        '''
        This is a method to check two side check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[check_two_side]-Check two side... ")

        self.driver.check_box("two_side")

    def uncheck_two_side(self):
        '''
        This is a method to uncheck two side check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[uncheck_two_side]-Uncheck two side... ")

        self.driver.check_box("two_side", uncheck=True)

    def choose_page_all(self):
        '''
        This is a method to choose all radio button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[choose_page_all]-Choose pages all... ")

        self.driver.click("page_all")

    def choose_page_partial(self):
        '''
        This is a method to choose partial radio button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[choose_page_partial]-Choose pages from... ")

        self.driver.click("page_partial")

    def set_page_from(self, from_value):
        '''
        This is a method to set page from value.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[set_page_from]-Set page from... ")

        self.driver.send_keys("page_from", from_value)

    def set_page_to(self, to_value):
        '''
        This is a method to set page to value.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[set_page_to]-Set page to... ")

        self.driver.send_keys("page_to", to_value)

    def choose_paper_size(self, size_value):
        '''
        This is a method to choose paper size.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[choose_paper_size]-Choose paper size option... ")

        self.driver.choose_combo_box_options("paper_size", option_index=size_value)

    def click_orientation_landscape(self):
        '''
        This is a method to click landscape button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_orientation_landscape]-Click landscape orientation ... ")

        self.driver.click("landscape")

    def click_orientation_vertical(self):
        '''
        This is a method to click vertical button.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[click_orientation_vertical]-Click vertical orientation ... ")

        self.driver.click("vertical")

    def choose_pop_section(self, pop_value):
        '''
        This is a method to choose pop up section.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[choose_pop_section]-Choose pop option... ")

        self.driver.choose_combo_box_options("pop_section", option_index=pop_value)

    def set_up_print_settings(self, print_settings):
        '''
        This is a method to set up print settings on the print dialog.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[set_up_print_settings]-Start to set up print settings... ")

        self.click_show_details_btn()

        preset_value = print_settings[smart_const.PRINT_SETTINGS.PRESETS]
        if(preset_value is not None):
            self.choose_presets(preset_value)

        copy_value = print_settings[smart_const.PRINT_SETTINGS.COPIES]
        if(copy_value is not None):
            self.set_copy_value(copy_value)

        color_value = print_settings[smart_const.PRINT_SETTINGS.COLOR_BLANK]
        if(color_value is not None and color_value == smart_const.CHECKBOX_VALUE.CHECK):
            self.check_black_and_white()
        elif(color_value is not None and color_value == smart_const.CHECKBOX_VALUE.UNCHECK):
            self.uncheck_black_and_white()

        side_value = print_settings[smart_const.PRINT_SETTINGS.TWO_SIDE]
        if(side_value is not None and color_value == smart_const.CHECKBOX_VALUE.CHECK):
            self.check_two_side()
        elif(side_value is not None and color_value == smart_const.CHECKBOX_VALUE.UNCHECK):
            self.uncheck_two_side()

        page_value = print_settings[smart_const.PRINT_SETTINGS.PAGES]
        if(page_value is not None and page_value == smart_const.PAPER_PAGES.ALL):
            self.choose_page_all()
        elif(page_value is not None and page_value == smart_const.PAPER_PAGES.PARTIAL):
            page_from = print_settings[smart_const.PRINT_SETTINGS.PAGE_From]
            page_to = print_settings[smart_const.PRINT_SETTINGS.PAGE_To]
            if(page_from is not None and page_to is not None):
                self.set_page_from(page_from)
                self.set_page_to(page_to)
            else:
                raise ItemNotFoundException("Please set the page from or page to value...")

        size_value = print_settings[smart_const.PRINT_SETTINGS.PAPER_SIZE]
        if(size_value is not None):
            self.choose_paper_size(size_value)

        orientation_value = print_settings[smart_const.PRINT_SETTINGS.ORIENTATION]
        if(orientation_value is not None and orientation_value == smart_const.ORIENTATION.VERTICAL):
            self.click_orientation_vertical()
        elif(orientation_value is not None and orientation_value == smart_const.ORIENTATION.LANDSCAPE):
            self.click_orientation_landscape()

        pop_button_value = print_settings[smart_const.PRINT_SETTINGS.POPUP_SECTION]
        if(pop_button_value is not None):
            self.choose_pop_section(pop_button_value)

    def get_value_of_printer_name(self):
        '''
        This is a method to get value of printer name.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_printer_name]-Get value of printer name ...  ")

        return self.driver.get_value("printer_name")

    def get_value_of_presets(self):
        '''
        This is a method to get value of presets.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_presets]-Get value of presets ...  ")

        return self.driver.get_value("presets")

    def get_value_of_copies(self):
        '''
        This is a method to get value of copies.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_copies]-Get value of copies ...  ")

        return self.driver.get_value("copy")

    def get_value_of_blank_checkbox(self):
        '''
        This is a method to get value of blank and white check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_blank_checkbox]-Get value of blank and white check box ...  ")

        return self.driver.get_value("color_black")

    def get_value_of_two_sides_checkbox(self):
        '''
        This is a method to get value of two sides check box.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_two_sides_checkbox]-Get value of two sides check box ...  ")

        return self.driver.get_value("two_side")

    def get_value_of_pages(self, is_detail=False):
        '''
        This is a method to get value of pages.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_pages]-Get value of pages ...  ")
        if is_detail:
            return self.driver.get_value("page_all")
        else:
            return self.driver.get_value("pages")

    def get_value_of_paper_size(self):
        '''
        This is a method to get value of paper size.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_paper_size]-Get value of paper size ...  ")

        return self.driver.get_value("paper_size")

    def get_value_of_orientation_vertical(self):
        '''
        This is a method to get value of orientation vertical.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_orientation_vertical]-Get value of orientation vertical ...  ")

        return self.driver.get_value("vertical")

    def get_value_of_popup_section(self):
        '''
        This is a method to get value of pop up section.
        :parameter:
        :return:
        '''
        logging.debug("[PrintScreen]:[get_value_of_popup_section]-Get value of pop up section ...  ")

        return self.driver.get_value("pop_section")

# -------------------------------Verification Methods--------------------------
    def verify_print_dialog_with_default_settings(self, printer_name, is_detail=False, is_local_env=False):
        '''
        This is a method to verify the default value on the print dialog.
        :parameter:
        :return:
        '''
        print_default_settings = self.set_print_settings_default_value(is_detail, is_local_env)

        if is_detail:
            assert self.get_value_of_printer_name() == printer_name
            assert self.get_value_of_presets() == print_default_settings[smart_const.PRINT_SETTINGS.PRESETS]
            assert self.get_value_of_copies() == print_default_settings[smart_const.PRINT_SETTINGS.COPIES]
            assert self.get_value_of_blank_checkbox() == print_default_settings[smart_const.PRINT_SETTINGS.COLOR_BLANK]
            assert self.get_value_of_two_sides_checkbox() == print_default_settings[smart_const.PRINT_SETTINGS.TWO_SIDE]
            assert self.get_value_of_pages() == print_default_settings[smart_const.PRINT_SETTINGS.PAGES]
            assert self.get_value_of_paper_size() == print_default_settings[smart_const.PRINT_SETTINGS.PAPER_SIZE]
            assert self.get_value_of_orientation_vertical() == print_default_settings[smart_const.PRINT_SETTINGS.ORIENTATION]
            assert self.get_value_of_popup_section() == print_default_settings[smart_const.PRINT_SETTINGS.POPUP_SECTION]
        else:
            assert self.get_value_of_printer_name() == printer_name
            assert self.get_value_of_presets() == print_default_settings[smart_const.PRINT_SETTINGS.PRESETS]
            assert self.get_value_of_copies() == print_default_settings[smart_const.PRINT_SETTINGS.COPIES]
            assert self.get_value_of_blank_checkbox() == print_default_settings[smart_const.PRINT_SETTINGS.COLOR_BLANK]
            assert self.get_value_of_two_sides_checkbox() == print_default_settings[smart_const.PRINT_SETTINGS.TWO_SIDE]
            assert self.get_value_of_pages() == print_default_settings[smart_const.PRINT_SETTINGS.PAGES]

    def set_print_settings_default_value(self, is_detail=False, is_local_env=False):
        '''
        This is a method to set the default value on the print dialog.
        :parameter:
        :return:
        '''
        print_default_settings = {}
        if is_local_env:
            # TODO: get from db
            pass
        else:
            print_default_settings[smart_const.PRINT_SETTINGS.PRESETS] = "Default Settings"
            print_default_settings[smart_const.PRINT_SETTINGS.COPIES] = "1"
            print_default_settings[smart_const.PRINT_SETTINGS.COLOR_BLANK] = smart_const.CHECKBOX_VALUE.UNCHECK
            print_default_settings[smart_const.PRINT_SETTINGS.TWO_SIDE] = smart_const.CHECKBOX_VALUE.CHECK
            if is_detail:
                print_default_settings[smart_const.PRINT_SETTINGS.PAGES] = smart_const.CHECKBOX_VALUE.CHECK
                print_default_settings[smart_const.PRINT_SETTINGS.PAPER_SIZE] = "US Letter"
                print_default_settings[smart_const.PRINT_SETTINGS.ORIENTATION] = smart_const.CHECKBOX_VALUE.CHECK
                print_default_settings[smart_const.PRINT_SETTINGS.POPUP_SECTION] = "Media & Quality"
            else:
                print_default_settings[smart_const.PRINT_SETTINGS.PAGES] = smart_const.PAPER_PAGES.ALL

        return print_default_settings
