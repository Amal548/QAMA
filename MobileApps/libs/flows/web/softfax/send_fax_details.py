from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
from selenium.common.exceptions import NoSuchElementException


class SendFaxDetails(SoftFaxFlow):
    flow_name = "send_fax_details"

    PRINT_CONFIRMATION_BTN = "print_confirmation_btn"
    HOME_BTN = "home_btn"
    RETRY_FAX_BTN = "retry_fax_btn"
    EDIT_RESEND_BTN = "edit_resend_btn"
    CANCEL_FAX_BTN = "cancel_fax_btn"
    MENU_DELETE_BTN = "menu_delete_btn"
    MENU_SAVE_LOG_BTN = "menu_save_log_btn"
    MENU_HOME_BTN = "menu_home_btn"
    MENU_EDIT_FORWARD_BTN = "menu_edit_forward_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_bottom_button(self, button_name):
        """
        Click on a bottom button by name
        :param button_name: using class constant
                PRINT_CONFIRMATION_BTN
                HOME_BTN
                RETRY_FAX_BTN
                EDIT_RESEND_BTN
                CANCEL_FAX_BTN
        """
        self.driver.click(button_name)

    def click_menu_btn(self, button_name):
        """
        Click on a button in menu list
            - CLick on 3 dots button
            - Click on button in menu
        :param button_name: use class constant
                MENU_DELETE_BTN
                MENU_SAVE_LOG_BTN
                MENU_HOME_BTN
        """
        self.driver.click("3_dots_menu_btn")
        self.driver.click(button_name, change_check={"wait_obj": button_name, "invisible": True})

    def dismiss_delete_confirmation_popup(self, is_yes=True):
        """
        Dismiss Are you sure? popup by clicking on Cancel or Delete button
        :param is_yes: click on Delete button -> True.
                       click on Cancel button -> False
        """
        self.driver.wait_for_object("delete_confirmation_popup_cancel_btn")
        self.driver.wait_for_object("delete_confirmation_popup_delete_btn")
        if is_yes:
            self.driver.click("delete_confirmation_popup_delete_btn")
        else:
            self.driver.click("delete_confirmation_popup_cancel_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_send_fax_detail_screen(self, invisible=False):
        """
        Verify current screen is Send Fax Detail screen
        Note: Use to check whether current screen is Send Fax Details
        """
        self.driver.wait_for_object("title", invisible=invisible)
        self.driver.wait_for_object("3_dots_menu_btn", invisible=invisible)

    def verify_send_fax_status(self, timeout=240, is_successful=True, check_sending=True):
        """
        Verify Send Fax successfully screen
        :param timeout: maximum time for sending fax
        :param is_successful: True -> successful job. False -> failed job
        :param check_sending: before send status, True -> check sending status. False -> skip checking sending status
                              It is used to check send fax status after clicking on Send Fax button on Compose screen
        """
        self.verify_send_fax_detail_screen()
        if check_sending:
            self.driver.wait_for_object("sending_status", invisible=False, timeout=60)
            self.driver.wait_for_object("sending_status", invisible=True, timeout=timeout)
        if is_successful:
            self.driver.wait_for_object("fax_delivered_status", timeout=10 if check_sending else timeout)
        else:
            self.driver.wait_for_object("delivery_failed_status", timeout=10 if check_sending else timeout)

    def verify_phone_number(self, phone_number):
        """
        Verify existed phone number on this screen
        :param phone_number: expected phone number
        """
        actual_phone =self.driver.find_object("to_phone_number").text
        actual_phone = actual_phone[actual_phone.find("+"):]
        if actual_phone != phone_number:
            raise ValueError ("{} is not displayed on screen. Actual: {}".format(phone_number, actual_phone))

    def verify_time_information(self, is_successful=True, check_end=True):
        """
        Verify Start and Finished/Failed time on screen
        :param is_successful: True -> Finish time. False -> Failed time
        """
        self.driver.wait_for_object("started_time", timeout=10)
        if check_end:
            obj = "finished_time" if is_successful else "failed_time"
            self.driver.wait_for_object(obj, timeout=10)

    def verify_file_information(self, file_name, number_page):
        """
        Verify file name and number page on screen
        :param file_name: expected file name
        :param number_page: expected number page
        """
        actual_name = self.driver.find_object("file_name").text
        actual_number = self.driver.find_object("file_number_pages").text
        if (file_name != actual_name) or (number_page != actual_number):
            raise ValueError("{} or {} are not displayed on screen. Actual: {} or {}".format_map(file_name, number_page, actual_name, actual_number))

    def verify_bottom_btn(self, button_names):
        """
        Verify visible bottom buttons by name
        :param button_names: list  of buttons or string for 1 button. The value of each button is following class constant
                PRINT_CONFIRMATION_BTN
                HOME_BTN
                RETRY_FAX_BTN
                EDIT_RESEND_BTN
                CANCEL_FAX_BTN
        """
        button_names = [button_names] if isinstance(button_names, str) else button_names
        for button in button_names:
            self.driver.wait_for_object(button, timeout=10)

    def verify_menu_save_fax_log(self, invisible=False):
        """
        Verify invisible/visible menu save fax log
        :param invisible:
        """
        self.driver.wait_for_object("menu_save_log_btn", invisible=invisible, timeout=10)