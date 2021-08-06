import pytest
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer
from MobileApps.resources.const.ios.const import *
from MobileApps.libs.ma_misc import ma_misc
from selenium.webdriver.support.ui import WebDriverWait

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Photomyne(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = session_setup
        cls.p = load_printers_session
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.home = cls.fc.fd["home"]

        def clean_up_class():
            cls.fc.go_hp_smart_files_and_delete_all_files()
        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("try_photomyne", [True, False])
    def test_01_photomyne_awareness_popup(self, try_photomyne):
        """
        C27655371, C27655372, C27655373
        capture 2 photos via camera scan, go home
        verify photomyne popup, tap on No Thanks or Try Photomyne
        """
        if try_photomyne:
            pytest.skip("AIOI-7754")
        self.fc.go_home(reset=True)
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(2)
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_photomyne_popup()
        if try_photomyne:
            self.fc.fd["home"].select_try_photomyne()
            # TODO: update after AIOI-7754 
            assert WebDriverWait(self.driver.wdvr, 20).until(lambda x: x.query_app_state("com.apple.mobilesafari") == 4)
            self.fc.fd["safari"].verify_photomyne_redirect_url()
        else:
            self.fc.fd["home"].select_no_thanks()
            self.fc.fd["home"].verify_home()
    
    def test_02_nonconsecutive_camera_scans(self):
        """
        C27655374
        capture 1 photo via camera scan and save file
        capture another photo via camera scan and go home, verify photomyne popup
        """
        self.fc.go_home(reset=True)
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_toolbar_icon(self.fc.fd["preview"].SHARE_AND_SAVE_TEXT)
        self.fc.save_file_to_hp_smart_files_and_go_home(self.test_02_nonconsecutive_camera_scans.__name__, "share_save_btn")
        self.fc.go_to_home_screen()
        self.fc.go_camera_screen_from_home(tile=True)
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_photomyne_popup()

    def test_03_photomyne_printer_scan(self):
        """
        C27655375
        scan 2 files, exit preview screen and verify photomyne popup
        """
        self.fc.go_home(reset=True)
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.add_multi_pages_scan(2)
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_photomyne_popup()

    @pytest.mark.parametrize("use_camera_scan", [True, False])
    def test_04_photomyne_nonconsecutive_scans(self, use_camera_scan):
        """
        C27655376, C27655377
        use printer to scan 1 file, save it and go home, perform 1)another scan or 2)camera capture,
        exit preview screen and go home to verify photomyne popup
        """
        self.fc.go_home(reset=True)
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_toolbar_icon(self.fc.fd["preview"].SHARE_AND_SAVE_TEXT)
        self.fc.save_file_to_hp_smart_files_and_go_home(self.test_04_photomyne_nonconsecutive_scans.__name__, "share_save_btn")
        self.fc.go_to_home_screen()
        if use_camera_scan:
            self.fc.go_camera_screen_from_home(tile=True)
            self.fc.fd["camera"].verify_camera_btn()
            self.fc.multiple_manual_camera_capture(1)
        else:
            self.fc.go_scan_screen_from_home(self.p)
            self.fc.fd["scan"].select_scan_job()
            self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_photomyne_popup()

    def test_05_photomyne_appears_only_once(self):
        """
        C27655378 
        trigger photomyne popup via 1 scan + 1 camera
        take 2 more scans and verify that popup doesn't appear again
        """
        self.fc.go_home(reset=True)
        self.fc.go_scan_screen_from_home(self.p)
        self.fc.fd["scan"].select_scan_job()
        self.fc.fd["preview"].verify_preview_screen()
        self.fc.fd["preview"].select_add_page()
        self.fc.fd['scan'].select_source_button()
        self.fc.fd['scan'].select_camera_option()
        self.fc.fd["camera"].select_allow_access_to_camera_on_popup()
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(1)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_photomyne_popup()
        self.fc.go_to_home_screen()
        self.fc.go_camera_screen_from_home(tile=False)
        self.fc.fd["camera"].verify_camera_btn()
        self.fc.multiple_manual_camera_capture(2)
        self.fc.fd["preview"].go_home_from_preview_screen()
        self.fc.fd["home"].close_smart_task_awareness_popup()
        self.fc.fd["home"].verify_home()