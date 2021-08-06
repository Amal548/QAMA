import types
import json
import inspect
import logging

from time import sleep
from abc import ABC, abstractmethod
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow

class PayloadNotFound(Exception):
    pass

class PayloadNotSend(Exception):
    pass

#Abstract base ows printer class
class OWSPrinter(ABC):
    @abstractmethod
    def select_country(self, country):
        raise NotImplementedError('Subclass missing method: select_country' )

    @abstractmethod
    def select_language(self, lang):
        raise NotImplementedError('Subclass missing method: select_language' )


class OWSSplPrinter(OWSPrinter):
    printer_type="real"

    def __init__(self, spl_p):
        self.spl_p = spl_p
        self.project_name = self.spl_p.p_obj.projectName

    def update_ledm(self, step, status):
        """
        It is called in Live ui flow.
        """
        pass

    def select_country(self, country):
        self.spl_p.set_country(country)

    def select_language(self, language):
        self.spl_p.set_language(language)

    def get_liveui_version(self):
        return self.spl_p.get_liveui_version()

    def return_oobe_status(self):
        return self.spl_p.return_oobe_status()

    def insert_ink(self):
        """
        Temporary implementaion. When finishing all printers chamber, 
        'if' statement is removed if all printers need to call fake setup cartridge
        """
        if self.project_name.split("_")[0] in ["vasari", "taccola", "palermo"]:
            self.spl_p.ows_fake_install_setup_cartridges()
    
    def insert_paper(self):
        pass

    def calibrate_printer(self, language="en", country="us"):
        if self.project_name.split("_")[0] in ["palermo"]:
            self.spl_p.skip_screens_until_calibration(language=language, country=country)
            # On front panel, printer make a unsuccessful printing alignment - 100%.
            # Temporarily, click on Later button on front panel of printer for passing this screen.
            # calibration process -> timeout increase to 30c
            skip_btn = "fb_option" if self.project_name.split("_")[1] == "minus" else "fb_skip"
            if self.spl_p.verify_front_panel_button(skip_btn, timeout=30, raise_e=False):
                self.spl_p.click_front_panel_btn(skip_btn)

    def semi_calibrate_print(self):
        pass

    def semi_calibrate_scan(self):
        if self.project_name.split("_")[0] in ["vasari"]:
            self.spl_p.press_blinking_copy_btn() 
            self.spl_p.fake_successfull_scan_alignment()

    def send_action(self, action):
        pass

class OWSEmuPrinter(OWSFlow, OWSPrinter):
    printer_type="emulated"
    flow_name = "ows_emu_printer"

    def __init__(self, printer_name, driver, live_ui_version, oobe_status_list, window_name=None):
        super(OWSEmuPrinter, self).__init__(driver)
        self.project_name = printer_name
        self.live_ui_version = live_ui_version
        self.oobe_status_list = oobe_status_list
        self.wn = None
        if window_name is None:
            logging.warning("OWSEmuPrinter flow init without window_name, please add it in before using it")
        else:
            self.wn = window_name

    def update_ledm(self, step, status):
        for item in self.oobe_status_list:
            if item["name"] == step:
                self.oobe_status_list[self.oobe_status_list.index(item)]["state"] = status
                return True
        logging.warning("Could not find LEDM step: " + step + " to update")

    def get_liveui_version(self):
        return self.live_ui_version

    def return_oobe_status(self):
        return self.oobe_status_list

    def verify_page_load(self):
        self.driver.wait_for_object("country_config_dropbox", timeout=10)

    def toggle_ledm_status(self, ledm_obj_name, option_value="completed", retry=3):
        sleep(1)
        self.driver.select(ledm_obj_name, option_value=option_value)
        sleep(1)
        self.click_get_oobe_status_btn(retry=retry)

    def select_country(self, country):
        self.toggle_ledm_status("country_config_dropbox", option_value="completed")
        sleep(1)
        self.update_ledm("countryConfig", "completed")

    def select_language(self, language):
        self.toggle_ledm_status("language_config_dropbox", option_value="completed")
        sleep(1)
        self.update_ledm("languageConfig", "completed")

    def insert_ink(self):
        self.toggle_ledm_status("insert_ink_dropbox", option_value="completed")
        sleep(1)
        self.driver.click("supplies_info_tab")
        sleep(1)
        self.driver.click("get_supply_info_btn")
        sleep(1)
        self.click_get_product_status_btn()
        self.update_ledm("insertInk", "completed")

    def insert_paper(self):
        self.toggle_ledm_status("load_main_tray_dropbox", option_value="completed")
        sleep(1)
        self.update_ledm("loadMainTray", "completed")

    def calibrate_printer(self):
        self.toggle_ledm_status("calibration_dropbox", option_value="completed")
        self.update_ledm("calibration", "completed")

    def semi_calibrate_print(self):
        self.toggle_ledm_status("semi_calibration_print_dropbox", option_value="completed")
        sleep(3)
        self.click_get_oobe_status_btn()
        self.update_ledm("semiCalibrationPrint", "completed")

    def semi_calibrate_scan(self):
        self.toggle_ledm_status("semi_calibration_scan_dropbox", option_value="completed")
        self.update_ledm("semiCalibrationScan", "completed")

    def remove_wrap(self):
        self.toggle_ledm_status("remove_wrap_dropbox", option_value="completed")
        self.update_ledm("removeWrap", "completed")

    def send_action(self, action):
        self.driver.click("actions_tab")
        self.driver.wait_for_object("actions_select")
        sleep(2)
        self.driver.wait_for_object("_shared_option_obj", format_specifier=[action])
        self.driver.select("actions_select", option_text=action)
        self.driver.click("actions_send_btn")

    def send_product_status(self, status):
        self.driver.wait_for_object("ledm_status_alert_select")
        self.driver.select("ledm_status_alert_select", option_text=status, clear_all=True)
        self.click_get_product_status_btn()

    def click_get_product_status_btn(self, retry=5):
        sleep(1)
        self.driver.click("get_product_status_btn")
        self.driver.click("get_product_status_btn")
        self.click_with_payload_check("get_product_status_btn")


    def click_get_oobe_status_btn(self, retry=5):
        sleep(1)
        self.driver.click("get_oobe_status_btn")
        self.driver.click("get_oobe_status_btn")
        self.click_with_payload_check("get_oobe_status_btn")

    def get_total_payload(self):
        print(len(self.driver.find_object("payload_div", multiple=True)))
        return len(self.driver.find_object("payload_div", multiple=True))

    def check_payload_sent(self, prev_total):
        return self.get_total_payload() > prev_total + 1
        
    def get_console_data(self, payload_txt, index=-1):
        #Alot of payload have dynamic id so it won't work
        #So we need to do a substring search for each payload
        #Not sure if this works for all payloads or if they all have unique ids
        
        #Return the payload as a dictionary if proper json format other wise returned as raw string

        payloads = self.driver.find_object("payload_div", multiple=True)
        for payload in payloads:
            if payload_txt in self.driver.find_object("payload_title_txt", root_obj=payload).text:
                payload_id = payload.get_attribute("id")
                if "collapsed" in self.driver.get_attribute("payload_collapse_div", "class", root_obj=payload):
                    payload.click()
                data = self.driver.wait_for_object("payload_content_pre", format_specifier=["collapse" + payload_id]).text
                try:
                    return json.loads(data)
                except ValueError:
                    logging.info("Cannot be converted to dict")
                    return data

        raise PayloadNotFound("Cannot find the payload with sub text: " + payload_txt)


    def login(self, authz_token, hpid_token):
        if self.driver.wait_for_object("authz_access_token_inb", timeout=2, raise_e=False) is False:
            self.driver.click("login_tab")
        self.driver.send_keys("authz_access_token_inb", authz_token)
        self.driver.send_keys("hpid_token_inb", hpid_token)
        self.driver.click("login_btn")
        sleep(1)
        self.driver.click("login_btn")
        sleep(1)
        self.click_with_payload_check("login_btn")

    def click_with_payload_check(self, obj_name, retry=5):
        total_payload = self.get_total_payload()
        for _ in range(retry):
            self.driver.click(obj_name)
            sleep(1)
            if self.check_payload_sent(total_payload) or self.driver.get_attribute(obj_name, "disabled") == "true":
                return True
        raise PayloadNotSend("Payload not sent after clicking: " + obj_name + " after: " + str(retry) + " times")

    def click_enable_ws(self):
        self.driver.click("enable_ws_btn")
