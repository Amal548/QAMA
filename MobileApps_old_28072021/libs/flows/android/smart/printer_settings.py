from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging
import time


class PrinterSettings(SmartFlow):
    flow_name = "printer_settings"
    PRINT_ANYWHERE = "print_anywhere_btn"
    PRINT_FROM_OTHER_DEVICES = "print_other_devices_btn"
    SUPPORTED_CARTRIDGES = "supported_supplies_btn"
    PRINTER_DISPLAY_LIGHTS = "printer_display_lights"
    TRAY_PAPER = "tray_paper_btn"
    QUIET_MODE = "quiet_mode_btn"
    PRINTER_REPORTS = "printer_reports_btn"
    PRINT_QUALITY_TOOLS = "print_quality_tools_btn"
    PRINTER_INFO = "printer_info_btn"
    NETWORK_INFO = "network_info_btn"
    ADVANCED_SETTINGS = "advanced_settings_btn"
    REPORT_PRINTER_STATUS = "printer_status_report"
    REPORT_DEMO_PAGE = "demo_page"
    REPORT_NETWORK_CONFIG = "network_configuration"
    REPORT_PRINT_QUALITY = "print_quality_report"
    REPORT_WIRELESS_TEST = "wireless_test_report"
    REPORT_WEB_ACCESS = "web_access_report"


    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_printer_setting_opt(self, opt):
        """
        Click on a option button on My Printer screen which is under HP Instant Ink / Get cartridges button
        :param opt: option button on My Printer. Using class constant:
                PRINT_ANYWHERE
                PRINT_FROM_OTHER_DEVICES
                SUPPORTED_CARTRIDGES
                TRAY_PAPER
                QUIET_MODE
                PRINTER_REPORTS
                PRINT_QUALITY_TOOLS
                PRINTER_INFO
                NETWORK_INFO
                ADVANCED_SETTINGS
        """
        item_name = self.driver.return_str_id_value(opt)
        if "{}_{}".format(self.driver.session_data["language"], self.driver.session_data["locale"] ) == "zh_TW" and\
                item_name[:2] == ' \"' and item_name[-2:] == '\" ':
            item_name = " {} ".format(item_name[2:-2])
        self.driver.scroll("printer_status_txt", "up", format_specifier=[self.driver.return_str_id_value("printer_status_txt")],full_object=False, timeout=60, check_end=False)
        self.driver.scroll("item_title", format_specifier=[item_name], full_object=False, check_end=False)
        self.driver.click("item_title", format_specifier=[item_name], change_check={"wait_obj": "my_printer_view", "invisible": True})

    def get_printer_info(self):
        """
        Get all printer's information on Printer Info/Printer Info following keys:
            - model name
            - serial number
            - service id
            - firmware version
            - printer ip

        Device: Phone
        :return:list of printer information
        """
        titles_list = {self.get_text_from_str_id("model_name_txt"): "model name",
                       self.get_text_from_str_id("serial_no_txt"): "serial number",
                       self.get_text_from_str_id("service_id_txt"): "service id",
                       self.get_text_from_str_id("firmware_ver_txt"): "firmware version",
                       self.get_text_from_str_id("ip_address_txt"): "ip address"}
        printer_info = {}
        self.driver.wait_for_object("printer_info_sv")
        timeout = time.time() + 30
        while len(titles_list) > 0 and time.time() < timeout:
            cells = self.driver.find_object("info_cell", multiple=True)
            for each_cell in cells:
                try:
                    title_txt = self.driver.find_object("info_cell_title", root_obj=each_cell).text
                    value_txt = self.driver.find_object("info_cell_value", root_obj=each_cell).text
                    if title_txt in titles_list:
                        if titles_list[title_txt] not in printer_info:
                            printer_info[titles_list[title_txt]] = value_txt
                        del titles_list[title_txt]
                except NoSuchElementException:
                    logging.info("One cell in Printer Info have no information")
            self.driver.swipe(swipe_object="printer_info_sv", check_end=False)
        return printer_info

    def get_wireless_info(self):
        """
        Get Wireless Information on Network Info following keys:
            - state
            - status
            - bonjour name
            - ip
            - ssid
            - mac address
            - host name
        :return: list of Wireless Info
        """
        titles_list = {self.get_text_from_str_id("wireless_txt"): "state",
                       self.get_text_from_str_id("status_txt"): "status",
                       self.get_text_from_str_id("bonjour_name_txt"): "bonjour name",
                       self.get_text_from_str_id("ip_address_txt"): "ip address",
                       self.get_text_from_str_id("network_name_txt"): "ssid",
                       self.get_text_from_str_id("mac_address_txt"): "mac address",
                       self.get_text_from_str_id("host_name"): "host name"}
        wireless_info = {}
        self.driver.wait_for_object("network_info_gv", timeout=30)
        self.driver.scroll("wireless_txt", direction="up", timeout=10, check_end=False)

        timeout = time.time() + 30
        while len(titles_list) > 0 and time.time() < timeout:
            cells = self.driver.find_object("info_cell", multiple=True)
            for each_cell in cells:
                try:
                    title_txt = self.driver.find_object("info_cell_title", root_obj=each_cell).text
                    value_txt = self.driver.find_object("info_cell_value", root_obj=each_cell).text
                    if title_txt in titles_list:
                        if titles_list[title_txt] not in wireless_info:
                            wireless_info[titles_list[title_txt]] = value_txt
                        del titles_list[title_txt]
                except NoSuchElementException:
                    logging.info("One cell in Printer Info have no information")
            self.driver.swipe( check_end=False)

        # Translate status of state and security to English if mobile device's language is not English
        # Purpose: These information will compare to the information from printer (in English)
        if self.driver.session_data["language"] != "en":
            if wireless_info["state"] == self.get_text_from_str_id("on_txt"):
                wireless_info["state"] = "On".lower()
            else:
                wireless_info["state"] = "Off".lower()
            if wireless_info["status"] == self.get_text_from_str_id("connected_txt"):
                wireless_info["status"] = "Connected"
        return wireless_info

    def get_wifi_direct_info(self):
        """
        Get Wi-Fi Direct's Info on Network Info following keys:
            - state (Status)
            - security
            - passcode
            - name
            - ip address
            - mac address

        :return: list of Wi-Fi Direct Info
        """
        titles_list = {self.get_text_from_str_id("security_txt"): "security",
                       self.get_text_from_str_id("passcode"): "passcode",
                       self.get_text_from_str_id("name_txt"): "name",
                       self.get_text_from_str_id("ip_address_txt"): "ip address",
                       self.get_text_from_str_id("mac_address_txt"): "mac address"}
        wifi_direct_info = {}
        self.driver.wait_for_object("network_info_gv")
        # To make sure, start at top of the Network Information screen
        self.driver.scroll("wifi_direct_txt", timeout=10, check_end=False)

        # Get Status value of wifi direct
        info_groups = self.driver.find_object("network_info_gv", multiple=True)
        for each_group in info_groups:
            try:
                header_txt = self.driver.find_object("info_group_header_title", root_obj=each_group).text
                if header_txt == self.driver.find_object("wifi_direct_txt").text:
                    status_cell = self.driver.find_object("info_cell", multiple=True, root_obj=each_group)[0]
                    wifi_direct_info["state"] = self.driver.find_object("info_cell_value", root_obj=status_cell).text
                    break
            except NoSuchElementException:
                logging.info("This group of network information is NOT Wi-Fi Direct")

        # Get all other information of Wi-Fi Direct if state is on
        if wifi_direct_info["state"] == self.get_text_from_str_id("on_txt"):
            # Make sure first cell is not mac address
            if self.driver.find_object("info_cell_title").text == self.get_text_from_str_id("mac_address_txt"):
                self.driver.swipe(check_end=False)
            timeout = time.time() + 30
            while len(titles_list) > 0 and time.time() < timeout:
                cells = self.driver.find_object("info_cell", multiple=True)
                for each_cell in cells:
                    try:
                        title_txt = self.driver.find_object("info_cell_title", root_obj=each_cell).text
                        if title_txt in titles_list:
                            if title_txt == self.get_text_from_str_id("passcode") and wifi_direct_info["security"] != self.get_text_from_str_id("on_txt"):
                                logging.info("Security of Wi-Fi Direct is off. Skip passcode!")
                            else:
                                value_txt = self.driver.find_object("info_cell_value", root_obj=each_cell).text
                                if titles_list[title_txt] not in wifi_direct_info:
                                    wifi_direct_info[titles_list[title_txt]] = value_txt
                            del titles_list[title_txt]
                    except NoSuchElementException:
                        logging.info("One cell in Printer Info have no information")
                self.driver.swipe(swipe_object="printer_info_sv", check_end=False)


            # Translate status of state and security to English if mobile device's language is not English
            # Purpose: These information will compare to the information from printer (in English)
            if self.driver.session_data["language"] != "en" and self.driver.session_data["language"] != "en-US":
                # Change state to English
                wifi_direct_info["state"] = "on"
                if wifi_direct_info["security"] == self.get_text_from_str_id("on_txt"):
                    wifi_direct_info["security"] = "on"
                else:
                    wifi_direct_info["security"] = "off"
        else:
            wifi_direct_info["state"] = "off"
        return wifi_direct_info

    def select_printer_reports_report_btn(self, report_name):
        """
        Click on one of 5 types of report button
        :param report_name: class constant variable:
                        REPORT_PRINTER_STATUS
                        REPORT_DEMO_PAGE
                        REPORT_NETWORK_CONFIG
                        REPORT_PRINT_QUALITY
                        REPORT_WIRELESS_TEST
                        REPORT_ACCESS_REPORT
        """
        self.driver.click(report_name)

    # *********************************************************************************
    #                          VERIFICATION FLOWS                                     *
    # *********************************************************************************
    def verify_my_printer(self, bonjour_name):
        """
        Verify current screen is My Printer screen via:
            - Bonjour name as title
            - HP Instant innk button
        """
        self.driver.wait_for_object("title",format_specifier=[bonjour_name], timeout=10)
        self.driver.scroll("printer_status_txt", direction="up", format_specifier=[self.driver.return_str_id_value("printer_status_txt")])

    def verify_ready_status(self):
        """
        Verify visible "Ready" status of printer
        """
        self.driver.wait_for_object("ready_txt", timeout=5)

    def verify_print_anywhere_sign_in_screen(self):
        """
        Verify Print Anywhere screen before enabled
            - enable message
            - Sign in button
        """
        self.driver.wait_for_object("print_anywhere_aware_title")
        self.driver.wait_for_object("enable_btn")

    def verify_print_from_other_devices_screen(self):
        """
        Verify current screen is Share Printer screen:
            - title
            - Share this printer button
        """
        self.driver.wait_for_object("share_printer")
        self.driver.wait_for_object("printer_image")
        self.driver.wait_for_object("send_link")

    def verify_printer_report_by_name(self, report_name, invisible=False, raise_e=True):
        """
        Verify each report on Printer Reports screen is visiable or invisible
        :param report_name:
           REPORT_PRINTER_STATUS
           REPORT_DEMO_PAGE
           REPORT_NETWORK_CONFIG
           REPORT_PRINT_QUALITY
           REPORT_WIRELESS_TEST
           REPORT_ACCESS_REPORT
        :param invisible: True or False
        :param raise_e:
        """
        return self.driver.wait_for_object("info_cell_title", timeout=15, format_specifier=[self.driver.return_str_id_value(report_name)], invisible=invisible, raise_e=raise_e)

    def verify_printer_settings_items(self, item_name, invisible=False, raise_e=True):
        """
        Verify the dynamic items on Printer Settings screen is visible or invisible.
        :param item_name: Using constant variable:
           + PRINTER_DISPLAY_LIGHTS
           + TRAY_PAPER
           + QUIET_MODE
           + PRINT_QUALITY_TOOLS
           + PRINT_ANYWHERE
           + ADVANCED SETTINGS
        :param invisible: True or False
        :param raise_e:
        """
        self.driver.scroll("printer_status_txt", "up", format_specifier=[self.driver.return_str_id_value("printer_status_txt")],full_object=False, timeout=30)
        error_message = ""
        try:
            self.driver.scroll("item_title", direction="down", format_specifier=[self.driver.return_str_id_value(item_name)], full_object=False, timeout=30)
            if invisible:
                error_message = u"{} displayed on screen".format(item_name)
        except NoSuchElementException as ex:
            if not invisible:
                error_message = ex.msg
        if error_message:
            if raise_e:
                raise NoSuchElementException(error_message)
            else:
                return False
        return True

    def verify_supported_supplies_webview(self):
        """
        Verify Supported Cartridge Webview (HP Instant ink web site):

        Note: beside english, cannot open this link because it cannot connect to server.
        """
        self.driver.wait_for_object("supplies_webview", timeout=30)








