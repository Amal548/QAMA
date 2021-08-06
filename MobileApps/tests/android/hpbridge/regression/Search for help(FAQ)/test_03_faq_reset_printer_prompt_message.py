# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestSearchForHelpRestPrinterPrompt(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
        self.mphome = self.fc.flow["mp_home"]
        self.print_notice = self.fc.flow["print_notice"]

        # Define variable
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        Pre-conditions:
            1. Enable the webservice with a test printer and got the printer QR code.
            2. Reset the printer email address. (The test printer QR code is invalid)
        """
    def test_01_faq_reset_printer_prompt_url(self):
        """
        Steps:
            1. Scan the QR code by WeChat App or scan the QR code through the WeChat Applet.
            2. Click on the link "如何绑定" on this page.
            3. Check the contents with the "设置打印机", "打印概述" and "常见问题" tabs of the FAQ page.
        Expected result:
            Verify the device (already reset printer) printer information page should be displayed,
                the rest message is shown on this page."打印机已重置，请扫描新的打印机二维码绑定。如何绑定？"
            Verify the text link will direct the user to FAQ page
            Verify the FAQ page should be displayed correctly, and user can learn how to bind a printer.
            Verify the contents of the FAQ page should be displayed correctly
        """
        self.wechat.send_qrcode(qrcode_index=7)
        self.wechat.scan_qrcode_to_mp()
        self.binding.verify_printer_reset_string()
        self.binding.click_how_to_bind_url()
        self.print_notice.click_printer_setting_tab()
        self.print_notice.click_print_description_tab()
        self.print_notice.click_faq_tab()
