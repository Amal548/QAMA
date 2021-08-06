# coding: utf-8
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PageTitle
import pytest
pytest.app_info = "hpbridge"


class TestFilePrint(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.pa_home = self.fc.flow["pa_home"]
        self.pa_search_help = self.fc.flow["pa_search_help"]

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. One or more printers bound to this login WeChat account.
            4. Follow the HP Cloud Print WeChat official account.
        """

    @pytest.fixture(scope="function", autouse="true")
    def recover_test_environment(self):
        self.driver.switch_to_webview()

    def test_01_new_function_introduction(self):
        """
        Steps:
                1.Go to public account and select "寻找帮助".
                2.Click "新功能介绍"
                3.Click the first time binding a printer lick
                4.Click page function introduction link

         Expected results:
                Verify the corresponding page can be opened successfully
        """
        self.wechat.goto_pa()
        self.pa_home.click_search_help()
        self.pa_home.click_new_function_introduction()
        self.pa_search_help.click_first_time_binding_printer()
        self.pa_search_help.check_web_page_title(PageTitle.FIRST_TIME_BINDING_PRINTER.value)
        self.pa_search_help.click_page_function_introduction()
        self.pa_search_help.check_web_page_title(PageTitle.PAGE_FUNCTION_INTRODUCTION.value)

    def test_02_wechat_print_notice(self):
        """
        Steps:
                1.Go to public account and select "寻找帮助".
                2.Click "微信打印须知"
                3.Click the first, second and thrid tab on the page
         Expected results:
                Verify the corresponding page can be opened successfully for each tab
        """
        self.wechat.goto_pa()
        self.pa_home.click_search_help()
        self.pa_home.click_wechat_print_notice()
        self.pa_search_help.click_print_description_tab()
        self.pa_search_help.click_faq_tab()
        self.pa_search_help.click_printer_setting_tab()
        self.pa_search_help.check_search_help_wechat_page_head(PageTitle.WECHAT_PRINT_NOTICE.value)

    def test_03_contact_support(self):
        """
        Steps:
                1.Go to public account and select "寻找帮助".
                2.Click "联系客服"
                3.Check the strings on the page

         Expected results:
                Verify the phone number and strings are correct
                Verify the page can be opened
        """
        self.wechat.goto_pa()
        self.pa_home.click_search_help()
        self.pa_home.click_contact_support()
        self.pa_search_help.get_page_texts()
        self.pa_search_help.check_search_help_wechat_page_head(PageTitle.CONTACT_SUPPORT.value)

    def test_04_suggestion_box(self):
        """
        Steps:
                1.Go to public account and select "寻找帮助".
                2.Click "意见箱"
                3.Click the dropdown menu and select a printer
                4. Enter comments into the inputbox
                5. Click submit button
         Expected results:
                Verify the page can be opened
                Verify comments can be successfully submitted
        """
        self.wechat.goto_pa()
        self.pa_home.click_search_help()
        self.pa_home.click_suggestion_box()
        self.pa_search_help.select_a_printer_on_popup(printer_index=1)
        self.pa_search_help.input_comments()
