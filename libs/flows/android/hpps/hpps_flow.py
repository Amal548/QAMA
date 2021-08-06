from abc import ABCMeta, abstractmethod
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class hppsFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "hpps"
    print_options_dict = {
        "pclm_default": "default_checkbox",
        "pclm_jpeg": "jpeg_checkbox",
        "pclm_flate": "flate_checkbox",
        "pclm_rle": "rle_checkbox",

        "protocol_auto": "auto_checkbox",
        "protocol_ipp": "ipp_checkbox",
        "protocol_ipps": "secure_ipp_checkbox",
        "protocol_legacy": "legacy_checkbox",
        "color": "color_option_color",
        "black_and_white": "color_option_black_and_white",
        "portrait": "orientation_portrait",
        "landscape": "orientation_landscape",
        "1_sided": "double_sided_none",
        "long_edge": "double_sided_long_edge",
        "short_edge": 'double_sided_short_edge',
        "letter": "_shared_paper_size_letter",
        "4x6": "_shared_paper_size_4x6",
        "automatic": "quality_automatic_btn",
        "best": "quality_best_btn",
        "draft": "quality_draft_btn",
        "normal": "quality_normal_btn",
        "fill_page": "scaling_fill_page_btn", 
        "fit_to_page": "scaling_fit_to_page_btn"
    }


    def __init__(self, driver):
        super(hppsFlow, self).__init__(driver)
        self.load_inOS_app_shared_ui()

    def load_inOS_app_shared_ui(self):
        ui_map = self.load_ui_map(system="ANDROID", project="hpps", flow_name="shared_obj")
        self.driver.load_ui_map("hpps", "shared_obj", ui_map)
        return True

    def check_parameter_in_dict(self, parameter):
        #Some flows use this universal options dict to map out all the options for hpps printing
        actual_param = self.print_options_dict.get(parameter, False)
        if not actual_param:
            raise ValueError("Option: " + parameter + " is not supported in system_ui")
        else:
            return actual_param