import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.libs.flows.ios.smart.camera import Camera
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner":True}

class Test_Suite_02_Ios_Smart_Camera_UI_Validation(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.stack = request.config.getoption("--stack")
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.p = load_printers_session

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self):
        self.fc.go_home(reset=True, stack=self.stack)

    def test_01_verify_adjust_boundaries_ui(self):
        """
        C27655100
        1. Launch app for the first time and go to the camera screen and take a picture with camera
        Expected Results:
            Verify adjust boundaries ui and back button returns to camera screen
        """
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.fd["camera"].select_manual_option()
        self.fc.fd["camera"].select_capture_btn()
        self.fc.fd["camera"].verify_adjust_boundaries_ui_elements()
        self.fc.fd["camera"].select_navigate_back()
        if self.fc.fd["camera"].verify_second_close_btn() is not False:
            self.fc.fd["camera"].select_second_close_btn()
        self.fc.fd["camera"].verify_camera_screen()

    def test_02_verify_exit_without_saving_popup(self):
        """
        C27655090 Precondition: fresh install, printer with scanner
        1. scan an item -> add another page -> camera screen -> select camera from source button
        2. Tap on "Don't Allow" on popup, then X button
        Expected Results:
            Verify popup: "Unsaved pages will be lost" with "yes" and "no" options
        :return:
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd['scan'].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        if self.fc.fd["scan"].verify_second_close_btn() is not False:
            self.fc.fd["scan"].select_second_close_btn()
        self.fc.fd['scan'].verify_source_button()
        self.fc.fd['scan'].select_source_button()
        self.fc.fd['scan'].select_camera_option()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=False)
        self.fc.fd["camera"].verify_allow_access_to_camera_ui_elements()
        self.fc.fd["camera"].select_enable_access_to_camera_link()
        # TODO: popup is removed, fix after test case changes
        # self.fc.fd["camera"].verify_popup_message(popup_title=Camera.POPUP_UNSAVED_PAGES)

    def test_03_verify_unsaved_pages_lost_popup(self):
        """
        C15988055   Precondition: fresh install, printer with scanner
        1. scan an item -> add another page -> camera screen -> select camera from source button
        2. Tap on "Don't Allow" on popup -> Tap on link "enable access to camera", then tap no
        Expected Results:
            Verify pop up: "Exit without saving?" with "yes" and "no" options
        :return:
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd['scan'].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        if self.fc.fd["scan"].verify_second_close_btn() is not False:
            self.fc.fd["scan"].select_second_close_btn()
        self.fc.fd['scan'].verify_source_button()
        self.fc.fd['scan'].select_source_button()
        self.fc.fd['scan'].select_camera_option()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=False)
        self.fc.fd["camera"].verify_allow_access_to_camera_ui_elements()
        self.fc.fd["camera"].select_close()
        self.fc.fd["camera"].verify_popup_message(popup_title=Camera.POPUP_EXIT_WITHOUT_SAVING)

    def test_04_verify_page_addition_camera_disabled(self):
        """
        C15988054   Precondition: fresh install, printer with scanner
        1. scan an item -> add another page -> camera screen -> select camera from source button
        2. Tap on "Don't Allow" on popup and then tap on X button, press no on popup
        Expected Results:
            Verify print preview screen should be displayed with image from step 2
        :return:
        """
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd['scan'].select_scan_job_button()
        self.fc.fd["preview"].nav_detect_edges_screen()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        if self.fc.fd["scan"].verify_second_close_btn() is not False:
            self.fc.fd["scan"].select_second_close_btn()
        self.fc.fd['scan'].verify_source_button()
        self.fc.fd['scan'].select_source_button()
        self.fc.fd['scan'].select_camera_option()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup(allow_access=False)
        self.fc.fd["camera"].verify_allow_access_to_camera_ui_elements()
        self.fc.fd["camera"].select_close()
        self.fc.fd["camera"].select_exit_without_saving_popup(allow_save=False)
        self.fc.fd["preview"].verify_print_preview_collection_view()