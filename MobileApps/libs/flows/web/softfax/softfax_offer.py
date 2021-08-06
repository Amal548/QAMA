from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow


class SoftfaxOffer(SoftFaxFlow):
    flow_name = "softfax_offer"

    #*********************************************************************************
    #                               ACTION FLOWS                                     *
    #*********************************************************************************
    def skip_get_started_screen(self, raise_e=False):
        """
            - Click on Accept Cookie if it exist 
            - Click on Get Started button
        """
        self.driver.click("accept_cookies_btn", timeout=10, raise_e=raise_e)
        self.driver.click("get_started_btn", change_check={"wait_obj": "get_started_btn", "invisible": True}, raise_e=raise_e)


    def select_accept_cookies(self):
        """
        Click on Accept Cookie 
        """
        self.driver.click("accept_cookies_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_get_started_screen(self, raise_e=True):
        return self.driver.wait_for_object("mobile_fax_header", raise_e=raise_e)

    def verify_accept_cookies_popup(self, raise_e=True):
        """
        Verify accept cookies screen
        :param raise_e:
        """
        return self.driver.wait_for_object("accept_cookies_btn", raise_e=raise_e)
    
    def enroll_business_associate_agreement(self, name , email, entity, date=None):
        """
          - Fill the information
          - Accept the agreement
          - Click Continue button
        """
        self.driver.send_keys("name_value", name)
        self.driver.send_keys("email_value", email)
        self.driver.send_keys("entity_value",entity)
        if date != None:
            self.driver.send_keys("date_value" , date)
        self.driver.click("accept_agreement")
        self.driver.click("continue_agreement")
