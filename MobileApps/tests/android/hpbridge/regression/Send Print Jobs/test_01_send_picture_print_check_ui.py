# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestPicturePrintFlowUI(object):
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
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        PreConditions:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to this login WeChat account.
        """

    def test_01_ui_check_with_picture_print_flow(self):
        """
        Steps:
            1. Go to Printer Home page, and sliding the printer icon to select one printer.
            2. Click on the "图片打印" on the home page. Check the option list.
            3. Click the "取消" on the option list.

        Expected result:
            1. Verify the option list should be displayed correctly.
            2. Verify the "拍照"/"从手机相册选择"/"从聊天记录选择/从百度网盘选择" and "取消" should be displayed correctly
                and clickable.
            3. Verify the option list should be closed and then the home page should be displayed correctly.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_picture_print()
        self.print.verify_select_options_exist()

    def tesst_02_ui_check_print_process(self):
        """
        Steps:
            1. Click the "从聊天记录选择" to open a chat choose page.
            2. Select one contact or group and then check the UI.
            3. Select one picture and then click "完成" button. Check the UI.
            4. Click the back button on the top left corner.
            5. Repeat the above steps with "拍照"/"从手机相册选择" on the option list.

        Expected result:
            1. Verify the various picture sent by contact or group should be displayed correctly.
            2. Verify the print settings page should be displayed correctly.
            3. Verify the picture thumbnail should be displayed correctly.
            4. Verify the print settings page should be closed and back to the home page correctly.
            5. Verify all the function work well. Verify all the page display correctly.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_picture_print()
        self.print.select_from_chat_history()
        self.print.select_img_from_chat_history()
        self.print_setting.select_print()
        self.print_setting.click_top_back_arrow_icon()
        self.print.select_picture_print()
        self.print.select_from_album()
        self.print.pick_a_photo()
        self.print_setting.select_print()
