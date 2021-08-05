# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
HPBridgeFlow.set_pytest_data()
pytest.app_info = "hpbridge"


class TestMCMultipleMessage(object):

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
        Pre-condition:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There are multiple message for the login WeChat account.
        """
    def test_01_multiple_message(self):
        """
        Steps:
            1. Launch the Applet.
            2. Trigger Multiple message(such as more than 10, 99) for currently account.
            3. Check the result.
            4. Click the bell icon on home page.
            5. Don't slide up on message center page. Click the back button to leave the Message Center page.
            6.Click the bell icon to the message center page.Don't slide up on message center page.
            7.Click the "dustbin" icon and select "全部".
            8.Click the bell icon to the message center page.
            9.Slide up on message center page till this page loading once.
            10.Click the "dustbin" icon and select "全部".

        Expected result:
            Verify the number display well at the upper right corner of bell icon.
            Verify there is no number at the upper right corner of bell icon as all the messages will be shown as read.
            Verify there is only 10 message can be selected.
            Verify there are more than 10 message can be selected for each loading.
            Verify there are 20 message can be selected.
        """
        self.wechat.goto_mp()
        pre_notification_num = self.mphome.get_mc_notifications_num()
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_top_back_arrow_icon()
        post_notification_num = self.mphome.get_mc_notifications_num()
        assert pre_notification_num != 0
        assert post_notification_num == 0
        self.mphome.click_message_center_bell_icon()
        self.mp_message_center.click_all_tab()
        self.mp_message_center.click_delete_icon()
        self.mp_message_center.click_select_all_btn()
        select_messages = self.mp_message_center.get_number_message_selected()
        assert select_messages == 10
        self.mp_message_center.click_cancel_btn()
        self.mp_message_center.swipe_message_center_page(swipe_times=1)
        self.mp_message_center.click_delete_icon()
        self.mp_message_center.click_select_all_btn()
        reselect_messages = self.mp_message_center.get_number_message_selected()
        assert reselect_messages == 20
