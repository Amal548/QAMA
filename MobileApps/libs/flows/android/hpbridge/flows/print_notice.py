# coding=utf-8

from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterNameOption, PrinterStatus, GroupName
from time import sleep
import logging


class PrintNotice(HPBridgeFlow):
    flow_name = "print_notice"

    def verify_reset_printer_service_question(self):
        """
        Verify the reset printer webservice question
        """
        self.driver.wait_for_object("reset_printer_webservice")

    def click_printer_setting_tab(self):
        """
        Wait for the printer setting tab then click on it
        """
        self.driver.wait_for_object("printer_setting_tab").click()

    def click_print_description_tab(self):
        """
        Wait for the print description tab then click on it
        """
        self.driver.wait_for_object("print_description_tab").click()

    def click_faq_tab(self):
        """
        Wait for the faq tab on print notice page then click on it
        """
        self.driver.wait_for_object("faq_tab").click()

    def click_how_to_contact_support_question(self):
        """
        Click on how to contact support question on faq tab
        """
        self.driver.wait_for_object("how_to_contact_support").click()

    def verify_content_in_contact_support(self):
        """
        Verify the content in how to contact support question on faq tab
        """
        self.driver.swipe(per_offset=0.3)
        self.driver.wait_for_object("contact_support_content")
        self.driver.wait_for_object("wechat_customer_support")