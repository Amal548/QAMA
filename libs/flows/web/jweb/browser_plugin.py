from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class BrowserPlugin(JwebFlow):
    flow_name = "browser_plugin"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_browser_toggle_tab(self):
        """
        toggles the browser open/close tab
        :return:
        """
        self.driver.click("browser_toggle_tab_item")

    def enter_browser_url(self,option):
        """
        sends the browser_url to open
        :param option:
        :return:
        """
        self.driver.send_keys("browser_url_field_txt_box", option)

    def enter_web_scheme(self,option):
        """
        sends the web scheme
        :param option:
        :return:
        """
        self.driver.send_keys("browser_scheme_field_txt_box", option)

    def select_browser_test(self):
        """
        selects the test button
        :return:
        """
        self.driver.click("browser_test_btn")

    def browser_sign_in_result(self):
        """
        :return the browser sign in result
        """
        return self.driver.find_object("browser_sign_in_result_txt").text