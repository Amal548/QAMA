# coding: utf-8
import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestPrintHistory(object):
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
        self.invoice_print = self.fc.flow["invoice_print"]

        # Define variables
        self.test_invoice = "武汉金拱门"
        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

    def test_01_check_print_history_with_print_invoice(self):
        """
        Steps:
            1. select "发票打印" and select an invoice, print it with default settings
            2. Go back to mini program home page, then go to public account page
            3. Go to personal center, select the print history
            4. Check the print results in print history
        Expected:
            Verify the job can be printed successfully
            Verify the print history will show the job printed
            Verify the print job completed status
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.select_invoice(self.test_invoice)
        self.invoice_print.click_confirm_btn()
        # self.print.select_invoice(self.test_invoice)
        self.print_setting.select_print()
        self.print_setting.click_return_home_btn()
        self.print_setting.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_print_history()
        self.pa_print_history.verify_print_status_from_print_history()
