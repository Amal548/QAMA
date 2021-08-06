from MobileApps.libs.flows.android.google_slides.google_slides_flows import GoogleSlidesFlow
from MobileApps.resources.const.android import const
from selenium.common.exceptions import NoSuchElementException
import time
import logging

class GoogleSlides(GoogleSlidesFlow):

    flow_name = "google_slides"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################
    def open_google_slides(self):
        """
        open the google slides home
        :return:
        """
        self.driver.wdvr.start_activity(const.PACKAGE.GOOGLE_SLIDES, const.LAUNCH_ACTIVITY.GOOGLE_SLIDES, app_wait_activity = const.WAIT_ACTIVITY.APP_DOC)
        if self.has_welcome_screen():
            self.handle_welcome_screen()


    def select_search(self):
        """
        select the search button to enter the document name:
        :return:
        """
        self.driver.click("search_bar")


    def search_for_file_by_name(self, name):
        """
        Search for the file by the given name
        :param name: String -  name of file //Saved in consts under google Docs
        :return:
        """
        self.driver.send_keys("search_text_field", name)
        self.driver.click("search_text_field")


    def select_3dot_menu(self):
        """
        click on the 3 dot menu button on the searched item
        :return:
        """
        self.driver.click("3dot_button")


    def select_print(self):
        """
        swiping down to select the print option available from the list, works for few listed languages
        :return:
        """
        self.driver.swipe(swipe_object="3dot_menu_sv", per_offset=0.95)
        print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
        r_objects = self.driver.find_object('menu_option_name', multiple=True)
        for obj in r_objects:
            if obj.get_attribute('text') == print_text:
                obj.click()
                return True
        raise NoSuchElementException("Could not find the print button")

        #Appium block
        #print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
        # self.driver.scroll("print_text", scroll_object= "3dot_menu_sv", format_specifier=[print_text])
        # self.driver.click("print_text", format_specifier=[print_text])

    def cancel_search(self):
        """
        cancel the current search to redo the search
        """
        self.driver.click("go_back")

    def handle_welcome_screen(self):
        """
        skip the welcome screen
        """
        self.driver.click("welcome_screen")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Verification Flows                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_google_slides_home(self):
        """
        verify search screen is present or not in slides
        :return:
        """
        self.driver.wait_for_object("drawer_layout")

    def verify_search_screen(self):
        """
        verify search results with given name was present or not;
        :return:
        """
        self.driver.wait_for_object("search_text_field")

    def has_search_result(self):
        """
        verify 3dot button is present or not to give print/share option through window:
        :return:
        """
        return self.driver.wait_for_object("3dot_button",raise_e=False) is not False

    def verify_3dot_menu_screen(self):
        """
        verify the screen is available with list of options
        :return:
        """
        self.driver.wait_for_object("3dot_menu_sv")
        
    def has_welcome_screen(self):
        """
        verify welcome screen is present or not in sheets
        """
        return self.driver.wait_for_object("welcome_screen", timeout=5, raise_e=False) is not False

########################################################################################################################
#                                                                                                                      #
#                                                Guard Code                                                            #
#                                                                                                                      #
########################################################################################################################

    def check_search_result_and_redo_the_search_if_needed(self, max_retry=3, file_search=const.GOOGLE_SLIDES.PPT_1):
        found_element = False
        for _ in range(max_retry):
            if self.has_search_result():
                found_element = True
                break
            else:
                logging.debug("Something happens. Redoing the search...")
                self.cancel_search()
                # An explicit wait rather than a verification
                self.verify_search_screen()
                self.search_for_file_by_name(file_search)
        if not found_element:
            raise NoSuchElementException("Search results failed to appear after " + str(max_retry + 1) + " retries")