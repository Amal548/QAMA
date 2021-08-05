from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from SAF.misc import saf_misc
import time


class DigitalCopy(SmartFlow):
    flow_name = "digital_copy"
    ORIGINAL_SIZE = "original_size"
    FIT_TO_PAGE = "fit_to_page"
    FILL_PAGE = "fill_page"
    PAPER_SIZE_LETTER= "digital_paper_size_letter"
    PAPER_SIZE_LEGAL = "digital_paper_size_legal"
    PAPER_SIZE_4X6 = "digital_paper_size_4x6"
    PAPER_SIZE_5X7 = "digital_paper_size_5x7"
    PAPER_SIZE_DRIVER_LICENSE = "digital_paper_size_driver_license"
    PRINTING_SETTINGS_CB = "printing_settings_cb"
    PRINT_PLUGIN_CB = "print_plugin_cb"
    PRINTER_SELECT_CB = "printer_select_cb"
    OPEN_PRINT_SETTINGS = "open_print_settings"
    OPEN_GOOGLE_PLAY = "open_google_play"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_flash_btn(self):
        """
        Click on Flash button on copy type screen
        """
        self.driver.click("flash_btn")

    def select_paper_size(self, paper_size_type):
        """
        Select on Paper size on copy paper size screen
        :param paper_size_type:
        """
        self.driver.wait_for_object("paper_size_btn")
        self.driver.click("paper_size_btn")
        self.driver.click(paper_size_type)
        self.driver.ga_container.insert_ga_key("copy_size_type", self.get_text_from_str_id(paper_size_type))

    def select_resize_btn(self):
        """
        Click on resize button on Copy screen
        """
        self.driver.click("resize_btn")

    def select_resize_type(self,resize_type):
        """
        Click on resize type from the list on copy resize screen
        :param resize_type: ORIGINAL_SIZE FIT_TO_PAGE FILL_PAGE
        """
        self.driver.click(resize_type, change_check={"wait_obj": resize_type, "invisible": True})
        self.driver.ga_container.insert_ga_key("copy_resize_type", self.get_text_from_str_id(resize_type))

    def select_copies_btn(self):
        """
        Click on Copies icon from Copy screen
        """
        self.driver.click("copies_btn")

    def select_num_of_copies(self, copies_num):
        """
        Click on copies number on Copies screen
        :param copies_num:
        """
        self.select_copies_btn()
        self.driver.click("digital_copy_spinner", copies_num)
        self.driver.ga_container.insert_ga_key("number_of_copies", copies_num)

    def select_add_btn(self):
        """
        Click on Add new page icon button
        """
        self.driver.click("add_btn")

    def select_black_copy_btn(self):
        """
        Click on Start Black copy button
        """
        self.driver.click("start_black_copy_btn")

    def select_color_copy_btn(self):
        """
        Click on Start Color copy button
        """
        self.driver.click("start_color_copy_btn")

    def capture_resize_image(self):
        """
        Capture image for resize icon on Copy screen.
        This function is main use for screen comparison before and after choose resize type to make sure choose successfully
        """
        resize_type = self.driver.find_object("resize_icon")
        return saf_misc.load_image_from_base64(resize_type.screenshot_as_base64)

    def select_print_help(self):
        """
        Click on Print Help button from more option icon
        """
        self.driver.wait_for_object("more_option_btn")
        self.driver.click("more_option_btn")
        self.driver.wait_for_object("print_help_btn")
        self.driver.click("print_help_btn", change_check={"wait_obj": "print_help_btn"})

    def toggle_cb_on_print_help(self, cb_name, uncheck=False):
        """
        Toggle the check box on print help screen:
          + Printing settings cb
          + print plugin cb
          + printer select cb
        :param cb_name: class constant variable:
          + PRINTING_SETTINGS_CB
          + PRINT_PLUGIN_CB
          + PRINTER_SELECT_CB
        :param uncheck: True - uncheck, False - check
        """
        self.driver.check_box(cb_name, uncheck=uncheck)

    def select_printer_setup_help_ok_btn(self):
        """
        Click on OK button on Printer Setup Help screen after checked all 3 checkboxes
        """
        self.driver.click("printer_setup_help_ok_btn")

    def select_delete_page_btn(self, num_of_del_pages):
        """
        Click on X button on Copy screen to delete copy page
        :param num: number of clicking delete button
        :return:
        """
        self.driver.wait_for_object("delete_page_button")
        if num_of_del_pages > 0:
            for i in range(num_of_del_pages):
                delete_btn = self.driver.find_object("delete_page_button")
                delete_btn.click()

    def select_previous_page_btn(self):
        """
        Click on Previous page button on Copy screen with multi pages screen
        """
        self.driver.click("previous_page_btn")

    def select_next_page_btn(self):
        """
        Click on Previous page button on Copy screen with multi pages screen
        """
        self.driver.click("next_page_btn")

    def select_link_on_print_help(self, link_name):
        """
        Click on OPen Printing settings link on Print Help screen
        """
        self.driver.click(link_name, change_check={"wait_obj": link_name, "invisible": True})

    def select_ok_btn(self):
        """
        Click on OK button on Digital Copy paper size mismatch screen
        """
        self.driver.click("ok_btn")

    def get_all_nums_of_copies_screen(self):
        """
        Get all copies numbers from Copies page screen:
        """
        self.driver.wait_for_object("digital_copy_spinner")
        copies_number = []
        timeout = time.time() + 20
        while time.time() < timeout:
            page_numbers = self.driver.find_object("digital_copy_spinner", multiple=True)
            for each in page_numbers:
                num_of_copies = each.text
                if num_of_copies not in copies_number:
                    copies_number.append(num_of_copies)
        return copies_number

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_copy_preview_screen(self):
        """
        Verify current screen is copy screen:
            - copy title
            - Start Black button
            - Start Color button
        """
        self.driver.wait_for_object("digital_copy_title")
        self.driver.wait_for_object("start_black_copy_btn")
        self.driver.wait_for_object("start_color_copy_btn")

    def verify_copy_job_finished_screen(self):
        """
        Verify Copy job finished screen with below points:
         +  Title
         + Sent! message
         + Home button
        """
        self.driver.wait_for_object("digital_copy_title", timeout=60)
        self.driver.wait_for_object("sent_message", timeout=60)
        self.driver.wait_for_object("home_btn", timeout=20)

    def verify_resize_mismatch_screen(self):
        """
        Verify current screen is resize is larger than the paper currently loaded in printer screen
        """
        self.driver.wait_for_object("copy_size_original_reduce")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("ok_btn")

    def verify_resize_screen(self):
        """
        Verify resize screen with below options:
         + Original Size
         + Fit to page
         + Fill page
         + Message
        """
        self.driver.wait_for_object("resize_hint")
        self.driver.wait_for_object("original_size")
        self.driver.wait_for_object("fit_to_page")
        self.driver.wait_for_object("fill_page")

    def verify_paper_size_dropbox(self, is_enabled=True):
        """
        Verify Paper Size dropbox is enabled or not
        :param is_enabled
        """
        self.driver.wait_for_object("paper_size_btn")
        paper_size_btn = self.driver.find_object("paper_size_btn")
        if is_enabled != (True if paper_size_btn.get_attribute("enabled").lower() =="true" else False):
            raise AssertionError("Paper Size dropbox doesn't display correctly")

    def verify_previous_next_page_btn(self, invisible=False):
        """
        Verify Previous and Next page button on Copy screen
        """
        self.driver.wait_for_object("previous_page_btn", invisible=invisible)
        self.driver.wait_for_object("next_page_btn", invisible=invisible)

    def verify_copy_page_number(self, invisible=False):
        """
        Verify Copy page number is visible or not on Copy screen
        """
        self.driver.wait_for_object("image_number", invisible=invisible)

    def verify_print_help_screen(self):
        """
        Verify Print Help screen with below points:
          + Title
          + 3 checkboxes
        """
        self.driver.wait_for_object("print_help_btn")
        self.driver.wait_for_object("print_plugin_cb")
        self.driver.wait_for_object("printing_settings_cb")
        self.driver.wait_for_object("printer_select_cb")

    def  verify_ok_button(self, is_enabled=False):
        """
        Check if OK button is enabled or not
        :param is_enabled:
        """
        self.driver.wait_for_object("printer_setup_help_ok_btn")
        ok_btn = self.driver.find_object("printer_setup_help_ok_btn")
        if is_enabled != (ok_btn.get_attribute("enabled").lower() =="true"):
            raise AssertionError("OK button doesn't enable correctly")

    def verify_are_you_sure_popup(self):
        """
        Verify Are you Sure popup screen with below points:
          + Title
          + CANCEL button
          + LEAVE button
        """
        self.driver.wait_for_object("are_you_sure_title")
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("leave_btn")

    def verify_google_play_link(self):
        """
        Verify Google Play store screen with HP Print Service Plugin displayed
        """
        self.driver.wait_for_object("hp_print_plugin")
        self.driver.wait_for_object("hp_icon")

    def verify_paper_size_mismatch_popup(self, raise_e=True):
        """
        Verify Digital Copy paper size mismatch popup
        """
        return self.driver.wait_for_object("digital_copy_original_reduce", raise_e=raise_e)