# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
pytest.app_info = "hpbridge"


class TestSearchForHelpContactSupport(object):

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
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
        """
    def test_01_faq_contact_support(self):
        """
        Steps:
            1. Launch the Wechat Applet and then scan the QR code to binding the device.
            2. Go to the home page and clicking "帮助和支持" in the lower right corner.
            3. Click the "常见问题" -> "11. 如何联系客服" in the FAQ page.
            4. Check the contents of "如何联系客服" .
        Expected result:
            1. Verify the FAQ page should be displayed correctly.
            2. Verify the "如何联系客服" should be expand and displayed correctly.
            3. Verify the contents of "如何联系客服" should be displayed correctly
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_help_and_support()
        self.print_notice.click_faq_tab()
        self.print_notice.click_how_to_contact_support_question()
        self.print_notice.verify_content_in_contact_support()