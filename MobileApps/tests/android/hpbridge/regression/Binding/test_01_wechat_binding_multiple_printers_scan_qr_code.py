# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
HPBridgeFlow.set_pytest_data()
pytest.app_info = "hpbridge"


class TestBindMultiplePrinter(object):

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
            1. Install the WeChat app.
            2. Login Wechat with a valid account which has already bound one or multiple printers.
            3. Enable the webservice with a new test printer and got the printer QR code.
        """
        self.api_utility.unbind_all_printers()
        self.api_utility.bind_default_printer()

    # We use api to binding a printer first then use scan qr code in Wechat app by scan a qr code image
    def test_01_binding_multiple_printer_with_scan_qr_code_wechat(self):
        """
        Steps:
            1. On Wechat app, go to "Contacts" or "Contacts" or "Discover" tab.
            2. Press on "+" button in the top right corner.
            3. In the "+" options list, click on "Scan QR Code" option.
            4. Click on "绑定打印机" button, and check the result.
            5. Click on "开始打印" button, and check the result.

        Expected:
            1. Verify the WeChat Applet should be launched and the scan is successful.
            2. Verify the printer is desired to be bound, and the "printer binding details page" is displayed.
            3. Verify the "设置为默认打印机" radio button is on by default.
            4. Verify the printer should be bound successfully, and "开始打印" page is displayed.
            5. Verify user will be directed to printer home - The printer that the user just bound is displayed
                on this page.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)

    # We use api to binding a printer first then use scan qr code in mini program by scan a qr code image
    # We use send QR code to wechat, and scan QR code to bind printer instead from mini program
    def test_02_binding_multiple_printer_with_scan_qr_code_mini_program(self):
        """
        Steps:
            1. Enter the Wechat Applet. (User has already used this Applet)
            2. Launch the "Scan QR Code" flow within the Applet.
            3. Click on "绑定打印机" button, and check the result.
            4. Click on "开始打印" button, and check the result.

        Expected results:
            1. Verify the scan is successful and the printer is desired to be bound with the Wechat account .
            2. Verify the printer is desired to be bound, and the "printer binding details page" is displayed.
            3. Verify the printer should be bound successfully, and "开始打印" page is displayed.
            4. Verify user will be directed to printer home - The printer that the user just bound is displayed on this page.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.binding.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.send_qrcode(qrcode_index=5)
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()

    # Notes: We'll need to update this tests for how to set these parameter when we run the tests on Linux system
    # Use api to bind a printer to a different account since we cannot switch wechat account on one mobile device
    def test_03_binding_binded_printer_different_account(self):
        """
        Steps:
            1. On Wechat app, login with a different account.
            2. Enter the Wechat Applet, scan the QR code of the bound printer.

        Expected result:
            1. Verify the WeChat Applet should be launched and the scan and binding are successful.
            2. Verify the printer is desired to be bound, and the "printer binding details page" is displayed.
            3.Verify the scan and binding are successful.
            4.Verify the printer is desired to be bound, and the "printer binding details page" is displaye
        """
        HPBridgeFlow.set_pytest_data(test_mobile="Honor 8")
        api = APIUtility()
        api.unbind_all_printers()
        api.bind_default_printer("TangoX")
        HPBridgeFlow.set_pytest_data()
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
