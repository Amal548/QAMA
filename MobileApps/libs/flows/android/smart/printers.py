from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time
import logging

class Printers(SmartFlow):
    flow_name = "printers"

    MY_PRINTER_IS_NOT_LISTED = "my_printer_is_not_listed_txt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_add(self):
        """
        Click on Add icon button on Printers screen
        End of flow: Add Printer screen.
                     Popup display for clicking this button first time.
        """
        try:
            self.driver.click("add_printer_btn")
        except NoSuchElementException:
            self.driver.click("alternative_add_printer_btn")

    def select_looking_for_wifi_direct_printers(self):
        """
        Click on Allow button of Looking for Wi-Fi printers? button
        ENd of flow: Printer screen
                        Note: App Permission display if it is clicked at first time
        """
        self.driver.click("looking_for_wifi_direct_printers_btn")

    def select_search_icon(self):
        """
        Click on Search icon button in Printers page (WiFi-Direct/network printer)
        End of flow: Search screen
        """
        self.driver.click("search_btn", change_check={"wait_obj": "search_btn", "invisible": True})

    def search_printer(self, key_word):
        """
        Enter key_word to text field
        Press enter on virtual key
        :param key_word:
        End of flow: found printer list or empty list
        """
        self.driver.send_keys("search_tf", key_word)

    def select_printer(self, printer_info, wifi_direct=False, is_searched=False, keyword=None, timeout=120):
        """
        Select target printer via its printer's ip address/Wifi-Direct name
        :param printer_info: IP address or Wifi-Direct name of printer
        :param wifi_direct: is Wi-Direct printer screen or not
        :param timeout: timeout for printer list loading and printer is on the list
        """
        logging.info("Select Printer - Printer Info: {} - via Search: {}".format(printer_info, is_searched))
        if wifi_direct:
            self.driver.wait_for_object("wifi_direct_printer_title", timeout=10)
            plist_obj = "wifi_direct_lv"
        else:
            self.driver.wait_for_object("printer_title", timeout=10)
            plist_obj = "printers_lv"
        self.driver.wait_for_object(plist_obj, timeout=timeout)
        logging.info("Waiting for 10 seconds for loading completely...")
        time.sleep(10)
        if is_searched:
            self.select_search_icon()
            self.search_printer(keyword)
            
        self.driver.scroll("printer_status_txt", scroll_object=plist_obj, format_specifier=[printer_info],
                               full_object=False, timeout=timeout, check_end=False)
        try:
            self.driver.click("printer_status_txt", format_specifier=[printer_info], change_check={"wait_obj": plist_obj, "invisible": True})
        except StaleElementReferenceException:
            self.driver.click("printer_status_txt", format_specifier=[printer_info], change_check={"wait_obj": plist_obj, "invisible": True})

    def select_search_printers_popup_continue(self, is_permission=False, raise_e=True):
        """
        Click on Continue button of Search for printers? popup
        ENd of flow: Printer screen
                        Note: App Permission display if it is clicked at first time
        """
        if self.driver.wait_for_object("search_printers_popup_continue_btn", timeout=10, raise_e=raise_e):
            self.driver.click("search_printers_popup_continue_btn")
            if is_permission:
                self.check_run_time_permission(accept=True)

    def dismiss_search_for_printers_popup(self, ga=False):
        """
        Dismiss the popup, 'Search for printers?'
            - Click on Allow button
            - Allow on App Permission popup
        End of flow: Add Printers screen
        """
        try:
            self.driver.wait_for_object("search_printers_popup_title")
            self.select_search_printers_popup_continue()
            self.check_run_time_permission(ga=ga)
        except (TimeoutException, NoSuchElementException):
            logging.info("Search for Printers? popup is not displayed")

    def count_printers(self, wifi_direct=False):
        """
        Count number of found IP/Wifi-Direct printers
        :param wifi_direct: is Wi-Direct printer screen or not
        :return number of printers
        """
        if wifi_direct:
            self.driver.wait_for_object("wifi_direct_lv", timeout=10)
        else:
            self.driver.wait_for_object("printers_lv", timeout=10)
        printer_list = []
        end = False
        timeout = time.time() + 60
        while not end and time.time() < timeout:
            status_els = self.driver.find_object("printer_status_txt", multiple=True)
            for el in status_els:
                if el.text not in printer_list:
                    printer_list.append(el.text)
            time.sleep(5)
            end = self.driver.swipe(check_end=True)[1]
        return len(printer_list)

    # -----------------      Add Printer screen      -------------------------
    def select_my_printer_is_not_listed(self):
        """
        On Android 7/8/9: Click on My print is not listed button
        On Android 10/11: Click on Printer Not Listed? button
        End of flow: Setup new printer screen
        """ 
        if int(self.driver.platform_version) > 9:
            self.driver.click("printer_not_listed_btn")
        else:
            self.driver.click("my_printer_is_not_listed_button")
    
    def select_get_more_help_button(self):
        """
        On Android 10/11 Only: Click on Get More Help button
        End of flow: Setup new printer screen
        """ 
        self.driver.click("get_more_help_button")

    def select_printer_setup_printer_model(self, model):
        """
        Select a printer model in list on Print Setup Instruction screen
        :param model: specific printer model. Random selection if model is empty value
        """
        self.driver.click("select_printer_spinner")
        self.driver.scroll("select_printer_item", scroll_object="select_printer_lists", format_specifier=[model],
                           check_end=False, full_object=False, timeout=90)
        self.driver.click("select_printer_item", format_specifier=[model],change_check={"wait_obj": "select_printer_lists", "invisible": True})

    def select_setup_instruction_link(self, is_network=True):
        """
        Click on instruction link (Setup Mode / Network)
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.click("network_setup_inst_link")
        else:
            self.driver.click("setup_mode_inst_link")

    def select_setup_instruction_popup_ok(self, is_network=True):
        """
        Click on OK button instruction popup
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.click("network_setup_inst_popup_ok_btn")
        else:
            self.driver.click("setup_mode_inst_popup_ok_btn")

    def toggle_setup_instruction_checkbox(self, is_network=True, enable=True):
        """
        Check/uncheck an checkbox
        :param is_network: setup network link (True). False: Setup Mode
        """
        if is_network:
            self.driver.check_box("printer_network_setup_cb", uncheck=not enable)
        else:
            self.driver.check_box("printer_setup_mode_cb", uncheck=not enable)

    def select_printer_setup_try_again(self):
        """
        Click on Try Again button
        """
        self.driver.click("try_again_button")

    def select_print_setup_cancel(self):
        """
        Click on Cancel button
        """
        self.driver.click("cancel_button")

    def select_oobe_printer(self, moobe_name):
        """
        Select OOBE printer on Add Printer screen
        :param moobe_name: moobe name or BLE mac address
        End of flow: Connected to Wifi of Moobe process
        """
        logging.info("OOBE Name: {}".format(moobe_name))
        for _ in range(3):
            self.driver.swipe(direction="up")         # Let list of printer is loaded
            if not self.driver.wait_for_object("printer_status_txt", format_specifier=[moobe_name], raise_e=False, timeout=30):
                continue
            return self.driver.click("printer_status_txt", format_specifier=[moobe_name], change_check={"wait_obj": "add_printer_title", "invisible": True}, raise_e=False)
        raise NoSuchElementException("Fail on selecting oobe printer {} after 3 tries".format(moobe_name))
    
    def select_oobe_awc_printer(self, moobe_name, ssid):
        """
        This flow is used for Select OOBE printer - AWC path on Android 10 and up
            - CLick on Printer not listted button
            - Click on Find printer
            - Click on target printer by moobe name
        """
        self.driver.click("printer_not_listed_btn", timeout=10)
        self.driver.click("find_printer_btn")
        # Based on developer's email.
        # It is system popup for scanning printer, user can quit whenever they want by clicking on cancel.
        # Therefore, no spec for it.
        # Also, 1 mitnute for timeout is valid for wirless discovery based on developer's expectation.
        # Tested with all pritners, 20 seconds is enough. 10 seconds is not enough.
        self.driver.click("printer_oobe_name", format_specifier=[moobe_name], timeout=20)
        self.driver.click("setup_printer_continue_btn")
        self.driver.click("select_network_ssid", format_specifier=[ssid], timeout=10)

    # -----------------      WiFi Direct Printer screen      -------------------------

    def select_connect_to_the_printer(self):
        """
        Click on Connect to the printer on 'Wi-Fi Direct Printer' screen
        End of flow: Connect t "printer name"
        """
        # if pytest.config.getoption("--ga"):
        self.driver.click("wifi_direct_connect_to_printer_button", change_check={"wait_obj": "wifi_direct_connect_to_printer_button", "invisible": True})

    def select_disconnect_to_the_printer(self):
        """
        Select Network printers for printer types
            - Click on Connect to the printer button
        End of flow: Connect to password screen
        """
        self.driver.click("wifi_direct_disconnect_from_printer_button")

    def connect_to_wifi_direct_printer(self, pwd):
        """
        At popup "Connect to <WiFi- Direct name>":
            - Enter password into text field
            - CLick on Connect button
        :param pwd:
        End of flow: Wi-Fi direct Printer screen with loading icon
        """
        self.driver.send_keys("pwd_edit_tf", pwd)
        self.driver.click("pwd_connect_button")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_search_printers_screen(self, is_empty=False, is_wifi_direct=False):
        """
        Verify current screen is searching screen
        :param is_empty: True -> empty list. False: has list
        :param is_wifi_direct: True -> for Wifi Direct. False: for Printer list
        """
        self.driver.wait_for_object("search_tf")
        if is_wifi_direct:
            self.driver.wait_for_object("wifi_direct_connection_status", invisible=is_empty, timeout=10)
        else:
            self.driver.wait_for_object("add_printer_connection_status", invisible=is_empty, timeout=10)

    #-----------------------        PRINTER SCREEN      ---------------------------

    def verify_printers_screen(self, raise_e=True):
        """
        Verify that current screen is Printers screen:
            - Printers title
            - Search icon button
            - Add icon printer
        """
        return bool(self.driver.wait_for_object("printer_title", raise_e=raise_e)) and bool(self.driver.wait_for_object("search_btn", raise_e=raise_e))

    def verify_search_printers_popup(self, raise_e=True):
        """
        Verify current popup is "Search for printers?" popup via:
            - title
            - Continue button
        """
        return self.driver.wait_for_object("search_printers_popup_title", raise_e=raise_e) is not False and \
            self.driver.wait_for_object("search_printers_popup_continue_btn", raise_e=raise_e)

    #-----------------------        WIFI DIRECT PRINTER SCREEN      ---------------------------
    def verify_wifi_direct_printers_screen(self):
        """
        Verify that current screen is Wifi Direct Printers screen:
            - Wifi Direct printers display
        """
        self.driver.wait_for_object("search_btn")
        self.driver.wait_for_object("wifi_direct_printer_title")

    def verify_connect_printers_wifi_direct_screen(self, is_disconnect=False):
        """
        Verify that current screen is Network Printers screen:
            - Wi-Fi Direct Printer description
            - Connect to the printer button
            - Disconnect button is is_disconnect = True
        :param is_disconnect: True: visible disconnect btn. False: invisible disconnect
        """
        self.driver.wait_for_object("wifi_direct_desc")
        self.driver.wait_for_object("wifi_direct_connect_to_printer_button")
        self.driver.wait_for_object("wifi_direct_disconnect_from_printer_button", invisible= not is_disconnect)

    def verify_visible_wifi_direct_wrong_pwd_txt(self):
        """
        Verify that 'Something might be wrong with your password.' is visible
        """
        self.driver.wait_for_object("wifi_direct_wrong_pwd_txt", timeout=60)

    def verify_setup_authentication_screen(self):
        """
        Verify that current screen is Wireless Password popup:
            - Enter pwd field
            - Cancel button
            - Connect button
        """
        self.driver.wait_for_object("pwd_edit_tf")
        self.driver.wait_for_object("pwd_cancel_button")
        self.driver.wait_for_object("pwd_connect_button")

    #-----------------------        ADD PRINTERS SCREEN      ---------------------------

    def verify_add_printers_screen(self):
        """
        Verify Add Printer screen with no printer on the list via: 
            - If platform is Android 9 or lower, then verify Add Printer title.
            - 'There are no printers in Setup Mode' text
        Note: This screen only for Android 7/8/9. Android 10 or higher, please refer verify_printer_setup_screen() for details
        """
        self.driver.wait_for_object("add_printer_title")
        self.driver.wait_for_object("my_printer_is_not_listed_button")
    
    def verify_printer_setup_screen(self, timeout=10):
        """
        Verify Printer Setup screen with no printer on the list via:
            - Verify Printer Setup title
            - Printer Not Listed? button
        Note: This function for Android 10 or higher
        """
        self.driver.wait_for_object("printer_setup_title")
        self.driver.wait_for_object("printer_not_listed_btn", timeout=timeout)

    def verify_add_printers_list(self, is_empty=False):
        """
        Verify Add Printers has printers on list or empty list
        :param is_empty: True -> empty list. False: has printer on list
        """
        if int(self.driver.platform_version) > 9:
            self.verify_printer_setup_screen()
        else:
            self.verify_add_printers_screen()
        if is_empty:
            self.driver.wait_for_object("add_printer_no_printers_txt")
        else:
            self.driver.wait_for_object("add_printer_lv")

    def verify_setup_printers_instruction_screen(self):
        """
        Verify that current screen is Setup Printer Instruction screen
            - Try again button
            - Cancel button
        """
        self.driver.wait_for_object("select_printer_spinner")
        self.driver.wait_for_object("try_again_button")
        self.driver.wait_for_object("cancel_button")

    def verify_my_printer_not_listed_help_msg(self):
        """
        Verify my printer not listed help text on Setup printers screen after clicking -My printer is not listed-
        """
        self.driver.wait_for_object("printer_not_listed_help_text")

    def verify_my_printer_setup_instruction(self):
        """
        Verify that current screen is printer setup screen with instruction:
            + checkbox for "Make sure printer is in Setup Mode" display
            + checkbox for "Make sure you know your network name and password" display
            + How do I do this? link display (2 links)
        """
        self.driver.wait_for_object("printer_setup_mode_cb")
        self.driver.wait_for_object("setup_mode_inst_link")
        self.driver.wait_for_object("printer_network_setup_cb")
        self.driver.wait_for_object("network_setup_inst_link")

    def verify_setup_instruction_link_popup(self, is_network=False):
        """
        Verify a popup after click the setup instruction link
        :param is_network: True: from network link. False: from setup mode link
        """
        if is_network:
            self.driver.wait_for_object("network_setup_inst_popup_title")
        else:
            self.driver.wait_for_object("setup_mode_inst_popup_title")

    def verify_try_again_button(self, is_enabled=False):
        """
        check if the button "Try Again" is enabled or not
        :param is_enabled:
        """
        self.driver.wait_for_object("try_again_button")
        try_btn = self.driver.find_object("try_again_button")
        current_status = True if try_btn.get_attribute("enabled").lower() == "true" else False
        if is_enabled != current_status:
            raise NoSuchElementException("Try Button is not matched with expected status {}".format(is_enabled))