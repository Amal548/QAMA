from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PageTitle
from time import sleep
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging


class PAHPSupply(HPBridgeFlow):
    flow_name = "pa_hp_supply"

    def select_a_printer(self):
        """
        Select a printer from purchase supply->select a printer page
        :return:
        """
        self.driver.wait_for_object("printer_list")
        self.driver.click("printer_list", index=0)

    def close_supply_page(self):
        """
        Close the current page and change back to native view
        :return:
        """
        self.driver.click("page_close_icon")
        self.driver.switch_to_webview()

    def assert_page_title_is(self, page_title):
        """
        Check the page title
        :param page_title: from prototype_uitility PageTitle
        :return:
        """
        self.driver.switch_to_webview()
        page_head = self.driver.get_text("page_head")
        assert page_head == page_title

    def verify_hp_supply_club_app_name(self, mini_program_name):
        """
        Check the app name
        :param mini_program_name:
        :return:
        """
        self.driver.switch_to_webview()
        app_name = self.driver.get_text("hp_supply_club_app_head")
        assert app_name == mini_program_name
