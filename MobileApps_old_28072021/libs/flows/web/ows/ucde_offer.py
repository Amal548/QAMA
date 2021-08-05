from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class UCDEOffer(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/program-offer/
    """
    flow_name = "ucde_offer"

    @screenshot_compare()
    def verify_ucde_offer(self):
        self.driver.wait_for_object("offer_page_div", timeout=20)

    def click_flex_sign_in_btn(self):
        self.driver.click("flex_sign_in_btn")

    def click_continue(self):
        self.driver.click("offer_page_continue_btn")

    @screenshot_compare()
    def verify_requirement_popup(self):
        self.driver.wait_for_object("requirement_popup_div")

    def click_requirement_popup_continue(self):
        self.driver.click("requirement_popup_continue_btn")

    def click_decline_account_btn(self):
        self.driver.click("decline_account_btn")

    def click_decline_offer_btn(self):
        self.driver.click("decline_offer_btn")

    #Manhattan pages
    @screenshot_compare()
    def verify_decline_offer_popup(self):
        self.driver.wait_for_object("decline_popup")

    def click_decline_hp_plus_offer_btn(self):
        self.driver.click("decline_hp+_btn")
    
    def click_back_to_offer_btn(self):
        self.driver.click("decline_popup_back_to_offer_btn")
