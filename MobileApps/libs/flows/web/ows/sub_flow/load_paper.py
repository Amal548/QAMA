import time
from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow, AndroidOWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class LoadPaper(OWSFlow):
    flow_name = "load_paper"
    flow_url = "load-paper"
    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    
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

    def navigate_load_paper(self):
        for _ in self.get_total_carousel_pages():
            self.scroll_carousel()
            time.sleep(3)
        self.paper_click_continue()
    
    def paper_click_continue(self):
        return self.driver.click("paper_continue_btn", timeout=10)


class AndroidLoadPaper(LoadPaper, AndroidOWSFlow):
    """
    Create this class for using functions in AndroidOWSFlow, not from base OWS flow.
    For example: scroll_carousel()
    """
    platform = "android"