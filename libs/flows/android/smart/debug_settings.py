from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging


class DebugSettings(SmartFlow):
    flow_name = "debug_settings"
    USAGE_TRACKING_OPT = "usage_tracking_title"
    SHOW_TILES_FALLING_ANIMATION_OPT = "show_tiles_falling_animation_title"
    DEBUG_XML_OPT = "debug_xml_title"
    SHOW_OWS_ERROR_LOGGING = "show_ows_error_logging_title"
    SOFTFAX_OPT = "softfax_txt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_option_cb(self, setting_opt, enable=True):
        """
        Click on check box of an setting option
        :param setting_opt: setting option object. Using class constant
        """
        self.driver.scroll(setting_opt, timeout=60, check_end=False)
        option_els = self.driver.find_object("option_el", multiple=True)
        for option in option_els:
            try:
                self.driver.find_object(setting_opt, root_obj=option)
                cb = self.driver.find_object("option_cb", root_obj=option)
                if enable != (True if cb.get_attribute("checked").lower() == "true" else False):
                    cb.click()
                #self.driver.check_box("option_cb", root_obj=option, uncheck=not enable)
                return True
            except NoSuchElementException:
                logging.info("This option is not target option")
        raise NoSuchElementException(u"There is no {} option".format(self.get_text_from_str_id(setting_opt)))

    def select_multiple_choice_option(self, setting_opt, opt_value):
        """
        Click on a value of multiple choice setting option
        :param setting_opt: setting option object. Using class constant
        :param opt_value: value of setting option. USing class constant
        """
        self.driver.scroll(setting_opt, timeout=60, check_end=False)
        self.driver.click(setting_opt)
        self.driver.wait_for_object(opt_value, timeout=5)
        self.driver.click(opt_value)

    # ***********************************************************************************************
    #                                      VERIFICATION FLOWS                                       *
    # ***********************************************************************************************
    def verify_debug_settings_screen(self):
        """
        Verify current screen is Debug Settings
            - Settings as title
        """
        self.driver.wait_for_object("settings_title")
        self.driver.wait_for_object("usage_tracking_title")