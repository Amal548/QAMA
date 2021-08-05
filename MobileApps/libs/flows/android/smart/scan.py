from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import sys
from SAF.decorator.saf_decorator import screenshot_capture
import logging

class Scan(SmartFlow):
    flow_name = "scan"

    SOURCE_OPT_GLASS = "source_scanner_glass"
    SOURCE_GLASS_SHORT = "source_scanner_glass_short"
    COLOR_OPT_COLOR = "color_color"
    COLOR_OPT_BLACK = "color_black"
    RESOLUTION_75 = "resolution_75"
    RESOLUTION_100 = "resolution_100"
    RESOLUTION_200 = "resolution_200"
    RESOLUTION_300 = "resolution_300"
    PAPER_SIZE_3_5 = "paper_size_3_5"
    PAPER_SIZE_4_6 = "paper_size_4_6"
    PAPER_SIZE_5_7 = "paper_size_5_7"
    PAPER_SIZE_LETTER = "paper_size_letter"
    PAPER_SIZE_A4 = "paper_size_a4"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_back(self):
        """
        Click on back button
        End of flow: Home page
        Device: Phone
        """
        self.driver.click("back_btn")


    def select_scan(self):
        """
        Click on Scan button
        """
        self.driver.wait_for_object("scan_btn")
        self.driver.click("scan_btn", change_check={"wait_obj": "scan_btn", "invisible": True})

    def select_scan_size(self, size_opt=""):
        """
        At Scan screen:
            - Click on Scan Size drop down button
            - Click on size based size option
        :param size_opt: size for scanning. Use class constant  for this variable
                PAPER_SIZE_3_5
                PAPER_SIZE_4_6
                PAPER_SIZE_5_7
                PAPER_SIZE_LETTER
                PAPER_SIZE_A4
        """
        self.driver.wait_for_object("paper_size_opt")
        self.driver.click("paper_size_opt", change_check={"wait_obj": "paper_size_opt", "invisible": True})
        self.driver.wait_for_object(size_opt)
        self.driver.click(size_opt, change_check={"wait_obj": "paper_size_opt", "invisible": False})
        self.driver.ga_container.insert_ga_key("current-area", self.get_text_from_str_id(size_opt))

    def select_preview(self):
        """
        Click on Preview button
        End of flow: Scan screen
        """
        self.driver.wait_for_object("paper_size_opt")
        self.driver.click("preview_btn")

    def select_source_option(self, source_type="", is_checked=True):
        """
        Select the corresponding source type in Source drop-down screen
        :param source_type: source glass. Use class constant for this variable
               - source_glass
        End of flow: Scan Settings screen
        """
        self.driver.find_object("scan_settings_spinner", index=0).click()
        if is_checked:
            self.verify_scan_settings_source()
        if source_type:
            self.driver.click(source_type)
            self.driver.ga_container.insert_ga_key("printer-sources", self.get_text_from_str_id(source_type))

    def select_color_option(self, color_opt="", is_checked=True):
        """
        Select the corresponding Color option in Color drop-down screen
        :param color_opt: Color and Black. USe class constant for this variable
               - COLOR_OPT_COLOR
               - COLOR_OPT_BLACK
        End of flow: Scan Settings screen
        """
        self.driver.find_object("scan_settings_spinner", index=1).click()
        if is_checked:
            self.verify_scan_settings_color()
        if color_opt:
            self.driver.click(color_opt)
            self.driver.ga_container.insert_ga_key("current-color", self.get_text_from_str_id(color_opt))

    def select_resolution_option(self, resolution_opt="", is_checked=True):
        """
        Select the corresponding resolution on Resolution drop-down screen
        :param resolution_opt: 75dpi 100dpi 200dpi 300dpi. USe class constant for this variable
                 - RESOLUTION_75
                 - RESOLUTION_100
                 - RESOLUTION_200
                 - RESOLUTION_300
        End of flow: Scan Settings screen
        """
        self.driver.find_object("scan_settings_spinner", index=2).click()
        if is_checked:
            self.verify_scan_settings_resolution()
        if resolution_opt:
            self.driver.click(resolution_opt)
            self.driver.ga_container.insert_ga_key("current-resolution", self.get_text_from_str_id(resolution_opt))

    def select_scan_settings_btn(self):
        """
        Click on Settings button on Scan Home screen
        End of flow: Scan Settings screen
        """
        self.driver.click("scan_settings_btn")

    def select_scan_settings_close(self):
        """
        Click on Close button in Scan Settings screen
        End of flow: Scan screen
        """
        self.driver.click("settings_close_btn")

    def select_cancel(self):
        """
        Click on Cancel button
        End of flow: Scan canceled pop-up
        """
        self.driver.click("cancel_btn")

    def select_ok_btn(self):
        """
        Click on OK button
        End of flow: Scan Home screen
        """
        self.driver.wait_for_object("ok_btn", timeout=10)
        self.driver.click("ok_btn")

    def get_scanned_file_size(self, file_path):
        """
        Get the size of the file from device
        :return file name
        """
        try:
            contents = self.driver.wdvr.pull_file(file_path).decode('base64')
            size = sys.getsizeof(contents)
            logging.debug("Scanned File: {} has file size of: {} bytes".format(file_path, size))
            return size
        except NoSuchElementException:
            logging.debug("Can not get file. {}".format(file_path))
            return 0

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    @screenshot_capture(file_name="scan_screen.png")
    def verify_scan_screen(self):
        """
        Verify that current screen is Scan screen via:
            - Paper Size drop-down (take longer timeout than other elements based on printer)
            - Scan & Preview button
        """
        self.driver.wait_for_object("title", timeout=10)
        self.driver.wait_for_object("preview_btn")
        #Based on defect AIOA-8059, paper size may take at least 40s to be loaded
        self.driver.wait_for_object("paper_size_opt", timeout=50)
        self.driver.wait_for_object("scan_btn", timeout=20)

    def verify_successful_scan_job(self, ga=False):
        """
        Verify that a scan job is successful via invisible of Cancel button

        Note: depending on printer, scan job can take time to complete

        """
        if not ga:
            self.driver.wait_for_object("cancel_btn", invisible=True, timeout=180)
        else:
            self.driver.wait_for_object("cancel_btn_ga", invisible=True, timeout=180)

    def verify_current_settings_info(self, settings_info):
        """
        Verify current setting info displays on screen
        :param settings_info: target setting info
        """
        # Timeout = 30 seconds because of taking more time for talking to printer.
        self.driver.wait_for_object("current_settings_txt", format_specifier=[settings_info])

    def verify_scan_settings_resolution(self):
        """
        Verify Resolution of Scan Settings menu:
            - 75
            - 100
            - 200
            - 300

        Device: Phone
        """
        self.driver.wait_for_object("resolution_75")
        self.driver.wait_for_object("resolution_100")
        self.driver.wait_for_object("resolution_200")
        self.driver.wait_for_object("resolution_300")

    def verify_scan_settings_color(self):
        """
        Verify Color of Scan Settings menu:
            - Color
            - Black

        Device: Phone
        """
        self.driver.wait_for_object("color_color")
        self.driver.wait_for_object("color_black")

    def verify_scan_settings_source(self):
        """
        Verify Source of Scan Settings menu:
            - Scanner Glass
            - Document Feeder (depending on printer)

        Device: Phone
        """
        self.driver.wait_for_object("source_scanner_glass")

    def verify_scan_size(self, scan_size=""):
        """
        Verify that current scan size on Scan screen via:
        @param scan_size: target scan size via following class constant
                PAPER_SIZE_3_5
                PAPER_SIZE_4_6
                PAPER_SIZE_5_7
                PAPER_SIZE_LETTER
                PAPER_SIZE_A4
        """
        self.driver.wait_for_object("paper_size_text", format_specifier=[self.get_text_from_str_id(scan_size)])

    def verify_scan_settings_popup(self):
        """
        Verify that current popup is Scan Settings via:
            - Tittle "Scan Settings"
            - Cancel and Save buttons
        """
        self.driver.wait_for_object("settings_title_txt")
        self.driver.wait_for_object("settings_close_btn")

    def verify_scan_canceled_popup(self, raise_e=True):
        """
        Verify Scan canceled popup:
            - Scan canceled text
            - Ok button
        """
        return self.driver.wait_for_object("scan_canceled_txt", timeout=10, raise_e=raise_e) is not False and \
        self.driver.wait_for_object("ok_btn", timeout=10, raise_e=raise_e) is not False

    def verify_scan_error_popup(self, raise_e=True):
        """
        Verify Scan error popup:
            - Scan error title
        """
        return self.driver.wait_for_object("scan_error_title", timeout=15, raise_e=raise_e)