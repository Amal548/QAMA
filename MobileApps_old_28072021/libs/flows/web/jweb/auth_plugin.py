from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow
import json

class AuthPlugin(JwebFlow):
    flow_name = "auth_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_auth_logged_in_toggle(self):
        """
        toggles the auth open item
        :return:
        """
        self.driver.click("auth_is_logged_in_toggle_item")

    def select_auth_logged_in_test(self):
        """
        clicks the auth logged in test
        :return:
        """
        self.driver.click("auth_is_logged_in_test_btn", timeout=5)

    def auth_logged_in_result(self):
        """
        returns the auth logged in result
        :return:
        """
        el_text = self.driver.wait_for_object("auth_is_logged_in_result_txt", timeout=15).text
        return json.loads(el_text)

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
        el_text = self.driver.wait_for_object("auth_get_token_result_txt", timeout=20).text
        return json.loads(el_text)

    def select_auth_get_token_close(self):
        """
        clicks the auth get token close
        :return:
        """
        self.driver.click("auth_get_token_close_item")

    def toggle_require_fresh_token(self, enable):
        """
        clicks the require_fresh_token_switch based on the enable flag
        :return:
        """
        state = self.driver.get_attribute("auth_require_fresh_token_switch", attribute="aria-checked")
        if state != enable:
            self.driver.click('auth_require_fresh_token_switch')

    def toggle_network_access(self, enable):
        """
        clicks the allow network_access_switch based on the enable flag
        :return:
        """
        state = self.driver.get_attribute("auth_network_access_switch", attribute="aria-checked")
        if state != enable:
            self.driver.click('auth_network_access_switch')

    def toggle_user_interaction(self, enable):
        """
        clicks the allow user_interaction_switch based on the enable flag
        :return:
        """
        state = self.driver.get_attribute("auth_user_interaction_switch", attribute="aria-checked")
        if state != enable:
            self.driver.click('auth_user_interaction_switch')

    def toggle_show_account_creation_link(self, enable):
        """
        clicks the allow account_creation_switch based on the option flag
        :return:
        """
        state = self.driver.get_attribute("auth_show_account_creation_link_switch", attribute="aria-checked")
        if state != enable:
            self.driver.click('auth_show_account_creation_link_switch')

    def toggle_skip_token_refresh(self, enable):
        """
        clicks the allow token_refresh_switch based on the enable flag
        :return:
        """
        state = self.driver.get_attribute("auth_skip_token_refresh_switch", attribute="aria-checked")
        if state != enable:
            self.driver.click('auth_skip_token_refresh_switch')

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

    def select_no_option_test_page_item(self):
        """
        selects the No Option (Test) page
        :return:
        """
        self.driver.click("auth_no_option_item")
    
    def select_invalid_test_option_page_item(self):
        """
        selects the No Option (Test) page
        :return:
        """
        self.driver.click("auth_invalid_option_item")

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
        el_text = self.driver.wait_for_object("auth_logout_result_txt").text
        return json.loads(el_text)

    def select_auth_logout_close(self):
        """
        clicks the auth logout close
        :return:
        """
        self.driver.click("auth_logout_close_item")

    def select_auth_add_listener_btn(self):
        """
        clicks the add listener btn
        :return:
        """
        self.driver.click("auth_add_listener_btn")

    def select_auth_remove_listener_btn(self):
        """
        clicks the remove listener btn
        :return:
        """
        self.driver.click("auth_remove_listener_btn")

    def auth_listener_text_result(self):
        """
        """
        return json.loads(self.driver.wait_for_object("auth_listener_result_text").text)
      
    def control_auth_token_switches(self, knobs):
        self.toggle_require_fresh_token(enable='true' if knobs[0] else 'false')
        self.toggle_network_access(enable='true' if knobs[1] else 'false')
        self.toggle_user_interaction(enable='true' if knobs[2] else 'false')
        self.toggle_show_account_creation_link(enable='true' if knobs[3] else 'false')
        self.toggle_skip_token_refresh(enable='true' if knobs[4] else 'false')

########################################################################################################################
#                                                                                                                      #
#                                        VERIFICATION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_logged_in_button(self):
        """
        verifies the loggedin button
        :return:
        """
        return self.driver.wait_for_object("logged_in_open_header_item", raise_e=False)

    def verify_get_token_button(self):
        """
        verifies the get token button
        :return:
        """
        return self.driver.wait_for_object("auth_get_token_test_btn", raise_e=False)

    def verify_logout_button(self):
        """
        verifies the logout button
        :return:
        """
        return self.driver.wait_for_object("auth_logout_test_btn", raise_e=False)