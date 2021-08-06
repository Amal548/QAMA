import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"
pytest.printer_feature = {"scanner": True}

class Test_Suite_04_Camera_Scan_Enhancement(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        # Initializing Printer
        cls.sys_config = ma_misc.load_system_config_file()
        cls.camera = cls.fc.fd["camera"]
        cls.home = cls.fc.fd["home"]
        cls.stack = request.config.getoption("--stack")
        cls.fc.go_home(stack=cls.stack)

    def test_01_verify_coach_mark(self):
        '''
            test cases regarding coach marks:
            C28992225: verify coach mark
            C28992229: coach mark 2-nd page
            C28992230: coach mark 3-rd page
            C28992231: coach mark 4-th page
            C28992232: coach mark (X) button behavior
            C28992233: coach mark (tapping anywhere on screen behavior)
            C28992234: coach mark "<" back button
            C28992235: coach mark only show once
            C28992236: next coach mark page show up after dissmissing previous
        '''
        # TODO: the coach marks did not show in 1st time launch the camera scan, instead the 2nd time.
        # waiting for the issue to be fixed

        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        self.camera.select_allow_access_to_camera_on_popup()
        self.camera.select_popup_option(camera=True)
        # verify coach mark first page
        assert self.camera.verify_adjust_scan_coach_mark(raise_e=False) is True
        # verify tap anywhere will ignore previous coach marks
        self.driver.click_by_coordinates(area="mm")
        self.fc.go_to_home_screen()
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        # verify second coach mark
        assert self.camera.verify_preset_coach_mark(raise_e=False) is True
        self.camera.select_next()
        # verify back button
        assert self.camera.verify_capture_coach_mark(raise_e=False) is True
        self.camera.select_navigate_back()
        assert self.camera.verify_preset_coach_mark(raise_e=False) is True
        # verify third and fouth page
        self.camera.select_next()
        assert self.camera.verify_capture_coach_mark(raise_e=False) is True
        self.camera.select_next()
        assert self.camera.verify_source_coach_mark(raise_e=False) is True
        self.camera.select_next()
        # coach mark should disappear
        self.camera.verify_camera_screen()
        # restart and coach mark never show again
        self.driver.restart_app(BUNDLE_ID.SMART)
        self.home.select_tile_by_name(HOME_TILES.TILE_CAMERA_SCAN)
        assert self.camera.verify_adjust_scan_coach_mark(raise_e=False) is False
        assert self.camera.verify_capture_coach_mark(raise_e=False) is False
        assert self.camera.verify_preset_coach_mark(raise_e=False) is False
        assert self.camera.verify_source_coach_mark(raise_e=False) is False

    def test_02_verify_batch_auto_manual_functionality(self):
        '''
            C28749144 batch mode auto and manual toggle
            Verify Auto vs Manual toggle is available in the Top Black bar for Batch mode.
            Verify the functionality of the "Auto" remain the same as the previous functionality.
            only in batch mode
            C28888404 Verify 'Auto' capture option is available on replace flow for Batch
        '''
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_batch_mode()
        # batch default "auto" mode, the button will be marked as blue
        self.camera.verify_auto_btn()
        assert self.camera.verify_auto_capture_mode() is True
        # switch to "manual", only "auto" button is displayed
        self.camera.select_manual_option()
        assert self.camera.verify_manual_capture_mode() is True
        # capture image on manual mode
        self.camera.select_capture_btn()
        self.camera.select_auto_image_collection_view()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_delete_page_icon()
        self.fc.fd["preview"].select_replace_btn_on_preview()
        if self.camera.verify_second_close_btn() is not False:
            self.camera.select_second_close_btn()
        # Defect https://jira.cso-hp.com/browse/AIOI-13493: 
        # after clicking replace, the camera will enable auto mode automatically
        # it will capture image immediately and redirect to preview screen driver is not able to catch the screen
        # self.camera.verify_auto_btn()

    def test_03_verify_document_photo_auto_manual_functionality(self):
        self.fc.go_camera_screen_from_home(tile=True)
        # auto and manual capture in Document
        self.camera.select_document_mode()
        assert self.camera.verify_manual_capture_mode() is True
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_ui_elements()
        self.camera.select_navigate_back()
        if self.camera.verify_second_close_btn() is not False:
            self.camera.select_second_close_btn()
        self.camera.select_auto_btn()
        assert self.camera.verify_auto_capture_mode() is True
        self.camera.capture_multiple_photos_by_auto_mode()
        # auto and manual capture in photo
        self.camera.select_photo_mode()
        assert self.camera.verify_manual_capture_mode() is True
        self.camera.select_capture_btn()
        self.camera.verify_adjust_boundaries_ui_elements()
        self.camera.select_navigate_back()
        if self.camera.verify_second_close_btn() is not False:
            self.camera.select_second_close_btn()
        self.camera.select_auto_btn()
        assert self.camera.verify_auto_capture_mode() is True
        self.camera.capture_multiple_photos_by_auto_mode()

    def test_04_verify_setting_capture_preference_ui(self):
        '''
            C28759572
            Verify that tapping on the Gear settings should open the "Camera Preferences" screen to enable Page Lift Enhancement options
            Verify Camera Preferences Screen displays the following options (auto-enhancement, auto-heal, auto-orientation) with a toggle switch
        '''
        self.fc.go_camera_screen_from_home(tile=True)
        self.camera.select_gear_setting_btn()
        assert self.camera.verify_capture_preference_screen(raise_e=False) is True
        self.camera.verify_capture_preference_options()