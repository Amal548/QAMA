# coding: utf-8
import pytest

pytest.app_info = "hpbridge"


class TestEnterMPFromPA(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.pa_home = self.fc.flow["pa_home"]

        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. User has followed the related WeChat official account.
        """
    def test_01_enter_miniprogram_from_public_account(self):
        """
        Steps:
            1.Enter the official account and click "小程序".
        Expected result:
            1. Verify the applet launched and applet home page displayed correctly.
        """
        self.wechat.goto_pa()
        self.pa_home.go_to_mp_from_pa()
        self.mphome.verify_home_page_displayed()


