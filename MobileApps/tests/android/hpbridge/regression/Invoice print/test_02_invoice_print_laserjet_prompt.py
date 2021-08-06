# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestInvoicePrintFlowLaserJetPrompt(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.print = self.fc.flow["print_flow"]
        self.pa_home = self.fc.flow["pa_home"]
        self.invoice_print = self.fc.flow["invoice_print"]
        self.print_setting = self.fc.flow["print_setting"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.test_invoice = "武汉金拱门"
        self.test_invoice2 = "武汉京东"
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Make sure user added some invoices to "微信卡包->我的票券"
            3. Login Wechat with a valid account which has bound some printer.
        """
    def test_01_invoice_print_laserjet_prompt(self):
        """
        Steps:
            1. Launch the WeChat Applet and choose Gen1 Inkjet printer to send invoice print job.
            2. Launch the WeChat Applet and choose Gen1 Laser Jet printer to send invoice print job.
            3. Check the print settings page.
            4. Send the invoice print job to Gen1 LaserJet printer.
        Expected result:
            Verify the selected invoice can be printed out successfully.
            Verify the printed result is consistent with the print Settings.
            Verify the prompt message "发票可能由于字体原因，无法正确打印，可以尝试在微信卡包中查看发票，并保存图片至小程序打印"
                should be displayed correctly on the print settings page and above the "打印" button.
            Verify the selected invoice can be printed out successfully.
            Verify the printed result is consistent with the print Settings.
        """
        self.wechat.send_qrcode(qrcode_index=9)
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.print.select_invoice_print()
        self.invoice_print.select_invoice(self.test_invoice)
        self.invoice_print.click_confirm_btn()
        self.print_setting.verify_laserjet_printer_compatibility_msg()
        self.print_setting.select_print()
        self.print_setting.click_return_home_btn()
        self.print_setting.close_mp()
        self.wechat.goto_pa()
        self.pa_home.click_print_history()
        assert self.pa_home.verify_print_results_from_notification()


