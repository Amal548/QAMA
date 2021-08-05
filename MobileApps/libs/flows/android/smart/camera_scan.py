from selenium.common.exceptions import TimeoutException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import logging
from SAF.decorator.saf_decorator import screenshot_capture


class CameraScan(SmartFlow):
    flow_name = "camera_scan"

    PHOTO_MODE = "photo_btn"
    DOCUMENT_MODE = "document_btn"
    BATCH_MODE = "batch_btn"
    MULTI_ITEM_MODE = "multi_item_btn"
    BOOK_MODE = "book_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def select_capture_mode(self, mode):
        """
        Select a capture mode
        :param mode: using class constant
                PHOTO_MODE
                DOCUMENT_MODE
                BATCH_MODE
        """
        self.driver.click(mode)

    def toggle_capture_mode(self, manual=True):
        """
        Toogle Capture Mode: It is for BATCH mode
        :param manual: True -> disable
                       False -> enable
        """
        current_status = self.driver.get_attribute("capture_mode", "selected")
        if (manual and current_status == "true") or (not manual and current_status == "false"):
            self.driver.click("capture_mode")

    def capture_photo(self, mode=None, number_pages=1, manual=True, is_copy=False):
        """
        Capture photos with one/multiple pages
            - If No Camera Acess, give access to camera
            - Select capture mode if is_copy=False
            - if mode = Batch, toggle auto/manual mode 
            - Capture photo. If mode = Batch, capturing 1/multiple pages
            - If mode = batch, click Done button
        :param mode: capture mode. Using class constant
                        PHOTO_MODE
                        DOCUMENT_MODE
                        BATCH_MODE
        :param number_pages: capture multiple pages if mode = Batch. Otherwise, capture 1 time
        :param manual: selct auto/manual for batch mode.
        :param is_copy: copy/camera scan feature
        """
        if self.verify_capture_no_access_screen(raise_e=False):
            self.select_camera_access_allow()
            self.check_run_time_permission()
        if not is_copy:
            self.select_capture_mode(mode)
        if mode == self.BATCH_MODE:
            self.toggle_capture_mode(manual=manual)
        for _ in range(number_pages):
            if not is_copy:
                self.driver.click("shutter_btn", change_check={"wait_obj": "camera_bottom_status_message", "invisible": False})
            else:
                self.driver.click("shutter_btn", change_check={"wait_obj": "camera_bottom_status_message", "invisible": True})
            self.driver.wait_for_object("progress_icon", invisible=True)
        if not is_copy and mode == self.BATCH_MODE:
            self.click_done()

    def click_done(self):
        """
        Click on Done button after capturing photos in batch mode
        """
        self.driver.click("done_btn")

    def select_camera_access_allow(self):
        """
        Click on Allow Access button on No Camera Access
        """
        self.driver.wait_for_object("allow_access_btn")
        self.driver.click("allow_access_btn")

    def select_camera_permission_allow_btn(self):
        """
        Click on ALLOW button on Camera permission access screen
        """
        self.driver.click("camera_permission_access_allow_btn")

    def dismiss_tips_camera_capture_popup(self):
        """
        Dismiss 'Tips for Camera Capture' popup if it displays
        Note: Add 20 seconds to timeout because of loading process
        """
        try:
            self.driver.wait_for_object("tips_capture_popup", timeout=20)
            self.driver.click("tips_capture_popup_ok_btn", change_check={"wait_obj": "tips_capture_popup_ok_btn", "invisible": True})
        except (TimeoutException):
            logging.info("'Tips for Camera Capture' is NOT displayed")

    def select_adjust_next_btn(self):
        """
        Click on Next button
        """
        self.driver.click("adjust_next_btn", change_check={"wait_obj": "adjust_next_btn", "invisible": True}, timeout=10)
        self.verify_invisible_crop_enhance_popup()

    def select_adjust_full_option_btn(self):
        """
        Click on full option on Adjust Boundaries screen
        """
        self.driver.wait_for_object("adjust_full_screen_btn")
        self.driver.click("adjust_full_screen_btn")

    def select_gallery_option(self):
        """
        Click on photo Gallery option on photo capture screen
        """
        self.driver.click("image_gallery_option")

    def select_x_button(self):
        """
        Click on X button on capture screen
        """
        self.driver.click("x_button")

    def select_settings_button(self):
        """
        Click on Settings button on capture screen
        """
        self.driver.click("settings_button")


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_capture_screen(self):
        """
        Verify that current screen is capture screen via:
            - Camera shutter button
            - Camera Photo/Document/and Batch buttons
        """
        self.driver.wait_for_object("photo_btn")
        self.driver.wait_for_object("document_btn")
        self.driver.wait_for_object("batch_btn")
        self.driver.wait_for_object("shutter_btn")
            
    @screenshot_capture(file_name="capture_screen.png")
    def verify_capture_no_access_screen(self, raise_e=True):
        """
        Verify current screen is capture screen with No Access message via:
            - No Camera message
            - Allow Access button
        :parameter: ga is True or False
        """
        return self.driver.wait_for_object("no_camera_access_title", raise_e=raise_e)

    def verify_camera_permission_access_screen(self):
        """
        Verify current screen is camera access screen with:
            - Allow HP Smart to take pictures and record video
            - Allow button
            - Deny button
        """
        self.driver.wait_for_object("camera_permission_access_popup")
        self.driver.wait_for_object("camera_permission_access_allow_btn")
        self.driver.wait_for_object("camera_permission_access_deny_btn")

    def verify_camera_adjust_screen(self):
        """
        Verify that current screen is adjust screen:
            - Next button   (add 20 seconds to timeout because of loading process after capturing a photo
            - Full screen icon button
        """
        self.driver.wait_for_object("adjust_next_btn")
        self.driver.wait_for_object("adjust_full_screen_btn")

    def verify_invisible_crop_enhance_popup(self):
        """
        Verify that Crop and Enhance popup invisible
        """
        self.driver.wait_for_object("crop_enhance_msg", invisible=True, timeout=30)

    def verify_slider_button_on_capture_screen(self, capture_mode):
        """
        Verify slider menu buttons on capture screen:
         - PHOTO_MODE
         - DOCUMENT_MODE
         - BATCH_MODE
         - MULTI_ITEM_MODE
         - BOOK_MODE

        """
        btn_name = self.driver.return_str_id_value(capture_mode)
        self.driver.scroll("capture_mode_option", direction="right", format_specifier=[btn_name], check_end=False)

    def verify_top_bar_menu_on_capture_screen(self, invisible=True):
        """
        Verify the top bar menu of capture screen through:
        - X button
        - Flash button
        - Settings button
        - Auto button for Batch mode only
        """
        self.driver.wait_for_object("x_button")
        self.driver.wait_for_object("flash_button")
        self.driver.wait_for_object("settings_button")
        self.driver.wait_for_object("auto_button", invisible=invisible)

    def verify_preference_screen(self):
        """
        Verify that current screen is Preference screen via:
            - Auto-Enhancements
            - Auto- Orientation
        """
        self.driver.wait_for_object("auto_enhancements")
        self.driver.wait_for_object("auto_orientation")


    # *********************************************************************************
    #                                IS FLOWS                                         *
    # *********************************************************************************
    def is_camera_screen(self):
        """
        Verify that current screen is camera screen via shuttle button
        :return: True if it is camera screen. Otherwise, False
        """
        try:
            self.verify_capture_screen()
            return True
        except TimeoutException:
            logging.info("Current screen is not Camera screen")
            return False
