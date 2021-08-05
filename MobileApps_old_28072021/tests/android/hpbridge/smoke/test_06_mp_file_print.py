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
        self.baidu_print = self.fc.flow["baidu_print"]

        # Define variables
        self.test_file = "wonder.docx"
        self.baidu_file = "BobPanda.doc"

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

    def test_01_file_print_select_from_chat(self):
        """
        Steps:
            1. select "文件打印" and select a test file from chat history, print it with default settings
        Expected:
            verify the job can be created successfully
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

    def test_02_file_print_select_from_baidu(self):
        """
        Steps:
            1. select "文件打印" and select a test file from baidu netdisk, print it with default settings
        Expected:
            verify the job can be created successfully
        :return:
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_file_print()
        self.print.select_from_baidu_disk()
        self.baidu_print.select_file(self.baidu_file)
        self.baidu_print.confirm_file_select(self.baidu_file)
        self.print_setting.select_print()
