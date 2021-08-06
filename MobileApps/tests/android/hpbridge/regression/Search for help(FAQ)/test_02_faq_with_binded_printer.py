# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestSearchForHelpOnHomePage(object):

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
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. There is one printer bound to this login WeChat account and not the admin.
        """
    def test_01_faq_home_page_url(self):
        """
        Steps:
            1. Enter the WeChat Applet, the default printer home page is displayed.
            2. Click the "帮助和支持" button .
            3. Check the contents with the "设置打印机", "打印概述" and "常见问题" tabs of the FAQ page.
        Expected result:
            Verify the button link will direct the user to FAQ home page.
            Verify the FAQ page should be displayed correctly
            Verify the contents of the FAQ page should be displayed correctly
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_help_and_support()
        self.print_notice.click_printer_setting_tab()
        self.print_notice.click_print_description_tab()
        self.print_notice.click_faq_tab()
