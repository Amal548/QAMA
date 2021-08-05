from MobileApps.libs.flows.android.adobe.adobe_flows import AdobeFlow
from selenium.common.exceptions import TimeoutException
from MobileApps.resources.const.android import const
import logging
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class Adobe(AdobeFlow):

    flow_name =  "adobe"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def open_adobe(self):
        """
        opens the adobe home
        :return:
        """
        self.driver.start_activity(const.PACKAGE.ADOBE,const.LAUNCH_ACTIVITY.ADOBE, wait_activity=const.PACKAGE.ADOBE + "*")
        if self.driver.wait_for_object("welcome_screen_exit_button", timeout=10, raise_e=False):
            self.driver.click("welcome_screen_exit_button")
        if self.has_overlay_ui():
            self.turn_off_overlay_ui_guide()

    def select_search(self):
        """
        select the search button to enter the document name:
        :return:
        """

        self.driver.click("search")

    def search_for_file_by_name(self, name):
        """
        search for the file by the given name:
        :param name: String - name of the file  and it is saved in the consts under adobe
        :return:
        """

        self.driver.send_keys("search_text_field", name)
        self.driver.wdvr.press_keycode(66)

    def open_file(self):
        """
        selects the files from results:
        :return:
        """
        self.driver.click("open_file", change_check={"wait_obj": "open_file", "invisible": True})

    def cancel_search(self):
        """
        cancels the text search for file
        :return:
        """
        self.driver.click("cancel_search_btn")


    def select_3dot_menu(self):
        """
        selects the 3dot button
        :return:
        """
        if self.has_overlay_ui():
            self.turn_off_overlay_ui_guide()
        self.driver.click("3dot_button")


    def select_print(self, timeout=180):
        """
        ##### this is system ui test #####
        select the print option available from the list, works for few listed languages:
        :return:
        """
        print_text = self.driver.session_data["app_strings"]["hpps"]["button_label__print"]
        self.driver.swipe(direction="down")
        self.driver.click("print_text", format_specifier=[print_text])

    def select_share_copy(self):
        """

        ### this trap door method ###
        open the share options and scroll down to share with HPPS
        :return:
        """
        if self.has_overlay_ui():
            self.turn_off_overlay_ui_guide()
        self.driver.click("select_trap_door_share_option")
        self.driver.wait_for_object("share_copy_button")
        self.driver.click("share_copy_button")

    def turn_off_overlay_ui_guide(self):
        self.driver.click("overlay_ui")

    def open_adobe_and_search_for_file(self, file):
        self.open_adobe()
        self.verify_adobe_home()
        self.select_search()
        self.verify_search_screen()
        self.search_for_file_by_name(file)
        self.check_run_time_permission()

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_adobe_home(self):
        """
        verifies the adobe home screen is available or not:
        :return:
        """
        self.handle_user_data_popup()
        self.driver.wait_for_object("home_screen")

    def verify_search_screen(self):
        """
        verifies the search screen is loaded or not:
        :return:
        """
        self.driver.wait_for_object("search_text_field")

    def verify_editor_screen(self):
        """
        verifies the pdf preview was loaded or not for both trapdoor and system ui process options:
        :return:
        """
        self.driver.wait_for_object("edit_button")

    def verify_3dot_menu_screen(self):
        """com.adobe.reader:id/bottom_sheet_main_container
        verifies the 3 dot menu screen is opened / with a list
        :return:
        """
        self.driver.wait_for_object("3dot_menu_sv")

    def verify_trap_door(self):
        """
        verifies the trap door is loaded or not;
        :return:
        """
        self.driver.wait_for_object("select_trap_door_share_option")

    def verify_local_files_selected(self):
        """
        Verifies that local files folder was selected or not : because all our test files are stored under local files folder
        :return:
        """
        self.driver.wait_for_object("try")
    
    def has_overlay_ui(self):
        """
        Check if there's an UI guide appear at home screen when first time opening the app
        """
        return self.driver.wait_for_object("overlay_ui", timeout=5, raise_e=False) is not False

    def has_search_result(self):
        return self.driver.wait_for_object("open_file", raise_e=False) is not False

########################################################################################################################
#                                                                                                                      #
#                                                Guard Code                                                            #
#                                                                                                                      #
########################################################################################################################

    def check_search_result_and_redo_the_search_if_needed(self, max_retry=3, file_search=const.ADOBE.PDF_1):
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
                # Happens on Nexus 6P
                # Sometimes after accepting the app permission, the same permission pop up again
                # Before this 2nd time pop, the permission is turned on in app settings, but after the 2nd pop, the permission is turned off
                self.check_run_time_permission()
        if not found_element:
            raise NoSuchElementException("Search results failed to appear after " + str(max_retry + 1) + " retries")

    def handle_user_data_popup(self):
        if self.driver.wait_for_object("user_data_usage_continue_button", timeout=5, raise_e=False) is not False:
            return self.driver.click("user_data_usage_continue_button")
        return True