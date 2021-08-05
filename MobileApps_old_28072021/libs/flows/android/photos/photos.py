from MobileApps.libs.flows.android.photos.photos_flow import PhotosFlow
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.system_flows.sys_flow_factory import system_flow_factory
import time, logging
from selenium.common.exceptions import NoSuchElementException, WebDriverException

class Photos(PhotosFlow):
    flow_name="photos"

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def open_google_photos(self):

        self.driver.wdvr.start_activity(const.PACKAGE.GOOGLE_PHOTOS, const.LAUNCH_ACTIVITY.GOOGLE_PHOTOS, app_wait_activity=const.LAUNCH_ACTIVITY.GOOGLE_PHOTOS)
        self.check_run_time_permission()
        self.backup_and_sync_confirm()
        if self.driver.wait_for_object("out_of_space_alert_message", timeout=5, raise_e=False):
            self.driver.back()

    def backup_and_sync_confirm(self):
        if self.driver.wait_for_object("backup_and_sync_confirm_btn", timeout=3, raise_e=False):
            self.driver.click("backup_and_sync_confirm_btn")
        if self.driver.wait_for_object("back_up_space_confirm_btn", timeout=3, raise_e=False):
            self.driver.click("back_up_space_confirm_btn")
        if self.driver.wait_for_object("welcome_page_skip_btn", timeout=3, raise_e=False):
            self.driver.click("welcome_page_skip_btn")

    def search_for_file(self, _file):
        self.select_search_bar()
        self.search_file(_file)
        self.select_auto_completion_text()
        self.select_photo()

    def select_photo(self):
        self.driver.click("photo_icons")

    def select_search_bar(self):
        self.driver.click("search_bar")

    def search_file(self, _file):
        self.driver.send_keys("search_bar_txt", _file, press_enter=True)

    def select_auto_completion_text(self):
        self.driver.click("auto_complete_suggestion_txt", raise_e=False)

    def select_search(self):
        """
        Click on the 3 bar button that opens the side menu
        :return:
        """
        self.driver.click("search_btn")

    def select_share(self, share_button_obj="share_btn"):
        """
        open the share options and scroll down to share with HPPS
        :return:
        """
        self.driver.wait_for_object(share_button_obj)
        self.driver.click(share_button_obj)
        self.check_run_time_permission()

    def select_3dot_menu(self):
        """
        selects the 3dot button:
        :return:
        """
        self.driver.click("3dot_btn")

        # Appium block
        # print_text = self.driver.get_ui_obj_dict("print_text")["languages"][self.driver.session_data['language']]
        # self.driver.click("print_text", format_specifier=[print_text])

    def select_back_button(self):
        """
        selects the back button to navigate to Google Photos home screen
        :return:
        """
        self.driver.wait_for_object("back_button")
        self.driver.click("back_button")

    def select_multiple_photo_files(self, number_of_photos):
        """
        selects multiple photos based on number_of_photos
        :return: total number of photo being selected
        """
        self.driver.wait_for_object("photo_thumbnail")
        self.driver.long_press("photo_thumbnail")
        photo_lists = self.driver.find_object("photo_thumbnail", multiple=True)
        if number_of_photos > len(photo_lists):
            raise WebDriverException("The number of photos to be selected is more than the number of current existing photos")
        for photo in photo_lists[1:number_of_photos]:
            photo.click()
        total_photos = self.driver.wait_for_object("number_of_selected_files")
        assert number_of_photos == int(total_photos.get_attribute("text"))

    def dismiss_new_feature_popup(self):
        self.driver.click("popup_ok_btn", timeout=5, raise_e=False)

########################################################################################################################
#                                                                                                                      #
#                                               Verification Flows                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_google_photos_home_screen(self):
        """
        verify that the current screen is google photos launch screen
        :return:
        """
        self.dismiss_new_feature_popup()
        self.driver.wait_for_object("drawer_layout")

    def verify_search_screen(self):
        """
        verify that the side menu is displayed
        :return:
        """
        self.driver.wait_for_object("search_bar")

    def verify_album_screen(self):
        """
        verify the album screen is displayed
        :return:
        """
        self.driver.wait_for_object("image_list")

    def verify_image_screen(self, raise_e = True):
        """
        Verify image screen is displayed
        :return:
        """
        return self.driver.wait_for_object("image_page_indicator", timeout=3, raise_e=raise_e)

    def verify_3dot_menu_screen(self):
        """
        verifies the 3dot menu screen with print option is available or not:
        :return:
        """
        self.driver.wait_for_object("3dot_menu_lv")