# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
pytest.app_info = "hpbridge"


class TestURLArticlePrint(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.urlprint = self.fc.flow["url_print"]
        self.printsetting = self.fc.flow["print_setting"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.url = "https://mp.weixin.qq.com/s/LidBpBbfbMK-G22RWNGW3A"

    def test_01_picture_print_mode(self):
        """
        Steps:
            1,Launch the Applet and then click the "网络文章打印" button.
            2,Copy and past a Valid URL from 今日头条 and back to the Applet.
            3,Check the "图文模式" section and then click the "获取文章" button.
            4,Click the "前往打印" button
            5,Click "打印" button.
        Expected:
            Verify the "网络文章打印" home page displayed correctly.
            Verify "图文模式生成中..." message pop up for a while and then it jumps to the article preview page successfully.
            Verify the picture and text on preview page displayed consistent with the original article.
            Verify the "打印设置" page display correctly with default settings.
            Verify the print job can be printed successfully, the out put result content is consistent with the preview.
        :return:
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.get_article()
        self.urlprint.process_to_print()
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()


    def test_02_txt_print_mode(self):
        """
        Steps:
            1,Launch the Applet and then click the "网络文章打印" button.
            2,Copy and past a Valid URL from 今日头条 and back to the Applet.
            3,Check the "纯文本模式" section and then click the "获取文章" button.
            4,Click the "前往打印" button
            5,Click "打印" button.
        Expected:
            Verify "纯文本模式生成中。。" message pop up for a while and then it jumps to the article preview page successfully.
            Verify just the text displayed on preview page correctly.
            Verify the print job can be printed successfully
        :return:
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.input_url_into_field("https://mp.weixin.qq.com/s/LidBpBbfbMK-G22RWNGW3A")
        self.urlprint.select_txt_mode_print()
        self.urlprint.get_article(pic_mode=False)
        self.urlprint.process_to_print()
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()

