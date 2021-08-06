
import re
import pytest
import string
import random
import logging
import datetime

from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.flows.web.web_flow import WebFlow
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from MobileApps.libs.flows.email.gmail_api import GmailAPI
from SAF.decorator.saf_decorator import screenshot_capture

class HPID(WebFlow):
    project = "hp_id"
    flow_name="hp_id"

    @screenshot_capture(file_name="signin_screen.png")
    def verify_hp_id_sign_in(self, raise_e=True, timeout=10):
        """
        Based on version 09/11 of sign in screen via Chrome browser, not sure for element "sign_in_page_identify_object"
        :param raise_e:
        :return:
        """
        if pytest.platform.lower() == "android":
            self.dismiss_connection_not_private()
            # After this function, a new window is added into the list. It is the right one for next line
            # Switch to the right window for next line
            self.switch_to_window(WEBVIEW_URL.HPID)
        self.handle_privacy_popup()
        return self.driver.wait_for_object("sign_in_username_txt_box", timeout=timeout, raise_e=raise_e)

    def handle_privacy_popup(self):
        if self.driver.wait_for_object("privacy_pop_up", timeout=3, raise_e=False) is not False:
            self.driver.click("privacy_accept_btn")
        return True

    @screenshot_capture(file_name="signup_Screen.png")
    def verify_hp_id_sign_up(self, timeout=10, raise_e=True):
        self.handle_privacy_popup()
        return self.driver.wait_for_object("sign_up_form_firstname_txtbx", timeout=timeout, raise_e=raise_e)

    def login(self, username, password):
        """
        Login to an account
        Note: Tested the flow of version 09/11 on via Chrome browser
        :param username:
        :param password:
        :return:
        """
        self.driver.send_keys("sign_in_username_txt_box", username)
        self.driver.click("sign_in_next_btn", change_check={"wait_obj": "sign_in_next_btn", "invisible": True})
        self.driver.wait_for_object("sign_in_password_txt_box", interval=1, timeout=10)
        self.driver.send_keys("sign_in_password_txt_box", password)
        self.driver.click("sign_in_button")
        self.driver.performance.start_timer("hpid_login")

    def click_create_account_link(self):
        #Clicking the don't have an account link at the enter account page
        self.driver.wait_for_object("create_account_link", timeout=20)
        self.driver.click("create_account_link", change_check={"wait_obj": "create_account_link", "invisible": True})

    def click_sign_in_link_from_create_account(self):
        self.driver.wait_for_object("sign_in_link_from_create_account").click()
    
    def click_back_button(self):
        """
        selects the back button if just the username is entered into the hpid login page, and clears the username text box
        """
        self.driver.click("back_btn")
        self.driver.click("sign_in_username_txt_box")
        self.driver.long_press("sign_in_username_txt_box")
        self.driver.find_object("sign_in_username_txt_box").send_keys(" ")
        self.driver.find_object("sign_in_username_txt_box").send_keys(Keys.BACK_SPACE)
        self.driver.find_object("sign_in_username_txt_box").send_keys(Keys.BACK_SPACE)
        

    def create_account(self, firstname="test", lastname="test", email=None, password="123456aA", gmail=None):
        """
        This method is for when you are at the HP ID sign up screen walk through the sign up form
        Required param of printer_serial and stack is for updating in the database for proper clean up
        @param gmail: GmailAPI -> used for another gmail token besides default one
        """
        self.driver.send_keys("sign_up_form_firstname_txtbx", firstname)
        self.driver.send_keys("sign_up_form_lastname_txtbx", lastname)
        if not email:
            username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
            domain = username.split("@")[1]
            # use + to create sub email from main email account
            # Adding a tiny salt to avoid collision further
            salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6)) 
            email = "{}+{:%Y_%m_%d_%H_%M_%S}_{}@{}".format(username[0:username.rfind("@")], datetime.datetime.now(), salt, domain)
        self.driver.send_keys("sign_up_form_email_txtbx", email)
        logging.info("Sign up email: " + email)
        self.driver.send_keys("sign_up_form_create_password", password)
        #V3 version have confirm password
        if self.driver.wait_for_object("sign_up_form_confirm_password", timeout=3, raise_e=False):
            self.driver.send_keys("sign_up_form_confirm_password", password)
        logging.info("Sign up password: " + password)
        #self.driver.swipe()
        captcha_iframe = self.driver.wait_for_object("captcha_iframe", timeout=3, raise_e=False)
        if captcha_iframe is not False:
            self.driver.wdvr.switch_to_frame(captcha_iframe)
            self.driver.click("captcha_check_box")
            self.driver.wdvr.switch_to_default_content()
        self.driver.click("sign_up_form_create_account_button", change_check={"wait_obj": "sign_up_form_create_account_button", "invisible": True})
        self.driver.performance.start_timer("hpid_create_account")
        try:
            self.driver.wait_for_object("sign_up_form_create_account_button", invisible=True, timeout=3)
        except WebDriverException:
            sleep(3)
        """
        timeout = 10
        start_time = time.time()
        while time.time() - start_time <= timeout:
            try:
                if self.driver.wait_for_object("verification_code_txt_box", timeout=3, raise_e=False) is not False:
                    gmail = GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH) if not gmail else gmail
                    self.dismiss_verification_email_screen(gmail, to=email)
                    break
            except WebDriverException:
                logging.debug("Possible the window closed for mobile testing so catching it here")
                sleep(2)
        """
        return email, password

    def dismiss_verification_email_screen(self, gmail, to):
        """
        It is new feature for Stratus Auth Z on Pie and Stage Stack server
        After creating accoun, if  "Verify your email address" screen display, dismiss it by
            - Get barcode from email which is used to create account 
            - Enter this barcode to text box -> click on SUBMIT button
            - Skip next screen by clicking on skip... buton
        @param gmail: GmailAPI
        @param to: to email address
        """
        code = gmail.get_hpid_verification_code(to=to) 
        self.driver.send_keys("verification_code_txt_box", code)
        self.driver.click("verification_code_submit_btn")
        self.driver.click("continue_btn", timeout=10)


    def dismiss_account_verification_again(self, gmail=None, timeout=10):
        """
        Dismiss Account Verification by sending email again:
            - Click on Send Email button
            - Using dismiss_verification_email_screen() to verify account
        @param gmail: GmailAPI
        """
        if self.driver.wait_for_object("send_email_msg_txt", timeout=timeout, raise_e=False):
            gmail = GmailAPI(credential_path=TEST_DATA.GMAIL_TOKEN_PATH) if not gmail else gmail
            email = re.search("\S+@\S+", self.driver.find_object("send_email_msg_txt").text).group(0)[:-1]
            # Delete all previous emails for verification code which have the same 'to' email
            gmail.delete_hpid_verification_code_email(to=email)
            self.driver.click("send_email_btn")
            self.dismiss_verification_email_screen(gmail, to=email)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************

    def verify_invalid_credential_msg(self):
        """
        Verify invisible invalid credential message after logging in with invalid account
        """
        self.driver.wait_for_object("invalid_credential_msg", timeout=10)

    def verify_create_an_account_page(self, raise_e=True):
        """
        verify the create an HP account page
        """
        return self.driver.wait_for_object("create_your_hp_account_button", raise_e=raise_e) is not False

    def verify_account_sign_up_link(self):
        """
        verify the 'Don't have an account?' sign up link 
        """
        return self.driver.wait_for_object("create_account_link", raise_e=False) is not False

class MobileHPID(HPID):
    context = "NATIVE_APP"

    def login(self, username, password, change_check=None):
        self.driver.click("sign_in_username_txt_box", timeout=10)
        self.driver.send_keys("sign_in_username_txt_box", username)
        self.driver.click("sign_in_next_btn", timeout=10, change_check={"wait_obj": "sign_in_password_txt_box"})
        self.driver.click("sign_in_password_txt_box")
        self.driver.send_keys("sign_in_password_txt_box", password)
        self.driver.click("sign_in_button", change_check=change_check)
        self.driver.performance.start_timer("hpid_login")