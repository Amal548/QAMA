# coding=utf-8
from selenium.common.exceptions import TimeoutException

from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import time


class PrintSetting(HPBridgeFlow):

    flow_name = "print_setting"

    def verify_print_setting_page(self):
        """
        Verify if the current page is print settings page or not
        :return: True
        """
        self.driver.wait_for_object("printer_txt")
        page_head = self.driver.get_attribute("print_setting_head","text",raise_e=False)
        page_head_txt = "打印设置"
        if page_head == page_head_txt:
            return True

    def select_printer(self, printer_name):
        """
        Click on the printer section
        :param printer_name: the printer's name you want to select, you can get the name when you bind the printer
        :return:
        """
        self.driver.click("printer_txt")
        self.driver.click("printer_spec", format_specifier=[printer_name])

    def change_copies(self, copies, timeout=60):
        """
        Change the copies on print setting page
        :param: copies eaqual to how many pages user want
        :return:
        """
        count = 1
        start_time = time.time()
        time_used = 0
        while count <= int(copies) and time_used <= timeout:
            self.driver.click("copies_add_icon")
            count += 1
            time_used = time.time() - start_time

        if time_used > timeout:
            raise TimeoutException("Click add copy button timeout, > %s" % timeout)

    def change_two_side_print(self):
        """
        Click on the 2 sided print switch button
        :return:
        """
        if self.get_switch_button_status(0) is False:
            self.driver.click("switch_buttons", index=0)

    def select_collapse_button(self):
        """
        click on the collapse icon to open more selections
        :return:
        """
        self.driver.click("collapse_btn_scrolled")

    def select_color_print(self):
        """
        Click on color print switch button
        :return:
        """
        if self.get_switch_button_status(1) is False:
            self.driver.click("switch_buttons", index=1)

    # This method does not available for photo print
    def select_quality(self, quality_type):
        """
        Select the quality from dropdown menu
        :return:
        """
        quality = self.check_parameter_in_dict(quality_type)
        self.driver.click("quality_option")
        self.driver.wait_for_object("picker_section")
        self.driver.swipe(swipe_object="current_selection", direction="up")
        self.driver.click(quality)
        self.driver.click("confirm_btn")

    def get_default_print_quality(self):
        """
        Get the default quality if available
        """
        return self.driver.get_text("get_default_quality")

    def set_to_default(self):
        """
        Change all settings to a default setting by click the switch button
        :return:
        """
        if self.get_switch_button_status(2) is False:
            self.driver.click("switch_buttons", index=2)

    def change_paper_size(self):
        """
        Change the paper size, option available for photo print
        :return:
        """
        self.driver.click("change_paper_size_menu")

    def select_print(self):
        """
        Click on the print button
        :return:
        """
        self.driver.wait_for_object("print_btn").click()

    # This method does not available for photo print and document print
    def change_paper_type(self):
        """
        Change the type of the paper
        :return:
        """
        self.driver.click("paper_type_selection")

    def close_expanded(self):
        """
        scrolled up the collapsed section
        :return:
        """
        self.driver.wait_for_object("collapse_btn_expanded").click()

    def get_switch_button_status(self, index):
        """
        Get the current status for the switch  button
        :param index: the index for the buttons on the print setting page, 0, 1,2
        :return: True or False
        """
        current_status = self.driver.find_object("switch_buttons", index=index).get_attribute("checked")
        return True if current_status.lower() == "true" else False

    def get_print_file_name(self):
        """
        Get the print file name on print preview page
        :return:
        """
        return self.driver.get_text("print_preview_file_name")

    def click_select_printer_section(self):
        """
        Click on select printer section
        :return:
        """
        self.driver.click("printer_selection_arrow_icon")

    def click_continue_print_btn(self):
        """
        Click on continue print button after previous print job submitted
        :return:
        """
        self.driver.wait_for_object("continue_print_btn").click()
        self.driver.wait_for_object("continue_print_btn", invisible=True)

    def click_return_home_btn(self):
        """
        Click on return to home page button after previous print job submitted
        :return:
        """
        self.driver.wait_for_object("return_home_btn").click()
        self.driver.wait_for_object("return_home_btn", invisible=True)

    def click_top_left_back_btn(self):
        """
        Click on the back button on top left of the print setting screen
        :return:
        """
        self.driver.wait_for_object("top_left_back").click()

    def verify_job_submit_prompt(self):
        """
        Verify the prompt message after click 'Print' button on printer setting page
        :return:
        """
        self.driver.wait_for_object("job_submit_prompt_message")

    def verify_print_job_name(self, file_name):
        """
        Verify the print job name on print setting page is the same as the file name
        :return:
        """
        assert file_name == self.driver.get_attribute("print_file_name", "text", raise_e=False)

    def verify_job_success_submitted_msg(self):
        """
        Verify the job success submitted message after print job sent
        :return:
        """
        self.driver.wait_for_object("job_success_submitted_msg")
        self.driver.wait_for_object("job_success_submitted_other_txt")

    def verify_laserjet_printer_compatibility_msg(self):
        """
        Verify the job success submitted message after print job sent
        :return:
        """
        self.driver.wait_for_object("invoice_compatibility_string")