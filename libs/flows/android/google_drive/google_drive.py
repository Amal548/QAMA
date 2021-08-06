
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException

from SAF.exceptions.saf_exceptions import ObjectFoundException
from MobileApps.libs.flows.android.android_flow import AndroidFlow

from MobileApps.resources.const.android import const

from MobileApps.libs.flows.android.system_flows.sys_flow_factory import system_flow_factory


import time
import logging

class DocPathIncorrect(Exception):
    pass

class TrapDoorDocTitleIncorrect(Exception):
    pass

class GoogleDrive(AndroidFlow):
    project = "google_drive"
    flow_name = "google_drive"

        ########################################################################################################################
        #                                                                                                                      #
        #                                                  Action Flows                                                        #
        #                                                                                                                      #
        ########################################################################################################################


    def launch_google_drive(self):
        self.driver.wdvr.start_activity(const.PACKAGE.GOOGLE_DRIVE, const.LAUNCH_ACTIVITY.GOOGLE_DRIVE, app_wait_activity = const.PACKAGE.GOOGLE_DRIVE + "*")

        if self.driver.wait_for_object('feature_highlights', timeout=3, raise_e=False):
            self.driver.click("feature_highlights")

    def search_and_open_file(self, file_name):
        self.driver.wait_for_object("search_btn")
        self.driver.click("search_btn")
        self.driver.send_keys("search_tf", file_name)
        self.driver.wait_for_object("file_el")
        self.driver.click("file_el")
        if self.driver.wait_for_object('feature_highlights', timeout=3, raise_e=False):
            self.driver.click("comment_button")

    def click_on_3_dot_menu(self):
        """
        click on 3-dot-menu (system_ui) in the top right corner of the screen
        :return:
        """
        self.driver.wait_for_object("3-dot-menu-btn", timeout=1)
        self.driver.click("3-dot-menu-btn")

    def select_print(self, timeout=180):
        """
        click on print from the scroll
        timeout - Number of seconds before throwing exception
        :return:
        """
        print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
        self.driver.scroll("print_text", scroll_object="3dot_menu_sv", format_specifier=[print_text])
        self.driver.click("print_text", format_specifier=[print_text])

    def select_account(self, account_name):

        self.driver.click("main_menu_icon")
        if self.driver.find_object("account_address").text == account_name:
            self.driver.back()
            return True

        self.driver.click("account_list_btn")
        accounts = self.driver.find_object("account_address", multiple=True)
        for el in accounts:
            if el.text == account_name:
                el.click()
        return True
    
    def print_file(self, file_name, index=0):
        self.search_and_open_file(file_name)

        self.driver.click("info_btn")
        self.driver.swipe(direction="down")
        self.driver.click("option_text", index=-3)

    def send_a_copy(self, file_name, target_app, index=0):
        # Will come back to this, if there's a need to use
        raise NotImplementedError
        # self.search_and_open_file(file_name, index=index)
        # self.driver.click("info_btn")
        # self.driver.swipe(direction="down")
        # self.driver.click("option_text", index=-9)
        # self.system_flow.select_app(target_app)

    def remove_file(self, file_name):
        self.search_and_open_file(file_name)
        self.driver.click("info_btn")
        self.driver.swipe(direction="down")
        self.driver.click("option_text", index=-2)
        try:
            self.driver.wait_for_object("trap_door_save_btn", timeout=5)
            self.driver.click("trap_door_save_btn")
        except (NoSuchElementException, TimeoutException):
            logging.info("No move to trash dialog")

    #Don't know what this is for i guess we'll find out
    def __select_skip(self):
        """
        From sheets home screen click the search button

        End of flow: search window
        """
        if self.__is_skip_button():
          self.driver.click("skip_btn")

    # -------------------           USING FROM ANOTHER APP THAT SHARE FILE TO GOOGLE DRIVE      ------------------------
    # -------------------                   START AT "Save to Drive" SCREEN                     ------------------------
    def get_current_folder_name(self):
        """
        At Save to Drive screen:
            Get current folder name
        :return: folder name
        """
        self.driver.wait_for_object("trap_door_title")
        return self.driver.find_object("trap_door_folder_btn").text

    def select_save(self):
        """
        At Save to Drive screen:
            Click on Save button
        """
        self.driver.click("trap_door_save_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Verification Flows                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_file_path(self, file_path):

        #Starting from image settings half menu
        path_list = file_path.split("/")
        path_list = path_list[:-1][::-1]
        if path_list[-1] == "":
            del path_list[-1]
        time.sleep(1)
        for num, path in enumerate(path_list):
            if num != 0:
                try:
                    self.driver.click("folder_info_btn")
                except NoSuchElementException:
                    self.driver.click("info_btn")
                self.driver.click("folder_info_options", index=-1)

            self.driver.click("info_btn")
            path_el = self.driver.find_object("location_title")
            if path_el.text != path:
                raise DocPathIncorrect("Expecting: " + path + " Got: " + path_el.text)
            path_el.click()
            time.sleep(1)
        self.launch_google_drive()

    def verify_save_to_drive(self, file_name=""):
        """
        Verify that current screen is Save to Drive screen:
            - Save to Drive title
            - Current file name matches with target file name
            - Save and Cancel button
        :param file_name: target file name, include its extension
        """
        self.driver.wait_for_object("trap_door_title")
        self.driver.wait_for_object("trap_door_cancel_btn")
        self.driver.wait_for_object("trap_door_save_btn")
        f_name = self.driver.find_object("trap_door_doc_title").text
        if file_name != "" and file_name not in f_name:
            raise TrapDoorDocTitleIncorrect("Displayed name ({}) is NOT target file name ({})".format( file_name, f_name))

    def verify_home_screen(self):
        """
        Verify home screen to make sure that app launches successfully.
        :return:
        """
        self.driver.wait_for_object("search_btn")

    def verify_opened_file_screen(self):
        """
        Verify screen to make sure that desired file opens successfully.
        :return:
        """
        self.driver.wait_for_object("3-dot-menu-btn")

    def verify_3_dot_menu_screen(self):
        """
        verify the scroll that appears after clicking on 3-dot-menu-btn.
        :return:
        """
        self.driver.wait_for_object("3-dot-menu")