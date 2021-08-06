import time
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.web.ows.flow_container_base import BaseFlowContainer
from MobileApps.libs.flows.web.ows.sub_flow.ows_flow_factory import sub_flow_factory


class LiveUI_1_0(BaseFlowContainer):
    liveui_version = 1
    def __init__(self, driver, p_obj, context=None, url=None):
        super(LiveUI_1_0, self).__init__(driver, p_obj, context=context, url=url)
        self.fd["country_language"] = sub_flow_factory(driver, "CountryLanguage",context=context, url=url)
        self.fd["load_ink"] = sub_flow_factory(driver, "LoadInk", context=context, url=url)
        self.fd["load_paper"] = sub_flow_factory(driver, "LoadPaper", context=context, url=url)
        self.fd["calibration"] = sub_flow_factory(driver, "Calibration", context=context, url=url)
        self.fd["semi_calibration_print"] = sub_flow_factory(driver, "SemiCalibrationPrint", context=context, url=url)
        self.fd["semi_calibration_scan"] = sub_flow_factory(driver, "SemiCalibrationScan", context=context, url=url)

        self.ows_method_dict["languageConfig"] = self.navigate_country_language
        self.ows_method_dict["loadMainTray"] = self.navigate_load_paper
        self.ows_method_dict["insertInk"] = self.navigate_load_ink
        self.ows_method_dict["calibration"] = self.navigate_calibration
        self.ows_method_dict["semiCalibrationPrint"] = self.navigate_semi_calibration_print
        self.ows_method_dict["semiCalibrationScan"] = self.navigate_semi_calibration_scan


    def navigate_country_language(self, country="us", language="en"):
        self.flow["country_language"].verify_web_page()
        self.ows_p.select_country(country)
        self.ows_p.select_language(language)
        self.flow["country_language"].validate_success_popup()
        self.flow["country_language"].click_continue()


    def navigate_load_ink(self):
        self.flow["load_ink"].verify_web_page()
        self.flow["load_ink"].handle_partial_screenshot()
        for _ in range(self.flow["load_ink"].get_total_carousel_pages() -1):
            self.flow["load_ink"].scroll_carousel()
            time.sleep(2)
    
        self.ows_p.insert_ink()
        self.flow["load_ink"].verify_ink_installed_popup()
        self.flow["load_ink"].ink_click_continue()

    def navigate_load_paper(self):
        self.flow["load_paper"].verify_web_page()
        self.flow["load_paper"].handle_partial_screenshot()
        for _ in range(self.flow["load_paper"].get_total_carousel_pages() -1):
            self.flow["load_paper"].scroll_carousel() 
            time.sleep(2)

        self.ows_p.insert_paper()       
        self.flow["load_paper"].paper_click_continue()

    def navigate_calibration(self):
        self.flow["calibration"].verify_web_page()
        self.ows_p.calibrate_printer()

    def navigate_semi_calibration_print(self):
        self.flow["semi_calibration_print"].verify_web_page()  
        self.ows_p.semi_calibrate_print()

    def navigate_semi_calibration_scan(self):
        self.flow["semi_calibration_scan"].verify_web_page()
        self.flow["semi_calibration_scan"].handle_partial_screenshot()
        for _ in range(self.flow["semi_calibration_scan"].get_total_carousel_pages() -1):
            self.flow["semi_calibration_scan"].scroll_carousel()    
            time.sleep(2)
        
        self.ows_p.semi_calibrate_scan()
        self.flow["semi_calibration_scan"].verify_success_popup()
        self.flow["semi_calibration_scan"].click_success_popup_ok()


class AndroidLiveUI_1_0(LiveUI_1_0):
    platform = "android" 

    def navigate_calibration(self):
        self.flow["calibration"].verify_web_page()
        self.ows_p.calibrate_printer(language=self.driver.session_data["language"].lower(), 
                                     country=self.driver.session_data["locale"].lower())