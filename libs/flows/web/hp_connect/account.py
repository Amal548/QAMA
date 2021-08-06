from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow

class Account(HPConnectFlow):

    flow_name="account"

    def __init__(self,driver, context=None):
        super(Account, self).__init__(driver, context=context)


    ###############################################################################
    #                             Action flows
    ###############################################################################

    def click_account_btn(self):
        """
        Click on Account button on HP Smart menu screen
        """
        self.driver.click("account_btn")

    def click_account_profile_btn(self):
        """
        Click on Account Profile button on Account menu screen
        """
        self.driver.click("account_profile_btn")

    def click_view_notifications_btn(self):
        """
        Click on View Notifications button on Account menu screen
        """
        self.driver.click("view_notifications_btn")

    def click_notification_settings_btn(self):
        """
        Click on Notification Settings button on Account menu screen
        """
        self.driver.click("notification_settings_btn")

    def click_privacy_settings_btn(self):
        """
        Click on Privacy Settings button on Account menu screen
        """
        self.driver.click("privacy_settings_btn")

    def click_billing_btn(self):
        """
        Click on Billing button on Account menu screen
        """
        self.driver.click("billing_btn")

    def click_shipping_btn(self):
        """
        Click on Shipping button on Account menu screen
        """
        self.driver.click("shipping_btn")

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_account_menu_screen(self):
        """
        Verify Account menu screen via:
        - Account Profile
        - View Notifications
        - Notification Settings
        - Privacy Settings
        """
        self.driver.wait_for_object("account_profile_btn")
        self.driver.wait_for_object("view_notifications_btn")
        self.driver.wait_for_object("notification_settings_btn")
        self.driver.wait_for_object("privacy_settings_btn")

    def verify_view_notifications_screen(self):
        """
        Verify View Notifications screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("view_notifications_title")
        self.driver.wait_for_object("view_notifications_container")

    def verify_notification_settings_screen(self):
        """
        Verify Notification Settings screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("notification_settings_title")
        self.driver.wait_for_object("notification_settings_container")

    def verify_privacy_settings_screen(self):
        """
        Verify Privacy Settings screen via:
        - title
        - Message
        """
        self.driver.wait_for_object("privacy_settings_title")
        self.driver.wait_for_object("privacy_settings_container")

    def verify_billing_screen(self):
        """
        Verify Billing screen via:
         - title
          - Message
        """
        self.driver.wait_for_object("billing_title")
        self.driver.wait_for_object("billing_container")

    def verify_shipping_screen(self):
        """
        Verify shipping screen via:
         - title
          - Message
        """
        self.driver.wait_for_object("shipping_title")
        self.driver.wait_for_object("shipping_container")