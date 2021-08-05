import logging

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from SAF.misc import saf_misc
from time import sleep
from MobileApps.libs.flows.common.edit.edit_flow import Edit_Flow


class Edit(Edit_Flow):
    # Base Flow for all involved platforms
    flow_name = "edit"
    folder_name = "edit"

    def __init__(self, driver):
        super(Edit, self).__init__(driver)

    AUTO = "edit_options_auto_txt"
    ADJUST = "edit_options_adjust_txt"
    FILTERS = "edit_options_filters_txt"
    CROP = "edit_options_crop_txt"
    TEXT = "edit_options_text_txt"
    TEXT_OPTIONS_TITLE = "edit_text_options_txt"
    FILTER_DOCUMENT = "filter_option_document_txt"
    FILTER_PHOTO = "filter_option_photo_txt"
    FILTER_ORIGINAL = "filter_option_original_txt"
    TEXT_SCREEN_TITLE = "add_text_screen_title"
    TEXT_FONTS = "text_option_fonts_txt"
    TEXT_COLOR = "text_option_color_txt"
    TEXT_BGCOLOR = "text_option_bgcolor_txt"
    TEXT_ALIGNMENT = "text_option_alignment_txt"

    EDIT_OPTIONS = [
        AUTO,
        ADJUST,
        FILTERS,
        CROP,
        TEXT
    ]

    FILTER_OPTIONS = [
        FILTER_ORIGINAL,
        FILTER_DOCUMENT,
        FILTER_PHOTO
    ]

    TEXT_OPTIONS = [
        TEXT_FONTS,
        TEXT_COLOR,
        TEXT_BGCOLOR,
        TEXT_ALIGNMENT
    ]

    EDIT_SCREEN_BUTTONS = ["done_btn", "cancel_btn"]

    TEXT_OPTIONS_SCREEN_BUTTONS = ["add_btn", "delete_btn", "bring_to_front_btn", "redo_btn", "undo_btn"]

    CROP_BUTTONS = ["crop_flip_btn", "crop_rotate_btn", "crop_transform_scale_picker"]

    ADD_TEXT_UI = ["done_btn", "cancel_btn", "add_text_editor", "keyboard_element"]

    DISCARD_EDIT_POP_UP_ELEMENTS = ["discard_edit_title_txt", "discard_edit_pop_up_msg", "discard_edit_btn",
                                    "discard_edit_cancel_btn"]

    def verify_edit_page_title(self, raise_e=True):
        return self.driver.wait_for_object("edit_title", raise_e=raise_e, timeout=20)

    def verify_screen_title(self, title):
        return self.driver.wait_for_object("edit_screen_navigation_bar",
                                           format_specifier=[self.driver.return_str_id_value(title)], timeout=10,
                                           raise_e=False) is not False

    def verify_and_swipe_adjust_slider(self, direction="left", per_offset=0.3):
        if self.driver.wait_for_object("adjustments_slider", raise_e=False) is not False:
            self.driver.swipe("adjustments_slider", direction=direction, per_offset=per_offset)
        else:
            logging.info("Adjust Slider not displayed")

    def verify_undo_button_enabled(self):
        return self.driver.get_attribute("undo_btn", attribute="enabled", raise_e=False)

    def verify_undo_redo_buttons(self):
        self.driver.wait_for_object("undo_btn")
        self.driver.wait_for_object("redo_btn")

    def verify_edit_text_displayed(self, text):
        return self.driver.wait_for_object("dynamic_text", format_specifier=[text], raise_e=False)

    def verify_edit_ui_elements(self, array_elements, direction="down", scroll_object=None):
        element_missing = []
        for element in array_elements:
            if not self.driver.wait_for_object(element, raise_e=False):
                if not self.driver.scroll(element, direction=direction, scroll_object=scroll_object, raise_e=False):
                    element_missing.append(element)
        if len(element_missing) > 0:
            raise NoSuchElementException("Following options {}:not displayed".format(element_missing))

    def verify_export_progress_pop_up(self, invisible=False, timeout=10):
        """
        Verify export progress pop up
         - verify label
         - verify progress bar(loading animation)
        """
        self.driver.wait_for_object("export_progress_label", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("export_progress_bar", invisible=invisible, timeout=timeout)

    def select_edit_main_option(self, edit_option):
        self.driver.click(edit_option)
        sleep(2)

    def select_edit_child_option(self, edit_option, direction="right", check_end=True, str_id=False):
        if str_id:
            edit_option = self.driver.return_str_id_value(edit_option)
        self.driver.scroll("edit_option_txt", format_specifier=[edit_option], direction=direction,
                           scroll_object="collection_view", click_obj=True, check_end=check_end)
        logging.info(edit_option + " - selected")

    def add_txt_string(self, text):
        """
        Enter text on Text screen
        Build a genera function for adding text that we cau use it flexible.
        Because there are 2 ways to add Text, One is clicking Text button, One is clicking Add button.
        """
        self.driver.wait_for_object("add_text_editor")
        self.driver.send_keys("add_text_editor", text)

    def select_text_and_enter_txtstring(self, text):
        self.select_edit_main_option(self.TEXT)
        self.add_txt_string(text=text)

    def select_edit_text_options(self, edit_feature, edit_option, direction="right", check_end=True, str_id=False):
        self.select_edit_main_option(edit_feature)
        sleep(5)
        self.select_edit_child_option(edit_option, direction=direction, check_end=check_end, str_id=str_id)

    def select_edit_cancel(self):
        self.driver.click("cancel_btn")

    def select_edit_done(self):
        self.driver.click("done_btn")

    def select_discard_changes_btn(self, btn_name=DISCARD_EDIT_POP_UP_ELEMENTS[2]):
        self.driver.click(btn_name)

    def get_elements_in_collection_view(self, edit_feature, edit_options_array, edit_type):
        edit_options = []
        self.select_edit_main_option(edit_feature)
        self.driver.wait_for_object("collection_view", timeout=15, raise_e=False)
        if edit_type == 'filter':
            self.driver.swipe(swipe_object='collection_view', direction="left", check_end=True)
        for _ in range(9):
            if edit_type == 'text':
                edit_sub_options = self.driver.find_object("text_options_collection_view", multiple=True)
            else:
                parent_element = self.driver.find_object("edit_options_collection_view",
                                                         format_specifier=[edit_type])
                edit_sub_options = self.driver.find_object("collection_view_class", root_obj=parent_element,
                                                           multiple=True)
            for i in range(len(edit_sub_options)):
                option_label = edit_sub_options[i].get_attribute("label")
                if option_label not in edit_options:
                    edit_options.append(option_label)
            if len(edit_options) == len(edit_options_array):
                break
            else:
                self.driver.swipe(swipe_object='collection_view', direction="right", check_end=True)
        logging.debug(edit_options)
        return edit_options

    def apply_edits(self, edit_feature, edit_option, direction="right", check_end=False, str_id=False):
        self.select_edit_main_option(edit_feature)
        sleep(2)
        self.select_edit_child_option(edit_option, direction=direction, check_end=check_end, str_id=str_id)
        if edit_option == self.driver.get_attribute("crop_option_custom", attribute="label", raise_e=False):
            self.apply_crop_rotate()
        if edit_feature == self.ADJUST:
            self.verify_and_swipe_adjust_slider()
        self.select_edit_done()

    def apply_crop_flip(self):
        self.driver.wait_for_object("crop_flip_btn").click()

    def apply_crop_rotate(self):
        self.driver.wait_for_object("crop_rotate_btn").click()

    def apply_crop_scale_picker(self):
        #According to iOS side comments, remove if state as not need use it
        self.driver.swipe("crop_transform_scale_picker", direction="left", per_offset=0.5)

    def apply_and_verify_all_edit_options(self, edit_feature, edit_feature_options, diff=0, direction="right",
                                          check_end=False, str_id=False):
        edit_apply_failed = []
        for edit_option in edit_feature_options:
            pre_edit_img = self.edit_img_screenshot()
            self.apply_edits(edit_feature, edit_option, direction=direction, check_end=check_end, str_id=str_id)
            edited_img = self.edit_img_screenshot()
            if self.edit_img_comparision(pre_edit_img, edited_img, compare_diff=diff) is False:
                edit_apply_failed.append(edit_option)
        return edit_apply_failed

    def edit_img_comparision(self, before_image, after_image, compare_diff=0):
        image_diff = saf_misc.img_comp(before_image, after_image)
        if image_diff > compare_diff:
            logging.info("Images are different by following %- {}".format(image_diff))
            return True
        else:
            logging.info("Images are identical with min % difference of- {}".format(image_diff))
            return False

    def edit_img_screenshot(self):
        return saf_misc.load_image_from_base64(self.driver.screenshot_element("edit_img"))
    
    def select_undo(self):
        """
        Click on Undo button on Adjust screen
        """
        self.driver.click("undo_btn")

    def select_redo(self):
        """
        Click on Undo button on Adjust screen
        """
        self.driver.click("redo_btn")

    def select_add_text(self):
        """
        Click on Add button on Text Options screen
        """
        self.driver.click("add_btn")
    
    def select_delete_text(self):
        """
        Click on Delete button on Text Options screen
        """
        self.driver.click("delete_btn", change_check={"wait_obj": "delete_btn", "invisible": True})
    
    def select_to_front(self):
        """
        Click on To Front on Text Options screen
        """
        self.driver.click("bring_to_front_btn")
    
    def select_color(self, color_name):
        """
        Select color from Text Color screen
        """
        self.driver.scroll("color_option", format_specifier=[self.driver.return_str_id_value(color_name)], direction="right", scroll_object="collection_view", click_obj=True, check_end=False)

    def verify_discard_edits_screen(self):
        """
        Verify Discard Edits screen:
            - Title
            - Yes button
            - No button
        """
        self.driver.wait_for_object("discard_edit_title_txt")
        self.driver.wait_for_object("discard_edit_pop_up_msg")
        self.driver.wait_for_object("discard_edit_btn")
        self.driver.wait_for_object("discard_edit_cancel_btn")


class IOSEdit(Edit):
    platform = "ios"
    # For needing to overload method in IOS
    # pass

    ADJUST_OPTIONS = [
        "Brightness", "Saturation", "Contrast", "Clarity", "Exposure",
        "Shadows", "Highlights", "Whites", "Blacks", "Temperature"
    ]

    FILTER_DOCUMENT_OPTIONS = ['Original', 'Document', 'B/W', 'B/W 2', 'Greyscale', 'Alabaster', 'Photo']
    FILTER_PHOTO_OPTIONS = ['Original', 'Document', 'Photo', 'Summer', 'Aurora', 'Ultraviolet', 'Ink Stains',
                            'Alabaster', 'Dusk', 'Noir',
                            'Daydream', 'Embers', 'Moonlight', 'Snowshine', 'Atmospheric', 'Honeybee', 'Fireside',
                            'Glacial', 'Sauna', 'Seafarer', 'Cameo', 'Timeworn', 'Sunlight']
    CROP_OPTIONS = ['Reset', 'Custom', 'Square', 'Letter', 'A4', '5:7', '4:6', '3.5:5']
    TEXT_FONT_OPTIONS = ['Playfair', 'Dancing', 'Meie Script', 'Concert', 'Abril', 'Old', 'Yatra', 'Oswald',
                         'Montserrat', 'Roboto', 'Lora', 'Rakkas', 'Cormorant', 'Ubuntu', 'Arvo']
    TEXT_COLOR_OPTIONS = ['Pipettable color', 'White', 'Gray', 'Black', 'Light blue', 'Blue', 'Purple', 'Orchid',
                          'Pink', 'Red', 'Orange', 'Gold', 'Yellow', 'Olive', 'Green', 'Aquamarin']
    TEXT_BGCOLOR_OPTIONS = ['Pipettable color', 'Transparent', 'White', 'Gray', 'Black', 'Light blue', 'Blue', 'Purple',
                            'Orchid', 'Pink', 'Red', 'Orange', 'Gold', 'Yellow', 'Olive', 'Green', 'Aquamarin']

    def modify_text_box(self, text, clear_text=False):
        self.driver.click("add_text_text_box")
        if clear_text:
            self.driver.long_press("add_text_editor")
            self.driver.click("_shared_select_all_btn")
        self.add_txt_string(text)
        self.select_edit_done()


class AndroidEdit(Edit):
    platform = "android"
    # For over loading method in Android
    # Android side use str_id as locator for below elements
    BRIGHTNESS = "brightness_option"
    SATURATION = "saturation_option"
    CONTRAST = "contrast_option"
    CLARITY = "clarity_option"
    EXPOSURE = "exposure_option"
    SHADOWS = "shadows_option"
    HIGHLIGHTS = "highlights_option"
    WHITES = "whites_option"
    BLACKS = "blacks_option"
    TEMPERATURE = "temperature_option"
    BW = "bw_option"
    BW2 = "bw2_option"
    GREYSCALE = "greyscale_option"
    ALABASTER = "alabaster_option"
    SUMMER = "summer_option"
    AURORA = "aurora_option"
    ULTRAVIOLET = "ultraviolet_option"
    INK_STAINS = "ink_stains_option"
    DUSK = "dusk_option"
    NOIR = "noir_option"
    DAYDREAM = "daydream_option"
    EMBERS = "embers_option"
    MOONLIGHT = "moonlight_option"
    SNOWSHINE = "snowshine_option"
    ATMOSPHERIC = "atmospheric_option"
    HONEYBEE = "honeybee_option"
    FIRESIDE = "fireside_option"
    GLACIAL = "glacial_option"
    SAUNA = "sauna_option"
    SEAFARER = "seafarer_option"
    CAMEMO = "cameo_option"
    TIMEWORN = "timeworn_option"
    SUNLIGHT = "sunlight_option"
    CUSTOM = "custom_txt"
    SQUARE = "square_txt"
    LETTER = "letter_txt"
    A4 = "a4_txt"
    SIZE_5_7 = "5_7_txt"
    SIZE_4_6 = "4_6_txt"
    SIZE_3_5_5 = "3_5_5_txt"
    TEXT_OPTION_TITLE = "text_option_title"
    FONTS_TITLE = "fonts_title"
    ABRIL = "abril_option"
    ARVO = "arvo_option"
    CONCERT = "concert_option"
    COMMIRANT = "commorant_option"
    DANCING_SCRIPT = "dancing_script_option"
    LORA = "lora_option"
    MEIE_SCRIPT = "meie_script_option"
    MONTSERRAT = "montserrat_option"
    OLD_STANDARD = "old_standard_option"
    OSWALD = "oswald_option"
    PLAYFAIR_DISPLAY = "playfair_display_option"
    RAKKAS = "rakkas_option"
    ROBOTO = "roboto_option"
    UBUNTU = "ubuntu_option"
    YATRA_ONE = "yatra_one_option"
    GRAY = "gray_color"
    BLACK = "black_color"
    LIGHT_BLUE = "light_blue_color"
    BLUE = "blue_color"
    PURPLE = "purple_color"
    ORCHID = "orchid_color"
    PINK = "pink_color"
    RED = "red_color"
    ORANGE = "orange_color"
    GOLD = "gold_color"
    YELLOW = "yellow_color"
    OLIVE = "olive_color"
    GREEN = "green_color"
    AQUAMARIN = "aquamarin_color"
    COLOR_BTN = "text_color"