# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestDocumentPrintFlowUI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables
        self.test_file = "wonder.docx"
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        pre-condition:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to this login WeChat account.
        """

    def test_01_ui_check_with_document_print_flow(self):
        """
        Steps:
            1. Go to Printer Home page, and sliding the printer icon to select one printer.
            2. Click on the "文件打印" on the home page.
            3. Check the option list.
            4. Click the "取消" on the option list.

        Expected result:
            1. Verify the option list should be displayed correctly
            2. Verify the "从聊天记录选择"/"从百度网盘选择" and "取消" should be displayed correctly and clickable.
            3. Verify the "从本地存储选择" should be displayed as gray and not clickable
            4. Verify the option list should be closed and then the home page should be displayed correctly.
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_file_print()
        self.print.verify_select_options_exist(picture_print=False)

    def test_02_ui_check_document_print_select_chat_history(self):
        """
        Steps:
            1. Click on the "文件打印" on the home page.
            2. Click the "从聊天记录选择" to open a chat choose page.
            3. Select one contact or group and then check the UI.
            4. Select one support file and then click "确定" button.
                (support file include ppt/pptx/doc/docx/xls/xlsx/pdf/rtf/txt… file). Check the UI.
            5. Click the back button on the top left corner.
        Expect result:
            1. Verify the various files sent by contact or group should be list with file icon and file name correctly.
            2. Verify the checkbox should be displayed in front and can be select.
            3. Verify the print settings page should be displayed correctly.
            4. Verify the file icon and file name should be displayed correctly.
            5. Verify the print settings page should be closed and back to the home page correctly.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_file_print()
        self.print.select_from_chat_history()
        self.print.select_doc_from_chat_history(self.test_file)
        self.print_setting.verify_print_job_name(self.test_file)
        self.print_setting.click_top_back_arrow_icon()
