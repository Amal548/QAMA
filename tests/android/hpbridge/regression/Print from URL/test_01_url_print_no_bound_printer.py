# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestURLPrintNoPrinter(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. No printer has been bound to this account.
        """
    def test_01_url_print_without_printer(self):
        """
        Steps:
            1. Search out the WeChat Applet and then launch the Applet.
            2. Click the "网络文章打印" button.
            3. Click "确定" button.
        Expected result:
            Verify there is new added "网络文章打印" icon under the "多功能打印" tab.
            Verify the home page display correctly.
            Verify the message "您还未绑定设备,请先添加打印机" pop up with "确定" button.
            Verify the pop up message disappear.
            Verify the home page display well.
        """
        self.wechat.goto_mp()
        self.mphome.check_invoice_print_no_device()