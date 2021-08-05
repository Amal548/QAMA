import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer, sleep
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_07_add_files_send_fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")

        # Initializing Printer
        cls.p = load_printers_session

        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.fc.go_home(stack=cls.stack, button_index=1)

    def test_01_files_and_photos_ui(self):
        """
        Load to Compose fax screen and verify files and photos ui
        """
        self.fc.nav_to_compose_fax()
        self.compose_fax.verify_add_your_files_options()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.fd["files"].verify_files_screen()
        self.fc.fd["files"].verify_google_drive_image()
        self.fc.fd["files"].verify_google_photos()
        self.fc.fd["files"].verify_drop_box_image()
        self.fc.fd["files"].verify_box_image()
        self.fc.fd["files"].verify_ever_note_image()
        self.fc.fd["files"].verify_face_book_button()
        self.fc.fd["files"].verify_other_image()

    def test_02_add_multiple_images(self):
        self.fc.nav_to_compose_fax()
        self.compose_fax.verify_add_your_files_options()
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.fd["photos"].select_allow_access_to_photos_popup()
        self.fc.select_photo_from_my_photos(no_of_photos=2)
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()

    def test_03_add_camera_images_and_send_fax(self):
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.CAMERA_BTN)
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(number=2)
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        sleep(1)
        self.compose_fax.click_send_fax_native_btn()
        # TODO: Added timeout using Android test example
        self.send_fax_details.verify_send_fax_status(timeout=600)

    def test_04_add_scan_images_and_send_fax(self):
        self.fc.go_to_home_screen()
        self.fc.add_printer_by_ip(printer_ip=self.p.get_printer_information()["ip address"])
        self.fc.fd["welcome"].allow_notifications_popup(raise_e=False)
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.SCANNER_BTN)
        self.fc.fd["scan"].select_scanner_if_first_time_popup_visible()
        self.fc.fd["scan"].select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.select_add_page()
        self.fc.fd["scan"].select_scan_job()
        self.preview.nav_detect_edges_screen()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        assert self.preview.get_no_pages_from_preview_label() == 2
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        sleep(5)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_send_fax_native_btn()
        # TODO: Added timeout using Android test example
        self.send_fax_details.verify_send_fax_status(timeout=600)
