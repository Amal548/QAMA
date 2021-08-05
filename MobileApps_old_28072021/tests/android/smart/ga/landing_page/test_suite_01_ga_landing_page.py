from MobileApps.libs.flows.android.smart.flow_container import FlowContainer, FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import GOOGLE_PHOTOS
import pytest
import time

pytest.app_info = "SMART"

class Test_Suite_01_GA_LandingPage(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, require_driver_session, load_printers_session):
        cls = cls.__class__
        cls.driver = require_driver_session
        cls.p = load_printers_session

        #Define the flows
        cls.fc = FlowContainer(cls.driver)
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress

    def test_01_ga_landing_page(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Select target printer on the list (not from search icon)
        - Verify Home screen with connected printer
        - Click on Scan icon button on Navigation bar
        - Verify App permission screen
        - Click on ALLOW button
        - Verify Scan screen
        - Click on Scan button on scan screen
        - Verify Scan success or not screen
        - Verify landing page screen with Share button is highlight
        - Click on PDF
        - Click on More Option icon from right top
        - Click on Print Help button
        - Verify Print Help screen
        - Click on Open Google Play App Link
        - Verify Google Play screen
        - Click on back button from mobile device
        - Click on Open printing settings
        - Verify printing screen
        - Click on back button from mobile device
        - Click on back button from mobile device
        - Verify landing page screen
        - Click on Save button
        - Click on Save main button
        - Click on Share button from the bottom of navigation bar
        - Click on Share main blue button
        - Verify share screen
        - Select Gmail
        - Press back button on mobile device
        - Click on add new page button
        - Click on Scan button
        - Verify landing page screen
        - Click on Edit button
        - Verify Edit screen
        - Click on Rotate button
        - Verify Rotate screen
        - Click on left rotate button
        - Click on Crop button
        - Verify Crop screen
        - Click on Done button
        - Verify landing page screen
        - Click on Rename button
        - Verify Rename screen
        - Click on Cancel button
        - Click on back button on left top
        - Verify Are you sure? popup screen
        - Click on LEAVE button
        - Verify Home screen with printer connected
        - Click on Photo icon on Navigation bar
        - Verify Photo screen
        - Click on My Photos
        - Verify My photos screen
        - Select one album
        - Verify album detail screen
        - Select one photo
        - Verify landing page screen with Print button on
        - Click on Smart Task icon
        - Verify Smart Task screen
        - Press back button from mobile device
        - Verify landing page screen
        - Click on Print button
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.select_printer(self.printer_ip, wifi_direct=False, is_searched=True, keyword=self.printer_ip)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_scan(is_permission=True, ga=True)
        self.scan.verify_scan_screen()
        self.scan.select_scan_settings_btn()
        self.scan.verify_scan_settings_popup()
        self.scan.select_source_option(self.scan.SOURCE_OPT_GLASS)
        self.scan.select_color_option(self.scan.COLOR_OPT_COLOR)
        self.scan.select_resolution_option(self.scan.RESOLUTION_300)
        self.scan.select_scan_settings_close()
        self.scan.select_scan_size(self.scan.PAPER_SIZE_3_5)
        self.scan.select_scan()
        self.scan.verify_successful_scan_job(ga=True)
        self.preview.verify_preview_nav()
        self.preview.verify_action_btn(self.preview.SHARE_ACTION)
        self.preview.select_file_format(file_type=self.preview.PDF_BTN)
        self.preview.select_option_print_help()
        self.preview.verify_more_option_print_help()
        self.preview.select_print_help_google_play_link()
        self.preview.verify_google_play_link()
        self.driver.press_key_back()
        self.preview.select_print_help_printer_settings_link()
        self.driver.press_key_back()
        self.driver.press_key_back()
        self.preview.verify_action_btn(self.preview.SHARE_ACTION)
        self.preview.select_bottom_nav_icon(icon_type=self.preview.SAVE_ICON)
        self.preview.verify_action_btn(self.preview.SAVE_ACTION)
        self.preview.select_action_btn(action_type=self.preview.SAVE_ACTION, num_of_pages=1)
        time.sleep(5)
        self.preview.select_bottom_nav_icon(icon_type=self.preview.SHARE_ICON)
        self.preview.verify_action_btn(self.preview.SHARE_ACTION)
        self.preview.select_action_btn(action_type=self.preview.SHARE_ACTION, num_of_pages=2)
        self.preview.select_share_gmail()
        self.driver.press_key_back()
        self.preview.select_add()
        self.scan.verify_scan_screen()
        self.scan.select_scan()
        self.scan.verify_successful_scan_job(ga=False)
        self.preview.verify_preview_nav()
        self.preview.verify_action_btn(self.preview.SHARE_ACTION)
        self.preview.select_edit()
        self.preview.verify_edit_screen()
        self.preview.select_edit_rotate()
        self.preview.verify_visible_edit_rotate_btns()
        self.preview.select_edit_rotate_left()
        self.preview.select_edit_done()
        self.preview.verify_action_btn(self.preview.SHARE_ACTION)
        self.preview.select_file_name(fn_type=self.preview.SHARE_FILENAME_TF)
        self.preview.verify_rename_popup()
        self.preview.select_rename_popup_cancel()
        self.fc.select_back()
        self.preview.verify_leave_confirmation_popup()
        self.preview.select_leave_confirm_popup_leave(number_of_items_deleted=2)
        self.driver.press_key_back()
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_photos(is_permission=False)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.select_local_item(item_name=self.files_photos.MY_PHOTOS_TXT)
        self.photo.select_album_photo_by_index(album_name=GOOGLE_PHOTOS.JPEG)
        self.preview.verify_preview_nav()
        self.preview.verify_action_btn(self.preview.PRINT_ACTION)
        self.preview.select_bottom_nav_icon(icon_type=self.preview.SMART_TASKS_ICON)
        self.preview.verify_smart_tasks_welcome_screen()
        self.driver.press_key_back()
        self.preview.verify_action_btn(self.preview.SMART_TASKS_ACTION)
        self.preview.select_bottom_nav_icon(self.preview.PRINT_ICON)
        self.preview.select_action_btn(self.preview.PRINT_ACTION)