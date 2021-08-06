# coding: utf-8
import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestInvoicePrint(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.invoice_print = self.fc.flow["invoice_print"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables
        self.test_invoice = "武汉金拱门"
        self.test_invoice2 = "武汉京东金德贸..."
        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

    def test_01_invoice_print(self):
        """
        Steps:
            1. select "发票打印" and select a invoice, print it with default settings
        Expected:
            verify the job can be created successfully
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.select_invoice(self.test_invoice2)
        self.invoice_print.click_confirm_btn()
        self.print_setting.select_print()
