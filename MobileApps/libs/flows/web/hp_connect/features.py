from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class Features(HPConnectFlow):

    flow_name="features"

    def __init__(self,driver, context=None):
        super(Features, self).__init__(driver, context=context)


    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_features_btn(self):
        """
        Click on Features button on HP Smart menu screen
        """
        self.driver.click("features_btn")

    def click_print_anywhere_btn(self):
        """
        Click on Print Anywhere button on Features menu screen
        """
        self.driver.click("print_anywhere_btn")

    def click_other_features_btn(self):
        """
        Click on Other Features button on Features menu screen
        """
        self.driver.click("other_features_btn")

    def click_smart_security_btn(self):
        """
        Click on Smart Security button on Features menu screen
        """
        self.driver.click("smart_security_btn")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_features_screen(self, invisible=False):
        """
        Verify Features list screen via:
        - Print Anywhere
        - Other Features
        - Smart Security
        """
        self.driver.wait_for_object("print_anywhere_btn", invisible=invisible)
        self.driver.wait_for_object("other_features_btn", invisible=invisible)
        self.driver.wait_for_object("smart_security_btn")

    def verify_print_anywhere_screen(self):
        """
        Verify Print Anywhere screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("print_anywhere_title")
        self.driver.wait_for_object("print_anywhere_container")

    def verify_other_features_screen(self):
        """
        Verify Other Features screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("other_features_title")
        self.driver.wait_for_object("other_features_container")

    def verify_smart_security_screen(self):
        """
        Verify Smart Security screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("smart_security_title")
        self.driver.wait_for_object("smart_security_container")