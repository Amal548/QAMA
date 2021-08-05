from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
import pytest
import logging
from selenium.common.exceptions import TimeoutException, NoSuchElementException

pytest.app_info = "SMART"


class Test_Suite_01_Camera_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]
        cls.fc.set_hpid_account("hp+", True, False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    # @pytest.mark.parametrize("permission", ["allow_later", "deny_again"])
    # def test_01_camera_scan_app_permission_deny_first_and(self, permission):
    #     """
    #     Description:
    #     1. Install and Launch app for the first time
    #     2. Click on Camera Scan tile
    #     3. Click on DENY button
    #     4. Click on Go Back button
    #     5. - If allow later, then Click on ALLOW button
    #        - If deny again, then click Deny button
    #     Expected Result:
    #     2. Verify permission popup with:
    #        - DENY and Allow button
    #        - Message
    #     3. Verify "Are you sure?" popup with:
    #        - Deny button
    #        - Go Back button
    #     4. Verify permission popup with:
    #        - Don't ask again checkbox
    #        - DENY and ALLOW button
    #     5. - If allow later: then verify No Camera Access screen
    #        - If deny again: then verify "Are you sure?" popup
    #     """
    #     self.fc.reset_app()
    #     self.fc.flow_load_home_screen()
    #     self.fc.flow_home_verify_smart_app_on_userboarding()
    #     self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN), is_permission=False)
    #     assert (self.home.is_app_permission_popup()), "App Permission popup is not displayed"
    #     self.home.check_run_time_permission(accept=False)
    #     self.home.verify_deny_confirmation_popup()
    #     self.home.select_deny_confirmation_popup_go_back()
    #     self.home.verify_do_not_ask_checkbox()
    #     if permission == "allow_later":
    #         self.home.check_run_time_permission(accept=True)
    #         self.camera_scan.verify_capture_no_access_screen()
    #     else:
    #         self.home.check_run_time_permission(accept=False)
    #         self.home.verify_deny_confirmation_popup()

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_02_camera_scan_share_single_page(self, file_type):
        """
        Description:
        1. Launch app to Home screen, and click on Camera Scan tile
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on share button:
        7. Select share file type:
           - JPG file
           Or:
           - PDF file
        8. Click on Share button
        9. Select Gmail
        Expected Result:
        4. Verify Tips for Camera Capture screen
        9. Verify that the email is sent to Gmail account
        """
        file_name = "{}_{}".format(self.test_02_camera_scan_share_single_page.__name__, file_type)
        self.__camera_scan_load_landing_page(is_printer=False, is_multiple_page=False, btn_name=self.preview.SHARE_BTN)
        self.preview.verify_option_screen(self.preview.SHARE_OPTION_TITLE)
        if file_type == "jpg":
            self.preview.make_action_option(is_pdf=False)
        else:
            self.preview.make_action_option(is_pdf=True)
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_03_camera_scan_share_multiple_page(self, file_type):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on "Add More page" button
        7. Take picture with manual mode
        8. Click on Next button
        9. Click on share button:
        10. Select share file type:
           - JPG file
           Or:
           - PDF file
        11. Click on Share button
        12. Select Gmail
        Expected Result:
        8. Verify Preview screen with multiple pictures displays
        12. Verify that the email is sent to Gmail account
        """
        file_name = "{}_{}".format(self.test_03_camera_scan_share_multiple_page.__name__, file_type)
        self.__camera_scan_load_landing_page(is_printer=False, is_multiple_page=True, btn_name=self.preview.SHARE_BTN)
        self.preview.verify_option_screen(self.preview.SHARE_OPTION_TITLE)
        if file_type == "jpg":
            self.preview.make_action_option(is_pdf=False)
        else:
            self.preview.make_action_option(is_pdf=True)
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_04_camera_scan_save_single_page(self, file_type):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. CLick on Full option
        6. Click on Next button
        7. Click on Save button:
        8. Select Save file type:
           - JPG file
           Or:
           - PDF file
        9. Click on Save button
        10. Click on OK button
        Expected Result:
        9. Verify Save successfully popup
        10. Verify Preview screen
        """
        file_name = "{}_{}".format(self.test_04_camera_scan_save_single_page.__name__, file_type)
        self.__camera_scan_load_landing_page(is_printer=False, is_multiple_page=False, btn_name=self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        if file_type == "jpg":
            self.preview.make_action_option(file_name, is_pdf=False)
        else:
            self.preview.make_action_option(file_name, is_pdf=True)
            self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()

    @pytest.mark.parametrize("file_type", ["jpg", "pdf"])
    def test_05_camera_scan_save_multiple_page(self, file_type):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. CLick on Full option
        6. Click on Next button
        7. Click on "+" button on preview screen
        8. Take picture with manual mode
        9. Click on Next button
        10. Click on Save button:
        11. Select Save file type:
           - JPG file
           Or:
           - PDF file
        12. Click on Save button
        13. Click on OK button
        Expected Result:
        12. Verify Save successfully popup
        13. Verify Preview screen
        """
        file_name = "{}_{}".format(self.test_05_camera_scan_save_multiple_page.__name__, file_type)
        self.__camera_scan_load_landing_page(is_printer=False, is_multiple_page=True, btn_name=self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        if file_type == "jpg":
            self.preview.make_action_option(file_name, is_pdf=False)
        else:
            self.preview.make_action_option(file_name, is_pdf=True)
            self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()

    def test_06_camera_scan_captured_image_print(self):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on Print button, and make a printing job via HPPS trapdoor ui
        Expected Result:
        6. Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui
        """
        self.__camera_scan_load_landing_page(is_printer=True, is_multiple_page=False)
        self.fc.flow_preview_make_printing_job(self.p, jobs=1)

    @pytest.mark.parametrize("popup_option", ["cancel_btn", "leave_btn"])
    def test_07_camera_scan_are_you_sure_popup(self, popup_option):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Take picture with manual mode
        4. Click on OK button if Tips camera capture screen popup
        5. Click on Next button
        6. Click on Back button on Preview screen
        7. - If cancel_btn option: click on Cancel button
           - If leave_btn option, click on LEAVE button
        Expected Result:
        6. Verify popup with:
           - Title
           - CANCEL and LEAVE button
        7. - cancel_btn: verify preview screen
           - leave_btn: verify home screen
        """
        self.__camera_scan_load_landing_page()
        self.fc.select_back()
        self.preview.verify_leave_confirmation_popup()
        if popup_option == "cancel_btn":
            self.preview.select_leave_confirm_popup_cancel()
            self.preview.verify_preview_nav()
        else:
            self.preview.select_leave_confirm_popup_leave()
            if self.home.verify_feature_popup(raise_e=False):
                self.home.select_feature_popup_close()
            self.home.verify_home_nav()

    def test_08_camera_scan_adjust_boundaries_screen_with_photo_from_gallery(self):
        """
        Description:
        1. Launch app, and click on Camera Scan tile on Home screen
        2. Allow permission and Click on ALLOW ACCESS button
        3. Click on Photo Gallery option
        4. Select any photo
        Expected Result:
        3. Verify Select a photo screen with:
           - Title
           - album lists
        4. Verify Adjust Boundaries screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN))
        try:
            self.camera_scan.select_camera_access_allow()
            self.camera_scan.check_run_time_permission()
        except (TimeoutException, NoSuchElementException):
            logging.info("There is no 'Capture Allow'")
        self.camera_scan.select_gallery_option()
        self.local_photos.select_album_photo_by_index(album_name="png")
        self.camera_scan.dismiss_tips_camera_capture_popup()
        self.camera_scan.verify_camera_adjust_screen()

    # ---------------     PRIVATE FUNCTIONS     ----------------------
    def __camera_scan_load_landing_page(self, is_printer=False, is_multiple_page=False, btn_name=""):
        """
        1. Click on Camera Scan tile on Home screen
        2. Capture page/pages
        5. Click on navigation button, like:
           - PRINT_BTN
           - SAVE_BTN
           - SHARE_BTN
        :param is_printer: True or False
        :param is_multiple_page: True or False
        :param btn_name:
        """
        self.fc.flow_load_home_screen()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.fc.flow_home_camera_scan_pages(number_pages= 2 if is_multiple_page else 1)
        self.preview.verify_multiple_pages("2" if is_multiple_page else "1")
        if btn_name:
            self.preview.select_bottom_nav_btn(btn=btn_name)