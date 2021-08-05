import time
from SAF.decorator.saf_decorator import native_context
from MobileApps.libs.flows.web.web_flow import WebFlow
from SAF.decorator.saf_decorator import screenshot_compare


class UnexpectedURLError(Exception):
    pass

class OWSFlow(WebFlow):
    project = "ows"

    def __init__(self, driver, context=None,  url=None):
        super(OWSFlow, self).__init__(driver, context=context, url=url)
        self.func_ignore_methods.append("load_ows_shared_ui")
        self.load_ows_shared_ui()
        

    def load_ows_shared_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="ows", flow_name="shared_obj")
        self.driver.load_ui_map("ows", "shared_obj", ui_map)
        return True
    
    def verify_web_page(self, sub_url=None, timeout=60, raise_e=True):
        start_time = time.time()
        while time.time() - start_time <=timeout:
            for window in self.driver.wdvr.window_handles:
                self.driver.wdvr.switch_to.window(window)
                cur_url = self.driver.current_url
                sub_url = self.flow_url if sub_url is None else sub_url 
                if sub_url in cur_url.split("/"):
                    return True
            time.sleep(5)

        if raise_e:
            raise UnexpectedURLError("Expecting: " + self.flow_url + " got: " + cur_url)
        else:
            return False
    
    
    def get_total_carousel_pages(self):
        self.driver.wait_for_object("_shared_carousel_owl_dot", timeout=10)
        return len(self.driver.find_object("_shared_carousel_owl_dot", multiple=True))
    
    
    def scroll_carousel(self, direction="right"):
        if self.driver.wait_for_object("_shared_arrow_right", timeout=3, raise_e=False):
            return self.driver.click("_shared_arrow_right")

        carousel_obj = self.driver.find_object("_shared_carousel_obj")
        if direction == "right":
            offset = -100
        elif direction == "left":
            offset = 100
        else:
            raise ValueError("Unknown direction: " + str(direction))
        self.driver.drag_and_drop(carousel_obj, x_offset=offset+1)

    
    def verify_carousel_screen_header(self):
        return self.driver.wait_for_object("_shared_carousel_screen_header")
    
    def verify_carousel_screen_owl_dots(self):
        return self.driver.wait_for_object("_shared_carousel_screen_owl_dots")

    def verify_carousel_screen_continue_or_skip_btn(self):
        return self.driver.wait_for_object("_shared_carousel_screen_continue_or_skip_btn")   

    def verify_carousel_screen_card_content(self):
        return self.driver.wait_for_object("_shared_carousel_screen_card_content")



    def verify_spinner_modal(self):
        return self.driver.wait_for_object("_shared_spinner_modal", timeout=15)
     
    @screenshot_compare(root_obj="_shared_error_modal")
    def verify_error_modal(self, invisible=False):
        return self.driver.wait_for_object("_shared_error_modal", invisible=invisible, timeout=15)

class AndroidOWSFlow(OWSFlow):

    def scroll_carousel(self, direction="right"):
        # Swipe() has native_context decorator.
        self.driver.swipe(direction=direction)