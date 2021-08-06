# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility

pytest.app_info = "hpbridge"


class TestMPHomePageNoPrinter(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()

    def test_01_homepage_add_printer(self):
        """
        Steps:
            1.For user who has bound printers before and unbound all the printers, the user launches the applet.
            2. Check the UI.
        Expected:
            Verify the "添加打印机，即可开始打印" should be displayed on the applet home page.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_add_printer_filed_no_device()

    def test_02_homepage_no_printer(self):
        """
        Steps:
            1. Follow above steps ,click "添加打印机，即可开始打印" on the applet home page.
            2. Exit the guide and click back button.
            3. Repeat above steps for several times.
        Expected:
            1.Verify the "getting started guide -开启打印之旅" for WeChat print should be displayed.
                "打印信息页须知" link is available.
                The Hand icon in the guide is an animation.
            2.Verify the applet home page should be displayed.
            3.The "getting started guide -开启打印之旅" won't pop up again after exit the "getting started guide -开启打印之旅".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_no_device_info_page()

    def test_03_homepage_voice(self):
        """
        Steps:
            1. Click "语音打印" on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_voice_print_no_device()

    def test_04_homepage_help_support(self):
        """
        Steps:
            1. Click "帮助和支持" on the applet home page.
            2. Check the UI.
        Expected:
            Verify the  FAQ page should be displayed.
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_help_support_no_device()

    def test_05_homepage_file_print(self):
        """
        Steps:
            1. Click on “文件打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_file_print_no_device()

    def test_06_homepage_img_print(self):
        """
        Steps:
            1. Click on “图片打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_img_print_no_device()

    def test_07_homepage_invoice_print(self):
        """
        Steps:
            1. Click on “发票打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_invoice_print_no_device()

    def test_08_homepage_id_copy(self):
        """
        Steps:
            1. Click on “身份证复印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_id_copy_no_device()

    def test_09_homepage_baidu_netdisk(self):
        """
        Steps:
            1. Click on “百度网盘打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_netdisk_print_no_device()

    # The "趣味打印" was removed in the new UI
    # def test_10_homepage_spice_print(self):
    #     """
    #     Steps:
    #         1. Click on “趣味打印” on the applet home page.
    #         2. Check the UI.
    #     Expected:
    #         Verify it go to the spice print plugin list page.
    #     :return:
    #     """
    #     self.wechat.goto_mp()
    #     self.mphome.check_spice_print_no_device()

    def test_10_homepage_url_print(self):
        """
        Steps:
            1. Click on “网络文章打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_url_print_no_device()

    def test_11_homepage_id_photo(self):
        """
        Steps:
            1. Click on “证件照打印” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_id_photo_no_device()

    def test_12_homepage_hp_consumable(self):
        """
        Steps:
            1. Click on “惠普耗材积分” on the applet home page.
            2. Check the UI.
        Expected:
            Verify the pop message should be displayed "您还未绑定设备，请先添加打印机".
        :return:
        """
        self.wechat.goto_mp()
        self.mphome.check_hp_consumable_no_device()
