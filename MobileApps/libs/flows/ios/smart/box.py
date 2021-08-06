from selenium.common.exceptions import *
import logging

from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Box(SmartFlow):
    flow_name = "box"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_box_image(self):
        """
        clicks on the box image to login into box:
        :return:
        """
        self.driver.click("box_drive")

    def enter_email_address(self, email_address):
        """
        send the email address in text field
        :param email_address:
        :return:
        """
        self.driver.send_keys("email_tf", email_address)

    def enter_password(self, password):
        """
        clicks in the password text field and send the keys
        :param password:
        :return:
        """
        self.driver.click("password_tf")
        self.driver.send_keys("password_tf", password)

    def select_auth_box(self):
        """
        clicks the authorize button to login
        :return:
        """
        self.driver.click("auth_btn")

    def select_grant_access_btn(self):
        """
        clicks on the grant access button in next screen
        after sending the correct email address and password into box text fields
        :return:
        """
        self.driver.click("grant_access_btn")

    def select_box_back_btn(self):
        """
        selects the back button on box screen:
        :return:
        """
        self.driver.click("back_btn")


########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_box_login_screen(self):
        """
        Verify Login Cloud Screen - Box via:
            - Username text field : box title is same for few screens so we cant verify using title for ga counts
        """
        self.driver.wait_for_object("email_tf")

    def verify_box_login_screen_with_error_msg(self):
        """
        Verify Box Login screen with error msg via:
            - Error msg
        :return:
        """
        self.driver.wait_for_object("invalid_login_credentials_msg")

    def verify_box_screen(self):
        """
        Verify Box screen after logging in successfully: (final entered screen into box)
            - Box title
        """
        self.driver.wait_for_object("box_title")
        self.driver.wait_for_object("box_documents_tv")

    def verify_box_success_screen(self):
        """
        Verifies the Box successful login popup and clicks the grant access button
        :return:
        """
        self.driver.wait_for_object("grant_access_btn")

    def verify_box_added_success_popup(self):
        """
        verify the box added successfully popup by using message on popup
            some times (many in real) popup displays too quick so we just send the logging.info to know
        :return:
        """
        try:
            self.driver.wait_for_object("box_added_success_popup")
        except TimeoutException:
            logging.info("box added successfully popup is disappeared too quickly")


########################################################################################################################
#                                                                                                                      #
#                                   Functionality Sets                                                                 #
#                                                                                                                      #
########################################################################################################################

    def login_cloud_box(self, user_name="qa.mobiauto@gmail.com", password="mobileapp"):

        self.select_box_image()
        self.verify_box_login_screen()
        self.enter_email_address(user_name)
        self.enter_password(password)
        self.select_auth_box()
        self.verify_box_success_screen()
        self.select_grant_access_btn()
        self.verify_box_added_success_popup()
        self.verify_box_screen()
        self.select_box_back_btn()
