from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Photo_Edit(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.edit = cls.fc.flow[FLOW_NAMES.EDIT]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]

    def test_01_photo_edit_ui(self):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         
        Expected Results:
         2. Verify Edit screen with:
            - Title
            - Cancel button
            - Done button
            - Adjust / Filters / Crop / Text displays
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.verify_edit_ui_elements(self.edit.EDIT_OPTIONS[1:])
        self.edit.verify_edit_ui_elements(self.edit.EDIT_SCREEN_BUTTONS)
        
    @pytest.mark.parametrize("btn_name", ["cancel", "done"])
    def test_02_edit_cancel(self, btn_name):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. If btn_name == "cancel": Click on Cancel button
            If btn_name == "done": Click on Done button
         
        Expected Results:
         3. Verify Preview screen
        """
        self.fc.load_edit_screen_through_camera_scan()
        if btn_name == "cancel":
            self.edit.select_edit_cancel()
        else:
            self.edit.select_edit_done()
        self.preview.verify_preview_nav()
        
    @pytest.mark.parametrize("btn_name", ["yes", "no"])
    def test_03_discard_edits(self, btn_name):
        """
        Description:
         1. Load to Preview screen through Camera Scan
         2. Click on Edit button
         3. Click on Adjust, and do some change on Brightness
         4. Click on Done button
         5. Click on Cancel button
         6. If btn_name == yes, then click on Yes button
            If btn_name == no, then click on No button

        Expected Results:
         5. Verify Discard Edits? popup with:
            - Title
            - Yes and No button
         6. If btn_name == yes, then verify Preview screen
            If btn_name == no, then verify Edit screen
        """
        self.fc.load_edit_screen_through_camera_scan()
        self.edit.select_edit_main_option(self.edit.ADJUST)
        self.edit.select_edit_child_option(self.edit.BRIGHTNESS, direction="right", check_end=False, str_id=True)
        self.edit.verify_and_swipe_adjust_slider()
        self.edit.select_edit_done()
        self.edit.verify_edit_page_title()
        self.edit.select_edit_cancel()
        self.edit.verify_discard_edits_screen()
        if btn_name == "yes":
            self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[2])
            self.preview.verify_preview_nav()
        else:
            self.edit.select_discard_changes_btn(self.edit.DISCARD_EDIT_POP_UP_ELEMENTS[3])
            self.edit.verify_edit_page_title()
    
    def test_04_progress_screen_for_large_image(self):
        """
        Description: C17029648
         1. Launch Smart App
         2. Select View & Print Navbar Button
         3. Load Large image
         4. Make lots of edits
         5. Select Done on edit screen
        Expected Results:
         1. Exporting Image screen should appear after step 5
         2. Ends up at preview screen after Exporting Image popup close
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.select_local_item(self.files_photos.MY_PHOTOS_TXT)
        self.local_photos.select_album_photo_by_index("jpeg_oversized")
        self.preview.verify_preview_nav()
        self.preview.select_preview_image_opts_btn(self.preview.EDIT_BTN)
        for adjust_opt in (self.edit.BRIGHTNESS, self.edit.SATURATION, self.edit.CONTRAST, self.edit.CLARITY, self.edit.EXPOSURE, 
            self.edit.SHADOWS, self.edit.HIGHLIGHTS, self.edit.WHITES, self.edit.BLACKS, self.edit.TEMPERATURE):
            self.edit.verify_edit_ui_elements([self.edit.ADJUST])
            self.edit.select_edit_main_option(self.edit.ADJUST)
            self.edit.select_edit_child_option(adjust_opt, direction="right", check_end=False, str_id=True)
            self.edit.verify_and_swipe_adjust_slider(direction="left")
            self.edit.select_edit_done()
        self.edit.select_edit_done()
        self.edit.verify_export_progress_pop_up()
        self.edit.verify_export_progress_pop_up(invisible=True, timeout=30)
        self.preview.verify_preview_nav()
