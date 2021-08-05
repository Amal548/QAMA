from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Notifications(SmartFlow):
    flow_name = "notifications"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_first_notification(self):
        """
        Click on the first notification
        End of flow: Notification Details
        Device: Phone, Tablet
        """
        self.driver.click("first_notification_btn")

    def select_notifications_by_title(self, notification_title):
        """
        Select the notification from the Notifications list
        :return:
        """
        self.driver.click(notification_title)

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_notifications_screen(self):
        """
        Verify Notification navigation bar:
            - Notification title
            - Close btn
        Device: Phone
        """
        self.driver.wait_for_object("notification_title")
