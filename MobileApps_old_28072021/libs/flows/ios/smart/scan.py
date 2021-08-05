import logging
from time import sleep

from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from MobileApps.resources.const.ios.const import SCAN_QUALITY, SCAN_SETTINGS
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class Scan(SmartFlow):
    flow_name = "scan"

    PAPER_SIZE_DROP_DOWN = "area_size"
    PAGE_SIZE = "page_size"
    PAPER_SIZE_TABLE_VIEW = "area_size_options"
    PAPER_SIZES = ["_const_paper_size_a4_option", "_const_paper_size_4x6_option", "_const_paper_size_5x7_option", "_const_paper_size_3_5x5_option"]

    INPUT_SOURCE = "input_source"
    QUALITY = "quality"
    COLOR = "color"

    ADJUST_SCAN_COACH_MARK = "adjust_scan_coach_mark"
    ADJUST_SCAN_CAPTURE_COACH_MARK = "adjust_scan_capture_coachmark"
    START_SCAN_COACHMARK = "start_scan_coachmark"
    SCAN_SOURCE_COACHMARK = "scan_source_coachmark"

    AUTO_ENHANCEMENT_SWITCH = "auto_enhancements"
    AUTO_ORIENTATION_SWITCH = "auto_orientation"
    AUTO_HEAL_SWITCH = "auto_heal_switch"
    FLATTEN_PAGES_SWITCH = "flatten_pages_switch"

    PHOTO_MODE = "photo_mode"
    DOCUMENT_MODE = "document_mode"
    BATCH_MODE = "batch_mode"
    MULTI_ITEM_MODE = "multi_item_mode"
    BOOK_MODE = "book_mode"

    SCAN_COACH_MARKS = [
        ADJUST_SCAN_CAPTURE_COACH_MARK,
        START_SCAN_COACHMARK,
        SCAN_SOURCE_COACHMARK
    ]

    SCAN_SETTINGS = [
        PAGE_SIZE,
        QUALITY,
        COLOR
    ]

########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows                                                        #
#                                                                                                                      #
########################################################################################################################

    def select_scanner_if_first_time_popup_visible(self):
        """
        :return:
        """
        try:
            self.driver.wait_for_object("scanner_popup_btn")
            self.driver.click("scanner_popup_btn")
        except TimeoutException:
            logging.info("Current Screen did NOT contain the first time scanner or camera popup")

    def select_scan_settings_wheel(self):
        """
        Click on Scan Settings

        End of flow: Scan Settings screen

        Device: Phone
        """
        self.driver.wait_for_object("setting_btn", timeout=30).click()

    def select_scan_settings_by_type_and_value(self, settings_option_type, settings_option_value=""):
        """
        Select scan settings by setting option and the item of that option

        End of flow: Scan screen

        Device: Phone
        """

        try:
            self.driver.click(settings_option_type)
            if settings_option_type == SCAN_SETTINGS.INPUT_SOURCE:
                self.driver.wait_for_object("input_src_title")
            if settings_option_type == SCAN_SETTINGS.QUALITY:
                self.driver.wait_for_object("quality_title")
            if settings_option_type == SCAN_SETTINGS.COLOR:
                self.driver.wait_for_object("color_title")
            self.driver.click(settings_option_value)
            self.select_navigate_back()
            self.verify_scan_settings_screen()
        except (NoSuchElementException, TimeoutException):
            logging.info("This settings_option is not exists !!" + settings_option_type)

    def select_from_papersize_drop_down(self, option):
        self.driver.click("area_size")
        self.driver.click(option)
        logging.info("Changed the papersize option to: " + self.get_area_size())

    def get_area_size(self):
        """
       Get scan area size on Scan screen

       Device: Phone
       """
        area_size = self.driver.find_object("area_size").text
        if area_size == 'Letter - 8.5x11 in':
            area_size = '215.9x279.4mm'
        return str(area_size)

    def select_scan_job_button(self):
        """
        Click Scan button on Scan screen
        Device: Phone
        """
        if self.verify_second_close_btn() is not False:
            self.select_second_close_btn()
        sleep(1)
        self.driver.click("scan_btn", change_check={"wait_obj": "cancel_scan_btn"}, timeout=20)

    def select_cancel_scanning_job(self):
        """
        Click Scan button on Scan screen to cancel scanning
        Device: Phone
        """
        self.driver.click("cancel_scan_btn")

    def select_preview_on_scanner_screen(self):
        """
        Click on Preview button on Scan screen

        End of flow: Scan screen

        Device: Phone
        """
        self.driver.wait_for_object("preview_btn").click()

    def select_source_button(self):
        """
        :return:
        """
        self.driver.click("source_btn")

    def select_no_button_to_scanner_screen(self):
        """
        Click on No button on navigate back popup, to return for scanner screen or camera screen
        """
        self.driver.click("add_page_no_btn")

    def select_camera_if_first_time_popup_visible(self):
        """

        :return:
        """

        try:
            self.driver.wait_for_object("camera_popup_btn")
            self.driver.click("camera_popup_btn")
        except TimeoutException:
            logging.warning("Current Screen did NOT contain the scanner or camera popup")

########################################################################################################################
#                                                                                                                      #
#                                             Verification Flows                                                       #
#                                                                                                                      #
########################################################################################################################

    def verify_scanner_screen(self, raise_e=True):
        """
        verifies the scan screen after selection in scanner or camera first time dialog popup:
        :return:
        """
        if self.driver.wait_for_object("preview_btn", timeout=90, raise_e=raise_e) == False:
            return False
        return True

    def verify_scan_settings_screen(self):
        """
        Verify Scan Settings Navigation bar:
            - Done button (phone only)
            - Scan Settings title

        Note: for tablet, there are 2 texts for "Scan Settings"

        Device: phone and tablet
        """
        self.driver.wait_for_object("scan_settings_title", timeout=30)

    def verify_scanning_screen(self):
        """
         verifies the scanning screen undergoing by using the same scan button(in red color):
        :return:
        """
        self.driver.wait_for_object("cancel_scan_btn")

    def verify_scanner_or_camera_popup_displayed(self, popup=True):
        """
        Verify Scanner and Camera options pop-up displayed or not

        Device: Phone
        """

        popup_displayed = self.driver.wait_for_object("scan_images_or_slash_documents_popup_msg", timeout=10,
                                                      raise_e=False)
        if popup_displayed == popup:
            return True
        else:
            return False

    def verify_x_button_on_scan_screen(self):
        """
        :return:
        """
        self.driver.wait_for_object("close_btn")

    def verify_area_size_field(self):
        """
        :return:
        """
        self.driver.wait_for_object("area_size")

    def verify_area_size_options(self):
        """
        :return:
        """
        # self.driver.click("area_size")
        self.driver.wait_for_object("area_size_options")

    def verify_down_arrow_icon(self):
        """
        :return:
        """
        self.driver.wait_for_object("down_arrow_icon")

    def verify_scan_setting_wheel(self):
        """
        :return:
        """
        self.driver.wait_for_object("setting_btn")

    def verify_preview_button_on_scan_screen(self, raise_e=True):
        """
        :return:
        """
        return self.driver.wait_for_object("preview_btn", timeout=10, raise_e=raise_e)

    def verify_scan_button(self):
        """
        :return:
        """
        self.driver.wait_for_object("scan_btn", timeout=30)

    def verify_source_button(self):
        self.driver.wait_for_object("source_btn")

    def select_files_photos_option(self):
        self.driver.click("files_and_photos_btn")

    def select_camera_option(self):
        self.driver.click("camera_btn")

    def select_scanner_option(self):
        self.driver.click("scanner_btn")

    def change_scan_settings_and_save(self, settings_option_type, settings_option_value):
        self.select_scan_settings_wheel()
        self.verify_scan_settings_screen()
        self.driver.wait_for_object(settings_option_type).click()
        self.driver.wait_for_object(settings_option_value).click()
        self.select_navigate_back()
        self.verify_scan_settings_screen()
        self.select_done()

    def verify_source_all_options(self):
        """
        :return:
        """
        self.driver.wait_for_object("files_and_photos_btn")
        self.driver.wait_for_object("scanner_btn")
        self.driver.wait_for_object("camera_btn")
    
    def verify_source_options_for_printer_without_scanner(self):
        """
        verify only camera and files and photos are available as sources
        """
        self.driver.wait_for_object("files_and_photos_btn")
        self.driver.wait_for_object("camera_btn")

    def verify_scan_settings_type_and_options(self, scan_setting_type, scan_setting_options):
        """
            scan_setting_type: Scan settings ex: Input Type, Quality
            scan_setting_options: option in each Scan Settings ex: Input Type conatin JPG, PDF
            Select scan_setting_type and verify options listed
         """
        if self.driver.wait_for_object(scan_setting_type, raise_e=False) is not False:
            self.driver.click(scan_setting_type)
            options = [a for a in dir(scan_setting_options) if not a.startswith("__")]
            for option in options:
                if self.driver.wait_for_object(getattr(scan_setting_options, option), raise_e=False) is not False:
                    logging.warning(scan_setting_type + " option " + option + "not found/not applicable to connected "
                                                                              "printer")
            self.select_navigate_back()
        else:
            logging.warning(scan_setting_type + " Not applicable/displayed for the connected printer")

    def verify_navigate_back_popup(self):
        """
        this popup will return to home screen or scanner screen
        """
        self.driver.wait_for_object("navigate_bck_popup")

    def verify_top_left_knob_on_scan_screen(self):
        """
         verifies the top left knob
        :return:
        """
        self.driver.wait_for_object("top_left_knob")

    ########################################################################################################################
    #                                                                                                                      #
    #                               //  SCAN //                                                                            #
    #                                                                                                                      #
    ########################################################################################################################

    def select_scan_job_with_cancel_for_ga(self):

        self.select_scan_job_button()
        self.verify_scanning_screen()
        self.select_cancel_scanning_job()
        self.verify_scanner_screen()

    def select_scan_job(self):
        self.select_scan_job_button()
        self.verify_scanning_screen()

    def verify_scan_screen_ui_elements(self):
        """
        :return:
        """
        self.verify_x_button_on_scan_screen()
        self.verify_area_size_field()
        self.verify_scan_setting_wheel()
        self.verify_preview_button_on_scan_screen()
        self.verify_scan_button()
        self.verify_source_button()

    def verify_scanning_messages(self):
        """
         Verify messages displayed while scanning a job
        :return:
        """
        if self.driver.wait_for_object("scanning_msg", raise_e=False) is not False:
            logging.info("Scanning.. msg not displayed")
        if self.driver.wait_for_object("scanning_finished_msg", raise_e=False) is not False:
            logging.info("Scanning Finished msg not displayed")

    def verify_scan_canceling_msg(self):
        if self.driver.wait_for_object("scanning_canceling_msg", raise_e=False) is not False:
            logging.info("Scanning canceled & canceling.. msg displayed")

    def verify_scan_coach_mark_pop_up(self, raise_e=False):
        return self.driver.wait_for_object("scan_coach_mark_pop_up", raise_e=raise_e)
    
    def verify_coachmark_on_scan_page(self, coachmark_no, raise_e=True):
        """        
        ADJUST_SCAN_COACH_MARK
        SCAN_COACH_MARK_1,
        SCAN_COACH_MARK_2
        """
        return self.driver.wait_for_object(coachmark_no, raise_e=raise_e)

    def select_next_on_coachmark(self):
        self.driver.click("next_btn")

    def select_gear_setting_btn(self):
        self.driver.click("scan_setting_gear")
