# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestSearchForHelp(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.binding = self.fc.flow["bind_printer"]
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
    def test_01_faq_none_admin_printer(self):
        """
        Steps:
            1. Enter the WeChat Applet.
            2. Launch the "Scan QR Code" to scan the above printer QR code again.
            3. Click the "重置打印机web服务" link on "温馨提示" message.
            3. Check the contents with the "设置打印机", "打印概述" and "常见问题" tabs of the FAQ page.
        Expected result:
            Verify "绑定打印机" page display correctly with "开始打印" button.
            Verify there is a "温馨提示(您当前不是管理员)" message display at the bottom of this page.
            Verify the "重置打印机Web服务" should be displayed as blue and clickable.
            Verify the FAQ - How to disable and enable web service page should be displayed correctly
            Verify the contents of the FAQ page should be displayed correctly
        """
        self.api_utility.bind_default_printer(printer_name="TangoX")
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.verify_kind_remind_message()
        self.binding.click_reset_printer_webservice_url()
        self.print_notice.verify_reset_printer_service_question()
        self.print_notice.click_printer_setting_tab()
        self.print_notice.click_print_description_tab()