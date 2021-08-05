from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow


class Offers(InstantinkFlow):
    """
    url: https://instantink-stage1.hpconnectedstage.com/us/en/n/signup/offers...
    Note: This url is for Moobe process in Smart app. 
          This link is redirected to another link when it is opened in browser
          Therefore, the flows are just for Moobe process in Mobile's Smart app.
    """
    flow_name="offers"

    def skip_instant_ink_enrollment(self):
        """
            - Swipe to right until last card displays
            - CLick on "Do not enable instant ink"
        """
        self.driver.wait_for_object("offer_title")
        for _ in range(3):
            # Since this flow is used for Mobile only, 
            # so using swipe() to scroll to right 
            self.driver.swipe(direction="right")
        self.driver.click("do_not_enable_ink_savings_btn")