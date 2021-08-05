from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class AppPlugin(JwebFlow):
    flow_name = "app_plugin"

    def select_add_listener_btn(self):
        """
        click the add listener button inside of the app plugin
        """
        self.driver.click("add_listener_btn")

    def select_remove_listener_btn(self):
        """
        click the remove listener button inside of the app plugin
        """
        self.driver.click("remove_listener_btn")
    
    def close_pop_up_toast_text(self):
        """
        clicks the close btn inside of the pop up toast notification
        """
        self.driver.click("app_pop_up_toast_close")

    def get_pop_up_toast_text(self):
        """
        :returns: text found within pop up toast notification
        """
        return self.driver.wait_for_object("app_pop_up_toast_text").text

    def verify_app_plugin(self):
        """
        verifies presently at the app plugin page of the application
        :return:
        """
        return self.driver.wait_for_object("add_listener_btn", raise_e=False)