# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestURLPrintUnhappyPath(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup
        # cls.p = load_printers_session

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mphome = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]
        self.urlprint = self.fc.flow["url_print"]

        # Define variables
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()
        self.invalid_url = "invalid url"
        self.blacklist_url = "https://www.toutiao.com/a6697860415793136142"
        """
        Pre-conditions:
            1.Install the WeChat app.
            2.Login Wechat with a valid account and enter the WeChat Applet.
            3.There is one or more printers bound to the account.
        """
    def test_01_url_print_without_url(self):
        """
        Steps:
            1.Launch the Applet and click the "网络文章打印" button.
            2.Click the "纯文本模式" section.
            3.Click the "获取文章" button without enter any content in "请将网络文章的链接粘贴至下方" input box.
            4.Click the "图文模式" section.
            5.Click the "获取文章" button without enter any content in "请将网络文章的链接粘贴至下方" input box.
        Expect results:
            1.Verify the "网络文章打印" home page displayed corectly.
            2.Verify the "纯文本模式" section can be checked successfully.
            3.Verify the "请粘贴网络文章链接!" message will pop up for a while and then disappear automatically.
            4.Verify the "图文模式" section can be checked successfully.
            5.Verify the "请粘贴网络文章链接!" message will pop up for a while and then disappear automatically.
        """
        # printer = utlitiy_misc.load_printer()
        # self.wechat.send_qrcode(printer["index"])
        self.wechat.send_qrcode(qrcode_index=0)
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.select_txt_mode_print()
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_paste_url_remind_msg()
        self.urlprint.select_picture_mode_print()
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_paste_url_remind_msg()

    def test_02_url_print_with_invalid_url(self):
        """
        Steps:
            1.Launch the Applet and click the "网络文章打印" button.
            2.Click the "纯文本模式" section.
            3.Enter some invalid URL or content to the "复制网络文章的链接至下方" input box.
            4.Click the "获取文章" button.
            5.Click the "确定" button.
            6.Click the "图文模式" section.
            7.Click the "获取文章" button.
            8.Click the "确定" button.
        Expected result:
            1.Verify the "网络文章打印" home page displayed correctly.
            2.Verify the "纯文本模式" section can be checked successfully.
            3.Verify the content can be entered successfully and the input box works well.
            4.Verify "纯文本模式生成中。。" message pop up for a while and then an error message " 获取网络文章失败，链接错误或当前网络文章不支持此功能" display with "确定" button.
            5.Verify the error message disappear and "网络文章打印" home page displayed with the entered invalid content.
            6.Verify the "图文模式" section can be checked successfully.
            7.Verify "图文模式生成中。。" message pop up for a while and then an error message " 获取网络文章失败，链接错误或当前网络文章不支持此功能" display with "确定" button.
            8.Verify the error message disappear and "网络文章打印" home page displayed with the entered invalid content.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.select_txt_mode_print()
        self.urlprint.input_url_into_field(self.invalid_url)
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_get_article_failed_prompt_msg()
        self.urlprint.click_confirm_btn()
        self.urlprint.select_picture_mode_print()
        self.urlprint.input_url_into_field(self.invalid_url)
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_get_article_failed_prompt_msg()
        self.urlprint.click_confirm_btn()

    def test_03_url_print_with_blacklist_urls(self):
        """
        Steps:
            1.Launch the Applet and click the "网络文章打印" button.
            2.Click the "纯文本模式" section.
            3.Enter or copy a blacklist URL to the "复制网络文章的链接至下方" input box.
            4.Click the "获取文章" button.
            5.Click the "确定" button.
            6.Click the "图文模式" section.
            7.Click the "获取文章" button.
            8.Click the "确定" button.
        Expected result:
            1.Verify the "网络文章打印" home page displayed correctly.
            2.Verify the "纯文本模式" section can be checked successfully.
            3.Verify the blacklist URL can be entered successfully and the input box works well.
            4.Verify "纯文本模式生成中。。" message pop up for a while and then an error message "无法获取该网站的网络文章，请重新选择其他链接地址" display with "确定" button.
            5.Verify the error message disappear and "网络文章打印" home page displayed with the entered blacklist URL.
            6.Verify the "图文模式" section can be checked successfully.
            7.Verify "图文模式生成中。。" message pop up for a while and then an error message "无法获取该网站的网络文章，请重新选择其他链接地址" display with "确定" button.
            8.Verify the error message disappear and "网络文章打印" home page displayed with the entered blacklist URL.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.verify_web_article_page_ui()
        self.urlprint.select_txt_mode_print()
        self.urlprint.input_url_into_field(self.blacklist_url)
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_get_article_failed_prompt_msg(invalid_url=False)
        self.urlprint.click_confirm_btn()
        self.urlprint.select_picture_mode_print()
        self.urlprint.input_url_into_field(self.blacklist_url)
        self.urlprint.click_get_article_btn()
        self.urlprint.verify_get_article_failed_prompt_msg(invalid_url=False)
        self.urlprint.click_confirm_btn()



