from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class UCDESafetyNet(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/safety-net/
    """
    flow_name = "ucde_safety_net"
    @screenshot_compare()
    def verify_ucde_safety_net(self):
        self.driver.wait_for_object("safety_net_page_div", timeout=20)

    def click_back_to_account_btn(self):
        self.driver.click("back_to_account_btn")

    def click_skip_warrenty_and_account_activation(self):
        self.driver.click("skip_warrenty_and_account_activation_btn")