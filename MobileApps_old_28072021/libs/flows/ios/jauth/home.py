from MobileApps.libs.flows.ios.jauth.jauth_flow import JauthFlow
import logging

class Home(JauthFlow):
    flow_name = "home"

    SIGN_IN_ERROR_RESULTS = {'network':'Error: networkNotAllowed("Attempted to open browser", nil)\n\nReason: Attempted to open browser',
                             'user_interaction':'Error: userInteractionNotAllowed("Attempted to open browser", nil)\n\nReason: Attempted to open browser',
                             'none':''}

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_settings(self):
        """
        clicks the settings button
        :return:
        """
        self.driver.click("settings_btn",timeout=10)

    def select_add(self):
        """
        clicks the add symbol
        :return:
        """
        self.driver.click("add_btn")

    def sign_in_result(self):
        """
        :return the sign_in_result
        """
        if self.driver.wait_for_object("sign_in_result", timeout=10):
            return self.driver.get_attribute("sign_in_result", "value")

    def select_accounts(self):
        """
        select accounts button to return to home
        """
        ## takes more time to show the hpid signed in accounts
        if self.driver.wait_for_object("accounts_button",timeout=30, interval=10):
            self.driver.click("accounts_button")

    def select_continue(self):
        """
        select continue button during the sign in
        """
        self.driver.click("continue_button",timeout=10, raise_e=False)

    def select_cancel(self):
        """
        select cancel button during the sign in
        """
        self.driver.click("cancel_button")

    def select_account_info(self,option):
        """
        select account info
        """
        if self.driver.wait_for_object("account_more_info_button",format_specifier=[option],timeout=10):
            self.driver.click("account_more_info_button",format_specifier=[option])

########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_home_settings(self, raise_e=False):
        """
            verifies the settings button on home page
        :return:
        """
        return self.driver.wait_for_object("settings_btn", raise_e=raise_e)

    def verify_empty_account_list(self, raise_e=True):
        """
            verifies the empty account list
        :return:
        """
        return self.driver.wait_for_object("empty_account_list", timeout=10, raise_e=raise_e)