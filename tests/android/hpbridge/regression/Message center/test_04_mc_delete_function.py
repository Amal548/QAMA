# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestMCDeleteFunction(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.mp_message_center = self.fc.flow["mp_message_center"]

        # Define variable
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        """
        Pre-condition:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There are multiple message for the login WeChat account.
        """

    def test_01_message_center_delete_function(self):
        """
        Steps:
            1.Search out the WeChat Applet and then launch the Applet.
            2.Click the bell icon on home page to enter the message center.
            3.Check the restul.
            4. Click the "dustbin" icon on "全部" tab.
            5. Click the other tab on delete page.
            6. Check and uncheck the option box in the front of all the message.
            7. Click the "取消" button.
            8.Check one or more message on "全部" tab.
            9.Click the "删除" button.
            10. Click the "删除" button.

        Expected results:
            Verify the classification for the all message correctly on the "分享" "打印任务" "打印机" tab.
            Verify there is a "dustbin" icon at the bottom right corner on the four tabs.
            Verify there is a option box display in the front of all the message.
            Verify the "全选" "取消" "删除" buttons lined at the bottom of this page.
            Verify the option box and "全选" "取消" "删除" buttons are disappeared on the other tab.
            Verify the message on the other tab display well.
            Verify all message can be checked and unchecked successfully.
            Verify the number behind the message display correctly when checked and unchecked option box.
            Verify the option box and "全选" "取消" "删除" buttons are disappeared.
            Verify the checked message can be delete successfully in "全部" tab and the classified tab.
            Verify the option box and "全选" "取消" "删除" buttons are disappeared.
            Verify the all message can be delete successfully in "全部" tab.
            Verify the option box and "全选" "取消" "删除" buttons are disappeared.
            Verify the "暂无消息" message display in the middle of "全部" tab.
        """
        self.wechat.goto_mp()
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.verify_dustin_icon_exist()
        self.mp_message_center.verify_select_all_cancel_delete_btn()
        self.mp_message_center.click_printer_tab()
        self.mp_message_center.verify_select_all_cancel_delete_btn(displayed=False)
        self.mp_message_center.click_delete_icon()
        self.mp_message_center.click_select_all_btn()
        self.mp_message_center.verify_records_selected()
        self.mp_message_center.verify_selected_number_notifications()
        self.mp_message_center.click_cancel_btn()
        self.mp_message_center.verify_select_all_cancel_delete_btn(displayed=False)
        self.mp_message_center.click_delete_icon()
        self.mp_message_center.click_select_all_btn()
        self.mp_message_center.click_delete_btn()
        self.mp_message_center.verify_select_all_cancel_delete_btn(displayed=False)
        self.mp_message_center.delete_all_records()
        self.mp_message_center.verify_no_more_msg()






