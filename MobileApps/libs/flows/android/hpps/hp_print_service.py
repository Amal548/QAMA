
from MobileApps.libs.flows.android.hpps.hpps_flow import hppsFlow
import time


class HP_Print_Service(hppsFlow):
    """
    HP_Print_Service - Contains all elements with the HP Print Service Screen. This screen is located by clicking on the
                       Hp Print Service button in the Android Printing Setting page.
    """
    # Flow_name - Title of the ui map used in this class
    flow_name = "hp_print_service"

    ########################################################################################################################
    #                                                                                                                      #
    #                                                  Action Flows                                                        #
    #                                                                                                                      #
    ########################################################################################################################

    def accept_ok_for_document_passing(self):
        """
            select the OK button to allow the document to pass through he service.
        :return:
        """
        for _ in range(3):
            if self.driver.wait_for_object("Doc_pass_through_popup_window", raise_e=False, timeout=4):
                self.driver.click("Doc_pass_through_popup_window")
            else:
                break

    def agree_and_accept_terms_and_condition_if_present(self):
        """
        if the terms and condition popup appears in the system ui process agree and accept the condition
        :return:
        """
        if self.driver.wait_for_object("privacy_agreement_checkbox", raise_e=False, timeout=30):
            self.driver.click("privacy_agreement_checkbox")
            self.driver.click("privacy_agreement_start_btn")
            return True
        return False

    def dismiss_file_not_available_popup(self):
        """
        Dismiss file not available popup if it presents
        :return:
        """
        if self.driver.wait_for_object("file_not_available_popup_msg", raise_e=False, timeout=30):
            return self.driver.click("ok_btn", raise_e=False)
        return False

    def handle_hpps_t_and_c_notification_on_android_10_11_if_present(self):
        # For android 10, when going to System UI, instead of showing the popup, the notification will appear first
        # This is new user privacy enhancement feature on android 10
        if self.driver.driver_info['platformVersion'].split(".")[0] in ["10","11"]:
            self.driver.wdvr.open_notifications()
            if self.driver.wait_for_object("os10_11_t_and_c_notification", raise_e=False, timeout=5) is not False:
                self.driver.click("os10_11_t_and_c_notification") 
            else:
                self.driver.back()

    def turn_off_wifi_direct_notification_on_android_10_11_if_present(self):
        # For android 10, after agree to the t_and_c pop up. The wifi direct notification will appear
        if self.driver.driver_info['platformVersion'].split(".")[0] in ["10","11"]:
            self.driver.wdvr.open_notifications()
            if self.driver.wait_for_object("os10_wifi_direct_notification", raise_e=False, timeout=5):
                self.driver.click("wifi_direct_dont_show_again_button")
                self.driver.wait_for_object("wifi_direct_cancel_message_screen", timeout=5)
                self.driver.click("ok_btn") 
            else:
                self.driver.back()
