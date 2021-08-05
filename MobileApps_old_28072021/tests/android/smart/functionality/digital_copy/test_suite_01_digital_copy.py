from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from SAF.misc import saf_misc
import time
from MobileApps.resources.const.android.const import PACKAGE


pytest.app_info = "SMART"

class Test_Suite_01_Digital_Copy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

    def test_01_copy_ui(self):
        """
        Description:
         1. Load Home screen with printer connected
         2. Enable Copy tile from Personalize screen
         3. Click on Copy tile from Home screen
         4. Click on ALLOW ACCESS button
         5. Click on Allow button
         6. Click on Capture button with Letter size
        Expected Result:
         6. Verify Copy preview screen with below points:
            + Title
            + Start Black button
            + Start Color button
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.verify_copy_preview_screen()

    @pytest.mark.parametrize("resize_type",["original_size", "fit_to_page", "fill_page"])
    def test_02_copy_resize_type(self, resize_type):
        """
        Description:
         1. Load to Copy preview screen
         2. Click on Resize button
         3. Select Resize type on Resize screen
            + Original Size
            + Fit to page
            + Fill page
        Expected Result:
         2. Verify Resize screen with below points:
            + Original Size
            + Fit to page
            + Fill page
         3. Verify Copy screen
        """
        resize_types = {
            "original_size": self.digital_copy.ORIGINAL_SIZE,
            "fit_to_page": self.digital_copy.FIT_TO_PAGE,
            "fill_page": self.digital_copy.FILL_PAGE
        }
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        current_resize_image = self.digital_copy.capture_resize_image()
        self.digital_copy.select_resize_btn()
        self.digital_copy.verify_resize_screen()
        self.digital_copy.select_resize_type(resize_types[resize_type])
        newest_resize_image = self.digital_copy.capture_resize_image()
        assert(saf_misc.img_comp(current_resize_image, newest_resize_image) != 0), "Resize type {} didn't select successfully!!!".format(resize_types[resize_type])

    def test_03_copy_number_of_copies(self):
        """
        Description:
         1. Load to Copy preview screen
         2. Click on Copies button
        Expected Result:
         2. Verify the maximum number of copy page is 9
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_copies_btn()
        max_page_numbers = max(map(int, self.digital_copy.get_all_nums_of_copies_screen()))
        assert(max_page_numbers == 9), "The maximum number {} in Copies page isn't 9".format(max_page_numbers)

    def test_04_copy_add_more_page(self):
        """
        Description:
         1. Load to Copy preview screen
         2. Click on Add more page button
         3. Click on Capture button with batch mode
        Expected Result:
         2. Verify Capture screen with below points:
            + Paper Size dropdown menu cannot click
         3. Verify Copy screen with below points:
            + Left and Right arrow is visible and clickable
            + Page of number is visible
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_add_btn()
        self.digital_copy.verify_paper_size_dropbox(is_enabled=False)
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE,is_copy=True)
        self.digital_copy.select_previous_page_btn()
        self.digital_copy.select_next_page_btn()
        self.digital_copy.verify_copy_page_number()

    def test_05_copy_print_help_ok(self):
        """
         Description:
         1. Load to Copy preview  screen
         2. Click on Print Help button under 3 dot icon
         3. Check 2 boxes
         4. Check the 3rd boxes, and click on OK button
        Expected Result:
         2. Verify Print Help screen with below points:
            + Title
            + 3 checkboxes
         3. OK button isn't clickable
         4. OK button is clickable -> Copy Preview screen display
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_print_help()
        self.digital_copy.verify_print_help_screen()
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINT_PLUGIN_CB)
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINTING_SETTINGS_CB)
        self.digital_copy.verify_ok_button(is_enabled=False)
        self.digital_copy.toggle_cb_on_print_help(self.digital_copy.PRINTER_SELECT_CB)
        self.digital_copy.verify_ok_button(is_enabled=True)
        self.digital_copy.select_printer_setup_help_ok_btn()
        self.digital_copy.verify_copy_preview_screen()

    @pytest.mark.parametrize("link_name",["open_google_play", "open_print_settings"])
    def test_06_copy_print_help_link_verify(self, link_name):
        """
        Description:
         1. Load to Copy preview  screen
         2. Click on Print Help button under 3 dot icon
         3. Click on Links on Print Help screen:
            + Open Printing Settings link
            + Google Play link
        Expected Result:
         3. Verify the link we clicked
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_print_help()
        if link_name == "open_google_play":
            self.digital_copy.select_link_on_print_help(self.digital_copy.OPEN_GOOGLE_PLAY)
            self.digital_copy.verify_google_play_link()
        else:
            self.digital_copy.select_link_on_print_help(self.digital_copy.OPEN_PRINT_SETTINGS)
            assert (self.driver.get_current_app_activity()[0] == PACKAGE.SETTINGS), "Android Settings is not launching"

    def test_07_copy_single_page_delete_single_page(self):
        """
        Description:
        1. Load to Copy preview  screen
        2. Click on x button on Copy screen
        Expected Result:
        2. Verify Camera Capture screen with below points:
           + Paper Size button can be clickable
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=1)
        self.digital_copy.verify_paper_size_dropbox(is_enabled=True)

    def test_08_copy_2_pages_delete_single_page(self):
        """
        Description:
        1. Load to Copy preview screen
        2. Click on Add more page button on Copy screen
        3. CLick on capture button with batch mode
        4. Click on x button on Copy screen
        Expected Result:
        4. Verify Copy screen with below points:
           + previous and next page button are invisible
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_add_btn()
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, is_copy=True)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=1)
        self.digital_copy.verify_previous_next_page_btn(invisible=True)

    def test_09_copy_3_pages_delete_single_page(self):
        """
        Description:
        1. Load to Copy preview screen
        2. Click on Add more page button on Copy screen
        3. CLick on capture button with batch mode
        4. Click on Add more page button on Copy screen
        5. CLick on capture button with manual mode
        6. Click on x button on Copy screen
        Expected Result:
        6. Verify Copy screen with below points:
           + number of page is visible
           + previous and next page button are visible
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        # Digital copy with Batch mode on smart app is not ready for multi page function
        for _ in range(2):
            self.digital_copy.select_add_btn()
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=1)
        self.digital_copy.verify_previous_next_page_btn(invisible=False)
        self.digital_copy.verify_copy_page_number(invisible=False)

    def test_10_copy_multi_pages_delete_all_pages(self):
        """
        Description:
        1. Load to Copy preview screen
        2. Click on Add more page button on Copy screen
        3. CLick on capture button with batch mode
        4. Click on x button on Copy screen
        5. Click on x button on Copy screen
        Expected Result:
        5. Verify Camera Capture screen with below points:
           + Paper Size button can be clickable
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.select_add_btn()
        self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
        self.digital_copy.select_delete_page_btn(num_of_del_pages=2)
        self.digital_copy.verify_paper_size_dropbox(is_enabled=True)

    def test_11_copy_are_you_sure_popup(self):
        """
        Description:
        1. Load to Copy preview  screen
        2. Click on Back button from left top
        Expected Result:
        2. Verify Are you sure screen with below points:
           + Title
           + CANCEL button
           + LEAVE button
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.driver.press_key_back()
        self.digital_copy.verify_are_you_sure_popup()

    # Currently this function only verify Copy send success on App side, Skip for verifying printing job on printer success or not as defect INOS-3861
    @pytest.mark.parametrize("pages_number", ["1_copy_1_page", "1_copy_multi_pages", "multi_copies_1_page", "multi_copies_pages"])
    def test_12_start_color_copy_by_pages(self, pages_number):
        """
        Description:
        1. Load to Copy preview screen
        2. Please select copy page and numbers (X X) based on parameter of "pages_number"
           + 1 copy 1 page
           + 1 copy with multi pages:
               + click add more page button
               + click on capture button with batch mode
           + multi copies with 1 page:
               + click on Copies button
               + Select 2 copies
           + multi copies and pages:
               + click add more page button
               + click on capture button with batch mode
               + click on Copies button
               + select 3 copies
        3. Click on Start Color Copy button on Copy screen
        Expected Result:
        3. Verify Copy sent screen with below points:
           + Sent! Message
           + Home button
           + Back button
        :param pages_number:
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        if pages_number == "1_copy_multi_pages":
            self.digital_copy.select_add_btn()
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
        elif pages_number == "multi_copies_1_page":
            self.digital_copy.select_num_of_copies(copies_num=2)
        elif pages_number == "multi_copies_pages":
            self.digital_copy.select_add_btn()
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
            self.digital_copy.select_num_of_copies(copies_num=3)
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_type(self.digital_copy.FIT_TO_PAGE)
        self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=True)

    # Currently this function only verify Copy send success on App side, Skip for verifying printing job on printer success or not as defect INOS-3861
    @pytest.mark.parametrize("pages_number", ["1_copy_1_page", "1_copy_multiple_pages", "multi_copies_pages", "multi_copies_1_page"])
    def test_13_start_black_copy_by_pages(self, pages_number):
        """
        Description:
        1. Load to Copy preview screen
        2. Please select copy page and numbers (X X) based on parameter of "pages_number"
           + 1 copy 1 page
           + 1 copy with multi pages:
               + click add more page button
               + click on capture button with batch mode
           + multi copies with 1 page:
               + click on Copies button
               + Select 2 copies
           + multi copies and pages:
               + click add more page button
               + click on capture button with batch mode
               + click on Copies button
               + select 3 copies
        3. Click on Start Color Copy button on Copy screen
        Expected Result:
        3. Verify Copy sent screen with below points:
           + Sent! Message
           + Home button
           + Back button
        :param pages_number:
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        if pages_number == "1_copy_multi_pages":
            self.digital_copy.select_add_btn()
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
        elif pages_number == "multi_copies_1_page":
            self.digital_copy.select_num_of_copies(copies_num=3)
        elif pages_number == "multi_copies_pages":
            self.digital_copy.select_add_btn()
            self.camera_scan.capture_photo(mode=self.camera_scan.BATCH_MODE, number_pages=1, is_copy=True)
            self.digital_copy.select_num_of_copies(copies_num=2)
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_type(self.digital_copy.FIT_TO_PAGE)
        self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=False)

    @pytest.mark.capture_screen
    def test_14_access_copy_without_printer_connected(self):
        """
        Description:
        1. Load to Home screen without printer connected
        2. Click on Copy Tile
        Expected Result:
        2. Verify popup screen with below points:
           + Feature Unavailable tile
           + Message
           + OK button
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.COPY), is_permission=False)
        self.home.dismiss_feature_unavailable_popup(is_checked=True)
        self.home.verify_home_nav()