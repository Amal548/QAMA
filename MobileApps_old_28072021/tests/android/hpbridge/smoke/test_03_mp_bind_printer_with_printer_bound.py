# coding: utf-8
import pytest

from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestBindPrinterWithPrinterBound(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.api_utility = APIUtility()

        """
        PreConditions:
            1.Install the Wechat app
            2.Login Wechat with valid account
            3.The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it. 
            4.One or more printers bound with the login Wechat account.
            5.The test printer is not bound with the login Wechat account.
        """

        self.api_utility.unbind_all_printers()
        self.api_utility.bind_default_printer()

    def test_01_bind_with_another_printer_bound(self):
        """
        Steps:
            1.Search out the WeChat Applet and then click it to enter this Applet.
            2. Click the "Add a Printer" on Applet home screen.(manual step)
                WeChat scan for a qroce
            3.Follow the rest flow and bind the printer.
        Expected:
            For step2,Verify the scan is successful and the printer is desired to be bound with the Wechat account .
                Note: The scan flow should work properly.

            For step3,Verify the printer should be bound successfully. --- Printer Information page should be displayed.
                Note: The binding flow should work properly.
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)

        """
        Steps: 
            Using Wechat “扫一扫” to scan the same printer QR code again.
        Expecated:
            Printer information page(已绑定页面) should shows up.
            "开始打印" button can be clicked with no error.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
