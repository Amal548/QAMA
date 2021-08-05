from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow
from MobileApps.libs.ma_misc import ma_misc

class BillingII(InstantinkFlow):
    flow_name="billing_ii"
    
    def select_payment_method(self):
        self.driver.click("select_creditcard_btn")

    def verify_creditcard_iframeload(self):
        self.driver.wait_for_object("creditcard_iframe")

    def load_card_details(self,cardtype):
        billing_info = ma_misc.load_json_file("resources/test_data/instant_ink/billing_info.json")[cardtype]

        # iframe=self.driver.wdvr.find_element_by_id("pgs-iframe-credit")
        # self.driver.wdvr.switch_to_frame(iframe)
        self.driver.switch_frame("creditcard_iframe")

        self.driver.click("creditcard_number_txt")
        self.driver.send_keys("creditcard_number_txt", billing_info["cardnumber"])
        self.driver.select("exp_month_dropdown", option_text=billing_info["month"])
        self.driver.select("exp_year_dropdown", option_text=billing_info["year"])
        self.driver.wait_for_object("cvv_txt")
        self.driver.send_keys("cvv_txt",billing_info["cvv"])
        # if frame_name == "default":
        #     self.wdvr.switch_to_default_content()
        self.driver.switch_frame()
        
        self.driver.click("SaveCreditdetails_btn",timeout=10)
        
        self.driver.click("PaymentOptionsContinue_btn",timeout=10)