import logging
import time

from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re


class InvalidElementNameException(Exception):
    pass


class Preview(SmartFlow):
    flow_name = "preview"

    # top header bar
    BACK_BUTTON = "_shared_back_arrow_btn"
    CANCEL_BUTTON = "_shared_cancel"
    DONE_BUTTON = "_shared_done"
    PREVIEW_TITLE = "preview_txt"
    PRINT_PREVIEW_TITLE = "print_preview"
    SHARE_AND_SAVE_TEXT = "share_save_text"
    SMART_TASKS_PREVIEW_TITLE = "smart_tasks_preview"
    SAVE_PREVIEW_TITLE = "save_preview"
    REORDER_BUTTON = "reorder_btn"
    FAX_PREVIEW_TITLE = "fax_preview"
    CONTINUE_TO_FAX_BTN = "continue_to_fax_btn"

    # middle
    EDIT_BUTTON = "edit_btn"
    ADD_PAGE_BUTTON = "add_page_btn"
    PAPER_SIZE_INFO = "paper_size_info"
    PREVIEW_IMAGE = "image_of_preview"
    PRINTER_NAME = "printer_name"
    PDF_BUTTON = "_const_file_type_pdf"
    JPG_BUTTON = "_const_file_type_jpg"
    FILE_NAME_FIELD = "file_name_textfield"
    FILE_SIZE_SMALL = "file_size_small"
    FILE_SIZE_ACTUAL = "file_size_actual"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_LARGE = "file_size_large"

    # bottom navigation bar
    PRINT = "print_text"
    SMART_TASKS = "smart_tasks_text"
    SHARE_AND_SAVE_BTN = "share_save_text"
    FAX = "fax_text"

    SMART_TASKS_SIGN_IN = "smart_tasks_sign_in_link"

    # action success popup
    GREEN_CHECK_ICON = "print_completed_icon"
    CONTINUE_BUTTON = "continue_btn"
    HOME_BUTTON = "home_btn"

    # dynamic locators
    DYNAMIC_PREVIEW_BUTTON = "_shared_dynamic_button"
    DYNAMIC_PREVIEW_TOOLBAR = "dynamic_toolbar_icons"

    # Share Screen
    FILE_NAME_TITLE = "file_name_title"
    FILE_SETTINGS_TITLE = "file_settings_title"
    # TODO: FORMAT string refactoring in next sprint
    FORMAT = "file_type"
    FILE_SIZE = "file_size"
    SHARE_SETTINGS_TIP = "share_settings_tip"
    FILE_SIZE_ACTUAL = "file_size_actual"
    FILE_SIZE_MEDIUM = "file_size_medium"
    FILE_SIZE_LARGE = "file_size_large"
    FILE_SIZE_SMALL = "file_size_small"
    SHARE_SAVE_BTN = "share_save_text"

    # Print Screen
    RE_PRINT_BTN = 're_print_btn'
    TRANSFORM_TXT = "transform_txt"
    YES_BTN = "yes_btn"
    NO_BTN = "no_btn"
    CANCEL_JOB_POP_UP_TITLE = "print_job_cancel_pop_up_title"
    CANCEL_JOB_POP_DES = "print_job_cancel_pop_up_txt"

    # Transform Screen
    TF_RESIZE_TXT = "resize_and_move_btn_txt"
    TF_ROTATE_TXT = "rotate_btn_txt"
    TF_COLLECTION_VIEW = "transform_collection_view"

    # print settings screen
    PRINT_SETTING_OPTIONS = "print_setting_options"
    PRINT_COPY = "print_copy_txt"
    COPIES_MINUS_BTN = "copies_minus_btn"
    COPIES_PLUS_BTN = "copies_plus_btn"
    PAPER = "paper_txt"
    COLOR_OPTION = "color_option_txt"
    PAGE_RANGE = "page_range_txt"
    PRINT_QUALITY = "print_quality_txt"
    TWO_SIDED = "two_sided_txt"
    PR_SCREEN_OPTIONS_UI = "page_range_options"
    PR_PAGE_SELECT_IMG = "page_selected_image"

    DELETE_PAGE_ICON = "delete_page_icon"
    REPLACE_BTN = "replace_btn"
    DELETE_BTN = "delete_btn"

    PREVIEW_TOOLBAR_ICONS = [
        PRINT,
        SHARE_AND_SAVE_TEXT,
        SMART_TASKS,
        FAX
    ]

    PREVIEW_BUTTON_NAMES = [
        PRINT,
        SHARE_AND_SAVE_BTN,
        SMART_TASKS,
        FAX,
        ADD_PAGE_BUTTON,
    ]

    ACTION_SUCCESS_POPUP_ELEMENTS = [
        GREEN_CHECK_ICON,
        CONTINUE_BUTTON,
        HOME_BUTTON
    ]

    PRINT_PREVIEW_UI_ELEMENTS = [
        BACK_BUTTON,
        PRINT_PREVIEW_TITLE,
        PREVIEW_IMAGE,
        TRANSFORM_TXT,
        PRINTER_NAME,
        PRINT
    ]

    PREVIEW_UI_ELEMENTS = [
        BACK_BUTTON,
        PREVIEW_TITLE,
        PREVIEW_IMAGE,
        SHARE_AND_SAVE_TEXT,
        SMART_TASKS,
        REORDER_BUTTON
    ]

    SHARE_PREVIEW_UI_ELEMENTS = [
        SHARE_AND_SAVE_TEXT,
        BACK_BUTTON,
        FILE_NAME_FIELD,
        FILE_NAME_TITLE,
        FILE_SETTINGS_TITLE,
        FORMAT,
        FILE_SIZE,
        SHARE_SETTINGS_TIP,
        SHARE_AND_SAVE_BTN
    ]

    SMART_TASKS_PREVIEW_UI_ELEMENTS = [
        SMART_TASKS_PREVIEW_TITLE,
        SMART_TASKS_SIGN_IN
    ]

    SAVE_PREVIEW_UI_ELEMENTS = [
        ADD_PAGE_BUTTON,
        PREVIEW_IMAGE,
        FILE_NAME_FIELD,
        SAVE_PREVIEW_TITLE
    ]

    PRINT_SETTINGS_UI_ELEMENTS = [
        PRINT_COPY,
        COPIES_MINUS_BTN,
        COPIES_PLUS_BTN,
        PAPER,
        COLOR_OPTION,
        PAGE_RANGE,
        PRINT_QUALITY,
        TWO_SIDED,
        PRINT
    ]

    CANCEL_JOB_ELEMENTS = [
        CANCEL_JOB_POP_UP_TITLE,
        CANCEL_JOB_POP_DES,
        YES_BTN,
        NO_BTN
    ]

    TRANSFORM_SCREEN_UI_ELEMENTS = [
        TF_RESIZE_TXT,
        TF_ROTATE_TXT
    ]

    PREVIEW_EDIT_OPTIONS = [
        EDIT_BUTTON,
        REPLACE_BTN,
        DELETE_BTN
    ]

    # File Reduction
    FILE_REDUCTION_POPUP = "reduce_size_popup"
    FILE_REDUCTION_ACTUAL_SIZE = "_const_save_actual_size"
    FILE_REDUCTION_MEDIUM_SIZE = "_const_save_medium_size"
    FILE_REDUCTION_SMALL_SIZE = "_const_save_small_size"

    # FILE_REDUCTION_MESSAGE = "file_reduction_msg"
    # FILE_REDUCTION_TIP = "file_reduction_tip"

    # Print Setting Options
    COLOR_OPTIONS = ["Color", "Black Only", "Grayscale"]
    PAGE_RANGE_OPTIONS = ["1", "2", "Pages 1-2", "Select All", "Deselect All", "Manual Input", "Page Range"]
    PRINT_QUALITY_OPTIONS = ["Draft", "Normal", "Best"]
    TWO_SIDED_OPTIONS = ["Off", "Short Edge", "Long Edge"]

    # Transform screent options
    TF_RESIZE_MOVE_OPTIONS = ["Manual", "Original Size", "Fit to Page", "Fill Page"]
    TF_ROTATE_OPTIONS = ['Left', 'Right', 'Flip H', 'Flip V']

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Preview Screen
    #                                                                                                                      #
    ########################################################################################################################

    def get_no_pages_from_preview_label(self, get_current_page=False):
        if self.driver.wait_for_object("preview_page_no_label", raise_e=False) is not False:
            page_count_label = str(self.driver.get_attribute("preview_page_no_label", attribute="label"))
            page_count_label = page_count_label.split()
            page_count = int(page_count_label[2])
            current_page = int(page_count_label[0])
            if get_current_page:
                return (page_count, current_page)
        else:
            page_count = 1
        return page_count

    def verify_preview_navigate_back_popup(self):
        """
        this popup will return to home screen or scanner screen
        """
        self.driver.wait_for_object("preview_exit_popup", timeout=10)
        self.driver.wait_for_object("yes_new_scan_btn")
        self.driver.wait_for_object("yes_go_home_btn")
        self.driver.wait_for_object("no_add_img_btn")
        self.driver.wait_for_object("cancel_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Print Preview
    #                                                                                                                      #
    ########################################################################################################################

    # Print job completion varies on printer and hence need extended timeout to validate
    def verify_job_sent_and_reprint_buttons_on_print_preview(self, timeout=60):
        self.dismiss_feedback_pop_up()
        self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False)
        self.verify_re_print_btn(timeout=timeout)

    def go_to_print_preview_pan_view(self, pan_view=True):
        """
        Click on pan view to expand or close Print settings screen
        """
        self.verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.select_toolbar_icon(Preview.PRINT)
        self.verify_preview_screen_title(Preview.PRINT_PREVIEW_TITLE)
        self.dismiss_print_preview_coach_mark()
        if pan_view:
            self.driver.click("print_preview_pan_view",
                              change_check={"wait_obj": "preview_navigation_bar_title_text", "invisible": True,
                                            "format_specifier": ["Print Preview"]}, timeout=5)

    def get_print_setting_selected_value(self, print_option):
        return self.driver.wait_for_object("print_option_selected_value",
                                           format_specifier=[print_option]).get_attribute("name")

    def verify_printer_name_displayed(self, printer_name):
        return self.driver.wait_for_object(self.PRINTER_NAME, format_specifier=[printer_name],
                                           raise_e=False) is not False

    def change_print_copies(self, copies_btn, no_of_copies=1):
        for _ in range(no_of_copies):
            self.driver.click(copies_btn)

    def get_copies_btn_enabled_status(self, copies_btn):
        return self.driver.get_attribute(copies_btn, "enabled")

    def get_no_of_copies(self):
        if self.driver.wait_for_object("print_multiple_copies_txt", raise_e=False) is not False:
            copies_label = self.driver.get_attribute("print_multiple_copies_txt", attribute="label")
            copies_label = copies_label.split()
            count = list(copies_label[1])
            copies_count = int(count[1])
        else:
            copies_count = 1
        return copies_count

    # Longer wait times is to accommodate printing progress verification
    def verify_printing_status_btn_changes(self, multi_print=False, timeout=60):
        if multi_print:
            self.driver.wait_for_object("multi_page_printing_txt", timeout=10)
        else:
            self.driver.wait_for_object("printing_btn_txt", raise_e=False)
        self.driver.wait_for_object("printing_msg_txt", raise_e=False)
        self.driver.wait_for_object("cancel_btn", raise_e=False)
        self.driver.wait_for_object("print_job_sent_btn", raise_e=False, timeout=30)
        self.verify_re_print_btn(timeout=timeout)

    def verify_re_print_btn(self, timeout=60):
        timeout = time.time() + timeout
        while time.time() < timeout:
            self.dismiss_feedback_pop_up()
            if self.driver.wait_for_object("re_print_btn", raise_e=False) is not False:
                logging.info("Re-Print button displayed")
                break
            else:
                time.sleep(5)
        return self.driver.wait_for_object("re_print_btn", timeout=3)

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Share / Save screen
    #                                                                                                                      #
    ########################################################################################################################

    def rename_file(self, file_name):
        # type: (str) -> None
        """
        clears the file text field and inputs a new string in the text field
        :param file_name: string of the new file name
        :return:
        """
        self.driver.wait_for_object(self.FILE_NAME_FIELD).click()
        self.select_rename_value_to_change(re_name=file_name, press_enter=True)

    def select_file_type(self, file_type):
        """
         Click Format option and select file_type
        """
        self.driver.wait_for_object(self.FORMAT).click()
        self.driver.wait_for_object("_shared_dynamic_navigation_bar",
                                    format_specifier=[self.get_text_from_str_id(self.FORMAT)])
        if self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[file_type],
                                       raise_e=False) is not False:
            self.driver.click("_shared_dynamic_text", format_specifier=[file_type])
            return True
        else:
            return False

    def select_file_size(self, file_size):
        self.driver.click(file_size)

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Action Flows
    #                                                                                                                      #
    ########################################################################################################################

    def save_scan_result(self, file_name=""):
        """
        Save the scan result
        End of flow: Preview screen
        Device: Phone
        """
        self.select_file_name()
        if file_name != "":
            self.driver.send_keys(self.FILE_NAME_FIELD, file_name)
        self.driver.click("rename_btn")

    # FIXME: use select_button()
    def select_preview_back(self):
        """
        Click on Back button on Preview screen
        End of flow: Home screen
        Device: Phone
        """
        self.driver.click("back_btn")

    def select_file_name_on_preview_screen(self):
        """
        Click on File name on Preview screen
        End of flow: Scan screen
        Device: Phone
        """
        self.driver.click("file_name_textfield")

    def select_rename_value_to_change(self, re_name="New_rename_file", press_enter=False):
        """

        :param re_name:
        :return:
        """
        self.driver.click("clear_text_btn")
        if re_name != "":
            self.driver.send_keys(self.FILE_NAME_FIELD, re_name, press_enter=press_enter)

    def select_rename_button(self):
        """
        :return:
        """
        self.driver.click("rename_btn")

    def select_delete_pages_in_current_job(self, no_of_pages_to_delete=2):
        """
        Click on "X" icon on Preview screen
        End of flow: Scan screen
        Device: Phone
        """
        try:
            for page in range(1, no_of_pages_to_delete):
                self.driver.click("delete_page_icon")
                self.driver.click("delete_btn")
        except TimeoutException:
            logging.info("we don't have {} many pages to delete on preview screen:".format(no_of_pages_to_delete))
            ga_dynamic_key_value = no_of_pages_to_delete
            self.driver.ga_container.insert_ga_key("deleted_pages_in_scan_dynamic_key", ga_dynamic_key_value)

    def select_delete_page_icon(self):
        self.driver.click("delete_page_icon")

    def select_file_converting_format(self, file_type):
        self.driver.click(file_type)
        current_file_format = self.driver.find_object(file_type).get_attribute("value")

        ga_dynamic_key_value = current_file_format
        self.driver.ga_container.insert_ga_key("file_format_on_preview_dynamic_key", ga_dynamic_key_value)

    def select_save_to_hp_smart_btn(self):
        """

        :return:
        """
        self.driver.wait_for_object("save_hp_smart_btn")
        self.driver.click("save_hp_smart_btn")

    def select_file_rename_cancel(self):
        """
        :return:
        """
        self.driver.click("rename_cancel_btn")

    def select_file_rename_save_btn(self):
        """
        Click on Save button on Scan result

        End of flow: Scan Result screen with Save As popup

        Device: Phone
        """
        self.driver.click("save_btn")

    def select_print_btn(self):

        self.driver.click(self.PRINT)

    def select_send_btn(self):
        """
        :return:
        """
        self.driver.click("send_btn")

    ########################################################################################################################
    #                                                                                                                      #
    #                                               Verification Flows                                                     #
    #                                                                                                                      #
    ########################################################################################################################

    def verify_rename_popup(self):
        """
        Verify Rename popup screen
        :return:
        """
        self.driver.wait_for_object("rename_title")

    def verify_preview_screen(self, raise_e=True):
        """
        Verify Preview screen with the following elements:
              - Preview title
        """
        self.dismiss_feedback_pop_up()
        return self.driver.wait_for_object(self.PREVIEW_TITLE, timeout=120, interval=5, raise_e=raise_e)

    def verify_preview_share_screen(self):
        """
        :return:
        """
        self.driver.wait_for_object("preview_share_screen")

    def verify_print_preview_collection_view(self):
        """
        verifies the image on the preview screen
        :return:
        """
        self.driver.wait_for_object(self.PREVIEW_IMAGE)

    def verify_delete_page_x_icon(self):
        """
        :return: True if x button is present else False
        """
        return self.driver.find_object("delete_page_icon", multiple=True, raise_e=False)

    def verify_delete_button(self):
        self.driver.click("delete_page_icon")
        delete_button = self.driver.wait_for_object("delete_btn", raise_e=False)
        self.driver.click_by_coordinates(area='bl')
        return delete_button

    def verify_file_type_selected(self, option, raise_e=False):
        """
        :return:
        """
        return self.driver.wait_for_object("file_format_type", format_specifier=[option],
                                           raise_e=raise_e) is not False

    def verify_preview_screen_title(self, title):
        """
        :param title: preview title name
        """
        self.dismiss_feedback_pop_up()
        return self.driver.wait_for_object("preview_navigation_bar_title_text",
                                           format_specifier=[self.get_text_from_str_id(title)], timeout=10,
                                           raise_e=False)

    def handle_share_preview_screen(self):
        """
        :return:
        """
        if self.driver.wait_for_object(self.SHARE_AND_SAVE_TEXT, raise_e=False):
            pass
        else:
            self.driver.click("share_btn")

    def select_back_to_exit_with_out_saving(self):

        self.select_navigate_back()
        self.verify_exit_with_out_saving_popup_options()
        self.select_cancel()

    def rename_scanned_file(self, choose_name="New_rename_for_file"):

        self.select_file_name_on_preview_screen()
        self.select_rename_value_to_change(re_name=choose_name)

    # ----------------------------- VERIFICATION FLOWS ----------------------------------------------
    def verify_toolbar_icons(self):
        """
        verifies the icons at the bottom of the preview screen:
            Print
            Share/Save
            Smart Tasks
        :return:
        """
        for i in self.PREVIEW_TOOLBAR_ICONS:
            self.driver.wait_for_object(i)

    def verify_print_preview_ui_elements(self, printer_name):
        self.dismiss_print_preview_coach_mark()
        for element in self.PRINT_PREVIEW_UI_ELEMENTS:
            if element == self.PRINTER_NAME:
                option_displayed = self.driver.wait_for_object(element, format_specifier=[printer_name],
                                                               raise_e=False) is not False
            else:
                option_displayed = self.driver.wait_for_object(element, raise_e=False) is not False
            if not option_displayed:
                raise Exception(element + " - not displayed/not applicable")

    def go_home_from_preview_screen(self):
        """
        Go back to home from preview screen
        :return:
        """
        self.dismiss_feedback_pop_up()
        self.driver.click("_shared_back_arrow_btn", change_check={"wait_obj": "preview_exit_popup"}, timeout=10)
        self.verify_preview_navigate_back_popup()
        self.driver.click("yes_go_home_btn")

    def verify_exit_with_out_saving_popup_options(self):
        """
        :return:
        """
        self.driver.wait_for_object("preview_exit_popup")
        self.driver.wait_for_object("yes_go_home_btn")
        self.driver.wait_for_object("yes_new_scan_btn")
        self.driver.wait_for_object("no_add_img_btn")
        self.driver.wait_for_object("cancel_btn")

    def verify_preview_edit_options(self):
        self.driver.wait_for_object("edit_btn")
        self.driver.wait_for_object("replace_btn")

    # ----------------------------- ACTION FLOWS ----------------------------------------------
    def select_save(self):
        """
        Save Button on the save preview tab
        """
        self.driver.wait_for_object(self.DYNAMIC_BUTTON, format_specifier=[self.get_text_from_str_id(self.SAVE)],
                                    timeout=5)
        self.driver.click(self.DYNAMIC_BUTTON, format_specifier=[self.get_text_from_str_id(self.SAVE)])

    def select_toolbar_icon(self, icon):
        """
        Click on bottom navigation icon (XCUIElementTypeStaticText)
        :param icon: name attribute of the element
        :return:
        """
        self.dismiss_feedback_pop_up()
        self.driver.click(icon)

    def select_button(self, button):
        """
        Click on a XCUIElementTypeButton on the page
        :param button: name attribute of the element
        :return:
        """
        if button not in self.PREVIEW_BUTTON_NAMES:
            raise InvalidElementNameException("Object: " + button + " not a valid button name")
        self.driver.wait_for_object(self.DYNAMIC_PREVIEW_BUTTON, format_specifier=[self.get_text_from_str_id(button)],
                                    timeout=15).click()
        # self.driver.click(self.DYNAMIC_PREVIEW_BUTTON, format_specifier=[self.get_text_from_str_id(button)])

    def select_add_page(self):
        """
        Click on Add Page icon button on Preview screen
        """
        self.driver.wait_for_object(self.ADD_PAGE_BUTTON, timeout=15).click()

    def select_edit(self):
        """
        Click on Edit button
        """
        self.dismiss_feedback_pop_up()
        if self.driver.wait_for_object(self.EDIT_BUTTON, raise_e=False) is not False:
            self.driver.click(self.EDIT_BUTTON)
        else:
            self.select_preview_image()

    def select_home_button(self):
        """
        Click on Home button
        """
        self.driver.wait_for_object(self.HOME_BUTTON, timeout=10).click()

    def select_yes_btn(self):
        """
        :return:
        """
        self.driver.click("yes_btn", timeout=5)

    def select_yes_go_home_btn(self):
        self.driver.click("yes_go_home_btn")

    def select_preview_image(self):
        self.driver.wait_for_object(self.PREVIEW_IMAGE, timeout=5)
        self.driver.click(self.PREVIEW_IMAGE)

    def zoom_preview_image(self):
        self.driver.wait_for_object(self.PREVIEW_IMAGE)
        self.driver.pinch(pinch_obj=self.PREVIEW_IMAGE, move_in=False)

    def verify_zoomed_mode(self):
        self.driver.wait_for_object("zoomed_mode")

    # ------------------- File Reduction Popup --------------------------------------

    def verify_file_reduction_popup(self):
        names = [attr for attr in dir(Preview) if attr.startswith("FILE_REDUCTION_")]
        for name in names:
            self.driver.wait_for_object(getattr(Preview, name), timeout=10)

    def select_file_reduction_size(self, size):
        if size not in [getattr(Preview, attr) for attr in dir(Preview) if attr.endswith("_SIZE")]:
            raise InvalidElementNameException("Object {}: is not a valid File Reduction size option".format(size))
        self.driver.wait_for_object(size).click()

    def get_reduced_file_sizes(self):
        p = re.compile(r'\((.*?) MB\)')
        actual_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_ACTUAL_SIZE).text).group(1).strip()
        medium_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_MEDIUM_SIZE).text).group(1).strip()
        small_size = re.search(p, self.driver.wait_for_object(self.FILE_REDUCTION_SMALL_SIZE).text).group(1).strip()
        return int(actual_size), int(medium_size), int(small_size)

        # Feedback pop-up

    def dismiss_feedback_pop_up(self):
        if self.driver.wait_for_object("_Shared_no_thanks_btn", raise_e=False) is not False:
            self.driver.click("_Shared_no_thanks_btn")
            logging.info("Selected No Thanks on Feedback pop_up")

    def get_option_selected_value(self, option):
        print_option = self.driver.wait_for_object(option).get_attribute("name")
        return self.driver.wait_for_object("cell_selected_value_txt", format_specifier=[print_option]).get_attribute(
            "name")

    def verify_pages_selected(self, page_no):
        return self.driver.wait_for_object("page_selected_image", format_specifier=[page_no], raise_e=False)

    def select_or_unselect_pages(self, page_no):
        for i in range(len(page_no)):
            self.driver.click("page_no_txt", format_specifier=[page_no[i]])

    def get_page_range(self):
        return self.driver.wait_for_object("page_range_displayed_txt").get_attribute("name")

    def check_manual_input_pop_up_msg(self, input_page_range=False):
        if self.driver.wait_for_object("in_app_alert", raise_e=False) is not False:
            if input_page_range:
                return self.driver.wait_for_object("manual_input_pop_up_msg", raise_e=False)
            else:
                return self.driver.wait_for_object("manual_input_pop_up_warning_msg", raise_e=False)
        else:
            return False

    def enter_page_range(self, page_nos):
        self.driver.click("clear_text_btn", raise_e=False)
        self.driver.send_keys("page_range_input_txt_field", page_nos)

    def verify_default_option_selected(self, option_name):
        return self.driver.wait_for_object("option_selected_image", format_specifier=[option_name], invisible=True,
                                           raise_e=False)

    def verify_button(self, button_name):
        return self.driver.wait_for_object(self.DYNAMIC_PREVIEW_BUTTON,
                                           format_specifier=[self.get_text_from_str_id(button_name)], raise_e=False)

    def verify_transform_screen_title(self, title):
        self.dismiss_feedback_pop_up()
        return self.driver.wait_for_object("preview_navigation_bar_title_text",
                                           format_specifier=[title], raise_e=False)

    def select_transform_options(self, tf_option1, tf_option_select=None):
        self.driver.click(tf_option1)
        self.verify_transform_screen_title(tf_option1)
        if tf_option_select is not None:
            self.driver.click("_shared_dynamic_text", format_specifier=[tf_option_select])

    def get_print_page_collection_view_cell(self, page_index=None):
        page_labels = []
        no_of_pages = self.driver.find_object("reorder_page_collection", multiple=True)
        if page_index is not None:
            page_labels = no_of_pages[page_index].text
        else:
            for i in range(len(no_of_pages)):
                page_label = no_of_pages[i].text
                page_labels.append(page_label)
        logging.debug(page_labels)
        return page_labels

    def toggle_share_as_original_btn(self):
        self.driver.click("share_as_original_toggle_btn")

    # implementation in progress, not tested yet
    def reorder_page_collection(self, index=1, direction="right"):
        page_objects = self.driver.find_object("no_of_pages", multiple=True)
        self.driver.drag_and_drop(page_objects[index], destination=direction)

    def preview_img_screenshot(self):
        return saf_misc.load_image_from_base64(self.driver.screenshot_element(self.PREVIEW_IMAGE))

    def verify_preview_image_edit_btn(self):
        self.driver.wait_for_object(self.EDIT_BUTTON, displayed=False)

    def verify_choose_your_printer_option(self):
        self.driver.wait_for_object("choose_your_printer_option")

    def dismiss_new_file_types_coachmark(self, raise_e=False):
        if self.driver.wait_for_object("new_file_types_coachmark", displayed=False, raise_e=raise_e) is not False:
            self.driver.click_by_coordinates(area='bl')

    def nav_detect_edges_screen(self):
        # Depending on printer, scan job takes longer sometimes
        self.driver.wait_for_object("adjust_boundaries_title", timeout=30)
        self.driver.click("next_btn", timeout=10)

    def verify_print_preview_coach_mark(self, raise_e=False):
        return self.driver.find_object("print_preview_coach_mark", raise_e=raise_e)

    def dismiss_print_preview_coach_mark(self):
        if self.verify_print_preview_coach_mark() is not False:
            self.driver.click_by_coordinates(area='bl')
            time.sleep(1)

    def select_edit_btn_on_preview_screen(self):
        self.driver.click("edit_btn")

    def verify_detect_edges_screen(self):
        self.driver.wait_for_object("adjust_boundaries_title", timeout=30)

    def select_replace_btn_on_preview(self):
        self.driver.click("replace_btn")
