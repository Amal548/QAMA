from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class System_UI(hppsFlow):
    """
        System_UI - All elements within the System UI flow of HPPs. Only reachable through click the Print button in
                    3rd Party apps.
    """
    # Flow_name - Title of the ui map used in this class
    flow_name = "system_ui"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def select_remote_printer(self):
        """
        Select remote printer from search out results in printers list
        :return:
        """
        if self.driver.wait_for_object("remote_printer_model", timeout=20, raise_e=False) is not False:
            self.driver.click("remote_printer_model")

    def select_all_printers(self):
        """
        Opens the drop down list and selects all pritners
        :return:
        """
        self.driver.wait_for_object("select_printer_list_btn", timeout=30).click()
        self.driver.wait_for_object("printers_lv", timeout=10)
        els = self.driver.find_object("printers", multiple=True)
        els[-1].click()

    def select_collapse_button(self):
        """
        clicks the down arrow to open the print options
        :return:
        """
        self.driver.click("print_options_arrow_btn")

    def select_print(self):
        """
        clicks on the print button
        :return:
        """
        self.driver.click("print_btn")

    def change_copies(self, copies):
        """
        change copies to the value given
        :param copies:
        :return:
        """
        copies = int(copies)
        if type(copies) is int and 10 >= copies > 0:

            self.driver.send_keys("copies_edit_txt_field", copies, check_key_sent=False)
        else:
            raise ValueError("copies need to be an int and a value between 1-10")

    def change_color(self, color):
        """
        change color to the value given
        :param color:
        :return:
        """
        color_obj_name = self.check_parameter_in_dict(color)
        self.driver.click("color_list_btn")
        self.driver.click(color_obj_name, change_check={"wait_obj": "print_option_lv", "invisible": True})

    def change_two_sided(self, ds):
        """
        change double sided to the value given
        :param ds:
        :return:
        """
        ds_obj_name = self.check_parameter_in_dict(ds)
        self.driver.click("double_sided_list_btn")
        if not self.driver.wait_for_object(ds_obj_name, raise_e=False):
            self.driver.click("double_sided_list_btn")
        self.driver.click(ds_obj_name, change_check={"wait_obj": "print_option_lv", "invisible": True})

    def change_paper_size(self, paper_size):
        """
        Change paper size to the value given
        :param paper_size:
        :return:
        """
        paper_size_obj_name = self.check_parameter_in_dict(paper_size)
        self.driver.click("paper_size_list_btn")
        self.driver.click(paper_size_obj_name, change_check={"wait_obj": "print_option_lv", "invisible": True})

    def change_orientation(self, orientation):
        """
        Change the orientation to the value given
        :param orientation:
        :return:
        """
        orientation_obj_name = self.check_parameter_in_dict(orientation)
        self.driver.click("orientation_list_btn")
        if not self.driver.wait_for_object(orientation_obj_name, raise_e=False):
            self.driver.click("orientation_list_btn")          
        self.driver.click(orientation_obj_name, change_check={"wait_obj": "print_option_lv", "invisible": True})
    
    
    #def change_of_range_of_pages(self,range_pages):
    #    """
    #    selects the range of pages. (actual we can send any combination of pages selection but test purpose we created three
    #    predefined ranges as start middle and last)
    #    :param range:
    #    :return:
    #    """
    #    self.driver.click("pages_range_button")
    #    self.driver.click("select_range_of_pages")
    #    self.driver.wait_for_object("range_text_field")
    #    self.driver.send_keys("range_text_field", range_pages)


    def select_more_options(self):
        """
        click on the more options button
        :return:
        """
        self.driver.click("more_options_btn", change_check={"wait_obj": "more_options_btn", "invisible": True})

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_system_ui_screen(self, timeout=120):
        """
        verify the system ui screen appeared
        :return:
        """

        self.driver.wait_for_object("summary_content_txt",timeout=timeout)

    def verify_system_ui_print_options_screen(self):
        """
        verify the print drop down options screens
        :return:
        """
        self.driver.wait_for_object("color_list_btn")
        self.driver.wait_for_object("paper_size_list_btn")
        self.driver.wait_for_object("orientation_list_btn")

    def verify_system_ui_preview_screen_with_print_button(self, raise_e = True):
        """
        verify the system ui screen appeared
        :return:
        """
        return self.driver.wait_for_object("print_btn", timeout=60, raise_e=raise_e)

    def does_print_button_disappear(self):
        # There's an known bug that clicking the print btn doesn't register
        # and the btn will disappear for a short period and reappears, several times
        if self.driver.wait_for_object("summary_content_txt", invisible=True, raise_e=False):
            return True
        self.driver.wait_for_object("print_btn", timeout=20, raise_e=False)
        return self.driver.wait_for_object("print_btn", invisible=True, raise_e=False) is not False
