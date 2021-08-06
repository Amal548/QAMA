from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Welcome(SmartFlow):
    flow_name = "welcome"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################


########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_data_usage_ui_elements(self):
        self.driver.wait_for_object("_shared_yes")
        self.driver.wait_for_object("_shared_no")
        self.driver.wait_for_object("share_usage_data_title")
        self.driver.wait_for_object("data_usage_privacy_statement_link")
        self.driver.wait_for_object("google_analytics_link")
        self.driver.wait_for_object("adobe_privacy_link")

    def handle_welcome_ga_agreement(self, ga_agreement=True):
        self.driver.wait_for_object("share_usage_data_title")
        if ga_agreement:
            self.driver.wait_for_object("_shared_yes").click()
        else:
            self.driver.wait_for_object("_shared_no").click()
            
    def swipe_down_scrollview(self):
        if self.driver.wait_for_object("_shared_scrollview", raise_e=False):
            self.driver.swipe("_shared_scrollview", direction="down")