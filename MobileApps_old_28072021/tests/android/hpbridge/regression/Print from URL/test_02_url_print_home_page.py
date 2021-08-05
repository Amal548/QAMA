# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
pytest.app_info = "hpbridge"


class TestURLPrintFlow(object):

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
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account and enter the WeChat Applet.
            3. There is one or more printers bound to the account.
        """
    def test_01_url_print_home_ui_check(self):
        """
        Steps:
            1. Launch the Applet, click the "网络文章打印" button
            2. Check the "网络文章打印" home page

        Expected result:
            Verify "复制网络文章的链接至下方" with an input box and "获取文章" button display on the top of this page.
            Verify there are "图文模式" and "纯文本模式" sections displayed on this page and "图文模式" section is checked by default.
            Verify there is a link "如何获取网络文章的链接?" displayed well with expand button.
            Verify there is a hint "温馨提示： a.打印前请先预览文档以确保打印最佳效果 b.此功能仅限个人学习使用。" displayed well on this page.
            Verify the "前往打印" button displayed with gray and un-clickable on the bottom of this page.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.verify_web_article_page_ui()

    def test_02_url_print_home_functional_test(self):
        """
        Steps:
            1. On URL web article print page, enter some content to the "复制网络文章的链接至下方" input box.
            2. Delete the entered content.
            3. Click the "纯文本模式" section
            4. Click the "图文模式" section.
            5. Click the "如何获取网络文章的链接?" link.
        Expected result:
            Verify the content can be entered successfully and the input box works well.
            Verify the content can be deleted successfully.
            Verify the "纯文本模式" section can be checked successfully.
            Verify the "图文模式" section can be checked successfully.
            Verify the link can be expanded correctly with 微信公众号，普通网络文章，今日头条 sections in a line.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.select_txt_mode_print()
        self.urlprint.select_picture_mode_print()
        self.urlprint.click_how_to_get_article()
        self.urlprint.verify_urls_expand()

    def test_03_url_print_home_page_button_check(self):
        """
        Steps:
            1.Launch the Applet and click the "网络文章打印" button.
            2.Click the "纯文本模式" section.
            3.Click the "图文模式" section.
            4.Click the"前往打印" button.
        Expected result:
            1.Verify the "网络文章打印" home page displayed correctly.
            2.Verify the "纯文本模式" section can be checked successfully.
            3.Verify the "图文模式" section can be checked successfully.
            4.Verify the "前往打印" button displayed with gray and unclickable on the bottom of this page.
        """
        self.wechat.scan_qrcode_to_mp()
        self.binding.bind_printer(bound=False)
        self.mphome.click_url_article_print_section()
        self.urlprint.select_txt_mode_print()
        self.urlprint.select_picture_mode_print()
        self.urlprint.click_goahead_print()
