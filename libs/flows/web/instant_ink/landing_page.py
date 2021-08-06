from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow

class LandingPage(InstantinkFlow):
    flow_name="landing_page"
    

    stack_url={"pie" : "https://instantink-pie1.hpconnectedpie.com/us/en/l/",
               "stage" : "https://instantink-stage1.hpconnectedstage.com/us/en/l/"}

    def navigate_instant_ink_page(self,stack):
        self.driver.wdvr.get(self.stack_url[stack])
           
    def verify_instant_ink_page_load(self):
        self.driver.wait_for_object("sign_up_btn")

    def click_sign_up_button(self):
        self.driver.click("sign_up_btn")