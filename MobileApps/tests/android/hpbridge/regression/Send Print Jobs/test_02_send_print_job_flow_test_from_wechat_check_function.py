# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestSendPicturePrintJob(object):
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
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. There is one or more printers bound to this login WeChat account.
        """

    def test_01_send_picture_print_job_from_miniprogram(self):
        """
        Steps:
            1. Go to Printer Home page, and sliding the printer icon to select one printer.
            2. Click on the "Photo Print" button on the selected printer home page. Check the result.
            3. Select one photo from the local photo album to print. -> The Photo Print Settings page is displayed.
            4. Change the Photo Print Settings according to user preferences.
            5. Click on the "Print" button on the Photo Print Settings page. Check the print Wechat Applet.
            6. Check the print status/print notification/print history in WeChat official account

        Expected result:
            1. Verify the button can open the local photo album or take a new photo to print.
            2. Verify a toast "文件正在上传" -> "任务正在提交" pops up on Print Settings page.
            3. Verify the "任务提交成功" page should be displayed correctly after the job send successful
            4. Verify the print status/print notification/print history should be displayed correctly.

        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.print.select_picture_print()
        self.print.select_from_album()
        self.print.pick_a_photo()
        self.print_setting.select_print()
        self.print_setting.click_return_home_btn()
        self.print_setting.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.goto_pa()
        self.pa_home.verify_print_results_from_notification()

