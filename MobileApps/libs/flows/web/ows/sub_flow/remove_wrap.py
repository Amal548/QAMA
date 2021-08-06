import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class RemoveWrap(OWSFlow):
    flow_name = "remove_wrap"
    flow_url = "remove-wrap"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

       
    def click_skip_this_step(self):
        self.driver.click("skip_this_step_btn")
    
    def verify_successful_popup(self):
        return self.driver.wait_for_object("success_popup")
    
    @screenshot_compare(root_obj="success_popup",at_end=False)
    def click_successful_continue(self):
        return self.driver.click("success_popup_continue_btn")