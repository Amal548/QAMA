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
        self.print = self.fc.flow["print_flow"]
        self.print_setting = self.fc.flow["print_setting"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_print_history = self.fc.flow["pa_print_history"]

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

    def test_01_print_job_tab(self):
        """
        Steps:
            1. Go to Applet Printer Home page, and sliding the printer icon to select one printer.
            2. Send a print job to this printer.
            3. After the job print successfully log out and log back in the Applet.
            4. Click the bell icon on home page.
            5. Click the other tab on message center page.
        Expected result:
            1. Verify the numbers at the upper right corner of bell icon on home page has increased successfully.
            2. Verify the message center page display correctly.
            3. Verify there is a new message "打印成功通知" display correctly on "全部" tab.
            4. Verify the new message "打印成功通知" only display on "打印任务" tab.
            5. Verify the new message "打印失败通知" display correctly on "全部" and "打印任务" tab.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        pre_notification_num = self.mphome.get_mc_notifications_num()
        self.print.select_file_print()
        self.print.select_from_chat_history()
        self.print.select_doc_from_chat_history(self.test_file)
        self.print_setting.select_print()
        self.print_setting.click_return_home_btn()
        self.mphome.close_mp()
        self.wechat.back_from_qrcode()
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_print_history()
        print_result = self.pa_print_history.verify_print_status_from_print_history()
        self.pa_print_history.close_print_history_page()
        self.pa_home.goto_mp_from_pa()
        post_notification_num = self.mphome.get_mc_notifications_num()
        assert post_notification_num == pre_notification_num + 1
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_print_job_tab()
        self.mp_message_center.verify_print_result_notification(passed=print_result)
