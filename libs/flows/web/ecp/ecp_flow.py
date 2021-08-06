import time
import math
import logging
from itertools import groupby 
from SAF.decorator.saf_decorator import native_context
from MobileApps.libs.flows.web.web_flow import WebFlow

class PaginationException(Exception):
    pass

class NoEntriesMissingException(Exception):
    pass

class WrongPageException(Exception):
    pass

class PageOutOfBound(Exception):
    pass

class IncorrectSortException(Exception):
    pass

class ECPFlow(WebFlow):
    project = "ecp"

    def __init__(self, driver, context=None,  url=None):
        super(ECPFlow, self).__init__(driver, context=context, url=url)
        self.func_ignore_methods.append("load_ecp_shared_ui")
        self.load_ecp_shared_ui()

    def load_ecp_shared_ui(self):
        ui_map = self.load_ui_map(system="WEB", project="ecp", flow_name="shared_obj")
        self.driver.load_ui_map("ecp", "shared_obj", ui_map)
        return True
    
    ######################## Common object verify ############################################
    def verify_all_page_size_options(self, page_sizes, root_obj=None):
        self.verify_page_size_btn(root_obj=root_obj)
        self.click_page_size_btn(root_obj=root_obj)
        for size in page_sizes:
            self.driver.wait_for_object("_shared_page_size_menu_entry", format_specifier=[str(size)], root_obj=root_obj)
            logging.info("Page size: " + str(size) + " is avaliable")
        self.click_page_size_btn(root_obj=root_obj)
        return True
    
    def verify_page_size_btn(self, root_obj=None):
        return self.driver.wait_for_object("_shared_page_size_btn", root_obj=root_obj)

    def verify_page_nav(self, root_obj=None):
        return self.driver.wait_for_object("_shared_all_pages_btn", root_obj=root_obj)

    def verify_table_displaying_correctly(self, page_size, page=1, root_obj=None):
        self.select_page_size(page_size, root_obj=root_obj)
        current_page = self.select_page(page, root_obj=root_obj)
        total_entries = self.get_total_entries(root_obj=root_obj)
        actual_max_page = self.get_max_page(root_obj=root_obj)
        page_size_btn_num = list(map(int, self.get_page_size_btn_txt(root_obj=root_obj).split(" - ")))

        if total_entries == 0:      
            if self.driver.wait_for_object("_shared_no_items_found_img", root_obj=root_obj, raise_e=False) is False:
                raise NoEntriesMissingException("Total entry is 0. But 'No Items found' is not displayed")
            max_page = math.ceil(total_entries/page_size) + 1
            total_visible_entries = self.get_total_table_entries(root_obj=root_obj) -1
            expected_from = 0
        else:
            max_page = math.ceil(total_entries/page_size)
            total_visible_entries = self.get_total_table_entries(root_obj=root_obj)
            expected_from = current_page*page_size-total_visible_entries - (page_size - total_visible_entries) +1

        expected_to = current_page*page_size - (page_size - total_visible_entries)

        if actual_max_page != max_page:
            raise PaginationException("Expected total page: " + str(max_page) + " != Actual total page: " + str(actual_max_page))

        if page_size_btn_num != [expected_from, expected_to]:
            raise PaginationException("Entry indicator: " + str(page_size_btn_num) + " Expecting: " + str([expected_from, expected_to]))
        return True

    def verify_table_sort(self, field, sort_order):
        #Params: field -> Which field to check the order for 
        #        sort_order -> The order the field should follow 
        header_index = self.get_header_index(field)
        all_field = [i.text for i in self.driver.find_object("_shared_table_all_col_by_index", format_specifier=[header_index], multiple=True)]
        order_set = [i[0] for i in groupby(all_field)]
        if order_set != sort_order:
            raise IncorrectSortException("Excected sort order: " + str(sort_order), " Actual sort order: " + str(order_set))
        return True

    def verify_header_column_loaded(self):
        self.driver.wait_for_object("_shared_all_table_header_column")

    ######################## Common flows #############################################
    def select_page_size(self, page_size, root_obj=None):
        self.click_page_size_btn(root_obj=root_obj)
        self.click_page_size_option_by_value(page_size, root_obj=root_obj)
        time.sleep(3)
        return True

    def select_page(self, page, root_obj=None):
        #First and last btn are the arrows
        self.verify_page_nav(root_obj=root_obj)        
        page_objects = self.driver.find_object("_shared_all_pages_btn", multiple=True, root_obj=root_obj)[1:-1]
        total_pages = int(page_objects[-1].text)
        if page > total_pages:
            raise PageOutOfBound("Total pages: " + str(total_pages) + " desired page: " + str(page))

        elif page >= int(total_pages/2):
            page_objects[-1].click()
            click_until_found = self.click_prev_nav
            total_clicks = total_pages - page
        else:
            click_until_found = self.click_next_nav
            total_clicks = page -1

        for _ in range(total_clicks):
            click_until_found(root_obj=root_obj)

        current_page = self.get_current_page(root_obj=root_obj)
        if current_page == page:
            time.sleep(3)
            return current_page
        else:
            raise WrongPageException("Expected page: " + str(page) + " ended up on: " + str(current_page))

    ######################## Common object click #############################################
    def click_page_nav(self, page_num, root_obj=None):
        return self.driver.click("_shared_page_nav_btn", format_specifier=page_num, root_obj=root_obj)

    def click_prev_nav(self, root_obj=None):
        return self.driver.click("_shared_page_prev_nav_btn", root_obj=root_obj)

    def click_next_nav(self, root_obj=None):
        return self.driver.click("_shared_page_next_nav_btn", root_obj=root_obj)
    
    def click_page_size_btn(self, root_obj=None):
        return self.driver.click("_shared_page_size_btn", root_obj=root_obj)

    def click_page_size_option_by_value(self, value, root_obj=None):
        return self.driver.js_click("_shared_page_size_menu_entry", format_specifier=[value], root_obj=root_obj)

    def click_table_header_by_name(self, header):
        self.verify_header_column_loaded()
        return self.driver.click(header + "_table_header")

    def get_page_size_btn_txt(self, root_obj=None):
        return self.driver.wait_for_object("_shared_page_size_btn", root_obj=root_obj).text

    def get_current_page_size(self, root_obj=None):
        self.click_page_size_btn(root_obj=root_obj)
        size = self.driver.wait_for_object("_shared_page_size_menu_selected_entry", root_obj=root_obj).text
        self.click_page_size_btn(root_obj=root_obj)
        return size

    def get_total_entries(self, root_obj=None):
        return int(self.driver.wait_for_object("_shared_page_size_total_txt", root_obj=root_obj).text.split("of ")[1])

    def get_total_table_entries(self,total_len=True, root_obj=None):
        entries = self.driver.find_object("_shared_table_entries", multiple=True, root_obj=root_obj)
        if total_len:
            return len(entries)
        else:
            return entries

    def get_current_page(self, root_obj=None):
        return int(self.driver.wait_for_object("_shared_current_page", root_obj=root_obj).text)
    
    def get_max_page(self, root_obj=None):
        #I can use -2 but this is to make it clear
        #strip the left/right nav then the last one after that is the max page
        return int(self.driver.find_object("_shared_all_pages_btn", multiple=True, root_obj=root_obj)[1:-1][-1].text)

    def get_header_index(self, header):
        self.verify_header_column_loaded()
        all_headers = self.driver.find_object("_shared_all_table_header_column", multiple=True)
        header = self.driver.find_object(header + "_table_header")
        return all_headers.index(header) + 1

    def click_refresh_button(self):
        return self.driver.click("sync_button")

    def get_sync_time_info(self):
        return self.driver.get_text("sync_time_label")