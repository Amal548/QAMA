from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow


class UCDEActivationSuccess(OWSFlow):
    """
    url: https://oss.hpconnectedpie.com/ucde/activation-success
    """
    flow_name = "ucde_activation_success"
    @screenshot_compare()
    def verify_ucde_activation_success(self, timeout=10):
        return self.driver.wait_for_object("activation_success_div", timeout=timeout)

    def click_continue(self, raise_e=True):
        self.driver.click("activation_success_continue_btn", raise_e=raise_e)