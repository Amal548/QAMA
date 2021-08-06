from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class ValueProp(OWSFlow):
    """
    base class for all value prop - contains common buttons and UI
    - generic buttons locators based on template, actual content depends on the value prop feature
    - https://docs.google.com/document/d/1x9kin_uQZP1DgaJeTaEHGt53oYZkZ_P9GOQ902zOPm0/edit
    """
    project = "ows"
    flow_name = "value_prop"

    def select_primary_btn(self, change_check=False, timeout=10):
        change_check={"wait_obj": "_shared_primary_btn", "invisible": True} if change_check else False
        self.driver.click("_shared_primary_btn", change_check=change_check, timeout=timeout)

    def select_secondary_btn(self, change_check=False, timeout=10):
        change_check={"wait_obj": "_shared_secondary_btn", "invisible": True} if change_check else False
        self.driver.click("_shared_secondary_btn", change_check=change_check, timeout=timeout)
    
    def select_tertiary_btn(self, timeout=10):
        self.driver.click("_shared_tertiary_btn", timeout=timeout)

class OWSValueProp(ValueProp):
    """
    https://oss.hpconnectedpie.com/ucde/account-prop/
    """
    def verify_ows_value_prop_screen(self, tile=False, timeout=10):
        self.driver.wait_for_object("_shared_primary_btn", timeout=timeout)
        self.driver.wait_for_object("_shared_secondary_btn")
        self.driver.wait_for_object("_shared_tertiary_btn")
        if tile:            
            self.driver.wait_for_object("image_carousel")
        else:
            self.driver.wait_for_object("background_image")
    
    def select_value_prop_buttons(self, index=0, timeout=10):
        """
        - 0: setup printer / Create account button
        - 1: use hp smart / Sign In button
        - 2: explore hp smart / Close button
        """
        [self.select_primary_btn, self.select_secondary_btn, self.select_tertiary_btn][index](timeout=timeout)

class MobileValueProp(OWSValueProp):
    context = "NATIVE_APP"

    def verify_native_value_prop_screen(self):
        """
        In app value prop screen, scenario: select notification bell without sign in
        """
        self.driver.wait_for_object("_shared_sign_in")
        self.driver.wait_for_object("_shared_create_account")
        self.driver.wait_for_object("_shared_close")

    def select_native_value_prop_buttons(self, index=0, timeout=10):
        """
        - 0: Create account button
        - 1: Sign In button
        - 2: Close button
        """
        btns = ["_shared_create_account", "_shared_sign_in", "_shared_close"]
        self.driver.wait_for_object(btns[index], timeout=timeout).click()

