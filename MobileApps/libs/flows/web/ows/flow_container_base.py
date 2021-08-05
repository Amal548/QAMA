import pytest
import logging
from SAF.decorator.saf_decorator import screenshot_compare
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.web.ows.sub_flow.ows_flow_factory import sub_flow_factory

class BaseFlowContainer():

    def __init__(self, driver, ows_p_obj, context=None, url=None):
        self.driver = driver
        self.fd = {"osprey": sub_flow_factory(driver, "Osprey", context=context, url=url),
                   "welcome": OWSWelcome(driver, context=context, url=url),
                   "hpid": HPID(driver, context=context, url=url),
                   "ucde_privacy": UCDEPrivacy(self.driver, context=context, url=url)}
        self.ows_p = ows_p_obj
        self.ows_method_dict = {}

    @property
    def flow(self):
        return self.fd

    def navigate_welcome(self):
        self.fd["welcome"].verify_welcome_screen()
        self.fd["welcome"].click_continue()
        #Needs refactoring as this method is moved out of hpid
        self.fd["welcome"].verify_welcome_screen()
        self.fd["welcome"].select_more_options()
        self.fd["welcome"].select_skip_option()
        self.fd["welcome"].select_yes_popup_option()

    def navigate_ows(self, p_obj, stop_at=None):
        oobe_flow_list = p_obj.return_oobe_status()
        for s_step in oobe_flow_list:
            if s_step["name"] == stop_at:
                return True
            elif s_step["state"] == "completed":
                continue 
            else:
                method = self.ows_method_dict.get(s_step["name"], None)
                if method is None:
                    logging.warning("No navigation flow for step: " + s_step["name"] + " will mark ledm completed")
                    p_obj.update_ledm(s_step["name"], "completed")
                else:
                    method()
        return True