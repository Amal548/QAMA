# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestEnterMPFromPA(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.pa_home = self.fc.flow["pa_home"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()

        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. There is no printer bound to this login WeChat account.
            4. User has followed the related WeChat official account.
        """
    def test_01_enter_miniprogram_from_public_account(self):
        """
        Steps:
            1.Enter to WeChat Official Account.
            2.Click on the Personal Center -> My Printer.
            3.Long press the QR code and then click "前往图中包含的小程序".
            4.Bind the printer from applet.
            5.Enter to WeChat Official Account and unbinding all the printer.
        Expected result:
            1.Verify the official account home page displayed correctly.
            2.Verify the "无绑定的打印机 请先启动小程序绑定打印机" and applet QR code should be shown on this page correctly.
            3.Verify the applet launched and applet home page displayed correctly.
            4.Verify the printer bind successful.
            5.Verify the "无绑定的打印机 请先启动小程序绑定打印机" and applet QR code should be shown on my printer page correctly.
        """
        self.wechat.goto_pa()
        self.pa_home.go_to_mp_from_pa()
        self.mphome.verify_home_page_displayed()


