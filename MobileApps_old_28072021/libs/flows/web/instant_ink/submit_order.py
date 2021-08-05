from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow
from MobileApps.libs.ma_misc import ma_misc

class SubmitOrder(InstantinkFlow):
    flow_name="submit_order"
    

    def verify_submitorder_page(self):
        self.driver.wait_for_object("enroll_btn")

    def complete_enrollment(self):
        self.driver.click("enroll_btn")
        self.driver.click("view_accountpage_btn",timeout=10)

        count_breadcrumbs=self.driver.find_object("breadcrumb_dots", multiple=True, raise_e=False)
        for cnt in count_breadcrumbs:
                self.driver.click("continue_btn")

        self.driver.click("finish_btn")