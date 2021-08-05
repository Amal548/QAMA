# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrintPreviewFileName

pytest.app_info = "hpbridge"


class TestURLPrintHappyPath(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.printsetting = self.fc.flow["print_setting"]
        self.urlprint = self.fc.flow["url_print"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.url = "https://mp.weixin.qq.com/s/LidBpBbfbMK-G22RWNGW3A"
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. There is one or more printers bound to the account.
        """
    def test_01_url_print_with_picture_mode(self):
        """
        Steps:
            1.Search out the WeChat Applet and then launch the Applet.
            2.Click the "网络文章打印" button.
            3.Send a Valid URL from 今日头条 to the input-box.
            4.Click the" 确定" button.
            5.Check the "图文模式" section and then click the "获取文章" button.
            6.Click the back button on preview page.
            7.Click the "前往打印" button.
            8.Modify Settings arbitrarily.
            9.Click "打印" button.
        Expected result:
            Verify the "网络文章打印" home page displayed correctly
            Verify the pop up message "已成功为您粘贴当前剪切面板链接 请点击'获取文章'预览效果" with "确定" button displayed correctly.
            Verify the "网络文章打印" home page displayed correctly.
            Verify the copy URL entered to the input box automatically.
            Verify "图文模式生成中。。" message pop up for a while and then it jumps to the article preview page successfully.
            Verify the picture and text on preview page displayed consistent with the original article.
            Verify the "网络文章打印" home page displayed correctly.
            Verify the copy URL displayed correctly in the input box.
            Verify the "获取文章" button changed to the "已获取" button with gray automatically.
            Verify the "前往打印" button changed to blue and clickable.
            Verify the "打印设置" page display correctly with default settings.
            Verify the file name displayed as "网络文章.pdf".
            Verify the print job can be printed successfully.
        """
        # printer = utlitiy_misc.load_printer()
        # self.wechat.send_qrcode(printer["index"])
        self.wechat.send_qrcode(qrcode_index=0)
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.check_if_reminder_pop_out()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.get_article()
        self.urlprint.back_from_print_preview()
        self.urlprint.verify_get_article_btn_changed()
        self.urlprint.click_goahead_print()
        assert self.printsetting.get_print_file_name() == PrintPreviewFileName.WEB_ARTICLE.value
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()

    def test_02_url_print_with_txt_mode(self):
        """
        Steps:
            1. After above steps, continue with text mode
            2. Check the "纯文本模式" section and then click the "获取文章" button.
            3. Click the back button on preview page.
            4. Click the "前往打印" button.
            5. Modify Settings arbitrarily. Click "打印" button.
        Expected result:
            Verify "纯文本模式生成中。。" message pop up for a while and then it jumps to the article preview page successfully.
            Verify just the text displayed on preview page correctly. (Include the author, time and whether original, not contains pictures.)
            Verify the "网络文章打印" home page displayed correctly.
            Verify the copy URL displayed correctly in the input box.
            Verify the "获取文章" button changed to the "已获取" button with gray automatically.
            Verify the "前往打印" button changed to blue and clickable.
            Verify the "打印设置" page display correctly with default settings.
            Verify the file name displayed as "网络文章.pdf".
            Verify the print job can be printed successfully.
            Verify the printed out content is consistent with the related settings.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer()
        self.urlprint.click_url_article_print()
        self.urlprint.check_if_reminder_pop_out()
        self.urlprint.input_url_into_field(self.url)
        self.urlprint.select_txt_mode_print()
        self.urlprint.get_article(pic_mode=False)
        self.urlprint.back_from_print_preview()
        self.urlprint.verify_get_article_btn_changed()
        self.urlprint.click_goahead_print()
        assert self.printsetting.get_print_file_name() == PrintPreviewFileName.WEB_ARTICLE.value
        self.printsetting.select_collapse_button()
        self.printsetting.select_print()
