from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow

import time

class Preview(SmartFlow):
    flow_name = "preview"

    PRINT_BTN = "print_btn"
    SHARE_BTN = "share_btn"
    SMART_TASKS_BTN = "smart_task_btn"
    SAVE_BTN = "save_btn"
    FAX_BTN = "fax_btn"
    RESIZE_SMALL_BTN = "reduce_size_popup_small_btn"
    RESIZE_MEDIUM_BTN = "reduce_size_popup_medium_btn"
    RESIZE_ACTUAL_SIZE_BTN = "reduce_size_popup_actual_size_btn"
    SHARE_OPTION_TITLE = "share_option_title"
    SAVE_OPTION_TITLE = "save_option_title"
    EDIT_ADJUST = "edit_adjust_btn"
    EDIT_FILTER = "edit_filter_btn"
    EDIT_CROP = "edit_crop_btn"
    EDIT_TEXT = "edit_text_btn"
    FILE_SIZE_ACTUAL = "file_size_actual_size"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_SMALL = "file_size_small"
    PRINTING_SETTINGS_CB = "printing_settings_cb"
    PRINT_PLUGIN_CB = "print_plugin_cb"
    PRINTER_SELECT_CB = "printer_select_cb"
    OPEN_PRINT_SETTINGS = "open_print_settings"
    OPEN_GOOGLE_PLAY = "open_google_play"
    EDIT_BTN = "edit_btn"
    REPLACE_BTN = "replace_btn"
    DELETE_BTN = "delete_btn"
    PRINT_SIZE_4x6_TWO_SIDED = "print_size_4x6_two_sided_btn"
    PRINT_SIZE_4x6_STANDARD = "print_size_4x6_standard_btn"
    PRINT_SIZE_5x7 = "print_size_5x7_btn"
    PRINT_SIZE_5x5_SQUARE = "print_size_5x5_square_btn"
    PRINT_SIZE_4x12_PANORAMIC = "print_size_4x12_panoramic_btn"
    PRINT_SIZE_8_5x11_LETTER = "print_size_8_5x11_letter_btn"
    PRINT_SIZE_A4 = "print_size_a4_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def swipe_to_preview_image(self, direction):
        """
        Swipe to an preview image
        :param direction: "left" or "right"
        """
        self.driver.swipe("preview_files_sv", direction=direction)

    def swipe_to_preview_image_index(self, image_index, timeout=30):
        """
        Swipe to a preview image by index
        :param image_index: index of image starting at 1 - matches index on ui
        :param timeout: timeout in seconds
        """
        start_time = time.time()
        image_count = self.get_preview_image_count()
        if image_count < image_index < 1:
            raise IndexError("image_index = {} is out of range[1, {}]")
        current_page = self.get_current_preview_image_index()
        while current_page != image_index:
            if time.time() - start_time >= timeout:
                raise TimeoutError("Could not swipe to preview image {} in {} seconds".format(image_index, timeout))
            self.swipe_to_preview_image("left" if current_page > image_index else "right")
            current_page = self.get_current_preview_image_index()

    def get_preview_image_count(self):
        return int(self.driver.wait_for_object("img_number_txt").text.split("/")[1])

    def get_current_preview_image_index(self):
        """Indexed at 1"""
        return int(self.driver.wait_for_object("img_number_txt").text.split("/")[0])
        
    def select_add(self):
        """
        Click on Add icon button

        End of flow: Scan or Document Capture screen

        Device: phone
        """
        self.driver.click("add_btn")

    def select_bottom_nav_btn(self, btn):
        """
        Click on a bottom navigation btn
        :param btn: use class constant
                    PRINT_BTN
                    SHARE_BTN
                    SMART_TASKS_BTN
                    SAVE_BTN
                    HP_ROAM_BTN
                    FAX_BTN
        """
        self.verify_bottom_nav_btn(btn, invisible=False)
        self.driver.click(btn)

    def select_next(self):
        """
        It is displayed when adding file to Compose Fax screen
        Click on Next button
        """
        self.driver.wait_for_object("next_btn", timeout=5)
        self.driver.click("next_btn")

    def reduce_file_size(self, size_opt):
        """
        Click on any reduced size button on 'File size Reduction' popup
        :param size_opt: option for reducing to a size. Use class constant variable
                    RESIZE_SMALL_BTN
                    RESIZE_MEDIUM_BTN
                    RESIZE_ACTUAL_SIZE_BTN
        :return:
        """
        self.driver.click(size_opt)

    def screenshot_img_preview(self, file_path=None):
        """
        Screenshots the currently selected preview image
        :param file_path: Path to save screenshot, if None image returned as Base64
        """
        self.driver.wait_for_object("preview_files_sv")
        return self.driver.screenshot_element("preview_files_sv", file_path=file_path)

    # -------------------           Edit / Replace / Delete buttons      ------------------------------------
    def select_preview_image_opts_btn(self, btn_name, image_index=1):
        """
        Click on Edit or Replace or Delete button on preview image based on index image
        :param image_index: index of preview image. Should be in range [1, total_page]
        :param btn_name: 
            - EDIT_BTN
            - REPLACE_BTN
            - DELETE_BTN
        """
        total_pages = int(self.driver.find_object("img_number_txt").text.split("/")[1])
        if image_index < 0 or image_index > total_pages:
            raise IndexError("image_index = {} is out of range[1, {}]".format(image_index, total_pages))
        for _ in range(abs(total_pages - image_index)):
            current_page = int(self.driver.find_object("img_number_txt").text.split("/")[0])
            if current_page == image_index:
                break
            else:
                self.swipe_to_preview_image("left" if image_index < current_page else "right")
        self.driver.click("page_options_btn", index=-1)  # click on  Page options "..." button of middle preview image
        self.driver.wait_for_object("option_icon")
        self.driver.click(btn_name) # Click on Edit or Delete or Replace button

    # -------------------           MORE OPTION      ------------------------------------
    def select_more_option(self):
        """
        Click on More Option icon button

        End of flow: More Option menu display on Preview
        """
        layout = self.driver.find_object("nav_btns_layout")
        btns = self.driver.find_object("more_opt_btn", multiple=True, root_obj=layout)
        btns[len(btns) - 1].click()

    def select_option_print_help(self):
        """
        Select option of Print Help in More options
        """
        self.select_more_option()
        self.driver.wait_for_object("opt_print_help")
        self.driver.click("opt_print_help")

    def toggle_cb_on_print_help(self, cb_name, uncheck=False):
        """
        Toggle the check box on print help screen:
          + Printing settings cb
          + print plugin cb
          + printer select cb
        :param cb_name: class constant variable:
          + PRINTING_SETTINGS_CB
          + PRINT_PLUGIN_CB
          + PRINTER_SELECT_CB
        :param uncheck: True - uncheck, False - check
        """
        self.driver.check_box(cb_name, uncheck=uncheck)

    def select_link_on_print_help(self, link_name):
        """
        Click on OPen Printing settings link on Print Help screen
        """
        self.driver.click(link_name, change_check={"wait_obj": link_name, "invisible": True})

    def select_print_help_ok_btn(self):
        """
        Check on OK button on Print Help screen
        """
        self.driver.click("print_help_ok_btn")

    def select_leave_confirm_popup_leave(self, number_of_items_deleted=None):
        """
        Click on LEAVE button from the 'Are you sure' popup

        End of flow: Scan screen
        """
        if number_of_items_deleted:
            self.driver.ga_container.insert_ga_key("Number-of-items-deleted", number_of_items_deleted)
        self.driver.click("are_you_sure_popup_leave_btn")

    def select_leave_confirm_popup_cancel(self):
        """
        Click on Cancel button from the 'Are you sure' popup

        End of flow: Preview
        """
        self.driver.click("are_you_sure_popup_cancel_btn")

    def select_option_print_format(self):
        """
        Select option of Print Help in More options
        """
        self.select_more_option()
        self.driver.wait_for_object("print_format")
        self.driver.click("print_format")

    def select_print_as_pdf_btn(self):
        """
        Click on Print as PDF on Print Format screen
        :param is_pdf:
        """
        self.driver.click("print_as_pdf")

    def select_print_as_jpg_btn(self):
        """
        Click on Print as JPG on Print Format screen
        :param is_pdf:
        """
        self.driver.click("print_as_jpg")

    # -------------------           ACTION OPTION (SAVE & SHARE)        -------------------
    def select_file_type_spinner_btn(self):
        """
        Click on File type on Save Option or Share Option screen
        :param is_pdf:
        """
        self.driver.click("option_screen_file_type_spinner_btn", change_check={"wait_obj": "option_screen_file_type_spinner_btn", "invisible": True})

    def select_format_type(self, is_pdf=True):
        """
        Select format type on Save Option or Share Option screen
        :param is_pdf:
        """
        opt_btn = "option_screen_pdf_btn" if is_pdf else "option_screen_jpg_btn"
        self.driver.click(opt_btn, change_check={"wait_obj": "option_screen_file_type_spinner_btn", "invisible": False})

    def rename_file_name(self, file_name):
        """
        Click on file name field for rename
        :param file_name:
        """
        self.driver.send_keys("option_screen_file_name_tf", file_name)

    def make_action_option(self, file_name=None, is_pdf=True):
        """
        Rename to file name if it has value
        Toggle pdf based on is_pdf
        Click on Action button
        :param file_name:
        :param is_pdf: True -> PDF button. False -> JPG button
        """
        if file_name:
            self.rename_file_name(file_name)
        self.select_file_type_spinner_btn()
        self.select_format_type(is_pdf=is_pdf)
        self.driver.scroll("option_screen_action_btn", timeout=10, check_end=False)
        self.driver.click("option_screen_action_btn",change_check={"wait_obj": "option_screen_action_btn", "invisible": True})

    def dismiss_saved_files_message_popup(self):
        """
        Dismiss it if it displays. Usually, it display when this function is used at first time
        """
        if self.driver.wait_for_object("option_screen_saved_file_message_popup", timeout=10, raise_e=False):
            self.driver.click("option_screen_saved_file_message_popup_ok_btn", change_check={"wait_obj": "option_screen_saved_file_message_popup_ok_btn", "invisible": True})

    def select_file_size(self, file_size):
        """
        Select file size on File Size screen:
        :param file_size: using class constant
            FILE_SIZE_ACTUAL
            FILE_SIZE_MEDIUM
            FILE_SMALL
        :return:
        """
        file_size_item = self.driver.return_str_id_value(file_size)
        self.driver.wait_for_object("file_size_spinner")
        self.driver.click("file_size_spinner")
        self.driver.click("file_size_list", format_specifier=[file_size_item[:file_size_item.find("(%s)")]])

    # -------------------           PRINT SIZE       ------------------------------------
    def select_print_size_btn(self, size_btn):
        """
        Click on button on Print Size screen
        Note: This screen is just for Novelli printer.
        :param size_btn: using following class constant.
                    PRINT_SIZE_4x6_TWO_SIDED    
                    PRINT_SIZE_4x6_STANDARD     
                    PRINT_SIZE_5x7  
                    PRINT_SIZE_5x5_SQUARE   
                    PRINT_SIZE_4x12_PANORAMIC 
                    PRINT_SIZE_8_5x11_LETTER    
                    PRINT_SIZE_A4   
        """
        self.driver.click(size_btn)

    def screenshot_img_preview(self, file_path=None):
        """
        Screenshots the currently selected preview image
        :param file_path: Path to save screenshot, if None image returned as Base64
        """
        self.driver.wait_for_object("preview_files_sv")
        return self.driver.screenshot_element("preview_files_sv", file_path=file_path)

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_preview_nav(self, is_edit = True):
        """
        Verify Scan navigation bar:
            - Preview title
            - Back button
            - Edit button
            - More Option
        :param: is_edit: visible Edit icon button or not.
        """
        self.driver.wait_for_object("title", timeout=30)
        self.driver.wait_for_object("_share_back_btn", timeout=10)
        self.driver.wait_for_object("page_options_btn", invisible= not is_edit)

    def verify_bottom_nav_btn(self, btn, invisible=False):
        """
        Verify invisible/visible of bottom navigation button
        :param btn: use class constant
                    PRINT_BTN
                    SHARE_BTN
                    SMART_TASKS_BTN
                    SAVE_BTN
                    FAX_BTN
        :param invisible: invisible/visible
        """
        if not self.driver.wait_for_object(btn, invisible=invisible, timeout=20, raise_e=False):
            self.driver.swipe("bottom_nav_sv", direction="right")
            self.driver.wait_for_object(btn, invisible=invisible, timeout=20)

    def verify_add_more_btn(self, invisible=False):
        """
        Verify the add more page button on  Preview
        :param invisible: verify if visibility or invisibility
               - True: is invisibility
               - False: is visibility
        """
        self.driver.wait_for_object("add_btn", invisible=invisible, timeout=10)

    def verify_multiple_pages(self, total_pages):
        """
        Verify multiple pages via total_pages:
            - Total number page on screen match with total_pages or not

        :param total_pages: number of pages
        :type total_pages: str
        """
        actual_total_pages = self.driver.find_object("img_number_txt").text.split("/")[1]
        if actual_total_pages != total_pages:
            raise NoSuchElementException("\nExpected total pages: {}\n"
                                         "Actual total pages: {}".format(total_pages,
                                                                         actual_total_pages))

    def verify_more_option(self, print_format_invisible=False):
        """
        Verify more option screen
        """
        self.driver.wait_for_object("opt_print_help")
        self.driver.wait_for_object("print_format", invisible=print_format_invisible)

    def verify_print_help_screen(self):
        """
        Verify the Capture Scan Screen for Full screen button and Done button
            - title
            - 2 links
        :return:
        """
        self.driver.wait_for_object("print_help_title")
        self.driver.wait_for_object("open_google_play")
        self.driver.wait_for_object("open_print_settings")

    def verify_ok_button(self, is_enabled=False):
        """
        Check if OK button is enabled or not
        :param is_enabled:
        """
        self.driver.wait_for_object("print_help_ok_btn")
        ok_btn = self.driver.find_object("print_help_ok_btn")
        if is_enabled != (ok_btn.get_attribute("enabled").lower() == "true"):
            raise AssertionError("OK button doesn't enable correctly")

    def verify_edit_screen(self):
        """
        Verify currently screen is edit screen with below items:
             - title
             - Done button
             - Cancel button
        """
        self.driver.wait_for_object("edit_title")
        self.driver.wait_for_object("edit_done_btn")
        self.driver.wait_for_object("edit_cancel_btn")

    def verify_leave_confirmation_popup(self):
        """
        Verify current screen is 'Are you sure' screen via:
            - Leave button
            - Cancel button
            - Leave button
        """
        self.driver.wait_for_object("are_you_sure_popup_title")
        self.driver.wait_for_object("are_you_sure_popup_leave_btn")
        self.driver.wait_for_object("are_you_sure_popup_cancel_btn")

    def verify_file_size_reduction_popup(self):
        """
        Verify 'File Size Reduction' popup
            - Title
            - 2 buttons
        """
        self.driver.wait_for_object("reduce_size_popup_title")
        self.driver.wait_for_object("reduce_size_popup_small_btn")
        self.driver.wait_for_object("reduce_size_popup_medium_btn")
        self.driver.wait_for_object("reduce_size_popup_actual_size_btn")

    def verify_option_screen(self, option_title, invisible=False):
        """
        Verify Option screen
        :param option_title: Share/Save Option. Using class constant:
                SHARE_OPTION_TITLE
                SAVE_OPTION_TITLE
        """
        self.driver.wait_for_object(option_title, timeout=10, invisible=invisible)
        if not invisible:
            action_btn = {self.SAVE_OPTION_TITLE: self.SAVE_BTN,
                          self.SHARE_OPTION_TITLE: self.SHARE_BTN}
            self.driver.scroll("option_screen_action_btn",
                           format_specifier=[self.driver.return_str_id_value(action_btn[option_title])],
                           timeout=10, check_end=False)

    def verify_softfax_limit_popup(self, is_size=True):
        """
        Verify visible limit popup for Softfax
        :param is_size: relate to limited size -> True. To limited pages -> False
        """
        if is_size:
            self.driver.wait_for_object("softfax_limit_msg",
                                        format_specifier=[self.get_text_from_str_id("softfax_size_limit_txt").replace("%1$s", "20")],
                                        timeout=30)
        else:
            self.driver.wait_for_object("softfax_limit_msg",
                                        format_specifier=[self.get_text_from_str_id("softfax_page_limit_txt").replace("%1$s", "50")],
                                        timeout=30)

    def verify_reorder_btn(self):
        """
        Verify Reorder button on Preview screen
        """
        self.driver.wait_for_object("reorder_btn")

    def verify_file_size_item(self, file_size):
        """
        Verify File Size on Share Option screen
        :param file_size
        """
        file_size_item = self.driver.return_str_id_value(file_size)
        self.driver.wait_for_object("file_size_list", format_specifier=[file_size_item[:file_size_item.find("(%s)")]])

    def verify_document_size_item(self, invisible=False):
        """
        Verify Document size item on Save Option screen
        :param invisible
        """
        self.driver.wait_for_object("document_size", invisible=invisible)
        self.driver.wait_for_object("document_size_spinner", invisible=invisible)

    def verify_print_format_screen(self):
        """
        Verify Print format screen with:
          + title
          + format type
        """
        self.driver.wait_for_object("print_format")
        self.driver.wait_for_object("print_as_jpg")
        self.driver.wait_for_object("print_as_pdf")

    def verify_print_size_screen(self, raise_e=True):
        """
        Verify current screen is Print Size
        Note: This screen is just for Novelli printer.
        """
        self.driver.wait_for_object("print_size_txt", raise_e=raise_e)
