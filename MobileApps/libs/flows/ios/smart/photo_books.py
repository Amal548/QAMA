import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Photo_Books(SmartFlow):
    flow_name = "photo_books"

    #############################################################################
    #                           VERIFICATION FLOWS                              #            
    #############################################################################
    def verify_create_photo_books_screen(self):
        # top nav bar
        self.driver.wait_for_object("create_photo_books_header")
        self.driver.wait_for_object("_shared_back_arrow_btn")
        # buttons and text
        self.driver.wait_for_object("chatbooks_consent_msg")
        self.driver.wait_for_object("no_thanks_btn")
        self.driver.wait_for_object("get_my_photobook_btn")


    #############################################################################
    #                                 ACTION FLOWS                              #            
    #############################################################################
    def select_get_my_photobooks_btn(self):
        self.driver.click("get_my_photobook_btn")

    def select_no_thanks_btn(self):
        self.driver.click("no_thanks_btn")