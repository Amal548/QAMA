import logging
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from MobileApps.resources.const.ios.const import FLASH_MODE
from SAF.misc import saf_misc
import time


class Camera(SmartFlow):
    flow_name = "camera"

    OPTION_FILES = "files_and_photos_str"
    OPTION_CAMERA = "camera_str"
    OPTION_SCANNER = "scanner_str"

    POPUP_UNSAVED_PAGES = "unsaved_pages_popup"
    POPUP_EXIT_WITHOUT_SAVING = "exit_without_saving_popup"
########################################################################################################################
#                                                                                                                      #
#                                                  Action Flows
#                                                                                                                      #
########################################################################################################################

    def select_camera_option_to_scan(self):
        """
            selects the camera option on scan screen:its on scan screen not from first time popup with scanner or camera
        :return:
        """
        self.driver.click("camera_btn")

    def select_allow_access_to_camera_on_popup(self, allow_access=True):
        """
            verifies the allow access to camera popup is present/not,if present based on param value it gives the access
        :param allow_access: True default, if you want to check no access screen , allow_access = False:
        :return:
        """
        try:
            if self.driver.wait_for_object("allow_camera_access_popup", timeout=10):
                if allow_access:
                    self.driver.click("allow_ok")
                else:
                    self.driver.click("dont_allow")
        except TimeoutException:
            logging.info("Current Screen did NOT contain the Allow access camera pop up")

    def select_popup_option(self, camera=True):
        """
        selects either scanner or camera on the first time popup
        :param camera: True to select Camera Button, False to select Scanner Button
        :return:
        """
        try:
            if camera:
                self.driver.wait_for_object(self.OPTION_CAMERA).click()
            else:
                self.driver.wait_for_object(self.OPTION_SCANNER).click()
        except TimeoutException:
            logging.info("Current Screen did NOT contain the first time scanner or camera popup")

    def select_capture_btn(self):
        """
        Selects the camera button
        :return:
        """
        self.driver.click("capture_btn")

    def select_adjust_boundaries_next(self):
        """
        Select the next button on the adjust boundaries screen
        """
        self.driver.click("next_btn")

    def select_manual_option(self):
        """
        Select Manual option on camera screen
        """
        if not self.verify_manual_capture_mode():
            self.select_auto_btn()

    def select_auto_option(self):
        if not self.verify_auto_capture_mode():
            self.select_auto_btn()

    def select_auto_btn(self):
        self.driver.click("auto_btn")

    def select_gear_setting_btn(self):
        self.driver.click("scan_setting_gear")

    def select_allow_access_to_unsaved_pages_popup(self, allow_save=True):
        if self.driver.wait_for_object("unsaved_pages_popup"):
            if allow_save:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_yes")])
            else:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_no")])

    def select_exit_without_saving_popup(self, allow_save=True):
        if self.driver.wait_for_object("exit_without_saving_popup"):
            if allow_save:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_yes")])
            else:
                self.driver.click("_shared_dynamic_button",
                                  format_specifier=[self.get_text_from_str_id("_shared_no")])

    def select_camera_enabled(self):
        if self.driver.get_attribute(obj_name="camera_toggle_btn", attribute="value") == u'0':
            self.driver.click("camera_toggle_btn")

    def select_flash_mode(self, mode, cycle_attempts=2):
        clicks = 0
        while self.driver.wait_for_object(mode, raise_e=False) is False:
            self.driver.click("flash_btn")
            time.sleep(2)
            clicks += 1
            if clicks//len([attr for attr in dir(FLASH_MODE) if not attr.startswith("__")]) >= cycle_attempts:
                break

    def select_enable_access_to_camera_link(self):
        self.driver.wait_for_object("enable_access_to_camera_text").click()

    def select_return_to_hp_smart_btn(self):
        self.driver.wait_for_object("return_to_hp_smart_btn")

    def select_return_to_hp_smart(self):
        self.driver.click("return")

    def select_return_to_hp_smart_r(self):
        self.driver.click("return_a")

    def select_return_to_hp_smart_b(self):
        self.driver.click("return_b")

    def select_return_to_hp_smart_c(self):
        self.driver.click("return_c")

    def select_photo_mode(self):
        self.driver.click("photo_mode")

    def select_document_mode(self):
        self.driver.click("document_mode")

    def select_multi_item_mode(self):
        self.driver.click("multi_item_mode")

    def select_batch_mode(self):
        self.driver.click("batch_mode")

    def select_book_mode(self):
        self.driver.click("book_mode")

    def select_auto_enhancements(self):
        self.driver.click("auto_enhancements")

    def select_auto_heal(self):
        self.driver.click("auto_heal")

    def select_auto_orientation(self):
        self.driver.click("auto_orientation")

    def select_auto_image_collection_view(self):
        """
        clicks the image collection icon that appears on top right of the Camera screen during auto capture
        :return:
        """
        self.driver.wait_for_object("auto_image_collection_view", timeout=10, interval=1).click()

    def select_source_button(self, invisible=False):
        """

        :return:
        """
        self.driver.wait_for_object("source_btn", invisible=invisible).click()

########################################################################################################################
#                                                                                                                      #
#                                                  Verification Flows
#                                                                                                                      #
########################################################################################################################

    def verify_adjust_boundaries_nav(self):
        """
        Verify Adjust Boundaries naviagation bar:

            - Adjust Boundaries title

        Device: Phone
        """
        self.driver.wait_for_object("adjust_boundaries_title")

    def verify_full_boundary_btn(self):
        """
        Verify full boundary button
        """
        self.driver.wait_for_object("full_boundary_btn")

    def verify_auto_boundary_btn(self):
        """
        Verify auto boundary button
        """
        self.driver.wait_for_object("auto_boundary_btn")

    def verify_allow_access_to_camera_text(self):
        """
        Verify text for allow access to the camera
        """
        self.driver.wait_for_object("allow_access_to_camera_text")

    def verify_enable_access_to_camera_link(self):
        """
        Verify the link to enable camera access
        """
        self.driver.wait_for_object("enable_access_to_camera_text")

    def verify_aio_needs_access_to_camera_text(self):
        """
        Verify text
        """
        self.driver.wait_for_object("_shared_dynamic_text", format_specifier=[
            self.get_text_from_str_id("aio_needs_access_to_camera_text").replace("%@", self.get_ios_device_type())])

    def verify_camera_screen(self, timeout=20, raise_e=True):
        """
        determines which type is selected and counts it
        :return: strings for AUTO or MANUAL
        """
        return self.driver.wait_for_object("capture_btn", timeout=timeout, raise_e=raise_e) is not False

    def verify_camera_btn(self):
        self.driver.wait_for_object("capture_btn")

    def verify_auto_btn(self):
        self.driver.wait_for_object("auto_btn")

    def verify_manual_btn(self):
        self.driver.wait_for_object("manual_btn")

    def verify_auto_capture_mode(self):
        '''
            auto capture mode is enabled if auto_btn have a value attribute equal to 1
        '''
        return self.driver.get_attribute("auto_btn", "value") == "1"

    def verify_manual_capture_mode(self):
        '''
            "Auto" button is disabled if auto_btn does not have a value attribute (default)
        '''
        return self.driver.get_attribute("auto_btn", "value") is None

    def verify_flash_btn(self):
        self.driver.wait_for_object("flash_btn")

    def verify_flash_mode_state(self, mode):
        if mode == FLASH_MODE.FLASH_OFF:
            if not self.driver.wait_for_object("default_flash_off", raise_e=False):
                logging.info("Flash not in given {} mode".format(mode))
        elif not self.driver.wait_for_object(mode, raise_e=False):
            logging.info("Flash not in given {} mode".format(mode))

    def verify_document_mode(self):
        self.driver.wait_for_object("document_mode")

    def verify_batch_mode(self):
        self.driver.wait_for_object("batch_mode")

    def verify_photo_mode(self):
        self.driver.wait_for_object("photo_mode")

    def verify_multi_item_mode(self):
        self.driver.wait_for_object("multi_item_mode")

    def verify_book_mode(self):
        self.driver.wait_for_object("book_mode")

    def verify_auto_enhancements(self):
        self.driver.wait_for_object("auto_enhancements")

    def verify_auto_heal(self):
        self.driver.wait_for_object("auto_heal")

    def verify_auto_orientation(self):
        self.driver.wait_for_object("auto_orientation")

    def verify_back_button(self):
        self.driver.wait_for_object("back_btn")

    def verify_adjust_boundaries_next_button(self):
        self.driver.wait_for_object("next_btn")

    def verify_allow_hp_smart_to_access_camera_screen(self):
        self.driver.wait_for_object("allow_hp_smart_access_camera")

    def verify_camera_adjust_text_to_capture_image(self):
        self.driver.wait_for_object("camera_adjust_text")

    def verify_source_button(self):
        self.driver.wait_for_object("source_btn")

    def verify_source_options(self, scanner=False):
        if scanner:
            self.driver.wait_for_object(self.OPTION_SCANNER)
        self.driver.wait_for_object(self.OPTION_FILES)
        self.driver.wait_for_object(self.OPTION_CAMERA)

    def return_capture_image(self):
        return saf_misc.load_image_from_base64(self.driver.wdvr.get_screenshot_as_base64())

    def capture_multiple_photos_by_auto_mode(self, no_of_images=2, timeout=30):
        timeout = time.time() + timeout
        while time.time() < timeout:
            try:
                captured_images = self.driver.get_attribute(obj_name="auto_image_collection_view", attribute='value')
                if int(captured_images) >= no_of_images:
                    logging.info("no of pages {}".format(int(captured_images)))
                    self.driver.click("auto_image_collection_view")
                    break
                else:
                    time.sleep(5)
            except (NoSuchElementException, ValueError):
                continue

    def verify_popup_message(self, popup_title):
        self.driver.wait_for_object(popup_title)
        self.driver.wait_for_object("_shared_no")
        self.driver.wait_for_object("_shared_yes")

    def verify_capture_preference_screen(self, raise_e=True):
        return self.driver.wait_for_object("capture_preference", raise_e=raise_e) is not False

    def verify_adjust_scan_coach_mark(self, raise_e=True):
        return self.driver.wait_for_object("adjust_scan_coach_mark", raise_e=raise_e) is not False

    def verify_preset_coach_mark(self, raise_e=True):
        return self.driver.wait_for_object("camera_preset_coach_mark", raise_e=raise_e) is not False

    def verify_capture_coach_mark(self, raise_e=True):
        return self.driver.wait_for_object("camera_capture_coach_mark", raise_e=raise_e) is not False

    def verify_source_coach_mark(self, raise_e=True):
        return self.driver.wait_for_object("camera_source_coach_mark", raise_e=raise_e) is not False

    def verify_gear_setting_btn(self):
        self.driver.wait_for_object("scan_setting_gear")

########################################################################################################################
#                                                                                                                      #
#                                                  Functionality Related sets
#                                                                                                                      #
########################################################################################################################

    def capture_manual_photo_by_camera(self, mode):
        """
        manual capture and skips adjust boundary screen
        :return:
        """
        #TODO - Update below steps as per new Scan story changes
        # self.select_manual()
        # self.select_flash_mode(mode)
        if self.verify_second_close_btn() is not False:
            self.select_second_close_btn()
        self.select_capture_btn()
        time.sleep(1)
        self.verify_adjust_boundaries_nav()
        self.select_adjust_boundaries_next()

    def verify_top_bar(self):
        self.verify_close()
        self.verify_flash_mode_state(FLASH_MODE.FLASH_OFF)
        self.verify_gear_setting_btn()

    def verify_bottom_bar(self, acc_type="normal"):
        self.verify_source_button()
        self.verify_preset_sliders(acc_type=acc_type)
        self.verify_camera_btn()

    def verify_camera_ui_elements(self, acc_type="normal"):
        self.verify_top_bar()
        self.verify_camera_adjust_text_to_capture_image()
        self.verify_bottom_bar(acc_type=acc_type)

    def verify_camera_ui_elements_for_copy_functionality(self):
        self.verify_camera_btn()
        self.verify_auto_btn()
        self.verify_manual_btn()
        self.verify_flash_mode_state(FLASH_MODE.FLASH_OFF)
        self.verify_camera_adjust_text_to_capture_image()
        self.verify_close()

    def verify_adjust_boundaries_ui_elements(self):
        self.verify_adjust_boundaries_nav()
        self.verify_adjust_boundaries_next_button()
        self.verify_back_button()
        self.verify_auto_boundary_btn()
        self.verify_full_boundary_btn()

    def verify_allow_access_to_camera_ui_elements(self):
        self.verify_close()
        self.verify_aio_needs_access_to_camera_text()
        self.verify_enable_access_to_camera_link()
        self.verify_allow_access_to_camera_text()

    def select_source_option(self, option):
        self.driver.wait_for_object(option).click()

    def verify_preset_sliders(self, acc_type="normal"):
        self.verify_document_mode()
        self.verify_photo_mode()
        self.verify_batch_mode()
        if acc_type == "hpplus":
            self.verify_multi_item_mode()
            self.verify_book_mode()

    def verify_capture_preference_options(self):
        self.verify_auto_enhancements()
        # self.verify_auto_heal()
        self.verify_auto_orientation()

    def verify_preset_default_capture_mode(self):
        self.select_photo_mode()
        self.verify_manual_capture_mode()
        self.select_batch_mode()
        self.verify_auto_capture_mode()
        self.select_document_mode()
        self.verify_manual_capture_mode()
