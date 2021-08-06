from MobileApps.libs.flows.mac.jweb.jweb_flow import JwebFlow

class Home(JwebFlow):
    flow_name = "home"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_menu(self):
        """
        clicks the menu button
        :return:
        """
        if self.driver.wait_for_object("menu_btn", timeout=15):
            self.driver.click("menu_btn")

    def select_auth_browser_plugin(self):
        """
        clicks the auth browser plugin
        :return:
        """
        self.driver.click("auth_browser_plugin_item")

    def select_auth_plugin(self):
        """
        clicks the auth plugin
        :return:
        """
        self.driver.click("auth_plugin_item")

    def select_eventing_plugin(self):
        """
        clicks the eventing plugin
        :return:
        """
        self.driver.click("eventing_plugin_item")

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

    def click_close_btn(self):
        """
        This is a method to click close button.
        """
        self.driver.click("close_app")

    def click_always_allow(self):
        """
        This is a method to click allow always button.
        """
        if self.driver.wait_for_object("always_allow_button", raise_e=False):
            self.driver.click("always_allow_button")

########################################################################################################################
#                                                                                                                      #
#                                        VERIFICATION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_menu_button(self):
        """
        clicks the menu button
        :return:
        """
        return self.driver.wait_for_object("menu_btn", timeout=15, raise_e=False)

    def verify_close_button(self):
        """
        clicks the menu button
        :return:
        """
        return self.driver.wait_for_object("close_app", timeout=15, raise_e=False)
