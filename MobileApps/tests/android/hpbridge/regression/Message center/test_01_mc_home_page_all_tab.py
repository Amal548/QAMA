# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
pytest.app_info = "hpbridge"


class TestMessageCenter(object):

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
        self.api_utility.bind_default_printer()
        """
        Pre-conditions:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to this login WeChat account.
        """

    def test_01_homepage_and_all_tab(self):
        """
        Steps:
            1.Search out the WeChat Applet and then launch the Applet. Check the UI on home page.
            2.Click the bell icon on home page. Check the result. Then check the UI on "全部" tab.
            3. For user has multiple message. Slide up to the top or down to the bottom
            4.Click the other tabs on this page.Check the result.
            5.Click the back button at top left corner on message center page.
            6.Check the result.
        Expected:
            Verify the home page display correctly.
            Verify there is new added bell icon at the upper right corner of home page.
            Verify the message center page display correctly.
            Verify there are four tabs "全部" "分享" "打印任务" "打印机" lined on message center page.
            Verify the user is on "全部" tab by default for each time enter.
            Verify the other tabs display correctly.
            Verify the Applet home page display correctly.
            Verify there is no number at the upper right corner of bell icon
        """
        self.wechat.goto_mp()
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_all_tab()
        self.mp_message_center.verify_dustin_icon_exist()
        self.mp_message_center.click_share_tab()
        self.mp_message_center.click_print_job_tab()
        self.mp_message_center.click_printer_tab()
        self.mp_message_center.click_top_back_arrow_icon()
        self.mphome.verify_new_message_reminder(message_exist=False)

    def test_02_message_center_multiple_records(self):
        """
        steps:
            1. For user has multiple message. Slide up to the top or down to the bottom
        Expected result:
            1.When user pull for new message in the upper side of the window, show user new message if there is,
                show "暂无新消息" for 2 seconds if no new message.
            2.When user pull for old message in the lower side of the window, show user old message if there is,
                show "已经到底部啦" if no more old message. "已经到底部啦" will stay there.
            3.For tab has related message, verify the message display well under currently tab, and there is a
                "dustbin" icon at the bottom right corner of this page.
            4.For tab has no related message, verify the "暂无消息" message display under currently tab.
        """
        self.wechat.goto_mp()
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_printer_tab()
        self.mp_message_center.find_bottom_bolder_msg()
        self.mp_message_center.delete_all_records()
        self.mp_message_center.verify_no_more_msg()
