# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestBindInvalidPrinter(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mp_home = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.api_utility = APIUtility()
        """
        PreConditions:
            1. Enable the webservice with a test printer and got the printer QR code.
            2. Reset the printer email address. (The test printer QR code is invalid)
        """
        self.api_utility.unbind_all_printers()

    # Please prepare a QR code which printer has been reset and also an invalid QR code before execute the test cases
    def test_01_binding_printer_invalid_qr_code_scan_from_wechat(self):
        """
        Steps:
            1. On Wechat app, go to "Contacts" or "Contacts" or "Discover" tab.
            2. Press on "+" button in the top right corner.
            3. In the "+" options list, click on "Scan QR Code" option.
            4. Scan the reset printer QR code.

        Expected result:
            1. Verify the WeChat Applet should be launched. The scan is successful but user cannot bind this reset printer.
            2. The device (already reset printer) printer information page should be displayed, the rest message is shown on this page
                and "绑定打印机" button is disabled/unclickable
        """
        # Invalid qr code: Printer has been reset. Scan from Wechat home page, scan function.
        reset_printer = utlitiy_misc.get_reset_printer()
        self.wechat.send_qrcode(reset_printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.verify_printer_reset_string()
        self.binding.get_binding_printer_button_status()

    # Invalid qr code: Printer has been reset. Scan from mini program home page
    def test_02_binding_invalid_qr_code_scan_from_miniprogram(self):
        """
        Steps:
            1. Enter the Wechat Applet.
            2. Launch the "Scan QR Code" flow within the Applet.
            3. Scan the reset printer QR code.

        Expected result:
            1. Verify the scan is successful but user cannot bind this reset printer.
            2. The device (already reset printer) printer information page should be displayed, the rest message is shown on this page
                and "绑定打印机" button is disabled/unclickable.
        """
        self.wechat.send_qrcode(qrcode_index=7)
        self.wechat.scan_qrcode_to_mp()
        self.binding.verify_printer_reset_string()
        self.binding.get_binding_printer_button_status()

    # Invalid qr code: Not a printer qr code, Scan from mini program home page
    def test_03_binding_bad_qr_code_scan_from_miniprogram(self):
        """
        Steps:
            1. Enter the Wechat Applet.
            2. Launch the "Scan QR Code" flow within the Applet.
            3. Scan a non-printer QR code.

        Expected result:
            1. Verify the scan is failed, user will be back to Applet printer home page with a prompt
                message "二维码错误，请扫描打印信息页上的二维码".
        """
        self.wechat.goto_mp()
        self.mp_home.select_add_printer()
        self.mp_home.scan_qrcode_with_camera(qr_code_valid=False)
        self.binding.verify_qr_code_error_message()




