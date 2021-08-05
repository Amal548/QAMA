# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestDocumentPrintFlowFunction(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.mp_home = self.fc.flow["mp_home"]
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables
        self.test_file = "wonder.docx"
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()

        """
        Pre-condition:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to this login WeChat account.
        """

    def test_01_send_document_print_one_file(self):
        """
        Steps:
            1. Go to Printer Home page, and sliding the printer icon to select one printer.
            2. Click on the "文件打印" on the home page.
            3. Click the "从聊天记录选择" on the option list. Select one contact or group.
            4. Select one file with and then click "确定" button.
            5. Change the copy value on the print settings page and then click the "打印" button to send the print job.
            6. Click the "确认" button or back button on the top left corner on "任务提交成功" page

        Expected result:
            1. Verify the various files sent by contact or group should be list with file icon and file name correctly.
            2. Verify the checkbox should be displayed in front and can be select.
            3. Verify the "任务提交成功" page display correctly.
            4. Verify the print job should be print out correctly and consistent with the settings.
            5. Verify the home page should be displayed correctly.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_file_print()
        self.print.select_from_chat_history()
        self.print.select_doc_from_chat_history(self.test_file)
        self.print_setting.change_copies(copies=2)
        self.print_setting.select_print()
        self.print_setting.verify_job_submit_prompt()
        self.print_setting.verify_job_success_submitted_msg()
        self.print_setting.click_return_home_btn()
        self.mp_home.verify_mini_program_home_page()

    def test_02_send_document_print_multi_copies(self):
        """
        Steps:
            1. Click on the "文件打印" on the home page.
            2. Click the "从聊天记录选择" to open a chat choose page.
            3. Select one file and then click "确定" button. Check the UI.
            4. Click the back button on the top left corner.

        Expected result:
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
        self.mp_home.verify_mini_program_home_page()
