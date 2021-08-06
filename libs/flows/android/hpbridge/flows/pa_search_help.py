# coding: utf-8
from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrintJobStatus
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import logging
from time import sleep


class PASearchHelp(HPBridgeFlow):
    flow_name = "pa_search_help"

    def click_first_time_binding_printer(self):
        """
        Click on the first time binding printer link on new function introduction page
        :return:
        """
        self.driver.wait_for_object("first_binding_printer").click()

    def click_page_function_introduction(self):
        """
        Click on the page function introduction link on new function introduction page
        :return:
        """
        self.driver.wait_for_object("page_function_intro").click()

    def check_web_page_title(self, web_page_title):
        """
        Check the web page - new function introduction page, page title
        :param web_page_title:
        :return:
        """
        self.driver.wait_for_object("first_time_binding_printer_page_title")
        page_title = self.driver.get_text("first_time_binding_printer_page_title")
        assert page_title == web_page_title
        logging.info("The web page title is:%s" % str(page_title).encode("utf-8"))
        self.driver.press_key_back()

    def check_search_help_wechat_page_head(self, page_head_name):
        """
        Check the search help page head which in wechat public account page
        :param page_head_name: from prototype_uitility PageTitle
        :return:
        """
        self.driver.switch_to_webview()
        page_head = self.driver.get_text("page_head_name")
        assert page_head == page_head_name
        logging.info("The android page head is: %s" % str(page_head).encode("utf-8"))

    def click_printer_setting_tab(self):
        """
        Click on printer setting tab on Wechat notice page
        :return:
        """
        self.driver.click("printer_setting_tab")
        sleep(1)

    def click_print_description_tab(self):
        """
        Click on printer description tab on Wechat notice page
        :return:
        """
        self.driver.wait_for_object("print_description_tab").click()
        sleep(1)

    def click_faq_tab(self):
        """
        Click on printer FAQ tab on Wechat notice page
        :return:
        """
        self.driver.click("faq_tab")
        sleep(1)

    def get_page_texts(self):
        """
        Get the page title and strings on contact customer support page
        :return:
        """
        self.driver.wait_for_object("contact_support_page_head")
        support_page_head = self.driver.get_text("contact_support_page_head")
        wechat_support = self.driver.get_text("contact_support_page_texts", index=0)
        phone_number_1 = self.driver.get_text("contact_support_page_texts", index=1)
        phone_number_3 = self.driver.get_text("contact_support_page_texts", index=3)
        logging.info("Contact customer page title %s \n details strings on the page: %s, \t %s \t %s" %
                     (support_page_head, wechat_support,
                      phone_number_1, phone_number_3))

    def select_a_printer_on_popup(self, printer_index):
        """
        Click on printer selection menu then select a printer
        :param printer_index: the index of the printer you want to select, starts from 1 since 0 is the
        option of the title
        :return:
        """
        self.driver.wait_for_object("submit_button")
        self.driver.click("printer_selection_box")
        # self.driver.click("select_printers_web",index=printer_index)
        self.driver.switch_to_webview()
        self.driver.click("select_printers_android", index=printer_index)
        self.driver.switch_to_webview(self.wechat_webview)

    def input_comments(self):
        """
        Enter strings in the input-box then click submit button
        :return:
        """
        self.driver.click("suggestion_box")
        self.driver.send_keys("suggestion_box",content="HP Bridge QA automation testing")
        self.driver.click("submit_button")
        logging.info("Your suggestion has been submitted")