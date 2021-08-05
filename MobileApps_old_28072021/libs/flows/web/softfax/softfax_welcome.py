from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow

class SoftfaxWelcome(SoftFaxFlow):
    flow_name = "softfax_welcome"

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_welcome_screen(self, raise_e=True):
        return self.driver.wait_for_object("welcome_title", raise_e=raise_e)

class MobileSoftfaxWelcome(SoftfaxWelcome):
    context = "NATIVE_APP"

    def skip_welcome_screen(self, is_hipaa=False):
        """
            - Check Term of Agreement
            - Check No/Yes of HIPAA 
            - CLick Continue button
        """
        self.driver.click("agree_term_service_cb", timeout=10)
        hipaa_cb = "hipaa_yes_cb" if is_hipaa else "hipaa_no_cb"
        # Todo: wait for confirmation from devloper. Temprarily, skip it if it is not displayed instead of rasing NoSuchElementException
        self.driver.click(hipaa_cb, raise_e=False)
        self.driver.click("continue_btn", change_check={"wait_obj": "continue_btn", "invisible": True})

