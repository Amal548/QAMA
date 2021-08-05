from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import logging

from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Printers(SmartFlow):
    flow_name = "printers"

    ####################################################################################################################
    #                                Printers - Add Printer button screen                                              #
    ####################################################################################################################
    def verify_printers_list_screen_ui(self):
        self.verify_printers_nav()
        self.verify_add_printers_btn()
        self.verify_back_arrow_btn()
        self.verify_printers_list()

    def verify_printers_list(self):
        self.driver.wait_for_object("printers_tv")

    def verify_add_printers_btn(self, raise_e=True):
        return self.driver.wait_for_object("add_printer_btn", raise_e=raise_e)

    def verify_printers_nav(self, raise_e=True):
        """
        Verify Printers screen navigation bar title
        """
        return self.driver.wait_for_object("printers_title", raise_e=raise_e)

    def verify_add_printer_screen(self):
        """
        Verify Add Printer Screen
        """
        self.driver.wait_for_object("add_printer_using_ip_btn")

    def verify_search_bar(self):
        """
        search bar on the printer list screen
        """
        return self.driver.wait_for_object("search_box")

    def verify_clear_text_button(self):
        """
        verify the small x button on search bar
        """
        return self.driver.wait_for_object("_shared_clear_text_btn")

    def verify_connect_the_printer_screen(self):
        """
        Verify the Connect the Printer screen
        """
        self.driver.wait_for_object("connect_the_printer_txt")

    def select_search_bar(self):
        self.verify_search_bar().click()

    def select_clear_text_button(self):
        self.verify_clear_text_button().click()

    def find_printer_using_search_bar(self, printer_str):
        """
        :param printer_str: name of the printer or ip address
        """
        self.driver.send_keys("search_box", printer_str)

    def verify_printer_in_list(self, printer_str, timeout=10, raise_e=True):
        """
        :param printer_str: ip or bonjour name of the printer
        """
        return self.driver.wait_for_object("dynamic_printer_cell", format_specifier=[printer_str], timeout=timeout, raise_e=raise_e)

    def select_printer_in_list(self, printer_str):
        self.verify_printer_in_list(printer_str).click()

    def count_number_of_printers(self):
        """
         gives the number of printers available in printer list
            dynamically changes but count approx before we click next button,
                keep this dynamic GA as special case, we will get mismatch in count but will be a subset
        :return: number of items on printer list
        """
        ## GA Purpose
        printers = self.driver.find_object("printers_cell", multiple=True)
        dynamic_ga_key_value = str(len(printers))
        logging.info("the availabel printers are {}".format(dynamic_ga_key_value))
        self.driver.ga_container.insert_ga_key("available_printers_count_dynamic_ga", dynamic_ga_key_value)

        self.driver.wait_for_object("printers_cell")
        return len(printers)

    def search_for_printer(self, query):
        self.driver.swipe(direction="up", per_offset=0.6)
        self.driver.send_keys("search_box", query)

    def select_moobe_printer_from_list(self, printer_name, attempt=20):
        for i in range(attempt):
            try:
                self.driver.wait_for_object("moobe_printer", format_specifier=[printer_name]).click()
                break
            except TimeoutException:
                if i == attempt-1:
                    raise TimeoutException("Could not find moobe printer")
                else:
                    logging.info("Could not find moobe printer, try#: {}".format(i+1))

    def search_for_printer_directly_using_ip(self,name):
        """
        Enters ip address into the text field and clicks done to search for a printer
        :param ip:String, ip address
        :return:
        """
        self.driver.click("enter_ip_address")
        self.driver.send_keys("enter_ip_address",name, press_enter=True)
        time.sleep(2)
    
    def select_is_this_your_printer(self, yes=True):
        if yes:
            self.driver.wait_for_object("is_this_your_printer_yes_btn", timeout=30).click()
            time.sleep(3)
        else:
            self.driver.wait_for_object("_shared_no").click()

    ####################################################################################################################
    #                   Printers - setup new printer OR connect to previously used printer                             #
    ####################################################################################################################
    def verify_printers_setup_screen_ui(self):
        self.driver.wait_for_object("set_up_new_printer_btn")
        self.driver.wait_for_object("add_printer_using_ip_btn")
        self.driver.wait_for_object("supported_printer_btn")
        self.driver.wait_for_object("connect_to_previously_used_printer_btn")
        self.verify_printers_nav()
        self.verify_back_arrow_btn()
    
    def select_set_up_a_new_printer(self):
        self.driver.wait_for_object("set_up_new_printer_btn").click()

    def select_add_printer_using_ip(self):
        """
        Selects the add printer using ip address button
        """
        self.driver.click("add_printer_using_ip_btn")

    def select_supported_printers_btn(self):
        """
        Clicks on the Supported printers button
        """
        self.driver.click("supported_printer_btn")

    def select_connect_to_previously_used_printer(self):
        """
        Clicks on the Connect to a previously used printer button on the empty printer list screen
        """
        self.driver.click("connect_to_previously_used_printer_btn")

    def select_add_printer(self):
        """
        select the add printer button on printers page [big list of printers,
        """
        self.verify_add_printers_btn().click()
    
    def select_printer_from_printer_list(self, printer_ip, timeout=120):
        """
        Select a printer according to its printer's ip address.
        Steps:
            - Scroll down printer list to target printer. IF not see, scroll up one time
            - Click on target printer
        End of flow: Printer Info screen of target printer
        :param printer_ip: printer's ip address
        """
        self.driver.wait_for_object("printers_tv", timeout=10)
        target_printer = self.driver.scroll("printer_ip", format_specifier=[printer_ip],
                                            full_object=False, timeout=timeout, check_end=False)
        # if it is not found for scrolling down, scroll up for finding one more time.
        if not target_printer:
            target_printer = self.driver.scroll("printer_ip", direction="up", format_specifier=[printer_ip],
                                                full_object=False, timeout=timeout, check_end=False)
        target_printer.click()

    def verify_bluetooth_on_by_invisible_popup(self):
        """

        :return:
        """
        self.driver.wait_for_object("connect_bluetooth_popup_title", invisible=True)

    def verify_connect_bluetooth_popup(self):
        """
        Verify current popup is "Connect using Bluetooth popup"
            - title
            - Close button
        """
        self.driver.wait_for_object("connect_bluetooth_popup_title")

    def is_connect_using_bluetooth_popup(self):
        """
        Checks if the current screen contains the bluetooth popup and dismisses it
        :return:
        """
        if self.verify_bluetooth_on_by_invisible_popup():
            logging.warning("Device-blue tooth is ON --Current Screen did NOT contain the Bluetooth Popup")
        else:
            try:
                self.verify_connect_bluetooth_popup()
                self.driver.click("connect_bluetooth_popup_close_btn")
            except TimeoutException:
                logging.warning("Current Screen did NOT contain the Bluetooth Popup")

    def select_get_connection_help(self):
        """
        Clicks on Get Connection help button on the wifi off screen
        :return:
        """
        self.driver.click("get_connection_help_btn")

    def select_learn_more(self):
        """
        Selects the learn more button on the wifi off screen
        :return:
        """
        self.driver.click("learn_more_btn")

    def verify_printer_list_wifi_off(self):
        """
        Verifies that the wifi off screen is displayed
        :return:
        """
        time.sleep(10)
        self.driver.wait_for_object("get_connection_help_btn")
        self.driver.wait_for_object("learn_more_btn")

    def verify_printer_list_empty(self):
        """
        Verify tha the printer list is displaying the empty printer list screen
        :return:
        """
        self.driver.wait_for_object("set_up_a_new_printer_btn")
        self.driver.wait_for_object("connect_to_previously_used_printer_btn")

    def select_set_up_a_new_printer_via_empty_printer_list(self):
        """
        Clicks on the Set up a new printer button on the empty printer list
        :return:
        """
        self.driver.click("set_up_a_new_printer_btn")

    def select_add_printer_using_ip_via_empty_printer_list(self):
        """
        SElects the add printer using ip address button
        :return:
        """
        self.driver.click("add_printer_using_ip_btn")

    def add_printer_ip(self, printer_ip):
        self.verify_printers_nav()
        if not self.verify_add_printers_btn(raise_e=False) is not False:
            self.driver.wait_for_object("connect_using_ip_address").click()
        else:
            self.select_add_printer()
            self.verify_add_printer_screen()
            self.select_add_printer_using_ip()
        self.verify_connect_the_printer_screen()
        self.search_for_printer_directly_using_ip(printer_ip)
        if self.driver.wait_for_object("printer_limited_support_pop_title_txt", raise_e=False) is not False:
            self.driver.click("_shared_str_ok")
        self.select_is_this_your_printer()

    def select_a_diff_printer(self, printer_name):
        printer_list = self.driver.find_object("printer_cell_visible", multiple=True)
        for printer in printer_list:
            displayed_printer_name = printer.text
            if displayed_printer_name != printer_name:
                self.driver.click("dynamic_printer_cell", format_specifier=[displayed_printer_name])
                logging.info("Printer selected- {}".format(displayed_printer_name))
                break

    def verify_automatically_put_device_on_network(self):
        self.driver.wait_for_object("connect_automatically_logo", displayed=False)

    def verify_found_printer_for_setup(self, bonjour_name):
        self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[
                self.get_text_from_str_id("found_printer_for_setup").replace("%@", bonjour_name)])

    ####################################################################################################################
    #                                                   Printer Connection                                             #
    ####################################################################################################################
    def verify_printer_connection_screen_ui(self, back_btn=True):
        self.driver.wait_for_object("printer_connection_navbar_title")
        self.driver.wait_for_object("how_do_i_do_this_link")
        self.driver.wait_for_object("follow_instructions_txt")
        self.driver.wait_for_object("check_printer_txt")
        self.driver.wait_for_object("check_printer_details_txt")
        self.driver.wait_for_object("check_network_conn_txt")
        if int(self.driver.platform_version) == 14:
            self.driver.wait_for_object("check_network_details_txt_os14")  
        else:
            self.driver.wait_for_object("check_network_details_txt")
        self.driver.wait_for_object("restart_router_txt")
        self.driver.wait_for_object("restart_router_details_txt")
        self.driver.wait_for_object("try_again_btn")
        self.driver.wait_for_object("get_more_help_link")
        self.driver.wait_for_object("contact_HP_on_facebook_messenger_link")

    def verify_connect_the_printer_screen_ui(self):
        self.verify_connect_the_printer_screen()
        self.verify_back_arrow_btn()
        self.driver.wait_for_object("enter_ip_address")
    
    def verify_enable_local_network_permission_blocker_screen(self):
        self.driver.wait_for_object("enable_local_network_blocker_screen")
