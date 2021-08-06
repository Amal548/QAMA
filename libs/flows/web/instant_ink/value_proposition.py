from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow

class ValueProposition(InstantinkFlow):
    #URL: https://instantink-pie1.hpconnectedpie.com/us/en/n/v2/woobe/value_proposition
    flow_name="value_proposition"
    
    def verify_value_proposition_page(self, timeout=10):
        return self.driver.wait_for_object("value_proposition_div", timeout=timeout)

    def skip_value_proposition_page(self, timeout=10):
        """
        Skip Value Proposition screen:
            - Click on 
            - CLick on Yes, Skip Offer button 
        """
        self.verify_value_proposition_page(timeout=timeout)
        self.driver.click("skip_button")
        self.driver.click("yes_skip_offer_btn")

