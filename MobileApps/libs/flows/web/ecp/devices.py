import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ecp.ecp_flow import ECPFlow

class DeviceSearchException(Exception):
    pass

class Devices(ECPFlow):
    flow_name = "devices"
    def verify_device_page(self):
        #self.verify_all_devices_tab()
        #This object make sure the table is loaded
        #Doesn't work if no entries are found
        self.driver.wait_for_object("_shared_table_entries_with_link")

    def verify_all_devices_tab(self):
        return self.driver.wait_for_object("all_devices_tab")
        
    def verify_search_results(self, search_text):
        device_name_index = self.get_header_index("device_name")
        all_devices = self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[device_name_index], multiple=True)
        for device_entry in all_devices:
            if search_text.lower() in device_entry.text.lower():
                continue
            else:
                raise DeviceSearchException("Device entry: " + device_entry.text + " does not contain the search string: " + search_text)
        return True

    def verify_search_device_name_txt(self):
        return self.driver.wait_for_object("search_device_name_txt")

    def search_device(self, dev_name):
        #Currently only pressing enter triggers the search it's probably a bug
        #As there is also a search button that doesn't work
        return self.driver.send_keys("search_device_name_txt", dev_name, press_enter=True)
