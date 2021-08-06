import logging
import time

from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.google_docs.google_docs_flows import GoogleDocsFlow
from MobileApps.resources.const.android import const

class GoogleDocs(GoogleDocsFlow):
    flow_name="google_docs"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def open_google_docs(self):
        self.driver.wdvr.start_activity(const.PACKAGE.GOOGLE_DOCS, const.LAUNCH_ACTIVITY.GOOGLE_DOCS, app_wait_activity = const.WAIT_ACTIVITY.APP_DOC)
        if self.has_welcome_screen():
            self.select_skip()

    def select_skip(self):
        """
        select the skip button on the google docs welcome page
        :return:
        """
        self.driver.click("skip_btn")

    def select_search(self):
        """
        click on the search button in google docs home page
        :return:
        """
        self.driver.click("search_btn")

    def search_for_file_by_name(self, name):
        """
        Search for the file by the given name
        :param name: String -  name of file //Saved in consts under google Docs
        :return:
        """
        self.driver.send_keys("search_tf", name)

    def select_3dot_menu(self):
        """
        click on the 3 dot menu button on the searched item
        :return:
        """                                                                                                                                                                                                                                                                                                                                     
        self.driver.click("3dot_button")

    def select_print(self):
        """
        click on the print button within the 3dot menu
        :return:
        """
        self.driver.swipe(swipe_object="3dot_menu_sv",per_offset=0.95)

        print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
        r_objects = self.driver.find_object('menu_option_name', multiple=True)
        for obj in r_objects:
            if obj.get_attribute('text') == print_text:
                obj.click()
                return True
        raise NoSuchElementException("Could not find the print button")

    def cancel_search(self):
        """
        cancel the current search to redo the search
        """
        self.driver.click("cancel_search")

    # Appium block
    # print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
    # self.driver.scroll("print_text", scroll_object="3dot_menu_sv",format_specifier=[print_text])
    # self.driver.click("print_text", format_specifier=[print_text])

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def has_welcome_screen(self):
        """
        verify the google docs welcome screen
        :return:
        """
        return self.driver.wait_for_object("skip_btn", timeout=5, raise_e=False) is not False

    def verify_google_docs_home_screen(self):
        """
        verify the google docs screen is present
        :return:
        """
        self.driver.wait_for_object("search_btn")

    def verify_search_screen(self):
        """
        verify the google docs search screen is present
        :return:
        """
        self.driver.wait_for_object("search_tf")

    def has_search_result(self):
        """
        verify the search result screen is present
        :return:
        """
        return self.driver.wait_for_object("3dot_button", raise_e=False) is not False

    def verify_3dot_menu_screen(self):
        """
        verify the 3dot menu screen is present
        :return:
        """
        self.driver.wait_for_object("3dot_menu_sv")

########################################################################################################################
#                                                                                                                      #
#                                                   Guard Code                                                         #
#                                                                                                                      #
########################################################################################################################

    def check_search_result_and_redo_the_search_if_needed(self, max_retry=3, file_search=const.GOOGLE_DOCS.DOCX_1):
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