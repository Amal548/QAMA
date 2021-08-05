from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException


class Clouds(SmartFlow):
    flow_name = "clouds"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_back(self):
        """
        Click on Back button on navigation bar
        End of flow: previous screen
        """
        self.driver.click("back_btn")

    def select_authorize(self):
        """
        Click on authorize after click on sign in button
        """
        self.driver.click("authorize_btn")

    def select_cloud_provider(self, cloud_name):
        """
        Click on a cloud button via its name
        End of flow: login screen of this cloud
        :param cloud_name: it is one of following constant value:
            BOX_NAME, DROP_BOX_NAME, EVER_NOTE_NAME
            FACEBOOK_NAME,GOOGLE_DRIVE_NAME,OTHER_NAME
        """
        self.driver.click(cloud_name)

########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_add_account_screen(self):
        """
         Verify Files screen
        """
        self.driver.wait_for_object("add_account_title")
        self.driver.wait_for_object("accounts")

    def verify_new_account_screen(self):
        """
         Verify Other - New Account screen
        """
        self.driver.wait_for_object("new_account_title")

    def login_to_evernote(self, username, password):
        """
        login into ever note using credentials
        :param username:
        :param password:
        :return:
        """
        self.driver.send_keys("email_tv", username)
        self.driver.click("continue_btn")
        self.driver.send_keys("password_tv", password)
        self.driver.click("signin_btn")
        try:
            self.driver.wait_for_object("authorized_btn")
            self.driver.click("authorized_btn")
        except TimeoutException:
            self.driver.click("reauthorize_btn")
    
    def verify_evernote_login_screen(self):
        """
        verify ever note login screen
        :return:
        """
        self.driver.wait_for_object("evernote_login_page_title")

    def verify_evernote_album_screen(self):
        """
        verify Ever note successfully linked to HP Smart
        :return:
        """
        self.driver.wait_for_object("evernote_album_header_title")

    def verify_evernote_authorize_screen(self):
        """
        verify Ever note successfully landed on authorize page after click on sign in button.
        :return:
        """
        self.driver.wait_for_object("evernote_authorize_page_header_title")
