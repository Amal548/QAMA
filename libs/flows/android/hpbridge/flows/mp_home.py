# coding: utf-8
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from time import sleep

class MPHome(HPBridgeFlow):
    flow_name = "mp_home"

    def check_add_printer_filed_no_device(self):
        """
        if there is no printer was bound, the message should be displayed: "添加打印机，即可开始打印"
        :return:
        """
        self.driver.wait_for_object("add_printer", timeout=20)

    def verify_printer_exist(self, printer_name):
        """
        verify the printer is exist in the home page printer list, by using the printer name
        :param printer_name: the printer's name going to check
        :return:
        """
        self.driver.wait_for_object("printer_spec", format_specifier=[printer_name])

    def verify_printer_new_icon(self, printer_name, invisible=False):
        """
        verify the printer is exist in the home page printer list, by using the printer name, and verify
        the new icon exist for the printer
        :param printer_name: the printer's name going to check
        :param invisible: if True, verify the new icon not exist
        :return:
        """
        self.driver.wait_for_object("new_icon", format_specifier=[printer_name], invisible=invisible)

    def verify_group_name(self, printer_name, group_name):
        """
        Check the group name on mini program home page
        :return:
        """
        printer = self.driver.wait_for_object("printer_spec", format_specifier=[printer_name])
        assert self.driver.get_text("group_name", root_obj=printer) == group_name

    def verify_mini_program_home_page(self):
        """
        Verify if the current page is mini program home page or not
        :return:
        """
        self.driver.wait_for_object("hp_cloud_print")

    def check_no_device_info_page(self):
        """
        Click the "add_printer" button if there is no printer bound, the no device info page will pop up
        :return:
        """
        self.driver.wait_for_object("add_printer", timeout=20)
        self.driver.click("add_printer")
        self.driver.wait_for_object("no_printer_page_msg1")
        self.driver.wait_for_object("no_printer_page_msg2")
        self.driver.wait_for_object("scan_button")
        self.driver.wait_for_object("no_printer_info")
        self.driver.press_key_back()

    def check_no_device_warm_promopt(self):
        """
        If there is no printer was bound, the warm prompt will pop up once you click the function button on home page
        if you click the "确定" button on the prompt, the pop up will be disappear
        :return:
        """
        self.driver.wait_for_object("warm_prompt_title")
        self.driver.wait_for_object("warm_prompt_msg")
        self.driver.click("warm_prompt_confirm")
        self.driver.wait_for_object("warm_prompt_msg", invisible=True)

    def check_voice_print_no_device(self):
        """
        Click the "语音打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("invoice_print")
        self.driver.click("invoice_print")
        self.check_no_device_warm_promopt()

    def check_help_support_no_device(self):
        """
        Click the "帮助和支持" button, and verify the FAQ page displayed
        if the mobile screen is small, the "帮助和支持" button maybe hide need to scroll the screen
        :return:
        """
        self.click_help_and_support()
        self.driver.wait_for_object("set_printer")
        self.driver.wait_for_object("print_summary")
        self.driver.wait_for_object("common_problems")
        self.driver.press_key_back()
        self.driver.wait_for_object("common_problems", invisible=True)
        self.driver.wait_for_object("question_mark")

    def click_help_and_support(self):
        """
        Click on help and support link on mini program home page
        """
        self.driver.wait_for_object("question_mark")
        self.click_question_mark()

    def check_file_print_no_device(self):
        """
        Click the "文件打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("file_print")
        self.driver.click("file_print")
        self.check_no_device_warm_promopt()

    def check_img_print_no_device(self):
        """
        Click the "文件打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("img_print")
        self.driver.click("img_print")
        self.check_no_device_warm_promopt()

    def check_invoice_print_no_device(self):
        """
        Click the "发票打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("invoice_print")
        self.driver.click("invoice_print")
        self.check_no_device_warm_promopt()

    def check_id_copy_no_device(self):
        """
        Click the "身份证复印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("ID_copy_print")
        self.driver.click("ID_copy_print")
        self.check_no_device_warm_promopt()

    def check_netdisk_print_no_device(self):
        """
        Click the "百度网盘打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("baidu_netdisk_print")
        self.driver.click("baidu_netdisk_print")
        self.check_no_device_warm_promopt()

    def check_spice_print_no_device(self):
        """
        Click the "趣味打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("spice_print")
        self.driver.click("spice_print")
        self.driver.wait_for_object("womoooo_plugin")
        self.driver.press_key_back()
        self.driver.wait_for_object("womoooo_plugin", invisible=True)

    def check_url_print_no_device(self):
        """
        Click the "网络文章打印" button， the warm prompt will pop up
        :return:
        """
        self.click_url_article_print_section()
        self.check_no_device_warm_promopt()

    def check_id_photo_no_device(self):
        """
        Click the "证件照打印" button， the warm prompt will pop up
        :return:
        """
        self.driver.wait_for_object("ID_photo_print")
        self.driver.click("ID_photo_print")
        self.check_no_device_warm_promopt()

    def check_hp_consumable_no_device(self):
        """
        Click the "惠普耗材积分" button， the warm prompt will pop up
        if the mobile screen is small, the "惠普耗材积分" button maybe hide need to scroll the screen
        :return:
        """
        self.driver.wait_for_object("HP_consumable")
        self.driver.swipe(per_offset=0.3)
        self.driver.click("HP_consumable")
        self.driver.wait_for_object("consumable_popup_title")
        self.driver.wait_for_object("consumable_popup_confirm")
        self.driver.click("consumable_popup_cancel")
        self.driver.wait_for_object("consumable_popup_title", invisible=True)

    def select_add_printer(self):
        """
        Click the "添加打印机" button to add a new printer
        :return:
        """
        if self.driver.wait_for_object("add_printer_btn"):
            self.driver.click("add_printer_btn")
        else:
            self.driver.wait_for_object("add_printer_plus_icon").click()

    def scan_qrcode_with_camera(self, qr_code_valid=True):
        """
        click "扫一扫" and launch camera to scan a qrcode, lead to printer binding page
        :param: If the qr code is an HP printer qr code, set to True, if the qr code is not a printer, set to False
        """
        self.driver.click("scan_button")
        if qr_code_valid:
            self.driver.wait_for_object("mp_loading_icon", timeout=15, raise_e=False)
            self.driver.wait_for_object("mp_loading_icon", invisible=True)

    def goto_print_info_page(self):
        """
        Click "添加打印机" and then click "没有打印机信息页？", goto "如何打印信息页" guide page
        :return:
        """
        self.select_add_printer()
        self.driver.click("no_printer_info")

    def click_message_center_bell_icon(self):
        """
        Click on the bell icon - message center on mini program home page
        :return:
        """
        self.driver.click("mc_bell_icon")

    def click_url_article_print_section(self):
        """
        Click on the URL article print section
        :return:
        """
        self.driver.wait_for_object("url_print")
        self.driver.click("url_print")

    def click_question_mark(self):
        """
        Click on the question mark - FAQ/Support on home mini program screen, click on it will open customer support & faq
        :return:
        """
        self.driver.click("question_mark")

    def click_person_icon(self):
        """
        Click on the personal center icon on mini program home screen
        :return:
        """
        self.driver.click("person_icon")

    def click_mp_home_3dot_menu(self):
        """
        Click the 3 dots menu on top right of the mini program home page
        :return:
        """
        self.driver.click("more_option_3dot_menu")

    def click_hb_test_account(self):
        """
        Click on the ‘HB测试号’ on the pops up menu after clicked the 3 dots more option menu
        :return:
        """
        self.driver.click("hp_test_account")

    def click_hp_pa_msg(self):
        """
        Click on the public account message after clicked the public account info on more option menu
        :return:
        """
        self.driver.click("hp_pa_account_msg")

    def click_hp_bridge_pa_test_account(self):
        """
        Click on the hp bridge pa test account to go to pa home page
        :return:
        """
        self.driver.click("hp_test_pa_account")

    def verify_new_message_reminder(self, message_exist=True):
        """
        Verify the new message count on top of the person icon
        :param message_exist: If you expect there is notification message, set the message_exist to true. Otherwise, set
                to False
        """
        sleep(1)
        current = self.driver.wait_for_object("message_number", timeout=2, raise_e=False)
        assert current if message_exist else current == message_exist

    def verify_home_page_displayed(self):
        """
        Verify the home page displayed with basic print option/menu
        :return:
        """
        self.driver.wait_for_object("hp_cloud_print_title")
        self.driver.wait_for_object("file_print", timeout=5)
        self.driver.wait_for_object("img_print", timeout=5)
        self.driver.wait_for_object("invoice_print", timeout=5)
        self.driver.wait_for_object("ID_copy_print", timeout=5)
        self.driver.wait_for_object("baidu_netdisk_print", timeout=5)
        self.driver.wait_for_object("voice_print", timeout=5)
        self.driver.wait_for_object("HP_consumable", timeout=5)
        self.driver.wait_for_object("url_print", timeout=5)
        self.driver.wait_for_object("ID_photo_print", timeout=5)

    def get_mc_notifications_num(self):
        """
        Get the notifications amount on mini program home page
        :return if there is a number then return the notification amount, otherwise return 0
        """
        sleep(1)
        if self.driver.wait_for_object("notification_messages", timeout=3, raise_e=False):
            return int(self.driver.get_text("notification_messages"))
        else:
            return 0
