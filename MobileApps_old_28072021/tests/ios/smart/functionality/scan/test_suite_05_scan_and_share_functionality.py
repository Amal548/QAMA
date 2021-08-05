import logging
import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.preview import Preview

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_05_Scan_And_Share_Funct(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session
        cls.printer_info = cls.p.get_printer_information()
        cls.stack = request.config.getoption("--stack")

        # Define Variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAIL_ACCOUNT))["email"]["account_01"][
            "username"]
        # Navigating to home screen
        cls.fc.go_home(stack=cls.stack)

        # Precondition_setup
        cls.fc.go_hp_smart_files_and_delete_all_files()
        cls.test_files = ["test1_" + cls.fc.get_random_str(), "test2_" + cls.fc.get_random_str()]
        cls.fc.scan_and_save_file_in_hp_smart_files(cls.p, cls.test_files[0], no_of_pages=1, file_type="jpg",
                                                    go_home=False)
        cls.fc.save_file_to_hp_smart_files_and_go_home(cls.test_files[1], cls.fc.fd["preview"].SHARE_AND_SAVE_BTN)

    def test_01_verify_default_scan_file_type_and_saved_file_type(self):
        """
        Scan image, validate default type, change file name and format in share/save screen, save and
        verify image saved accordingly- C27655334, - C17153731, C15077508
        :return:
        """
        file_types = ["jpg", "PDF", "PNG", "TIF", "HEIF"]
        file_names = []
        file_type_missing = []
        self.navigate_to_share_save_screen()
        assert self.fc.fd["preview"].verify_file_type_selected("jpg") is not False
        for file_type in file_types:
            file_name = 'scan_image_format_changed_' + file_type
            self.fc.fd["preview"].rename_file(file_name)
            if self.fc.fd["preview"].select_file_type(file_type) is True:
                self.fc.fd["preview"].select_navigate_back()
                self.fc.fd["preview"].verify_file_type_selected(file_type, raise_e=True)
                self.fc.fd["preview"].select_button(Preview.SHARE_AND_SAVE_BTN)
                self.fc.fd["share"].verify_share_popup()
                self.fc.fd["share"].select_save_to_hp_smart()
                file_names.append(file_name + "." + file_type.lower())
            else:
                file_type_missing.append(file_type)
            self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.go_hp_smart_files_screen_from_home()
        for file_name in file_names:
            # Validate file saved with selected format
            self.fc.fd["files"].verify_file_name_exists(file_name)
        logging.info("File type - {} is missing".format(file_type_missing))

    def test_06_validate_scan_and_share_email(self):
        """
        Scan image as type=pdf and verify share to email - C16017812, C15081185
        :return:
        """
        # General Setup
        self.navigate_to_share_save_screen()
        self.fc.fd["preview"].select_button(Preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["share"].select_mail()
        self.fc.send_and_verify_email(from_email_id=self.email_address, to_email_id=self.email_address,
                                      subject="scan_type_pdf_share")

    def test_09_verify_addition_of_files_and_photos_image_to_a_scanned_image_preview(self):
        """
        Scan any file, tap add in preview, select files and photos source, select a photo and
        verify photo added to preview successfully - C15967991
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == 1
        self.fc.fd["preview"].select_add_page()
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].select_files_photos_option()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].select_hp_smart_files_folder_icon()
        self.fc.fd["files"].verify_hp_smart_files_screen()
        self.fc.fd["files"].select_multiple_files(self.test_files)
        self.fc.fd["files"].select_next_btn()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == 3

    def test_10_verify_addition_of_files_and_photos_to_preview(self):
        """
        Navigate to scan screen, select Files & Photos source, select multiple files and import,
        and verify files opened in preview- C15968000
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].select_files_photos_option()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].select_hp_smart_files_folder_icon()
        self.fc.fd["files"].verify_hp_smart_files_screen()
        self.fc.fd["files"].select_multiple_files(self.test_files)
        self.fc.fd["files"].select_next_btn()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == 2

    def navigate_to_share_save_screen(self):
        if not self.fc.fd["preview"].verify_preview_screen_title(Preview.SHARE_AND_SAVE_TEXT):
            self.fc.go_scan_screen_from_home(self.p)
            self.fc.fd["scan"].select_scan_job_button()
            self.fc.fd["preview"].nav_detect_edges_screen()
            self.fc.fd["preview"].verify_preview_screen()
            self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_BTN)
