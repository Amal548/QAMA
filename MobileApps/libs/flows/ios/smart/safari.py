from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Safari(SmartFlow):
    flow_name = "safari"

########################################################################################################################                                                                                                                      #
#                                                  Verification Flows                                                  #
########################################################################################################################
    def verify_help_center_container(self, back_btn=True):
        """
        :param back_btn: (bool) True to check for back button, False to check for Close button on nav bar
        """
        self.driver.wait_for_object("help_center_nav_bar", format_specifier=[self.get_text_from_str_id("_shared_help_center")])
        self.driver.wait_for_object("help_document_web_view")
        if back_btn:
            self.driver.wait_for_object("_shared_back_arrow_btn")   
        else:
            self.driver.wait_for_object("_shared_close")

    def verify_account_prop(self):
        """
        verifies the account prop page https://oss.hpconnectedpie.com/account-prop/ native container
        longer timeout required since it waits until webview contents are loaded
        """
        self.driver.wait_for_object("account_prop_nav_bar", timeout=60)
        self.driver.wait_for_object("account_prop_more_btn")

    def verify_hp_privacy_statement(self):
        """
        verifies native top nav bar for HP Privacy Statement page: https://www8.hp.com/us/en/privacy/privacy-central.html
        """
        self.driver.wait_for_object("_shared_back_arrow_btn")
        self.driver.wait_for_object("hp_privacy_statement_navbar")

    def verify_photomyne_redirect_url(self):
        """
        verify redirected page for Try Photomyne button 
        """
        self.driver.wait_for_object("photomyne_url", timeout=20)
 