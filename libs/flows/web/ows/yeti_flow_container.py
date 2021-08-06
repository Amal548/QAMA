import pytest
import logging

from SAF.decorator.saf_decorator import screenshot_compare

from MobileApps.libs.flows.web.ows import ows_utility
from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.ucde_offer import UCDEOffer
from MobileApps.libs.flows.web.ows.ows_welcome import OWSWelcome
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.ucde_safety_net import UCDESafetyNet

from MobileApps.libs.flows.web.instant_ink.value_proposition import ValueProposition
from MobileApps.libs.flows.web.smart.smart_printer_consent import SmartPrinterConsent
from MobileApps.libs.flows.web.ows.ucde_activation_success import UCDEActivationSuccess

class YetiFlowContainer():
    printer_profile_dict ={"skyreach": "horizon", "manhattan_yeti": "manhattan"}
    printer_offer_dict ={"manhattan_yeti": 1, "skyreach": 0}
    def __init__(self, driver, context=None,  url=None):
        self.driver = driver
        self.fd = {"hpid": HPID(driver, context=context, url=url),
                   "smart_printer_consent": SmartPrinterConsent(driver, context=context, url=url),
                   "ucde_offer": UCDEOffer(driver, context=context, url=url),
                   "ucde_privacy": UCDEPrivacy(self.driver, context=context, url=url),
                   "ucde_activation_success": UCDEActivationSuccess(driver, context=context, url=url),
                   "ucde_safety_net": UCDESafetyNet(driver, context=context, url=url),
                   "value_proposition": ValueProposition(driver, context=context, url=url),
                   "ows_emulator": OWSEmulator(driver)}

    @property
    def flow(self):
        return self.fd

    def get_printer_name_from_profile(self, profile):
        return self.printer_profile_dict[profile]

    def get_printer_offer_from_profile(self, profile):
        return self.printer_offer_dict[profile]

    def emulator_start_yeti(self, stack, profile, biz_model):
        emu_platform = self.driver.session_data["request"].config.getoption("--emu-platform") 
        sim_printer_info = ows_utility.create_simulated_gen2_printer(stack=stack, profile=profile, biz_model=biz_model, offer=self.get_printer_offer_from_profile(profile))
        self.flow["ows_emulator"].open_emulator(stack)
        self.flow["ows_emulator"].select_dev_menu_list_item()
        self.flow["ows_emulator"].click_hpid_login_button()
        self.flow["hpid"].verify_hp_id_sign_up(timeout=20)
        self.flow["hpid"].create_account()
        self.flow["ows_emulator"].verify_emulator_load()
        self.flow["ows_emulator"].dismiss_banner()
        self.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        access_token = self.flow["ows_emulator"].get_web_auth_access_token()
        self.flow["ows_emulator"].clear_web_auth_access_token()
        id_token = self.flow["ows_emulator"].get_id_token()
        self.flow["ows_emulator"].clear_id_token()
        self.flow["ows_emulator"].toggle_app_authenticate_user(on=False)
        self.flow["ows_emulator"].select_quick_option_by_printer(profile)
        self.flow["ows_emulator"].select_device_menu_list_item()
        self.flow["ows_emulator"].enter_claim_postcard(sim_printer_info["claim_postcard"])
        self.flow["ows_emulator"].enter_uuid(sim_printer_info["uuid"])
        logging.info("UUID: " + sim_printer_info["uuid"])
        self.flow["ows_emulator"].enter_cdm_printer_fingerprint(sim_printer_info["fingerprint"])
        self.flow["ows_emulator"].enter_serial_number(sim_printer_info["serial_number"])
        self.flow["ows_emulator"].enter_sku(sim_printer_info["model_number"])
        self.flow["ows_emulator"].select_language_config_dropdown_and_choose("completed")
        self.flow["ows_emulator"].select_country_config_dropdown_and_choose("completed")
        ows_status = self.flow["ows_emulator"].return_oobe_status()
        self.flow["ows_emulator"].select_app_or_post_oobe_list_item()
        self.flow["ows_emulator"].select_app_type_dropdown_and_choose(option=emu_platform)
        self.flow["ows_emulator"].select_actions_button()
        return ows_status, access_token, id_token

    def navigate_yeti(self, profile, biz_model):
        self.flow["ucde_offer"].verify_ucde_offer()
        if profile.lower() == "skyreach" and biz_model.lower() == "flex":
            self.flow["ucde_offer"].click_decline_account_btn()
            self.flow["ucde_safety_net"].verify_ucde_safety_net()
            self.flow["ucde_safety_net"].click_back_to_account_btn()
            #self.flow["ucde_offer"].click_flex_sign_in_btn()
        # elif profile.lower() == "manhattan_yeti":
        #     self.flow["ucde_offer"].click_decline_offer_btn()
        #     self.flow["ucde_offer"].verify_decline_offer_popup()
        #     self.flow["ucde_offer"].click_decline_hp_plus_offer_btn()
        #     self.flow["ucde_offer"].verify_ucde_offer()
        #     self.flow["ucde_offer"].click_flex_sign_in_btn()
        
        # The flow in else statement works for taccola yeti
        else:
            self.flow["ucde_offer"].click_continue()
            self.flow["ucde_offer"].verify_requirement_popup()
            self.flow["ucde_offer"].click_requirement_popup_continue()