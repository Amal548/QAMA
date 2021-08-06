# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestMCPrintJobTab(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.mp_message_center = self.fc.flow["mp_message_center"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_my_printer = self.fc.flow["pa_my_printer"]

        # Define variable
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.test_file = "wonder.docx"

        """
        Pre-condition:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to this login WeChat account.
        """

    def test_01_mc_printer_tab(self):
        """
        Steps:
            1. Launch the Applet and bind one new printer successfully.
            2. Check the result. And then click the bell icon on home page.
            3. Click the other tab on message center page.
            4. Unbind one printer in WeChat official account. Check the Message center.
        Expected result:
            1. Verify the Applet home page display well.
            2. Verify there is new added bell icon at the upper right corner of home page.
            3. Verify the numbers at the upper right corner of bell icon on home page has increased successfully.
            4. Verify the message center page display correctly.
            5. Verify there is a new message "打印机绑定通知" display correctly on "全部" tab.
            6. Verify the new message "打印机绑定通知" only display on "打印机" tab.
            7. Verify the numbers at the upper right corner of bell icon on home page has increased successfully.
            8. Verify the new message "打印机解绑通知" display correctly on "全部" and "打印机" tab.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        printer_name = self.binding.get_printer_name()
        print(printer_name)
        self.binding.bind_printer(bound=False)
        pre_notification_num = self.mphome.get_mc_notifications_num()
        print(pre_notification_num)
        self.mphome.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_my_printer()
        self.pa_my_printer.unbind_printer(printer_name)
        self.pa_home.goto_wechat_from_pa()
        self.wechat.goto_mp()
        post_notification_num = self.mphome.get_mc_notifications_num()
        assert post_notification_num == pre_notification_num + 1
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_printer_tab()
        self.mp_message_center.verify_bind_and_unbind_notification(bind=False)
        self.mp_message_center.verify_bind_and_unbind_notification(bind=True, notification_order=1)


