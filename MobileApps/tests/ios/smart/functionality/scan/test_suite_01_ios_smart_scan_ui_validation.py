from time import sleep

import pytest

from MobileApps.libs.flows.common.edit.edit import Edit
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.flows.ios.smart.preview import Preview
from MobileApps.libs.flows.ios.smart.scan import Scan

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}


class Test_Suite_01_Ios_Smart_Scan_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")

    # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_first_time_scan_popup(self):
        """
        verify bottom action bar scan button and first time pop_up- C27655111
        :return:
        """
        self.fc.fd["home"].select_scan_icon()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()
        self.fc.fd["camera"].verify_document_mode()

    def test_02_verify_scan_screen_ui_elements(self):
        """
        Verifies all UI elements on scan screen- C14590689
        :return:
        """
        # Setup
        self.fc.go_scan_screen_from_home(self.p)

        # Validation
        self.fc.fd["scan"].verify_scan_screen_ui_elements()

    def test_03_verify_source_tray_ui_elements(self):
        """
        Verifies different options of source tray - C15077471
        :return:
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        # Verifies photo screen navigates through source button
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].verify_source_all_options()
        self.fc.fd["scan"].select_files_photos_option()
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].select_close()
        # Verifies camera screen navigates through from source button
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].select_camera_option()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["camera"].verify_camera_screen()
        # Verifies scanner screen navigates through from source button
        self.fc.fd["scan"].select_source_button()
        self.fc.fd["scan"].select_scanner_option()
        self.fc.fd["scan"].verify_scanner_screen()

    def test_06_verify_scan_job_print_and_share_preview_screen_ui_elements(self):
        """
        Verifies ui elements of preview screen after scanning a document - C27655333
        :return:
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job_button()
        sleep(2)
        self.fc.fd["preview"].nav_detect_edges_screen()
        # Validation
        assert self.fc.fd["preview"].verify_preview_screen() is not False
        self.fc.fd["preview"].select_print_btn()
        self.fc.fd["preview"].verify_print_preview_ui_elements(self.p.get_printer_information()["bonjour name"])
        self.fc.fd["preview"].select_navigate_back()
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        self.fc.fd["preview"].select_toolbar_icon(Preview.SHARE_AND_SAVE_BTN)
        self.fc.fd["preview"].verify_array_of_elements(Preview.SHARE_PREVIEW_UI_ELEMENTS)

    def test_07_verify_scan_edit_ui_elements(self):
        """
        Verifies ui elements of scan_edit screen after scanning a document - C16827461
        testing
        :return:
        """
        # General Setup
        self.fc.go_to_edit_screen_with_printer_scan_image(self.p)
        self.fc.fd["edit"].verify_edit_page_title()
        self.fc.fd["edit"].verify_edit_ui_elements(Edit.EDIT_OPTIONS)
        self.fc.fd["edit"].verify_edit_ui_elements(Edit.EDIT_SCREEN_BUTTONS)

    def test_08_verify_scan_job_preview_screen_ui_elements(self):
        """
        Verifies preview screen UI elements after scanning a document -
        :return:
        """
        # General Setup
        self.fc.go_scan_screen_from_home(self.p)
        no_of_pages = 2
        self.fc.add_multi_pages_scan(no_of_pages)
        # Validation
        assert self.fc.fd["preview"].verify_preview_screen() is not False
        self.fc.fd["preview"].verify_preview_screen_title(Preview.PREVIEW_TITLE)
        assert self.fc.fd["preview"].get_no_pages_from_preview_label() == no_of_pages
        assert self.fc.fd["preview"].verify_delete_button is not False
        self.fc.fd["preview"].verify_array_of_elements(Preview.PREVIEW_UI_ELEMENTS)