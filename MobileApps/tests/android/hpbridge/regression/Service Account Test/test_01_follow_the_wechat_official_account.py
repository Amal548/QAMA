# coding: utf-8
import pytest

pytest.app_info = "hpbridge"


class TestFollowPublicAccount(object):

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

        """
        Pre-conditions:
            1.Install the Wechat app
            2.Login Wechat with valid account
            3.The "HP Cloud print" Applet is added on account.
            4.Not follow the "HP Cloud print" Offcial Account.
        """
    def test_01_follow_the_wechat_official_account(self):
        """
        Steps:
            1.Launch the "HP cloud print" applet.
            2.Click the "Setting"(shows as three dots) icon on top right->"HP cloud print" icon-> "该团队的相关公众号"-> "惠普云打印".
            3.Click the "关注公众号".
        Expected result:
            1.Verify the applet home page is displayed normally.
            2.Verify the official account info page displayed.
            3.Verify the official account home page displayed with "已关注" popup and welcome message "您好，欢迎关注惠普
            云打印, 随时随地，方便快捷，在这里您能实时获得打印任务结果以及其他相关服务。" pushed automatically.
        """
        # Note: Appium is not able to get the attribute for the wechat chat text, not able to verify step3
        # printer = utlitiy_misc.load_printer()
        # self.wechat.send_qrcode(printer["index"])
        self.wechat.send_qrcode(pa_qrcode=True, stage_pa_qr=True)  # Stage public account QR code
        self.wechat.scan_qrcode_to_mp(public_account_qr_code=True)
        self.pa_home.follow_public_account()

    def test_02_enter_wechat_pa_via_mini_app(self):
        """
        Steps:
            1.Launch the "HP cloud print" applet.
            2.Click the "Setting"(shows as three dots) icon on top right->"HP cloud print" icon-> "该团队的相关公众号"-> "惠普云打印".
            3.Click the "关注公众号".
        Expected result:
            1.Verify the applet home page is displayed normally.
            2.Verify the official account info page displayed.
        """
        self.wechat.goto_mp()
        self.mphome.click_mp_home_3dot_menu()
        self.mphome.click_hb_test_account()
        self.mphome.click_hp_pa_msg()
        self.mphome.click_hp_bridge_pa_test_account()
        self.pa_home.follow_public_account()

