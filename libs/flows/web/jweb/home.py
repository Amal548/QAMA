from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

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
        self.driver.click("menu_btn")

    def select_plugins_tab_from_menu(self):
        """
        clicks the plugins tab from the menu 
        :returns:
        """
        self.driver.click("expand_plugins_menu_btn")

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

    def select_service_routing_plugin(self):
        """
        clicks the service routing plugin
        :return:
        """
        self.driver.click("service_routing_plugin_item")

    def select_device_plugin(self):
        """
        clicks the device plugin
        :return:
        """
        self.driver.click("device_plugin_item")

    def select_app_plugin(self):
        """
        clicks the app plugin (only on android)
        :return:
        """
        self.driver.click("app_plugin_item")

    def select_eventing_plugin_from_home(self):
        """
        from app homepage, navigate to eventing plugin
        :return:
        """
        self.select_menu()
        self.select_plugins_tab_from_menu()
        self.select_eventing_plugin()

    def select_app_plugin_from_home(self):
        """
        from app homepage, navigate to app plugin
        :return:
        """
        self.select_menu()
        self.select_plugins_tab_from_menu()
        self.select_app_plugin()

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def verify_menu_button(self):
        """
        verifies the menu button
        :return:
        """
        return self.driver.wait_for_object("menu_btn", raise_e=False)

    def verify_main_page(self):
        """
        verifies presently at the main page of the application
        :return:
        """
        return self.driver.wait_for_object("main_page", raise_e=False)