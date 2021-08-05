# coding=utf-8

from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from time import sleep


class URLPrint(HPBridgeFlow):
    flow_name = "url_print"

    def click_url_article_print(self):
        """
        Click on web article print on mini program home screen
        :return
        """
        self.driver.wait_for_object("web_article_print")
        self.driver.click("web_article_print")

    def input_url_into_field(self, url):
        """
        Enter an URL into the text filed
        :return:
        """
        self.driver.wait_for_object("url_input_field")
        self.driver.click("url_input_field")
        self.driver.send_keys("url_input_field_click", url)

    def clear_input_input_box(self):
        """
        Clear the URL input field
        """
        self.driver.clear_text("url_input_field_click")

    def get_article(self, pic_mode=True):
        """
        On web article print page, send an url to the input-box then click on the get article button
        :param:pic_mode, default is picture mode, if txt mode, please set the pic_mode to false
        """
        self.click_get_article_btn()
        if pic_mode:
            self.driver.wait_for_object("pic_mode_prompt", timeout=15)
        else:
            self.driver.wait_for_object("txt_mode_prompt", timeout=15)
        self.driver.wait_for_object("generating_document_prompt", invisible=True)
        sleep(1)

    def click_get_article_btn(self):
        """
        Click on get article button on web article print page
        :return:
        """
        self.driver.wait_for_object("get_article_button").click()

    def back_from_print_preview(self):
        """
        Press key back from print preview page
        :return:
        """
        self.driver.press_key_back()

    def select_picture_mode_print(self):
        """
        Select the picture print mode radio button
        :return:
        """
        self.driver.click("picture_mode_radio_button")

    def select_txt_mode_print(self):
        """
        Select the text print mode radio button
        :return:
        """
        self.driver.click("txt_mode_radio_button")

    def process_to_print(self):
        """
        Click on process to print button
        :return:
        """
        self.back_from_print_preview()
        self.driver.wait_for_object("process_to_button", clickable=True, timeout=15)
        self.driver.click("process_to_button")

    def is_remind_pop_out(self):
        """
        Check if the copy message auto paste reminder pops out
        :return: True
        """
        return self.driver.wait_for_object("auto_past_prompt", raise_e=False)

    def check_if_reminder_pop_out(self):
        """
        Check if the copy message auto paste reminder pops out, if yes, click on confirm button
        :return:
        """
        if self.is_remind_pop_out():
            self.click_confirm_btn()

    def click_confirm_btn(self):
        """
        Click on the confirm button on the remind pops out
        """
        self.driver.click("confirm_btn")

    def click_how_to_get_article(self):
        """
        Click on how to get web article link
        :return:
        """
        self.driver.wait_for_object("how_to_get_article_url").click()

    def click_goahead_print(self):
        """
        Click on goahead print button
        :return:
        """
        self.driver.wait_for_object("process_to_button").click()

    def verify_urls_expand(self):
        """
        Verify the 3 urls after clicked how to get web article url
        :return:
        """
        self.driver.wait_for_object("wechat_public_account")
        self.driver.wait_for_object("regular_web_article")
        self.driver.wait_for_object("toutiao_url")

    def verify_paste_url_remind_msg(self):
        """
        Wait for the pops out message without enter URL on web article print page
        :return:
        """
        self.driver.wait_for_object("paste_url_reminder", timeout=6)

    def verify_web_article_page_ui(self):
        """
        Check the elements on web article home page
        :return:
        """
        self.check_if_reminder_pop_out()
        self.driver.wait_for_object("url_input_field")
        self.driver.wait_for_object("get_article_button")
        self.driver.wait_for_object("picture_mode_radio_button")
        self.driver.wait_for_object("txt_mode_radio_button")
        self.driver.wait_for_object("how_to_get_article_url")
        self.driver.wait_for_object("process_to_button")

    def verify_get_article_failed_prompt_msg(self, invalid_url=True):
        """
        After entered invalid url and click get web article, then check the prompt dialog
        :return:
        """
        self.driver.wait_for_object("get_article_failure_title")
        if invalid_url:
            self.driver.wait_for_object("get_article_failure_body")
        else:
            self.driver.wait_for_object("get_article_failure_body_blacklist_url")

    def verify_get_article_btn_changed(self):
        """
        Verify the get web article button changed to already got
        :return:
        """
        if not self.driver.wait_for_object("get_article_button",timeout=5, raise_e=False):
            self.driver.wait_for_object("got_button")


