import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class NoEmailAccount(Exception):
    pass

class SpecificEmailAccountDoesNotExist(Exception):
    pass

class Gmail(SmartFlow):
    flow_name = "gmail"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def compose_and_send_email(self, to_email, subject_text="", body_text=""):
        self.driver.wait_for_object("to_field")
        self.driver.click("to_field")
        self.driver.send_keys("to_field", to_email, press_enter=True)
        if subject_text:
            try:
                self.driver.click("subject_field")
                self.driver.long_press("subject_field")
                self.driver.click("_shared_select_all_btn")
            except NoSuchElementException:
                logging.info("subject field is empty")
            self.driver.send_keys("subject_field", subject_text)
        self.driver.click("send_btn")
        if (self.handle_send_email_popup() or self.verify_reduce_message_displayed()) is not False:
            self.click_on_btn('actual')

    def handle_send_email_popup(self):
        return self.driver.wait_for_object("continue_btn", timeout=20, raise_e=False) is not False

    def verify_reduce_message_displayed(self):
        return self.driver.wait_for_object("reduce_message_size_title_txt", timeout=20, raise_e=False) is not False

    def click_on_btn(self, btn_name):
        all_btn_on_page = self.driver.find_object("all_btn_in_page", multiple=True)
        for btn in all_btn_on_page:
            if btn_name.lower() in btn.text.lower():
                btn.click()

    def get_email_navigation_bar_title(self):

        self.driver.wait_for_object("to_field")
        return str(self.driver.get_attribute("navigation_bar_title", attribute="name")).strip()