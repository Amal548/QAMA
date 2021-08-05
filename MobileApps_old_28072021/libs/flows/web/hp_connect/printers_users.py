from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class PrintersUsers(HPConnectFlow):

    flow_name="printers_users"

    def __init__(self,driver, context=None):
        super(PrintersUsers, self).__init__(driver, context=context)

    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_users_btn(self):
        """
        Click on Users button on HP Smart menu screen
        """
        self.driver.click("users_btn")

    def click_printers_btn(self):
        """
        Click on Printers button on HP Smart menu screen
        """
        self.driver.click("printers_btn")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_users_screen(self):
        """
        Verify Users screen via:
        - Users title
        - Invite button
        """
        self.driver.wait_for_object("users_title")
        self.driver.wait_for_object("invite_button")

    def verify_printers_screen(self):
        """
        Verify Printers screen via:
        - printers title
        """
        self.driver.wait_for_object("printers_title")

class IOSPrintersUsers(PrintersUsers):

    context = "NATIVE_APP"

    # wasn't able to get webview clicks working on these 2 functions
    # seems like clicking the icon in native doesn't trigger the link
    # so you'd have to click the 'Users' textbox
    def click_users_btn(self):
        """
        Click on Users button on HP Smart menu screen
        """
        self.driver.click("users_btn")

    def click_printers_btn(self):
        """
        Click on Printers button on HP Smart menu screen
        """
        self.driver.click("printers_btn")