from MobileApps.libs.flows.mac.jweb.jweb_flow import JwebFlow
import json
from time import sleep

class AuthPlugin(JwebFlow):
    flow_name = "auth_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_auth_logged_in_open(self):
        """
        clicks the auth open item
        :return:
        """
        self.driver.click("auth_is_logged_in_open_item")

    def select_auth_logged_in_test(self):
        """
        clicks the auth logged in test
        :return:
        """
        self.driver.click("auth_logged_in_test_btn")

    def auth_logged_in_result(self):
        """
        returns the auth logged in result
        :return:
        """
        self.driver.wait_for_object("auth_is_logged_in_result_txt")
        result = self.driver.get_attribute("auth_is_logged_in_result_txt", "AXValue")
        return json.loads(result)

    def select_auth_logged_in_close(self):
        """
        clicks the auth logged close item
        :return:
        """
        self.driver.click("auth_is_logged_in_close_item")

    def select_auth_get_token_open(self):
        """
        clicks the auth get token open
        :return:
        """
        self.driver.click("auth_get_token_open_item")


    def select_auth_get_token_test(self):
        """
        clicks the auth get token test button
        :return:
        """
        self.driver.click("auth_get_token_test_btn")

    def auth_get_token_result(self):
        """
        returns the auth get token result
        :return:
        """
        # get token result takes more time
        self.driver.wait_for_object("auth_get_token_result_txt")
        result = self.driver.get_attribute("auth_get_token_result_txt", "AXValue")
        return json.loads(result)

    def select_auth_get_token_close(self):
        """
        clicks the auth get token close
        :return:
        """
        self.driver.click("auth_get_token_close_item")

    def toggle_network_access(self, option):
        """
        clicks the allow network access switch based on the option flag
        :return:
        """
        self.driver.check_box('auth_network_access_switch', uncheck=option)

    def toggle_user_interaction(self, option):
        """
        clicks the allow user interaction switch based on the uncheck flag
        :return:
        """
        self.driver.check_box("auth_user_interaction_switch", uncheck=option)

    def toggle_show_account_creation_link(self, option):
        """
        clicks the allow account_creation_switch based on the option flag
        :return:
        """
        self.driver.check_box("auth_show_account_creation_link_switch", uncheck=option)

    def toggle_require_fresh_token(self, option):
        """
        clicks the require_fresh_token based on the option flag
        :return:
        """
        self.driver.check_box("auth_require_fresh_token_switch", uncheck=option)

    def toggle_skip_token_refresh(self, option):
        """
        clicks the require fresh token switch based on the option flag
        :return:
        """
        self.driver.check_box("auth_skip_token_refresh_switch", uncheck=option)

    def control_auth_token_switches(self,knobs):
        """
        controls the switches in auth plugin
        :return:
        """
        self.toggle_require_fresh_token(option=knobs[0])
        self.toggle_network_access(option=knobs[1])
        self.toggle_user_interaction(option=knobs[2])
        self.toggle_show_account_creation_link(option=knobs[3])
        self.toggle_skip_token_refresh(option=knobs[4])

    def select_auth_user_interaction_entry_point_selector(self):
        """
        selects the user interaction starting point
        :return:
        """
        self.driver.click("auth_user_interaction_entry_point_selector")

    def select_auth_sign_in_page_item(self):
        """
        selects the auth signin page
        :return:
        """
        self.driver.click("auth_sign_in_page_item")

    def select_auth_create_account_page_item(self):
        """
        selects the auth createAccount page
        :return:
        """
        self.driver.click("auth_create_account_page_item")

    def select_auth_logout_open(self):
        """
        clicks the auth logout open
        :return:
        """
        self.driver.click("auth_logout_open_item")

    def select_auth_logout_test(self):
        """
        clicks the auth logout test
        :return:
        """
        self.driver.click("auth_logout_test_btn")

    def auth_logout_result(self):
        """
        returns the auth logout result
        :return:
        """
        result = self.driver.get_attribute("auth_logout_result_txt", "AXValue")
        return json.loads(result)

    def select_auth_logout_close(self):
        """
        clicks the auth logout close
        :return:
        """
        self.driver.click("auth_logout_close_item")