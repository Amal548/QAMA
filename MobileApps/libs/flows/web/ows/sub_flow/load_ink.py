import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class CannotFindElement(Exception):
    pass

class LoadInk(OWSFlow):
    flow_name = "load_ink"
    flow_url = "install-ink"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

 

    def navigate_load_ink(self):
        for _ in self.get_total_carousel_pages():
            self.scroll_carousel()
            time.sleep(3)
    
    def handle_partial_screenshot(self): 
        self.verify_carousel_screen_header()
        self.driver.process_screenshot(__file__,("verify_carousel_screen_header"), root_obj="_shared_carousel_screen_header")
        
        for index in range(self.get_total_carousel_pages() ):
            self.verify_carousel_screen_owl_dots()
            self.driver.process_screenshot(__file__,("carousel_screen_owl_dots"+ str(index+1)), root_obj="_shared_carousel_screen_owl_dots")
            self.verify_carousel_screen_card_content()
            self.driver.process_screenshot(__file__,("carousel_screen_card_content"+ str(index+1)), root_obj="_shared_carousel_screen_card_content")
            if self.driver.wait_for_object("_shared_carousel_screen_continue_or_skip_btn", raise_e=False) is not False: 
                self.driver.process_screenshot(__file__,("carousel_screen_continue_or_skip_btn"+ str(index+1)), root_obj="_shared_carousel_screen_continue_or_skip_btn")
            
            self.scroll_carousel()    
    
    def verify_ink_installed_popup(self):
        return self.driver.wait_for_object("ink_installed_popup")
    
    @screenshot_compare(root_obj="ink_installed_popup",at_end=False)
    def ink_click_continue(self):
        self.driver.wait_for_object("ink_popup_continue_btn")
        return self.driver.click("ink_popup_continue_btn")

    @screenshot_compare(root_obj="ink_error_popup",at_end=False)
    def click_error_modal_learn_more_btn(self): 
        return self.driver.click("ink_error_popup_learn_more_btn")
    
    def verify_collapsed_error_body(self, invisible=False):
        timeout = time.time() + 5
        while time.time()< timeout:
            found = self.driver.find_object("ink_error_collapsed_error_body", raise_e=False)
            if not invisible and found: 
                return True 
            elif invisible and not found:
                return True
        raise CannotFindElement("Cannot verify collapsed_error_body")
        #return self.driver.wait_for_object("ink_error_collapsed_error_body", invisible=invisible)

    @screenshot_compare(root_obj="ink_error_collapsed_error_body")
    def click_collapsed_error_body(self):
        return self.driver.click_by_coordinates("_shared_main_title")


class AndroidLoadInk(LoadInk, AndroidOWSFlow):
    """
    Create this class for using functions in AndroidOWSFlow, not from base OWS flow.
    For example: scroll_carousel()
    """
    platform = "android"