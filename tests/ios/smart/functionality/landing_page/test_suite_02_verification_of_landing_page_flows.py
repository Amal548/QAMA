import pytest

from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"

class Test_Suite_02_Verification_Of_Landing_Page_Flows(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.preview = cls.fc.fd["preview"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)
        cls.file_name = "4pages"

    def test_01_verify_ui_for_new_preview_landing_screen_single_photo(self):
        """
        Verify the UI for new preview landing screen for single photo - C27655363
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=2)
        self.preview.select_edit()
        self.fc.fd["edit"].verify_edit_page_title()
        self.preview.select_cancel()
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["photos"].verify_photos_screen()

    def test_02_verify_ui_for_new_preview_landing_screen_document(self):
        """
        Verify the UI for new preview landing screen for document - C27655356
        """

        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type="pdf", file_name=self.file_name)
        self.preview.verify_preview_screen()
        for page in range(1,5):
            total_pages, current_page = self.preview.get_no_pages_from_preview_label(get_current_page=True)
            assert current_page == page
            self.driver.swipe(direction="right")

    def test_03_verify_ui_for_new_preview_landing_screen_multiple_photos(self):
        """
        Verify the UI for new preview landing screen for multiple photos - C27655361
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=4)
        for image in range(1,5):
            self.preview.verify_preview_image_edit_btn()
            self.preview.verify_delete_page_x_icon()
            total_pages, current_page = self.preview.get_no_pages_from_preview_label(get_current_page=True)
            assert current_page == image
            self.driver.swipe(self.preview.PREVIEW_IMAGE, direction="right", per_offset=1)
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["photos"].verify_photos_screen()

    def test_04_verify_the_preview_for_xlsx_formats(self):
        """
        Verify the preview for xl files - C27655357
        """
        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type="xlsx", file_name=self.file_name)
        self.preview.verify_preview_screen()
        assert self.preview.get_no_pages_from_preview_label() == 1
    
    def test_05_verify_the_preview_for_docx_formats(self):
        """
        Verify the preview for docx files - C27655359
        """
        self.fc.navigate_to_google_drive_in_files()
        self.fc.select_file_in_google_drive(file_type="docx", file_name=self.file_name)
        self.preview.verify_preview_screen()
        assert self.preview.get_no_pages_from_preview_label() == 1

    # This test case is commented due to an issue faced where pptx files are not loaded on 
    # preview screen, will be added again after resolution of the issue
    # Issue: WPPX1-2099
    
    # def test_06_verify_the_preview_for_pptx_formats(self):
    #     """
    #     Verify the preview for pptx files - C27655358
    #     """
    #     self.fc.navigate_to_google_drive_in_files()
    #     import pdb
    #     pdb.set_trace()
    #     self.fc.select_file_in_google_drive(file_type="pptx", file_name=self.file_name)
    #     self.preview.verify_preview_screen()
    #     for page in range(1,5):
    #         total_pages, current_page = self.preview.get_no_pages_from_preview_label(get_current_page=True)
    #         assert current_page == page
    #         self.driver.swipe(self.preview.PREVIEW_IMAGE, direction="right", per_offset=1)

    def test_07_verify_choose_your_printer_button(self):
        """
        Verify "Choose your printer" button on Print Preview page - C27655365
        """
        self.fc.select_multiple_photos_to_preview(no_of_photos=1)
        self.preview.select_toolbar_icon(self.preview.PRINT)
        self.fc.fd["preview"].dismiss_print_preview_coach_mark()
        self.preview.verify_choose_your_printer_option()