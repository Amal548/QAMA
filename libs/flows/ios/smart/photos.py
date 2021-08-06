import logging

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Photos(SmartFlow):
    flow_name = "photos"

    RECENT_PHOTOS_TEXT = "recents_btn_txt"

########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def select_allow_access_to_photos_popup(self, allow_access=True, raise_e=False):
        """
        verifies the photos access popup, if it is there it will give access based on parameter value:
        :param allow_access: True default, if you want to check no access screen , set_to = False:
        :return:
        """
        if self.driver.wait_for_object("photos_access_popup_txt", timeout=10, raise_e=raise_e):
            if allow_access:
                self.driver.click("allow_access_btn")
            else:
                self.driver.click("do_not_allow_access_btn")
        else:
            logging.info("Current Screen did NOT contain the Allow Access photos pop up")

    def select_my_photos(self):
        """
        Selects my photos
        :return:
        """
        self.driver.click("my_photos_btn", change_check={"wait_obj": "view_and_print_txt", "invisible": True},
                          timeout=5)

    def select_all_photos(self):
        """
        Selects all photos
        :return:
        """
        self.driver.click("all_photos_btn")

    def select_recents_or_first_option(self):

        if self.driver.wait_for_object("recents_btn_txt", raise_e=False) is not False:
            self.driver.click("recents_btn_txt")
        else:
            self.driver.click("my_photos_first_option")

    def select_add_account(self):
        """
            Selects add Account
        """
        self.driver.click("add_account_btn")

    def select_remove_facebook(self):
        """
        Removes facebook from photos accounts
        :return:
        """
        cell_list = self.driver.find_object("album_cell_list")
        cells = cell_list.find_object("album_cell")
        logging.info("number of cells: {}".format(len(cells)))
        found = False
        for cell in cells:
            album_name = cell.find_object("cell_text")[0]
            logging.info("cell name: {}".format(album_name.get_attribute("name")))
            if album_name.get_attribute("name") == "Facebook":
                logging.info("Facebook Album found. Clicking X button!")
                cell.find_object("delete_btn").click()
                logging.info("Confirming Remove album accepted.")
                found = True
                break

        if not found:
            logging.info("Facebook delete button was not located on the screen")

    def select_photos_select_option(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_btn")

    def select_all_photos_option_select_all(self):
        """
        Select the album detials select button
        :return:
        """
        self.driver.click("select_all_btn")

    def select_multiple_photos(self, start=0, end=2):
        if self.driver.wait_for_object("select_btn", raise_e=False) is not False:
            self.driver.click("select_btn")
        all_photos_list = self.driver.find_object("all_photos", multiple=True)
        if len(all_photos_list) <= 0:
            raise NoSuchElementException
        for i in range(start, end):
            if i < len(all_photos_list):
                all_photos_list[i].click()

    def select_next_button(self):
        self.driver.click("next_btn")

    def select_photo_by_index(self, index=0):
        """
        selects the photo by index given
        :param index: int , 0 = first photo
        :return:
        """
        self.driver.wait_for_object("photos_lv")
        photos_list = self.driver.find_object("photos_lv_xpath", multiple=True)
        photos_list[index].click()

    def click_select_photos_option(self):
        self.driver.click("select_photos")
    
    def select_access_btn(self):
        self.driver.click("access_btn")
    
    def select_set_photos_access_btn(self):
        self.driver.click("set_photo_access_btn")
    
    def select_show_selected_photos_btn(self):
        self.driver.click("show_selected_photos_btn")
    
    def select_screenshots_folder(self):
        self.driver.click("screenshot_folder")

########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_add_account_screen(self):
        """
        verify add account screen
        :return:
        """
        self.driver.wait_for_object("facebook_btn")
        title = self.driver.find_object("add_account_title")
        if not title.get_attribute("name") == "Add Account":
            logging.info("Current Screen is not Add Account")

    def verify_photos_screen(self):
        """
        Verify Photos screen loaded with photos
        """
        return self.driver.wait_for_object("photos_lv", raise_e=False)

    def verify_all_photos_screen(self):
        """
        Verify All photos detail Screen
        :return:
        """

        self.driver.wait_for_object("all_photos_title")

    def verify_screen_with_select_all_options(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("select_all_btn")
        self.driver.wait_for_object("select_print_btn")

    def verify_multi_selected_photos_screen(self):
        """
        verifies the facebook album multi select screen
        :return:
        """
        self.driver.wait_for_object("cancel_btn")
        self.driver.wait_for_object("next_btn")

    def verify_my_photos_screen(self):
        """
        Verify My Photos Screen
        :return:
        """
        self.driver.wait_for_object("my_photos_title")
    
    def verify_access_btn(self, raise_e=True):
        return self.driver.wait_for_object("access_btn", raise_e=raise_e)
            
    def verify_select_photos_btn(self):
        self.driver.wait_for_object("select_photos")
    
    def verify_allow_photos_access_page(self):
        self.driver.wait_for_object("access_btn")
        self.driver.wait_for_object("set_photo_access_btn")
    
    def verify_set_photo_access_btn(self):
        self.driver.wait_for_object("set_photo_access_btn")

    def get_photos_count_on_view_and_print_screen(self):
        if self.driver.wait_for_object("no_of_photos_preview_label", raise_e=False) is not False:
            photos_count = str(self.driver.get_attribute("no_of_photos_preview_label", attribute="label"))
            photos_count = photos_count.split()
            photos_count = int(photos_count[1])
        else:
            photos_count = 0
        return photos_count
    
    def verify_allow_access_to_photos(self):
        self.driver.wait_for_object("allow_access_btn")

    def verify_dont_allow_access_to_photos(self):
        self.driver.click("do_not_allow_access_btn")
    
    def verify_select_photos_page_after_popup(self):
        self.driver.wait_for_object("select_photos_page_after_popup")
