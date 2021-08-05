# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PageTitle

pytest.app_info = "hpbridge"


class TestFilePrint(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_hp_supply = self.fc.flow["pa_hp_supply"]

        # Define variables
        self.page_title = PageTitle.SUPPLY_PURCHASE.value
        self.hp_supply_points_app_name = PageTitle.HP_SUPPLY_CLUB_APP_NAME.value
        """
        PreConditions:
            1.Install the Wechat app
            2.Login Wechat with valid account
            3.The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it. 
            4.One or more printers bound with the login Wechat account.
            5.The test printer is not bound with the login Wechat account.
        """

    def test_01_supply_purchase_page(self):
        """
         Steps:
                1.Go to public account and select "个人中心".
                2.Open "购买耗材"
                3.Select a printer
         Expected results:
                1. Printer list shows up first.
                2. Corresponding ink type shows up successful after choose printer.
                3. The corresponding page can be opened
        Notes: the checkpoint 2 can only be tested by Gen1 printer
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_purchase_supply()
        self.pa_hp_supply.select_a_printer()
        self.pa_hp_supply.assert_page_title_is(self.page_title)

    def test_02_hp_supply_points_page(self):
        """
        Steps:
                1.Go to public account and select "个人中心".
                2.Open "惠普耗材积分"
         Expected results:
                Verify it jumps to the "惠普原装耗材积分俱乐部" applet without any errors.
        :return:
        """
        self.wechat.goto_pa()
        self.pa_home.select_personal_center()
        self.pa_home.click_hp_supply_points()
        self.pa_hp_supply.verify_hp_supply_club_app_name(self.hp_supply_points_app_name)
