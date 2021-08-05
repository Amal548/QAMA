# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
pytest.app_info = "hpbridge"


class TestBindPrinterWithNoPrinterBound(object):

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
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. no printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """
        self.api_utility.unbind_all_printers()

    def test_01_bind_printer(self):
        """
        Steps:
            1.Search out the WeChat Applet and then click it to enter this Applet.
            2.  Click the "Add a Printer" on Applet home screen.(manual step)
                 WeChat scan  for a qroce(automation step)
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


