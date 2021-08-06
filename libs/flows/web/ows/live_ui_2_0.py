from time import sleep
from MobileApps.libs.flows.web.ows.flow_container_base import BaseFlowContainer
from MobileApps.libs.flows.web.ows.sub_flow.ows_flow_factory import sub_flow_factory
from selenium.common.exceptions import NoSuchElementException

class LiveUI_2_0(BaseFlowContainer):
    liveui_version = 2

    def __init__(self, driver, p_obj, context=None, url=None):
        super(LiveUI_2_0, self).__init__(driver, p_obj, context=context, url=url)
        self.fd["country_language"] = sub_flow_factory(driver, "CountryLanguage", context=context, url=url)
        self.fd["load_ink"] = sub_flow_factory(driver, "LoadInk", context=context, url=url)
        self.fd["load_paper"] = sub_flow_factory(driver, "LoadPaper", context=context, url=url)
        self.fd["calibration"] = sub_flow_factory(driver, "Calibration2_0", context=context, url=url)
        self.fd["semi_calibration_print"] = sub_flow_factory(driver, "SemiCalibrationPrint", context=context, url=url)
        self.fd["semi_calibration_scan"] = sub_flow_factory(driver, "SemiCalibrationScan", context=context, url=url)
        self.fd["remove_wrap"] = sub_flow_factory(driver, "RemoveWrap", context=context, url=url)
        self.fd["remove_protective_sheet"] = sub_flow_factory(driver, "RemoveProtectiveSheet", context=context, url=url)
        
        self.ows_method_dict["removeWrap"] = self.navigate_remove_wrap
        self.ows_method_dict["languageConfig"] = self.navigate_country_language
        self.ows_method_dict["loadMainTray"] = self.navigate_load_paper
        self.ows_method_dict["insertInk"] = self.navigate_load_ink
        self.ows_method_dict["calibration"] = self.navigate_calibration
        self.ows_method_dict["semiCalibrationPrint"] = self.navigate_semi_calibration_print
        self.ows_method_dict["semiCalibrationScan"] = self.navigate_semi_calibration_scan
        self.ows_method_dict["removeProtectiveSheet"] = self.navigate_remove_protective_sheet
    
        
    def navigate_remove_wrap(self):
        self.flow["remove_wrap"].verify_web_page()
        self.ows_p.remove_wrap()
        self.flow["remove_wrap"].verify_successful_popup()
        self.flow["remove_wrap"].click_successful_continue()

    def navigate_country_language(self, country="us", language="en"):
        self.flow["country_language"].verify_web_page()
        self.ows_p.select_country(country)
        self.ows_p.select_language(language)
        self.flow["country_language"].click_continue()

    def navigate_load_ink(self):
        self.flow["load_ink"].verify_web_page()
        self.flow["load_ink"].handle_partial_screenshot()
        for _ in range(self.flow["load_ink"].get_total_carousel_pages()-1):
            self.flow["load_ink"].scroll_carousel()

        self.ows_p.insert_ink()
        self.flow["load_ink"].ink_click_continue()

    def navigate_load_paper(self):
        self.flow["load_paper"].verify_web_page()
        self.flow["load_paper"].handle_partial_screenshot()
        for _ in range(self.flow["load_paper"].get_total_carousel_pages()-1):
            self.flow["load_paper"].scroll_carousel() 

        sleep(1)
        self.ows_p.insert_paper()       
        self.flow["load_paper"].paper_click_continue()

    def navigate_calibration(self):
        self.flow["calibration"].verify_web_page()
        self.flow["calibration"].click_start_calibration()
        self.ows_p.calibrate_printer()
        self.ows_p.send_action("CalibratePrinter")
            
    def navigate_semi_calibration_print(self):
        self.flow["semi_calibration_print"].verify_web_page() 
        self.flow["semi_calibration_print"].verify_header()
        self.flow["semi_calibration_print"].verify_card_content() 
        self.flow["semi_calibration_print"].verify_continue_btn()
        self.flow["semi_calibration_print"].verify_skip_alignment_btn()
        self.flow["semi_calibration_print"].click_start_calibration()
        self.ows_p.send_action("CalibratePrinter")
        self.ows_p.semi_calibrate_print()

    def navigate_semi_calibration_scan(self):
        self.flow["semi_calibration_scan"].verify_web_page()
        self.flow["semi_calibration_scan"].handle_partial_screenshot()
        for _ in range(self.flow["semi_calibration_scan"].get_total_carousel_pages() -1):
            self.flow["semi_calibration_scan"].scroll_carousel() 
       
        self.ows_p.semi_calibrate_scan()
        # Real printer needs take more time to load this popup, so increase it to 20 for timeout
        timeout = 20 if self.ows_p.printer_type == "real" else 10
        self.flow["semi_calibration_scan"].verify_success_popup(timeout=timeout)
        self.flow["semi_calibration_scan"].click_success_popup_ok()
    
    def navigate_remove_protective_sheet(self):
        self.flow["remove_protective_sheet"].verify_web_page()
        self.flow["remove_protective_sheet"].handle_partial_screenshot()
        for index in range(self.flow["remove_protective_sheet"].get_total_carousel_pages() -1):
            self.driver.process_screenshot(__file__,("remove_protective_sheet_scroll_carousel_" + str(index+1)))
            self.flow["remove_protective_sheet"].scroll_carousel() 
        self.driver.process_screenshot(__file__,("remove_protective_sheet_scroll_carousel_" + str(self.flow["remove_protective_sheet"].get_total_carousel_pages())))  
        self.flow["remove_protective_sheet"].click_continue()
        self.ows_p.update_ledm("removeProtectiveSheet", "completed")


class AndroidLiveUI_2_0(LiveUI_2_0):
    platform = "android"  

    def navigate_calibration(self):
        self.flow["calibration"].verify_web_page()
        for _ in range(5):
            self.ows_p.calibrate_printer()

            if self.flow["calibration"].click_skip_alignment():
                return True 
        raise NoSuchElementException("Cannot find skip button after sending printer calibration ack")
        