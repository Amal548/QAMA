from mobiauto.mobiauto import MobiEzApp, MobiConfig, MobiUiMap
from mobiauto.mobidecor import MobiDecor
from selenium.common.exceptions import *
import logging
import time


class Gmail_v5_10(object):
    def __init__(self, app, cfg, ui):
        """

        :param app:
        :type app: MobiEzApp
        :param cfg:
        :type cfg: MobiConfig
        :param ui:
        :type ui: MobiUiMap
        :return:
        """
        self.app = app
        self.cfg = cfg
        self.ui = ui
        self.timeout = int(self.cfg.get("TIME", "timeout-5"))
        self.loading_timeout = int(self.cfg.get("TIME", "timeout-1"))

    #*****************************************************************************
    #                              ACTION FLOWS                                  *
    #*****************************************************************************
    @MobiDecor.start_end_flow
    def skip_welcome(self):
        """
        Skip all Welcome screen of Gmail app

        End of flow: Primary screen of one gmail

        Device: Phone
        """
        try:
            self.app.wait_for_visibility_of_element_located(self.ui.get_element("title", "welcome", check_screen=False), timeout=self.loading_timeout)
            self.app.click_on_element_by_pair_value(self.ui.get_element("got_it_btn", "welcome", check_screen=False), timeout=self.loading_timeout)
            self.app.click_on_element_by_pair_value(self.ui.get_element("take_me_btn", "welcome", check_screen=False), timeout=self.loading_timeout)
        except (TimeoutException, NoSuchElementException):
            logging.info("Current screen is NOT: Welcome")

    @MobiDecor.start_end_flow
    def select_gmail_menu(self):
        """
        Select Menu button on Gmail screen

        End of flow: Vertical navigation bar is displayed

        Device: Phone
        """
        self.app.click_on_element_by_pair_value(self.ui.get_element("menu_btn", "gmail_inbox", check_screen=False), timeout=self.loading_timeout)

    @MobiDecor.start_end_flow
    def switch_account(self, email_addr):
        """
        Switch to target account at vertical navigation bar
        :param email_addr: email's address

        End of flow: Gmail screen pf a folder

        Device: Phone
        """
        cur_acc = self.app.find_element_by_pair_value(self.ui.get_element("current_email_txt", "gmail_nav", check_screen=False)).text
        if cur_acc != email_addr:
            self.app.click_on_element_by_pair_value(self.ui.get_element("acc_list_btn", "gmail_nav", check_screen=False), timeout=self.loading_timeout)
            self.app.click_on_element_by_name(email_addr, timeout=self.loading_timeout)
        else:
            self.app.press_key_back()

    @MobiDecor.start_end_flow
    def select_folder(self, folder_name):
        """
        Select a folder in vertical navigation bar

        End of flow: Gmail screen of this folder
        :param folder_name: folder's name

        Device: Phone
        """
        self.app.scroll_down_to_element_by_name(self.app.find_element_by_pair_value(self.ui.get_element("nav_lv", "gmail_nav", check_screen=False)),
                                                name=folder_name, offset=int(self.cfg.get("SETTINGS", "offset-3")))
        self.app.click_on_element_by_name(folder_name, timeout=self.loading_timeout)

    @MobiDecor.start_end_flow
    def select_email_by_index(self, index=0):
        """
        Select an email of a folder by index

        :param index: index number. Default: 0

        Device: Phone
        """
        timeout = time.time() + self.loading_timeout + 10
        while time.time() < timeout:
            email_list = self.app.find_element_by_pair_value(self.ui.get_element("emails_lv", "gmail_inbox", check_screen=False))
            emails = email_list.find_elements_by_class_name(self.ui.get_class_name("email_cell", "gmail_inbox"))
            if len(emails) > 0:
                emails[index].click()
                break

    @MobiDecor.start_end_flow
    def select_print(self):
        """
        Click on Print button for an email

        End of flow: HPPS via system UI

        Device: Phone
        """
        self.app.click_on_element_by_pair_value(self.ui.get_element("option_btn", "email", check_screen=False), timeout=self.loading_timeout)
        self.app.click_on_element_by_pair_value(self.ui.get_element("print_btn", "email", check_screen=False), timeout=self.loading_timeout)

    @MobiDecor.start_end_flow
    def refresh_emails_list(self):
        """
        Refresh an email list by swiping down

        Device: Phone
        """
        self.app.wait_for_visibility_of_element_located_by_id(self.ui.get_id("email_frame_layout", "gmail_inbox"), timeout=self.loading_timeout)
        self.app.swipe_down(self.app.find_element_by_id(self.ui.get_id("email_frame_layout", "gmail_inbox")), offset=int(self.cfg.get("SETTINGS", "offset-2")))
        self.app.wait_for_visibility_of_element_located_by_id(self.ui.get_id("emails_lv", "gmail_inbox"), timeout=self.loading_timeout)