from MobileApps.libs.flows.web.instant_ink.instantink_flow import InstantinkFlow
from MobileApps.libs.ma_misc import ma_misc

class ShippingII(InstantinkFlow):
    flow_name="shipping_ii"
    
    def verify_shipping_page_load(self):
        self.driver.wait_for_object("streetname_txt")

    def load_address(self):
        locale = "{}-{}".format(self.driver.session_data["language"], self.driver.session_data["locale"] )
        shipping_info = ma_misc.load_json_file("resources/test_data/instant_ink/shipping_info.json")[locale]
        self.driver.send_keys("streetname_txt", shipping_info["street"])
        self.driver.send_keys("cityname_txt",shipping_info["city"])
        self.driver.select("statename_dropdown", option_text=shipping_info["state"])
        self.driver.send_keys("zipcode_txt",shipping_info["zipcode"])
        self.driver.send_keys("phonenumber_txt",shipping_info["phone"])
    
    def save_shipping_address(self):
        self.driver.click("save_btn")

    def quick_add_address(self):
        self.driver.click("quick_add_address_btn")
    
    def printer_setup(self):
        self.driver.click("add_local_printer_btn")
        self.driver.click("save_local_printer_btn")
        self.driver.click("continue_printer_setup_btn")