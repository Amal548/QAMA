from MobileApps.libs.flows.ios.jauth.jauth_flow import JauthFlow

class AccountInfo(JauthFlow):
    flow_name = "account_info"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_user_id(self,id):
        """
        verifies the user id for the account
        :return:
        """
        self.driver.find_object("email_and_user_id_txt",format_specifier=[id])

    def verify_email_id(self,id):
        """
        verifies the email address for the log in account
        :param id:
        :return:
        """
        self.driver.find_object("email_and_user_id_txt",format_specifier=[id])

    def select_get_token(self):
        """
        select the get token button
        :return:
        """
        self.driver.click("get_token_button", timeout=5)

    def select_sign_in(self):
        """
        select the sign in button
        :return:
        """
        self.driver.click("sign_in_button")

    def select_logout_button(self):
        """
        select the logout button
        :return:
        """
        self.driver.click("logout_button")

    def select_jarvis_auto(self):
        """
        select the jarvis auto button
        :return:
        """
        self.driver.click("jarvis_auto_btn")