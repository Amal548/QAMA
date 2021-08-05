from MobileApps.libs.flows.ios.jauth.jauth_flow import JauthFlow

class Settings(JauthFlow):
    flow_name = "settings"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def toggle_network_access(self,disable):
        """
        clicks the allow network access switch based on the disable flag
        :return:
        """
        self.driver.check_box('network_access_switch',uncheck=disable)       

    def toggle_user_interaction(self,disable):
        """
        clicks the allow user interaction switch based on the disable flag
        :return:
        """
        self.driver.check_box("user_interaction_switch",uncheck=disable)
            
    def toggle_show_account_creation_link(self,disable):
        """
        clicks the allow account_creation_switch based on the disable flag
        :return:
        """
        self.driver.check_box("show_account_creation_link_switch",uncheck=disable)

    def toggle_start_on_create_account_switch(self,disable):
        """
        clicks the allow start on create account switch based on the disable flag
        :return:
        """
        self.driver.check_box("start_on_create_account_switch",uncheck=disable)
    
    def toggle_skip_token_refresh(self,disable):
        """
        clicks the allow token_refresh_switch based on the disable flag
        :return:
        """
        self.driver.check_box("token_refresh_switch",uncheck=disable)
            
    def toggle_require_fresh_token(self,disable):
        """
        clicks the require fresh token switch based on the disable flag
        :return:
        """
        self.driver.check_box("require_fresh_token_switch",uncheck=disable)
            
    def control_auth_token_switches(self,knobs):
        self.toggle_network_access(disable=knobs[0])
        self.toggle_user_interaction(disable=knobs[1])
        self.toggle_show_account_creation_link(disable=knobs[2])
        self.toggle_start_on_create_account_switch(disable=knobs[3])
        self.toggle_skip_token_refresh(disable=knobs[4])
        self.toggle_require_fresh_token(disable=knobs[5])

    def select_scopes_requested(self):
        """
        clicks the scopes requested tab
        :return:
        """       
        self.driver.click("scopes_requested")
        
    def toggle_use_biometrics(self,disable):
        """
        clicks the use biometrics tab based on the disable flag
        :return:
        """
        self.driver.check_box("use_biometrics_switch",uncheck=disable)
        
    def select_done(self):
        """
        clicks the done button
        :return:
        """
        self.driver.click("done_button")

    def select_app_settings(self):
        """
        clicks the apps settings
        :return:
        """
        self.driver.click("app_settings")

    def toggle_self_signed_certificates(self,disable):
        """
        checks the accept self signed certificates switch based on the disable flag
        :return:
        """
        if self.driver.wait_for_object("accept_self_signed_certificates_switch",timeout=20):
            self.driver.check_box("accept_self_signed_certificates_switch", uncheck=disable)