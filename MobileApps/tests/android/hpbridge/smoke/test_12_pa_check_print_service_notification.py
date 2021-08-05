# coding: utf-8

import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestFilePrint(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.print_setting = self.fc.flow["print_setting"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_print_history = self.fc.flow["pa_print_history"]

        # Define variables
        self.test_file = "wonder.docx"
        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

    def test_01_check_print_notification_with_file_printed(self):
        """
        Steps:
            1. select "文件打印" and select a test file from chat history, print it with default settings
            2. Go back to mini program home page, then go to public account
            3. Check the service notification for the print job
        Expected:
            Verify the notification can be received
            Verify the notification indicate that the print job is failed or not
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_file_print()
        self.print.select_from_chat_history()
        self.print.select_doc_from_chat_history(self.test_file)
        self.print_setting.select_print()
        self.print_setting.click_return_home_btn()
        self.print_setting.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.goto_pa()
        self.pa_home.verify_print_results_from_notification()
