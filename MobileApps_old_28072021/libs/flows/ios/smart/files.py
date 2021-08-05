import logging
import re
from selenium.common.exceptions import TimeoutException, NoSuchElementException, InvalidElementStateException
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
import time


class Files(SmartFlow):
    flow_name = "files"
#####################################################################################################################
#                                           New Refactored code goes below this line
#####################################################################################################################

    def verify_view_and_print_screen(self):
        self.driver.wait_for_object("view_and_print_text")

    def select_next_btn(self):
        self.driver.wait_for_object("next_btn").click()


########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_hp_smart_files_folder_icon(self):
        """
        :return:
        """
        self.driver.wait_for_object("hp_smart_files_image_button", timeout=10)
        self.driver.click("hp_smart_files_image_button")

    def select_hp_smart_files_create_folder_icon(self):
        """

         :return:
        """
        self.driver.wait_for_object("hp_smart_files_create_folder_image")
        self.driver.click("hp_smart_files_create_folder_image")

    def create_folder_by_passing_name(self, default_name="TestFolder"):
        """
        Create a folder with folder name on Create Folder popup
        :param default_name: folder name

        End of flow: My File screen displays with created folder name
        """
        self.driver.send_keys("folder_name_tf", default_name)
        self.driver.click("create_folder_create_btn")

    def select_hp_smart_files_3dot_button(self):
        """
        Clicks on the 3dots button to open a new window to create, select any folder

        :return:
        """
        self.driver.wait_for_object("hp_smart_files_more_button", timeout=50)
        self.driver.click("hp_smart_files_more_button")

    def select_hp_smart_files_select_option_from_list(self):
        """
         :return:
        """

        self.driver.wait_for_object("hp_smart_files_select_image")
        self.driver.click("hp_smart_files_select_image")

    def enter_search_item_in_search_box(self, default_name="TestFolder"):
        """
        selects the folder by searching the given folder name:
        :param default_name: if we know the existed folders will pass that from calling
            else it will search for default folder "TestFolder" which we created in create folder method
        """
        self.driver.wait_for_object("search_box", timeout=10).click()
        self.driver.send_keys("search_box", default_name)

    def select_radio_btn(self):
        """
        :return:
        """
        self.driver.click("radio_btn")

    def select_delete(self):
        """
        Click on Delete button

        """
        self.driver.wait_for_object("delete_btn")
        self.driver.click("delete_btn")

    def select_select_all_button(self):
        self.driver.wait_for_object("select_files_select_all_btn", timeout=15).click()


    def my_files_select_search_cancel(self):
        """
        Click on Cancel button on navigation bar

        End of flow: My Files screen
        """
        self.driver.wait_for_object("search_cancel_btn").click()

    def select_dropdown_options_button(self):
        """
        :return:
        """
        self.driver.wait_for_object("show_options_menu")
        self.driver.click("show_options_menu")

    def select_move_folder_option(self):
        """
        :return:
        """
        self.driver.click("select_move_folder_option")

    def create_folder_for_move_options(self, default_name="MoveFolder"):
        """

        :param default_name:
        :return:
        """
        self.driver.send_keys("folder_name_tf", default_name)
        self.driver.click("create_folder_create_btn")

    def select_move_from_navigation(self):
        """
        :return:
        """
        self.driver.wait_for_object("move_bottom_navigation", timeout=60)
        self.driver.click("move_bottom_navigation")

    def select_rename_folder_option(self):
        """
        :return:
        """
        self.driver.click("select_rename_folder_option")

    def select_clear_text(self):
        """
        :return:
        """
        self.driver.click("clear_text")

    def select_delete_folder_option(self):
        """
        :return:
        """
        self.driver.click("select_delete_folder_option")

    def select_my_files_back_btn(self):
        """

        :return:
        """
        self.driver.click("back_btn")

    def select_all_files_image(self):
        """

        :return:
        """

        self.driver.click("all_files_image_button")

    def select_x_button_on_given_cloud(self):
        """
        :return:
        """
        self.driver.click("remove_btn")

    def select_remove_on_popup(self):
        """
        :return:
        """
        self.driver.click("remove_btn")

    def select_hp_smart_files(self):
        """
        Click on My Files
        :param
        """
        self.driver.click("hp_smart_files_btn")

    def is_empty_screen(self):
        """
        Checks if HP Smart Files is empty or not
        :return:
        """
        return self.driver.wait_for_object("files_empty_screen", timeout=10, raise_e=False) is not False


    def select_learn_more_link_on_empty_files_screen(self):
        """

        :return:
        """

        self.driver.click("learn_more_link")


    def select_sort_by_name_option(self):
        self.driver.click("sort_by_name_optn")

    def select_sort_by_date_option(self):
        self.driver.click("sort_by_date")

    def select_drop_box_option(self):
        """

        :return:
        """

        self.driver.click("drop_box")

    def select_folder_from_list(self, name):
        """
        :param name:
        :return:
        """
        try:
            folder_list = self.driver.find_object(obj_name="folder_list", multiple=True)
            for folder in folder_list:
                if name.lower() == folder.text.lower():
                    folder.click()
        except NoSuchElementException:
            raise NoSuchElementException("No folders were found")

    def select_google_drive_image(self):
        """

        :return:
        """

        self.driver.click("google_drive")

    def select_dest_folder_from_list(self, folder_name):
        """

        :return:
        """
        folder_list = self.driver.find_object("dest_folder_list", multiple=True)
        for folder in folder_list:
            if folder_name.lower() in folder.text.lower():
                folder.click()
                break


    def select_recent_button(self):
        """
        :return:
        """
        self.driver.click("recent_btn")

    def select_back_btn_on_recent_document_screen(self):
        """
        :return:
        """
        self.driver.click("recent_back_btn")

    def select_browse_button(self):
        """

        :return:
        """
        self.driver.click("browse_btn")

    def select_cloud_screen_back_button(self):
        """

        :return:
        """
        self.driver.click("locations_back_btn")

    def select_locations_folder_drive_btn(self):
        """

        :return:
        """
        self.driver.click("locations_google_drive")

    def select_locations_folder_drop_box(self):
        """

        :return:
        """
        self.driver.click("locations_drop_box_btn")

    def select_icloud_button(self):
        """

        :return:
        """
        self.driver.click("icloud_btn")

    def select_recently_deleted_button(self):
        """

        :return:
        """
        self.driver.click("recently_deleted_btn")

    def select_folder_from_cloud_list(self, folder_name):
        """

        :return:
        """
        folder_list = self.driver.find_object("icloud_folder_list", multiple=True)
        for folder in folder_list:
            if folder_name.lower() in folder.text.lower():
                folder.click()
                break

    def select_recover(self):
        """

        :return:
        """
        self.driver.click("recover_btn")

    def select_show_more_item_arrow(self):
        """

        :return:
        """
        self.driver.click("show_more_item_arrow")


    def select_my_photos_button_on_files_screen(self):
        """

        :return:
        """
        self.driver.click("files_my_photos")

    def select_allow_access_to_facebook_popup(self, allow_access=True):
        """
        verifies the facebook access popup, if it is there it will give access based on parameter value:
        :param allow_access: True default, if you want to check no access screen , set_to = False:
        :return:
        """

        if self.driver.wait_for_object("facebook_access_popup_txt", raise_e=False):
            if allow_access:
                self.driver.click("continue_btn")
            else:
                self.driver.click("file_cancel_btn")
        else:
            logging.info("Current Screen did NOT contain the Allow Access Facebook  pop up")


    def select_facebook_on_files_screen(self):
        """
        :return:
        """
        self.driver.scroll(object_to_find='face_book', direction='down')
        self.driver.click("face_book")

    def select_x_button_to_delete(self):
        """
        :return:
        """
        self.driver.click("remove_btn")

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_files_screen(self, timeout=20, raise_e=True):
        """
        Verify Files screen
        """
        return self.driver.wait_for_object("files_title", timeout=timeout, raise_e=raise_e)

    def verify_hp_smart_files_home_screen(self):
        """
        This method is verify empty screen of HP Smart files
        :return:
        """

        if self.is_empty_screen():
            logging.info("HP Smart Files has no files available !!")
        else:
            self.driver.wait_for_object("hp_smart_files_title")
            logging.info("HP Smart Files has some files available !!")

    def verify_create_folder_popup(self):
        """
        :return:
        """
        self.driver.wait_for_object("create_folder_title")

    def verify_more_options_door(self):
        """
        Verify the 3dots(menu) window

        :return:
        """
        self.driver.wait_for_object("more_options_button")

    def verify_my_files_select_files_screen(self):
        """
        Verify current screen is Select Files via:
            - Select Files title
            - Select All button
        """

        self.driver.wait_for_object("select_files_select_all_btn")

    def verify_file_delete_confirmation_popup(self):
        """
        Verify current popup is Delete Confirmation popup via:
            - Delete message
            - Delete button
        """
        if not self.driver.wait_for_object("delete_popup_msg", raise_e=False, timeout=10):
            self.driver.wait_for_object("delete_multi_popup_msg", raise_e=False, timeout=10)
            logging.info("Are you sure you want to delete these items- msg displayed")
        else:
            logging.info("Are you sure you want to delete this items- msg displayed")
        self.driver.wait_for_object("delete_btn")
        self.driver.wait_for_object("delete_popup_cancel_btn")

    def verify_menu_door_from_down(self):
        """

        :return:
        """
        self.driver.wait_for_object("menu_door_popup")

    def verify_my_files_with_choose_dest_text(self):
        """
        Verify current screen is 'My Files' with 'Choose a destination' text via:
            - My Files title
            - 'Choose a destination' text
        """
        self.driver.wait_for_object("choose_dest_txt")

    def verify_rename_folder_popup(self):
        """
        Verify current popup is Rename Folder via:
            - Rename Folder title
            - Rename button
        """
        self.driver.wait_for_object("rename_folder_title")
        self.driver.wait_for_object("rename_btn")

    def verify_hp_smart_recent_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("hp_smart_ah_recent_title")

    def verify_cloud_remove_popup(self):
        """
        :return:
        """
        self.driver.wait_for_object("remove_btn")

    def verify_Edit_button(self):
        """
        :return:
        """
        self.driver.wait_for_object("edit_btn")

    def verify_all_files_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("all_files_image_button")

    def verify_drop_box_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("drop_box")

    def verify_google_drive_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("google_drive")

    def verify_google_photos(self):
        self.driver.wait_for_object("google_photos")

    def verify_box_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("box")

    def verify_ever_note_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("ever_note")

    def verify_face_book_button(self):
        """

        :return:
        """

        self.driver.scroll("face_book")

    def verify_instagram_image(self):
        """

        :return:
        """

        self.driver.wait_for_object("instagram_btn")

    def verify_other_image(self):
        """

        :return:
        """

        self.driver.scroll("other_btn")

    def verify_files_and_photos(self):
        """
        It verifies, file and photos on the root bar is selected ot not
        :return:
        """

        if self.driver.get_attribute(obj_name="file_and_photos_option", attribute="value") == '1':
            logging.info("Files and photos selected")
        else:
            raise NoSuchElementException("Files and photos not selected")

    def verify_all_files_home_screen(self):
        """
        :return:
        """

        if self.is_all_files_screen_empty():
            logging.info("All Files screen  has no documents available !!")
        else:
            self.driver.wait_for_object("hp_smart_ah_recent_title")
            logging.info("All Files screen  has some documents available !!")

    def verify_recent_button(self):
        """

        :return:
        """
        self.driver.wait_for_object("recent_btn")

    def verify_browse_button(self):
        """

        :return:
        """
        self.driver.wait_for_object("browse_btn")

    def verify_hp_smart_files_screen(self, raise_e=True):
        """
        :return:
        """
        return self.driver.wait_for_object("hp_smart_files_title", timeout=15, raise_e=raise_e)


    def verify_all_action_for_selected_files(self):
        """

        :return:
        """

        self.driver.wait_for_object("delete_btn")
        self.driver.wait_for_object("select_files_select_all_btn")
        self.driver.wait_for_object("move_bottom_navigation")

    def verify_rename_option(self):
        """

        :return:
        """

        self.driver.wait_for_object("select_rename_folder_option")

    def verify_move_folder_option(self):
        """

        :return:
        """

        self.driver.wait_for_object("select_move_folder_option")

    def verify_delete_folder_option(self):
        """

        :return:
        """
        self.driver.wait_for_object("select_delete_folder_option")

    def verify_create_folder_option(self):
        """

        :return:
        """
        self.driver.wait_for_object("create_folder")

    def verify_move_option(self):
        """

        :return:
        """
        self.driver.wait_for_object("move_bottom_navigation")

    def verify_files_my_photos_button(self):
        """

        :return:
        """
        self.driver.wait_for_object("files_my_photos")

    def verify_folder_from_list(self, name):
        """

        :param name:
        :return:
        """
        return_val = False
        try:
            folder_list = self.driver.find_object(obj_name="folder_list", multiple=True)
            for folder in folder_list:
                if name.lower() in folder.text.lower():
                    logging.info("Folder {} present in list".format(name))
                    return True
                else:
                    logging.info("Folder {} notpresent in list".format(name))
                    return_val = False
        except NoSuchElementException:
            logging.info("Folder {} not present in list".format(name))
            return_val = False
        return return_val

    def verify_folder_order(self, folder_names):
        folder_list = self.driver.find_object(obj_name="folder_list", multiple=True)
        for i in range(len(folder_names)):
            if folder_names[i].lower() in folder_list[i].text.lower():
                logging.info("found folder {} at location {}".format(folder_names[i], i + 1))
                continue
            else:
                logging.info("Folder's are not in alphabetical order")

    def is_all_files_screen_empty(self):
        """
        Checks if HP Smart Files is empty or not
        :return:
        """
        self.driver.wait_for_object("no_recent_files", raise_e=False)

    def verify_select_files_screen(self):
        return self.driver.wait_for_object("select_files_title", raise_e=False) is not False

    def verify_drive_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("locations_google_drive")

    def verify_select_button(self):
        """

        :return:
        """
        self.driver.wait_for_object("select_btn")

    def verify_back_btn_on_recent_document_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("recent_back_btn")

    def verify_location_folder_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("locations_title")

    def verify_favorites_folder_title(self):
        """

        :return:
        """
        self.driver.wait_for_object("favorites_folder_title")

    def verify_tags_folder_title(self):
        """

        :return:
        """
        self.driver.wait_for_object("tags_folder_title")

    def verify_hp_smart_ah_folders_names(self):
        """

        :return:
        """
        self.verify_location_folder_screen()
        self.verify_favorites_folder_title()
        self.verify_tags_folder_title()

    def verify_ui_elements_on_recent_documents_screen(self):
        """

        :return:
        """
        self.verify_select_button()
        self.verify_close()
        self.verify_back_btn_on_recent_document_screen()
        self.verify_browse_button()

    def verify_icloud_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("icloud_drive_title")

    def verify_locations_button(self):
        """

        :return:
        """
        self.driver.wait_for_object("locations_title")

    def verify_icloud_ui_elements_screen(self):
        """

        :return:
        """
        self.verify_locations_button()
        self.verify_close()
        self.verify_select_button()
        self.verify_browse_button()
        self.verify_recent_button()

    def long_press_on_file(self):
        """
        :return:
        """
        self.driver.long_press("test_file")

    def action_on_folder_from_cloud_list(self, folder_name, delete, recover):
        """

        :return:
        """
        folder_list = self.driver.find_object("icloud_folder_list", multiple=True)
        for folder in folder_list:
            if folder_name.lower() in folder.get_attribute("name").lower():
                self.driver.swipe(swipe_object=folder)
                self.driver.long_press(folder)
                if delete:
                    self.select_show_more_item_arrow()
                    self.select_delete()
                    break
                if recover:
                    self.select_recover()

    def verify_edit_button_response(self):
        """

        :return:
        """
        self.select_edit()
        if self.driver.wait_for_object("done_btn", raise_e=False):
            logging.info("Failed, Edit button is responding")
            raise InvalidElementStateException

        else:
            logging.info("Passed")

    def handle_location_screen(self):
        """

        :return:
        """
        if self.driver.wait_for_object("locations_title", raise_e=False):
            pass
        else:
            self.select_cloud_screen_back_button()

    def verify_see_all_ui_elements(self):
        """
        :return:
        """
        try:
            self.driver.click("see_all_btn")
            logging.info("HP Smart AH Screen contains more number of files")
            self.verify_ui_elements_on_recent_documents_screen()
            self.select_back_btn_on_recent_document_screen()
        except NoSuchElementException:
            logging.info("HP Smart AH Screen not having enough files to enable See all button")

    def verify_hp_smart_choose_dest_screen_options(self):
        """

        :return:
        """
        self.verify_hp_smart_files_screen()
        self.verify_cancel()
        self.verify_create_folder_option()
        self.verify_move_option()

    def verify_x_button_on_files_screen(self):
        """
        :return:
        """
        self.driver.wait_for_object("remove_btn")

    def verify_facebook_account_deleted_popup(self):
        """
        :return:
        """
        self.driver.click("fb_delete_popup")

    def verify_my_photos_files_screen(self):
        """

        :return:
        """
        self.driver.wait_for_object("files_my_photos")



########################################################################################################################
#
#                                       Functionality related sets
#
########################################################################################################################

    def create_a_folder(self, folder_name="TestFolder"):
        """

        :return:
        """
        self.select_hp_smart_files_3dot_button()
        self.verify_more_options_door()
        self.select_hp_smart_files_create_folder_icon()
        self.verify_create_folder_popup()
        self.create_folder_by_passing_name(default_name=folder_name)
        self.verify_hp_smart_files_screen()

    def delete_a_folder_by_name(self, folder_name="TestFolder"):

        self.select_hp_smart_files_3dot_button()
        self.verify_more_options_door()
        self.select_hp_smart_files_select_option_from_list()
        self.verify_all_action_for_selected_files()
        self.verify_my_files_select_files_screen()
        self.verify_select_files_screen()
        self.select_cancel()
        self.verify_hp_smart_files_home_screen()
        self.enter_search_item_in_search_box(default_name=folder_name)
        self.select_dropdown_options_button()
        self.verify_menu_door_from_down()
        self.select_delete_for_file_deletion()
        self.verify_file_delete_confirmation_popup()
        self.select_delete()
        self.my_files_select_search_cancel(timeout=30)

    def move_folder_into_this_folder(self, starter_folder="New Folder", mover_folder="Fish Bowl"):

        self.create_a_folder(folder_name=starter_folder)
        self.enter_search_item_in_search_box(default_name=starter_folder)

        self.select_dropdown_options_button()

        self.verify_menu_door_from_down()
        self.select_move_folder_option()
        self.verify_my_files_with_choose_dest_text()
        self.verify_create_folder_option()
        self.verify_move_option()
        self.select_hp_smart_files_create_folder_icon()
        self.create_folder_for_move_options(default_name=mover_folder)
        self.select_move_from_navigation()
        self.select_done()
        self.my_files_select_search_cancel()
        self.verify_hp_smart_files_screen()
        self.enter_search_item_in_search_box(default_name=mover_folder)
        self.select_folder_from_list(name=mover_folder)
        #self.verify_select_files_screen()
        self.enter_search_item_in_search_box(default_name=starter_folder)
        self.select_folder_from_list(name=starter_folder)

    def rename_and_delete_folder_moved_folder(self):

        self.enter_search_item_in_search_box(default_name="TestFolderRename")
        self.select_dropdown_options_button()
        self.verify_menu_door_from_down()
        self.verify_ui_options_elements_menu_door_from_down()
        self.select_rename_folder_option()
        self.verify_rename_folder_popup()
        self.select_clear_text()
        self.create_folder_by_passing_name("MoveFunctionality")
        self.my_files_select_search_cancel()
        self.enter_search_item_in_search_box("MoveFunctionality")
        self.select_dropdown_options_button()
        self.select_delete_folder_option()
        self.verify_file_delete_confirmation_popup()
        self.select_delete()
        self.my_files_select_search_cancel()
        self.verify_hp_smart_files_home_screen()

    def select_and_verify_all_files(self):

        self.select_all_files_image()
        self.verify_hp_smart_recent_screen()
        self.select_close()
        self.verify_files_screen()

    def delete_cloud_account_by_name(self):

        self.select_edit()
        self.select_x_button_on_given_cloud()
        self.verify_cloud_remove_popup()
        self.select_remove_on_popup()

    def verify_ui_elements_of_file_and_photos_screen(self):
        """

        :return:
        """
        self.verify_files_screen()
        self.verify_Edit_button()
        self.verify_all_files_image()
        self.verify_files_my_photos_button()
        self.verify_drop_box_image()
        self.verify_google_drive_image()
        self.verify_box_image()
        self.verify_ever_note_image()
        self.driver.swipe(direction="down")
        self.verify_face_book_button()
        self.verify_instagram_image()

    def verify_ui_options_elements_menu_door_from_down(self):
        """
        :return:
        """
        self.verify_rename_option()
        self.verify_move_folder_option()
        self.verify_delete_folder_option()
        self.driver.wait_for_object("menu_options_cancel_btn")


    def select_and_verify_cloud_ui_elements(self):
        """

        :return:
        """
        self.select_icloud_button()
        self.verify_icloud_screen()
        self.verify_icloud_ui_elements_screen()
        self.enter_search_item_in_search_box(default_name="New file")
        self.select_folder_from_cloud_list("New file")


    def select_and_verify_google_drive(self):
        """

        :return:
        """
        self.verify_location_folder_screen()
        self.select_locations_folder_drive_btn()
        self.verify_drive_screen()
        self.enter_search_item_in_search_box(default_name="Test file")
        self.select_folder_from_cloud_list("Test file")

    def verify_file_name_exists(self, saved_file_name):

        self.driver.scroll("file_name", format_specifier=[saved_file_name], full_object=False, timeout=30, check_end=False)

    def delete_a_file(self, file_name, cancel_delete=False):
        """
        :param file_name: File name to search and delete
        :param cancel_delete: true to click cancel on the delete confirmation
        """
        self.enter_search_item_in_search_box(file_name)
        self.select_dropdown_options_button()
        self.verify_menu_door_from_down()
        self.select_delete_folder_option()
        self.verify_file_delete_confirmation_popup()
        if cancel_delete:
            self.driver.click("delete_popup_cancel_btn")
        else:
            self.select_delete()
            self.my_files_select_search_cancel()

    def delete_all_hp_smart_files(self):

        if not self.is_empty_screen():
            self.select_hp_smart_files_3dot_button()
            self.select_hp_smart_files_select_option_from_list()
            self.select_select_all_button()
            self.select_delete()
            self.verify_file_delete_confirmation_popup()
            self.select_delete()
        else:
            logging.info("HP Smart Files is empty")

    def select_a_file(self, saved_file_name, tries=3):
        for _ in range(tries):
            self.enter_search_item_in_search_box(saved_file_name)
            if self.driver.wait_for_object("file_name", format_specifier=[saved_file_name], raise_e=False) is not False:
                self.driver.click("file_name", format_specifier=[saved_file_name])
                break
            else:
                self.select_cancel()

    def get_file_size(self, file_name):
        """
        :param file_name: <string> name of the file
        :return: <int> size of the file in MBs
        """
        p = re.compile(r'(.*?) MB')
        self.enter_search_item_in_search_box(file_name)
        text = self.driver.wait_for_object("file_size", format_specifier=[file_name]).text
        return int(re.search(p, text).group(1).strip())

    def select_multiple_files(self, file_name_array):
        for file_name in file_name_array:
            if not self.verify_select_files_screen():
                self.select_hp_smart_files_3dot_button()
                self.select_hp_smart_files_select_option_from_list()
            self.driver.wait_for_object("file_name", format_specifier=["{}.jpg".format(file_name)]).click()

    def find_and_rename_file(self, file_name, search_result_name, cancel_rename=False, new_name="renamed"):
        self.enter_search_item_in_search_box(file_name)
        self.verify_static_text(search_result_name, raise_e=True)
        self.select_dropdown_options_button()
        self.verify_menu_door_from_down()
        self.select_rename_folder_option()
        self.verify_rename_folder_popup()
        if cancel_rename:
            self.driver.click("rename_popup_cancel_btn")
        else:
            self.select_clear_text()
            self.create_folder_by_passing_name(new_name)  

    def select_edit_options_cancel_btn(self):
        self.driver.click("menu_options_cancel_btn") 

    def select_save_to_my_iphone(self, raise_e=True):
        self.driver.click("save_to_iphone", raise_e=raise_e)

    def verify_on_my_iphone(self):
        self.driver.wait_for_object("on_my_iphone")