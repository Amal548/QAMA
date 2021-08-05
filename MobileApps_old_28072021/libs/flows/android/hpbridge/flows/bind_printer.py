# coding=utf-8

from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption, PrinterStatus, GroupName
from time import sleep
import logging


class BindPrinter(HPBridgeFlow):
    flow_name = "bind_printer"

    def verify_printer_status(self, printer_status):
        """
        check the printer status as expected
        :param printer_status: the expected printer status
        :return:
        """
        self.driver.wait_for_object("printer_status", timeout=30)
        status = self.driver.get_attribute("printer_status", "text")
        assert status == printer_status

    def verify_default_printer_name(self, printer_name=None):
        """
        Check the printer default name, if never changed, the printer name should be the same as printer model name
        :param printer_name: the expected printer name, if None, compared with printer model name
        :return:
        """
        self.driver.wait_for_object("group_bedroom", timeout=30)
        default_printer_name = self.driver.get_attribute("printer_name", "text")
        printer_model_name = self.driver.get_attribute("printer_model_name", "text")
        if printer_name is not None:
            assert default_printer_name == printer_name
        else:
            assert default_printer_name == printer_model_name

    def change_printer_name(self, printer_name):
        """
        Customise the printer name, there are four default printer name options
        :param printer_name: the print name you want to input, if you set it to the one of the default options,, it will
        choose the corresponding button, otherwise, it will set to your customised printer name
        :return:
        """
        self.click_edit_pencil_icon()
        if printer_name is PrinterNameOption.HOME.value:
            self.driver.click("name_options_home")
        elif printer_name is PrinterNameOption.OFFICE.value:
            self.driver.click("name_options_office")
        elif printer_name is PrinterNameOption.FRIEND.value:
            self.driver.click("name_options_friend")
        elif printer_name is PrinterNameOption.PUBLIC.value:
            self.driver.click("name_options_public")
        else:
            self.enter_value_into_text_field(printer_name)
            '''
            self.driver.wdvr.keyevent(66)
            self.driver.wdvr.press_keycode(66)
            '''
            self.click_binding_btn()  # this step will be replaced by above one once the above one works

    def click_edit_pencil_icon(self):
        """
        Click on the pencil icon to edit the printer name
        :return:
        """
        self.driver.wait_for_object("change_printer_name", timeout=25)
        self.driver.click("change_printer_name")

    def enter_value_into_text_field(self, printer_name):
        """
        Enter strings into the customize printer name field
        :return:
        """
        self.driver.click("input_box")
        self.driver.send_keys("input_box", printer_name, press_enter=True)  # send keys does not work currently

    def get_printer_name(self):
        """
        Get the printer name on binding printer page
        :return:
        """
        return self.driver.get_attribute("printer_name", "text")

    def verify_printer_name(self, printer_name):
        """
        Verify if the printer name on the page is the same as the given name
        :return:
        """
        assert printer_name == self.get_printer_name()

    def click_binding_btn(self):
        """
        Click on binding printer button
        :return:
        """
        self.driver.click("binding_btn")

    def click_add_btn(self):
        """
        Click on the '+' button to add a group on binding printer page
        """
        self.driver.wait_for_object("add_group", timeout=15)
        self.driver.click("add_group")

    def add_group(self, group_name):
        """
        Add a new customized printer group while binding the printer. the new group will be selected as default after added.
        :param group_name: the customized printer group name, the length of group_name should no more than 5
        :return:
        """
        # if len(group_name) > 5:
        #     raise Exception("the length of input group name should no more than 5")
        self.click_add_btn()
        self.driver.wait_for_object("add_group_complete")
        self.driver.send_keys("input_box", group_name)
        self.driver.click("add_group_complete")
        sleep(1)

    def add_more_groups(self, group_num=5):
        """
        The group limit is 8, there are 3 defaults one, so set the default to 5. The group name are random generate
        :return:
        """
        for i in range(group_num):
            self.add_group(RandomUtility.generate_digit_letter_strs(5))
        logging.info("The total group limit is 8, current total is %d, prompt message will pop-out if more than 8"
                     % (3 + group_num))

    def remove_group(self, group_name):
        """
        Remove a new added group, the default groups cannot be removed
        :param group_name:
        :return:
        """
        remove_group = self.driver.find_object("remove_group_name", format_specifier=[group_name])
        self.driver.long_press(remove_group)
        self.driver.click("remove_group_button", format_specifier=[group_name])
        self.driver.wait_for_object("remove_group_name", format_specifier=[group_name], invisible=True)

    def select_a_group(self, group_name):
        """
        Select a group on binding printer page
        :param group_name: select a group than user want the printer to be
        """
        self.driver.wait_for_object("which_group", format_specifier=[group_name]).click()

    def bind_printer(self, bound=True):
        """
        Click the "绑定打印机" button to bind the printer, from s
        :param bound: if the printer is bound or you don't know it is already bound, please set it to True,
        otherwise, we treat it as not bound before
        :return:
        """
        if not bound or self.driver.wait_for_object("binding_btn", raise_e=False, timeout=1):
            self.driver.click("binding_btn")
            self.driver.wait_for_object("success_msg")
            self.driver.wait_for_object("success_img")

        self.click_start_print_btn()
        # self.driver.click("start_print_btn", change_check={"wait_obj": "file_print", "invisible": True,
        #                                                    "format_specifier": [], "flow_change": "mp_home"})
        self.driver.wait_for_object("mp_loading_icon", timeout=3, raise_e=False)
        self.driver.wait_for_object("mp_loading_icon", invisible=True)

    def click_start_print_btn(self):
        """
        Click on "start print" button after successful binding a printer page
        """
        self.driver.click("start_print_btn")

    def click_how_to_bind_url(self):
        """
        Click on how to bind a printer on prompt message after scanned a re-set QR code
        """
        self.driver.click_element_by_offset("printer_reset_string", x=0.6, y=0.7)

    def is_printer_ready(self):
        """
        Check if the printer is ready to print or not
        :return: if printer status return True, otherwise return the printer status
        """
        printer_status = self.driver.find_object("printer_status_strings").get_attribute("text")
        if printer_status == PrinterStatus.SEARCHING.value:
            self.driver.wait_for_object("printer_status_placeholder",
                                        format_specifier=[PrinterStatus.SEARCHING.value], invisible=True)
            printer_status = self.driver.find_object("printer_status_strings").get_attribute("text")
        if printer_status == PrinterStatus.READY.value:
            return True
        elif printer_status == PrinterStatus.OFFLINE.value:
            logging.warning("The printer is offline, please check the printer")
            return printer_status
        elif printer_status == PrinterStatus.RESET.value:
            logging.warning("The printer has been reset")
            return printer_status
        elif PrinterStatus == PrinterStatus.NOT_AVAILABLE:
            logging.warning("The printer status is not available")
            return printer_status
        else:
            logging.warning("The printer status is unknown")
            return printer_status

    def verify_kind_remind_message(self):
        """
        Verify the kind remind message when user is not the administrator of the printer
        """
        self.driver.wait_for_object("kind_remind_message")

    def click_reset_printer_webservice_url(self):
        """
        Click on reset printer webservice URL
        """
        self.driver.swipe()
        self.driver.click_element_by_offset("reset_printer_web_service_url", x=0.65, y=0.5)

    def verify_printer_reset_string(self):
        """
        Verify a reset printer strings when trying to bind a printer with a re-set printer QR code
        :return:
        """
        self.driver.wait_for_object("printer_reset_string", timeout=15, raise_e=True)

    def get_binding_printer_button_status(self):
        """
        Verify the binding printer button is disabled after scanned a invalid(reseted) QR code
        :return:
        """
        assert not self.driver.find_object("binding_btn").is_enabled()

    def verify_qr_code_error_message(self):
        """
         Verify the error message after scan a bad QR code(not a printer QR code) from mini program
        :return:
        """
        self.driver.wait_for_object("qr_code_error_message")

    def verify_invalid_character_strings(self):
        """
        Verify the strings after user entered invalid character for customize the printer name
        :return:
        """
        self.driver.wait_for_object("invalid_character_prompt_message", timeout=5, raise_e=True)

    def verify_binding_printer_btn_status(self):
        """
        Verify the binding printer button enabled or not
        :return:
        """
        assert not self.driver.find_object("binding_btn").is_enabled()

    def verify_prompt_message_add_group(self):
        """
        Verify the prompt message for add a long name for a group
        :return:
        """
        self.driver.wait_for_object("long_printer_name_prompt_message")

    def verify_same_name_prompt_message(self):
        """
        The prompt message after entered the same name for a group
        :return:
        """
        self.driver.wait_for_object("same_name_prompt_message")

    def verify_eight_group_limit_message(self):
        """
        The error message when trying to add more than 8 groups on binding printer page
        """
        self.driver.wait_for_object("eight_group_limit_prompt_message")

    def verify_no_remove_icon(self, group_name):
        """
        Long press the default printer group, verify there is no remove icon and user cannot remove the button
        :return:
        """
        remove_group = self.driver.find_object("remove_group_name", format_specifier=[group_name])
        self.driver.long_press(remove_group)
        self.driver.wait_for_object("remove_group_button", format_specifier=[group_name], invisible=True)

    def verify_remove_default_groups(self):
        """
        Try to remove all default groups, negative
        :return:
        """
        for group in GroupName.__members__.values():
            self.verify_no_remove_icon(group.value)
