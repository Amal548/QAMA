import time
from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class All_Printers(hppsFlow):
    """
    All_Printers - Contains all elements within the All Printers screen. This screen only appears when a user need to
                   select a printer from the system ui flow by selecting all printers in the printer drop down list.
    """

    # Flow_name - Title of the ui map used in this class
    flow_name = "all_printers"
    ###############################################################################
    #                         Action Flows                                        #
    ###############################################################################
    def select_printer(self, bonjour_name, is_searched=True, timeout=120):
        """
        Select a printer on All printer list or via searching
        :param bonjour_name: bonjour name of printer
        :param is_searched: using searching or scrolling to printer for selection
        :param timeout: timeout for selecting on the list
        """
        if is_searched:
            self.select_search()
            self.driver.send_keys("search_tf", bonjour_name)
        
        self.driver.wait_for_object("printers_lv", timeout=timeout)
        timeout = time.time() + timeout
        while time.time() < timeout:
            printer_cells = self.driver.find_object("printer_cell_linear_layout", multiple=True)
            # printer_cells = self.driver.find_object("printer_cell", multiple=True)
            for printer in printer_cells:
                try:
                    # Make sure printer element is for HPPS
                    if not self.driver.wait_for_object("printer_cell_more_info", root_obj=printer, timeout=5, raise_e=False):
                        continue
                    self.driver.wait_for_object("printer_cell_title", format_specifier=[bonjour_name], root_obj=printer)
                    self.driver.wait_for_object("printer_cell_subtitle",
                                            format_specifier=[self.get_text_from_str_id("_shared_hp_print_service_title")],
                                            root_obj=printer)                          
                    printer.click()
                    if not self.driver.wait_for_object("search_tf", invisible=True, timeout=3, raise_e=False):
                        printer.click()
                    return True
                except NoSuchElementException:
                    continue
            self.driver.swipe()
        raise TimeoutException("Cannot select printer ({}) in {} seconds".format(bonjour_name, timeout))

    def select_search(self):
        """
        Click on the search button
        :return:
        """
        self.driver.click("search_btn")

    ###############################################################################
    #                         Verification Flows                                  #
    ###############################################################################
    def verify_all_printers_screen(self, raise_e=True):
        """
        verify the All Printer screen loaded
        :return:
        """
        return self.driver.wait_for_object("search_btn", timeout=5, raise_e=raise_e)

    def search_remote_printer(self):
        self.select_search()
        self.verify_all_printers_screen()
        self.driver.send_keys("remote printer")