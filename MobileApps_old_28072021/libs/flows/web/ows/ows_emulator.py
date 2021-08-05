import logging

from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow

class OWSEmulator(OWSFlow):
    """
        Contains all of the elements and flows associated in the emulator screen for ows
    """
    flow_name = "ows_emu_screen"
    emulator_url = {
        "pie": "https://oss.hpconnectedpie.com/emulate/v7",
        "stage": "https://oss.hpconnectedstage.com/emulate/v7",
        "production": "https://oss.hpconnected.com/emulate/v7"
    }

    def __init__(self, driver):
        super(OWSEmulator, self).__init__(driver)
        self.profile_to_printer = {"skyreach": "horizon", "manhattan_yeti": "3m"}

    def verify_emulator_load(self):
        self.driver.wait_for_object("emulator_load_div")
        #These sleeps are to slow the test down
        #Running too fast breaks the script
        sleep(1)
        return True
        
    def open_emulator(self, stack, v7=False):
        url = self.emulator_url[stack]
        self.driver.navigate(url)
#########################################################################################
#                                                                                       #
#                                     Action Flows                                      #
#                                                                                       #
#########################################################################################

    #############################
    #   Top-left menu section   #
    #############################
    def launch_flow_by_printer(self, printer_name, platform=None):
        self.select_app_or_post_oobe_list_item()
        self.select_app_type_dropdown_and_choose(option=platform)
        self.set_country_language()
        self.select_device_menu_list_item()
        self.select_quick_option_by_printer(printer_name)
        live_ui_version = self.get_liveui_version()
        oobe_status = self.return_oobe_status()
        self.select_actions_button()
        return live_ui_version, oobe_status

    def get_liveui_version(self):
        option_value = self.driver.get_selected_option("device_live_ui_list_item").text
        if option_value == "":
            return 1
        else:
            return int(float(option_value))

    def return_oobe_status(self):
        oobe_status_list = []
        div_list = self.driver.find_object("ledm_item_div", multiple=True)
        for div in div_list:
            status_dict = {}
            label = self.driver.find_object("ledm_item_label", root_obj=div).text
            value = self.driver.get_selected_option("ledm_item_select", root_obj=div).text
            if value != "":
                status_dict["order"] = div_list.index(div)
                status_dict["name"] = label
                status_dict["state"] = value
                oobe_status_list.append(status_dict)
        return oobe_status_list

    def set_country_language(self):
        #locale info is already stored in the driver
        self.select_app_or_post_oobe_list_item()
        country = self.driver.session_data.get("locale", None)
        language = self.driver.session_data.get("language", None)
        if country is not None:
            self.enter_app_country(country)
        if language is not None:
            self.enter_app_language(language)

    def dismiss_banner(self):
        self.driver.click("banner_x_button")

    def select_device_menu_list_item(self):
        self.driver.click("device_menu_list_item")
        sleep(1)

    def select_app_or_post_oobe_list_item(self):
        self.driver.click("app_or_post_oobe_menu_list_item", change_check={"wait_obj": "app_type_dropdown_list"})
        sleep(1)

    def select_setup_complete_list_item(self):
        self.driver.click("setup_complete_menu_list_item")
        sleep(1)

    def select_dev_menu_list_item(self):
        self.driver.click("dev_menu_list_item", change_check={"wait_obj": "dev_hpid_login_btn"})
        sleep(1)

    #############################
    #       Device section      #
    #############################

    def enter_model_name(self, option):
        self.driver.send_keys("device_model_name_txt_box", option)

    def enter_serial_number(self, serial_number):
        self.driver.send_keys("device_serial_number_txt_box", serial_number)

    def enter_sku(self, sku):
        self.driver.send_keys("device_sku_txt_box", sku)

    def enter_product_config_dyn(self, product_config):
        self.driver.send_keys("device_product_config_txt_box", product_config)

    def select_printer_country_dropdown_and_choose(self, option):
        self.driver.select("device_printer_country_dropdown_list", option_value=option)

    def select_printer_language_dropdown_and_choose(self, option):
        self.driver.select("device_printer_language_dropdown_list", option_value=option)

    def select_usage_tracking_consent_dropdown_and_choose(self, option):
        self.driver.select("device_usage_tracking_dropdown_list", option_value=option)

    def select_registration_state_dropdown_and_choose(self, option):
        self.driver.select("device_registration_state_dropdown_list", option_value=option)

    def click_gen2_enable_button(self):
        self.driver.click("device_gen2_check_box")

    def enter_claim_postcard(self, postcard):
        self.driver.send_keys("device_claim_postcard_text_box", postcard)

    def enter_uuid(self, uuid):
        self.driver.send_keys("device_uuid_text_box", uuid)
        
    def enter_cloud_id(self, option):
        self.driver.send_keys("device_cloud_id_text_box", option)

    def select_live_ui_version_dropdown_and_choose(self, option):
        self.driver.select("device_live_ui_list_item", option_value=option)

    def select_supplies_info_dropdown_and_choose(self, option):
        self.driver.select("device_supplies_info_list_item", option_value=option)

    def click_populate_all_printer_locales_enable_button(self):
        self.driver.click("device_pop_printer_local_checkbox")

    def select_remove_wrap_dropdown_and_choose(self, option):
        self.driver.select("device_remove_wrap_list_item", option_value=option)

    def select_language_config_dropdown_and_choose(self, option):
        self.driver.select("device_language_config_list_item", option_value=option)

    def select_country_config_dropdown_and_choose(self, option):
        self.driver.select("device_country_config_list_item", option_value=option)

    def select_remove_protective_sheet_dropdown_and_choose(self, option):
        self.driver.select("device_remove_prot_sheet_list_item", option_value=option)

    def select_insert_ink_dropdown_and_choose(self, option):
        self.driver.select("device_insert_ink_list_item", option_value=option)

    def select_load_main_tray_dropdown_and_choose(self, option):
        self.driver.select("device_load_main_tray_list_item", option_value=option)

    def select_load_photo_tray_dropdown_and_choose(self, option):
        self.driver.select("device_load_photo_tray_list_item", option_value=option)

    def select_calibration_dropdown_and_choose(self, option):
        self.driver.select("device_calibration_list_item", option_value=option)

    def select_semi_calibration_print_dropdown_and_choose(self, option):
        self.driver.select("device_semi_calib_print_list_item", option_value=option)

    def select_semi_calibration_scan_dropdown_and_choose(self, option):
        self.driver.select("device_semi_calib_scan_list_item", option_value=option)

    def enter_cdm_printer_fingerprint(self, fingerprint):
        self.driver.send_keys("device_cmd_printer_fingerprint_txt", fingerprint)
    #############################
    #   App/Post-OOBE section   #
    #############################

    def select_app_type_dropdown_and_choose(self, option=None):
        if option is None:
            self.driver.select("app_type_dropdown_list", random_option=True)
        else:
            self.driver.select("app_type_dropdown_list", option_value=option)

    def enter_app_country(self, country):
        self.driver.send_keys("app_country_textbox", country)

    def enter_app_language(self, language):
        self.driver.send_keys("app_language_textbox", language)

    def enter_oss_session_id(self, option):
        self.driver.select("app_oss_session_id_textbox", option_value=option)

    def enter_web_auth_access_token(self, token):
        self.driver.send_keys("app_webauth_token_textbox", token)

    def get_web_auth_access_token(self):
        return self.driver.get_attribute("app_webauth_token_textbox", "value")

    def clear_web_auth_access_token(self):
        return self.driver.clear_text("app_webauth_token_textbox")

    def get_id_token(self):
        return self.driver.get_attribute("app_id_token_textbox", "value")

    def clear_id_token(self):
        return self.driver.clear_text("app_id_token_textbox")

    def toggle_app_authenticate_user(self, on=False):
        #Not a toggle we can use properly
        if not on:
            self.driver.click("app_authenticate_user_toggle")
        else:
            pass
    def select_product_registration_dropdown_and_choose(self, option):
        self.driver.select("app_product_registration_dropdown_list", option_value=option)

    def select_create_user_dropdown_and_choose(self, option):
        self.driver.select("app_create_user_dropdown_list", option_value=option)

    def select_connectivity_to_device_dropdown_and_choose(self, option):
        self.driver.select("app_connectivity_to_device_dropdown_list", option_value=option)

    def select_printer_claim_dropdown_and_choose(self, option):
        self.driver.select("app_printer_claim_dropdown_list", option_value=option)

    def click_ink_subscription_enable_button(self):
        self.driver.click("app_ink_subscription_checkbox")

    def click_oobe_enable_button(self):
        self.driver.click("app_oobe_checkbox")



    #############################
    #  Setup Complete section   #
    #############################

    def select_flow_dropdown_and_choose(self, option):
        self.driver.select("setup_flow_list_item", option_value=option)

    def enter_subscription_id(self, option):
        self.driver.select("setup_subscription_id_checkbox", option_value=option)

    def enter_subscription_nonce(self, option):
        self.driver.select("setup_subscription_nonce_checkbox", option_value=option)

    def select_ink_subscription_dropdown_and_choose(self, option):
        self.driver.select("setup_ink_subscription_list_item", option_value=option)

    def click_no_ink_version_enable_button(self):
        self.driver.click("setup_no_ink_version_checkbox")

    #############################
    #       Dev section         #
    #############################

    def enter_gemini_moobe_url(self, option):
        self.driver.select("dev_gemini_moobe_url_textbox", option_value=option)

    def enter_oss_url(self, option):
        self.driver.select("dev_oss_url_textbox", option_value=option)

    def click_fresh_install_version_enable_button(self):
        self.driver.click("dev_fresh_install_checkbox")

    def click_yeti_enable_button(self):
        self.driver.click("dev_yeti_checkbox")

    def select_api_name_dropdown_and_choose(self, option):
        self.driver.select("dev_api_name_list_item", option_value=option)

    def click_response_code_add_button(self):
        self.driver.click("dev_response_code_add_button")

    def click_response_code_remove_button(self):
        self.driver.click("dev_response_code_remove_button")

    def click_hpid_login_button(self):
        self.driver.click("dev_hpid_login_btn")

    #############################
    #   Quick Option section    #
    #############################
    def select_quick_option_by_printer(self, printer_name):
        actual_printer_name = self.profile_to_printer.get(printer_name, printer_name)
        self.driver.click("quick_option_printer_btn", format_specifier=[actual_printer_name])
    ##############################################
    #   Buttons to trigger new emulator screens  #
    ##############################################

    def select_start_flow_button(self):
        self.driver.click("start_flow_button", change_check={"wait_obj": "start_flow_button", "invisible": True})

    def select_actions_button(self):
        self.driver.click("actions_button", change_check={"wait_obj": "actions_button", "invisible": True})

    def select_account_prop_button(self):
        self.driver.click("account_prop_button", change_check={"wait_obj": "account_prop_button", "invisible": True})

    def select_setup_complete_button(self):
        self.driver.click("setup_complete_button", change_check={"wait_obj": "setup_complete_button", "invisible": True})

#########################################################################################
#                                                                                       #
#                                  Verification Flows                                   #
#                                                                                       #
#########################################################################################