from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path
from SAF.decorator.saf_decorator import screenshot_compare

class RemoveProtectiveSheet(OWSFlow):
    flow_name = "remove_protective_sheet"
    flow_url = "remove-protective-sheet"
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
    
    
    def click_continue(self):
        return self.driver.click("remove_protective_sheet_continue")