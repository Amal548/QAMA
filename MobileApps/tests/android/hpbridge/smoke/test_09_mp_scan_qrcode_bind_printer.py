# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
pytest.app_info = "hpbridge"


class TestBindPrinterByMPScan(object):

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
            2. Login Wechat with a valid account.
        """

    def test_01_bind_printer_with_camera(self):
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
        self.wechat.goto_mp()
        self.mp_home.select_add_printer()
        self.mp_home.scan_qrcode_with_camera()
        self.binding.bind_printer()


