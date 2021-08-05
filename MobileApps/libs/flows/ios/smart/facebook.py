from selenium.common.exceptions import TimeoutException
import logging
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Facebook(SmartFlow):
    flow_name = "facebook"

    ########################################################################################################################
    #                                                                                                                      #
    #                                              ACTION  FLOWS                                                           #
    #                                                                                                                      #
    ########################################################################################################################

    def select_facebook(self):
        """
        :return:
        """
        self.driver.click("facebook_title")

    def select_back(self):
        """
        Select back arrow button
        """
        self.driver.click("back_arrow_btn")

    def select_first_album(self):
        """
        Selects the fist album listed in the facebook section
        :return:
        """
        self.driver.click("first_album")

    def select_multiple_photos_select_option(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_btn")

    def select_album_select(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_btn")

    def select_album_select_all(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.wait_for_object("select_all_btn")
        self.driver.click("select_all_btn")

    def select_confirm_ok(self):
        """
        Selects the ok button on the confirm page, if displayed
        :return:
        """
        try:
            self.driver.wait_for_object("auth_ok_btn")
            self.driver.click("auth_ok_btn")
        except TimeoutException:
            logging.warning("Facebook Confirm page was not displayed")

    def select_open_in_facebook(self):
        """
        Selects log in with facebook app
        :return:
        """
        self.driver.click("open_btn")

    def select_time_line_album(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("time_line_album")

    def select_log_in_with_the_facebook_app(self):
        """
        Selects log in with facebook app
        :return:
        """
        try:
            self.driver.click("continue_as_QA_btn")
        except TimeoutException:
            self.driver.click("continue_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Verification Flows
    #                                                                                                                      #
    ########################################################################################################################
    def verify_facebook_photos_login(self):
        """
        Verify if facebook was login screen / log in with app screen
        :return:
        """
        try:
            self.driver.wait_for_object("continue_as_QA_btn")
        except TimeoutException:
            self.driver.wait_for_object("continue_btn")

    def verify_facebook_photos_screen(self):
        """
        Verify if facebook was successfully imported into Photos
        :return:
        """
        self.driver.wait_for_object("facebook_title")

    def verify_facebook_photos_details(self):
        """
        verifies that you are in the albums folder
        :return:
        """
        self.driver.wait_for_object("album_title")

    def verify_facebook_photos_multi_select(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("select_all_btn")

    def verify_facebook_photos_albums_screen(self):
        """
        verifies that you are in the albums folder
        :return:
        """
        self.driver.wait_for_object("fb_photos_screen")

    def verify_photos_album(self):
        """
        verifies that you are in the albums folder
        :return:
        """
        self.driver.wait_for_object("photos_album")

    def verify_multiple_selected_photos_screen(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("next_btn")

    def fb_login_credentials(self, username="qa.mobiauto@gmail.com", password="mobileapp"):
        """

        :return:
        """
        self.driver.send_keys(obj_name="fb_user_name", content=username)
        self.driver.click("fb_password")
        self.driver.send_keys(obj_name="fb_password", content=password)
        self.driver.click("fb_login_btn")
        self.driver.click("continue_btn")

    def handle_facebook_is_already_login(self, username="qa.mobiauto@gmail.com", password="mobileapp"):
        """

        :return:
        """
        if self.driver.wait_for_object("continue_btn", raise_e=False):
            self.driver.click("continue_btn")
            logging.info("Facebook already logged in")
        else:
            self.driver.wait_for_object("login_text")
            logging.info("facebook on login screen")
            self.fb_login_credentials(username, password)

    def handle_messenger_is_already_login(self):
        """

        :return:
        """
        try:
            self.driver.wait_for_object("messenger_login_screen")
            logging.info("messenger on login screen")
        except TimeoutException:
            self.driver.wait_for_object("welcome_to_messenger_screen")
            self.driver.click("this_isnt_me_btn")
            logging.info("messenger already login screen")
