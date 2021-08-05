from MobileApps.libs.flows.windows.jweb.jweb_flow import JwebFlow

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
        self.driver.click("menu_btn", timeout=15)

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