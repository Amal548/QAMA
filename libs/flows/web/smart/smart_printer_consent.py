from MobileApps.libs.flows.web.smart.smart_flow import SmartFlow


class SmartPrinterConsent(SmartFlow):
    """
    url: https://www.hpsmartstage.com/in-app/android/v1_1/printer-consents?redirectU
    """
    flow_name = "smart_printer_consent"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_accept_all(self):
        """"
        Click on Accept All button
        """
        self.driver.click("accept_all_btn")

    def click_full_page_consent_continue(self):
        """"
        Click on continue button
        """
        self.driver.click("full_page_consent_title")
    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_printer_consent_screen(self, timeout=10):
        """
        Verify current screen is "Connected printing services"
        """
        self.driver.wait_for_object("title", timeout=timeout)
        self.driver.wait_for_object("accept_all_btn", timeout=timeout)
        self.driver.wait_for_object("manage_option_btn", timeout=timeout)

    def verify_printer_full_page_consent_screen(self):
        """"
        Verify the full page version of the consent page
        Usually shows up after creating an new account
        """        
        self.driver.wait_for_object("full_page_consent_title", timeout=20)
        self.driver.wait_for_object("full_page_consent_continue_btn")
    