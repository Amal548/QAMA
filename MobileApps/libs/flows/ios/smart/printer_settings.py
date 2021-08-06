from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
import time
import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException


class PrinterSettings(SmartFlow):
    flow_name = "printer_settings"

    # Printer Settings screen
    DYNAMIC_OPTION_TEXT = "_shared_dynamic_text"
    DYNAMIC_OPTION_BUTTON = "_shared_dynamic_button"
    PS_BACK_BUTTON = "_shared_back_arrow_btn"
    PS_SCREEN_TITLE = "printer_settings_screen_title"
    PS_STATUS_TITLE = "printer_status_title"
    PS_STATUS_READY = "printer_status_ready"
    PS_PRINT_ANYWHERE = "print_anywhere"
    PS_REMOTE_PRINTING = "remote_printing"
    PS_PRINT_FROM_OTHER_DEVICES = "print_from_other_devices"
    PS_SELECT_A_DIFFERENT_PRINTER = "select_a_different_printer"
    PS_SUPPORTED_SUPPLIES = "supported_supplies"
    PS_RENAME_MY_PRINTER = "rename_my_printer"
    PS_TRAY_AND_PAPER = "tray_and_paper"
    PS_QUIET_MODE = "quiet_mode"
    PS_PRINTER_REPORTS = "printer_reports"
    PS_PRINT_QUALITY_TOOLS = "print_quality_tools"
    PS_PRINTER_INFORMATION = "printer_information"
    PS_NETWORK_INFORMATION = "network_information"
    PS_ADVANCED_SETTINGS = "advanced_settings"
    PS_FORGET_THIS_PRINTER = "forget_this_printer"
    SAVE_BUTTON = "_shared_save_btn"
    RENAME_PRINTER_NAME_TEXT_FIELD = "rename_printer_text_field"
    RENAME_PRINTER_CHARACTERS_TEXT = "characters_left_text"
    RENAME_PRINTER_NOTE = "renaming_printer_note"
    SEND_LINK_BUTTON = "send_link_button"
    ON_RADIO_BUTTON = "on_radio_btn"
    OFF_RADIO_BUTTON = "off_radio_btn"
    PRINT_BUTTON = "print_btn"
    PQ_TOOLS_ALIGN_BUTTON = "align_btn"
    PQ_TOOLS_CLEAN_BUTTON = "clean_btn"
    PQ_TOOLS_CLEAN_PRINTHEAD = ["clean_printhead"]
    PQ_TOOLS_ALIGN_PRINTER = ["align_printer"]
    NETWORK_INFO_DIRECT_CONNECTION_NAME = "direct_connection_name"
    NETWORK_INFO_BONJOUR_NAME = "bonjour_name"
    WIFI_DIRECT_FIND_PRINTER_PIN = "find_printer_txt"

    PS_RENAME_PRINTER_UI_ELEMENTS = [
        PS_BACK_BUTTON,
        SAVE_BUTTON,
        RENAME_PRINTER_NAME_TEXT_FIELD,
        RENAME_PRINTER_CHARACTERS_TEXT,
        RENAME_PRINTER_NOTE
    ]

    PS_SCREEN_OPTIONS = [
        PS_BACK_BUTTON,
        PS_STATUS_TITLE,
        PS_STATUS_READY,
        PS_PRINT_FROM_OTHER_DEVICES,
        PS_SELECT_A_DIFFERENT_PRINTER,
        PS_SUPPORTED_SUPPLIES,
        PS_RENAME_MY_PRINTER,
        PS_PRINT_ANYWHERE,
        PS_REMOTE_PRINTING,
        PS_TRAY_AND_PAPER,
        PS_QUIET_MODE,
        PS_PRINTER_REPORTS,
        PS_PRINT_QUALITY_TOOLS,
        PS_PRINTER_INFORMATION,
        PS_NETWORK_INFORMATION,
        PS_ADVANCED_SETTINGS,
        PS_FORGET_THIS_PRINTER
    ]

    TRAY_AND_PAPER_UI_ELEMENTS = [PS_BACK_BUTTON, "tray", "status", "paper_size", "paper_type",
                                  "_shared_cancel", "apply_btn", "advanced_btn"]
    QUITE_MODE_UI_ELEMENTS = [PS_BACK_BUTTON, "apply_btn", "_shared_cancel", "on_radio_btn", "off_radio_btn"]

    PRINTER_REPORTS_UI_ELEMENTS = ["printer_status_title", "demo_page", "network_configuration",
                                   "wireless_test_report", "print_quality_report", "web_access_report"]

    def verify_printer_settings_screen(self, raise_e=False):
        return self.driver.wait_for_object("printer_settings_screen_title", raise_e=raise_e)

    def verify_printer_status(self, status):
        return self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=[status],
                                           raise_e=False) is not False

    def verify_ui_elements(self, ui_elements, button_label=None):
        for element in ui_elements:
            try:
                option_displayed = self.driver.wait_for_object(element)
            except (TimeoutException, NoSuchElementException):
                option_displayed = self.driver.scroll(element, raise_e=False) is not False
            if not option_displayed:
                logging.error(element + " - not displayed/not applicable")
            else:
                if button_label is not None:
                    c = self.driver.find_object(self.DYNAMIC_OPTION_BUTTON,
                                                format_specifier=[self.get_text_from_str_id(element)])
                    if str(c.get_attribute("label")) == str(self.get_text_from_str_id(button_label)) and \
                            str(c.get_attribute("enabled")).lower() == "true":
                        logging.info(c.get_attribute("name") + " - " + button_label + " button enabled")
                    else:
                        logging.error(c.get_attribute("name") + " - " + button_label + " button enabled")

    def verify_printer_status_screen(self, status):
        """
        :param status: Expected Printer Status
        :return:
        """
        if not self.verify_printer_status(status):
            raise Exception("Printer Status is not " + status)
        else:
            self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=[status]).click()
            time.sleep(2)
            ui_elements = ["printer_status_title", "printer_status_ready_text", self.PS_BACK_BUTTON]
            self.verify_printer_status(status)
            self.verify_ui_elements(ui_elements)

    def go_to_print_from_other_devices_screen(self):
        self.driver.scroll(self.PS_PRINT_FROM_OTHER_DEVICES, direction="up").click()
        time.sleep(2)

    def verify_print_from_other_device_screen_ui_elements(self):
        print_from_other_device_screen_ui_elements = ["print_from_other_devices_screen_title",
                                                      "123_hp_com_link", "send_link_btn"]
        self.verify_ui_elements(print_from_other_device_screen_ui_elements)

    def go_to_123_hp_com_page_and_navigate_back(self):
        self.driver.wait_for_object("123_hp_com_link").click()
        time.sleep(2)
        # Verify Print from other devices link opened
        self.driver.wait_for_object(self.DYNAMIC_OPTION_TEXT, format_specifier=['Complete setup using HP Smart'])
        self.driver.wait_for_object("_shared_close").click()
        time.sleep(2)
        self.driver.wait_for_object("print_from_other_devices_screen_title")

    def ps_select_send_link(self, raise_e=True):
        return self.driver.click("send_link_btn", raise_e=raise_e)

    def verify_link_sent_screen_ui_elements(self):
        self.driver.wait_for_object("link_sent")
        self.driver.wait_for_object("send_another_link_btn")

    def select_select_a_different_printer(self):
        self.driver.wait_for_object(self.PS_SELECT_A_DIFFERENT_PRINTER).click()

    def verify_rename_printer_screen(self):
        return self.driver.wait_for_object(self.RENAME_PRINTER_NAME_TEXT_FIELD, timeout=20, raise_e=False) is not False

    def edit_printer_name_and_save(self, name):
        self.driver.long_press(self.RENAME_PRINTER_NAME_TEXT_FIELD)
        self.driver.click("_shared_select_all_btn")
        self.driver.send_keys(self.RENAME_PRINTER_NAME_TEXT_FIELD, name)
        self.driver.wait_for_object(self.SAVE_BUTTON).click()
        time.sleep(2)

    def get_radio_button_value(self, radio_button):
        return self.driver.find_object(radio_button).get_attribute("value")

    def find_ui_element_exists(self, element):
        return self.driver.scroll(element, raise_e=False) is not False

    def select_ui_option(self, ui_option):
        try:
            self.driver.wait_for_object(ui_option, timeout=15)
        except (TimeoutException, NoSuchElementException):
            self.driver.scroll(ui_option, timeout=10)
        self.driver.click(ui_option)
        time.sleep(5)
        if ui_option == self.NETWORK_INFO_DIRECT_CONNECTION_NAME:
            self.driver.wait_for_object("_shared_dynamic_navigation_bar",
                                        format_specifier=["Name"])
        else:
            self.driver.wait_for_object("_shared_dynamic_navigation_bar",
                                        format_specifier=[self.get_text_from_str_id(ui_option)])

    def get_ethernet_status(self):
        if self.driver.scroll("ethernet_info_title", raise_e=False) is not False:
            return str(self.driver.get_attribute("ethernet_status_cell", attribute="label", raise_e=False)).lower()
        else:
            return False

    def verify_title_and_get_value(self, element_title):
        element = self.driver.scroll("network_info", format_specifier=[element_title], raise_e=False)
        if element is not False:
            return str(element.get_attribute("label"))
        else:
            return element

    def verify_ui_option_displayed(self, ui_option):
        return self.driver.wait_for_object(ui_option, raise_e=False) is not False

    def go_to_wi_fi_direct(self):
        self.driver.scroll("wi_fi_direct_txt").click()
        self.driver.wait_for_object("wi_fi_direct_title", timeout=20)