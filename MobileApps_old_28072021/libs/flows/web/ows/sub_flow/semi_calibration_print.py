from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class SemiCalibrationPrint(OWSFlow):
    flow_name = "semi_calibration_print"
    flow_url = "semi-auto-alignment"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

 
    @screenshot_compare(root_obj="semi_calibration_print_header")
    def verify_header(self):
        return self.driver.wait_for_object("semi_calibration_print_header")

    @screenshot_compare(root_obj="semi_calibration_print_card_content")
    def verify_card_content(self):
        return self.driver.wait_for_object("semi_calibration_print_card_content")

    @screenshot_compare(root_obj="semi_calibration_print_continue_btn")
    def verify_continue_btn(self):
        return self.driver.wait_for_object("semi_calibration_print_continue_btn")
    
    @screenshot_compare(root_obj="semi_calibration_print_skip_alignment_btn")
    def verify_skip_alignment_btn(self):
        return self.driver.wait_for_object("semi_calibration_print_skip_alignment_btn") 
    
    def click_start_calibration(self):
        return self.driver.click("start_calibration_btn")


class AndroidSemiCalibrationPrint(SemiCalibrationPrint, AndroidOWSFlow):
    """
    Create this class for using functions in AndroidOWSFlow, not from base OWS flow.
    For example: scroll_carousel()
    """
    platform = "android"