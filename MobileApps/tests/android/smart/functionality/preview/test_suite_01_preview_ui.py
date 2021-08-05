from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"

class Test_Suite_01_Preview_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.local_photos = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"]["username"]

    def test_01_preview_ui_single_page_from_photo(self):
        """
        Description:
        1. Load to Hom screen
        2. Click on View & Print on Home screen
        3. Click on My Photo on View & Print screen
        4. Select a photo

        Expected Results:
         4. Verify Preview screen with:
           + Preview title
           + Back button
           + Save button disappears (from_photo)
           "+" button disappears
           + "Edit" button displays
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=False)
        self.preview.verify_bottom_nav_btn(self.preview.SAVE_BTN, invisible=True)
        self.preview.verify_bottom_nav_btn(self.preview.SHARE_BTN, invisible=False)
        self.preview.verify_add_more_btn(invisible=True)

    def test_02_share_option_screen_from_photos(self):
        """
        Description:
         1. Load to Home screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan on Home screen
         5. Click on Scan button on Scan screen
         6. Click on Share button on Preview screen

        Expected Results:
         6. Verify Share Option screen is invisible:
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=False)
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_option_screen(self.preview.SHARE_OPTION_TITLE, invisible=True)

    def test_03_save_success_popup(self):
        """
        Description:
          1. Do app cache clear to make sure that app is launched first time.
          2. Load to Home screen
          3. Click on Add icon to access printers list
          4. Select a target printer
          5. Click on Printer Scan on Home screen
          6. Click on Scan button on Scan screen
          7. Click on Save button
          8. Click on Name field to rename the filename
          9. Click on Save button
          10. Click on Home screen
        Expected Results:
          9. Verify save success popup:
             + Message
             + OK button
          10. Verify Preview screen
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.make_action_option(self.test_03_save_success_popup.__name__,
                                        is_pdf=False)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()

    def test_04_preview_ui_single_page_from_scanner(self):
        """
        Description:
         1. Load to Hom screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan on Home screen
         5. Click on Scan button

       Expected Results:
         4. Verify Preview screen with:
           + Preview title
           + Back button
           + Edit button displays
           + Save button displays (from_scanner)
           + Share button displays (from_scanner)
           + "+" button displays
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.verify_bottom_nav_btn(btn=self.preview.SAVE_BTN)
        self.preview.verify_bottom_nav_btn(btn=self.preview.SHARE_BTN)
        self.preview.verify_add_more_btn()

    def test_05_preview_ui_multiple_page(self):
        """
        Description:
         1. Load to Hom screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan
         5. Click on Scan button
         6. Click on "+" button on Preview screen
         7. Click on Scan button

        Expected Results:
         7. Verify Preview screen with:
           + number of page "2/2" displays
           + Reorder button displays
        """
        self.__load_preview_screen(is_multiple=True, from_scanner=True)
        self.preview.verify_multiple_pages(total_pages="2")
        self.preview.verify_reorder_btn()

    @pytest.mark.parametrize("file_size", ["actual_size", "medium", "small"])
    def test_06_share_option_by_file_size(self, file_size):
        """
        Description:
         1. Load to Home screen
         2. Click on Add icon to access printers list
         3. Select a target printer
         4. Click on Printer Scan on Home screen
         5. Click on Scan button on Scan screen
         6. Click on Share button on Preview screen
         7. Click file size drop-down box
         8. Select a file zie
         9. Click on Share button

        Expected Results:
         8. Verify Share screen with file size select success

        :param file_size:
        """
        file_sizes = {
            "actual_size": self.preview.FILE_SIZE_ACTUAL,
            "medium": self.preview.FILE_SIZE_MEDIUM,
            "small": self.preview.FILE_SIZE_SMALL
        }
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.select_file_size(file_sizes[file_size])
        self.preview.verify_file_size_item(file_sizes[file_size])

    @pytest.mark.parametrize("file_name", ["all_charcters", "2020_02_20_13"])
    def test_07_share_option_file_name(self, file_name):
        """
        Description:
          1. Load to Home screen
          2. Click on Add icon to access printers list
          3. Select a target printer
          4. Click on Printer Scan on Home screen
          5. Click on Scan button on Scan screen
          6. Click on Share button on Preview screen
          7. Click on file name to rename file name
          8. Click on Share button
          9. Click on Gmail

        Expected Results:
          9. Make sure file can be shared success
        :param file_name:
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.make_action_option(file_name, is_pdf=True)
        self.fc.flow_preview_share_via_gmail(self.email_address, file_name, from_email=self.email_address)

    @pytest.mark.parametrize("format_type", ["jpg", "pdf"])
    def test_08_save_option_screen(self, format_type):
        """
        Description:
          1. Load to Home screen
          2. Click on Camera Scan on Home screen
          3. Click on Capture button on Camera scan screen, and click Next button to preview screen
          4. Click on Save button
          5. Select format type

        Expected Results:
          5. If format type = "JPG", then verify Save Option screen:
               + Title
               + Save button
               + Document size is invisible
           If format type = "PDF", then verify Save Option screen:
               + Title
               + Save button
               + Document size is visible
          :param format_type:
        """
        is_pdf = True if format_type == "pdf" else False
        self.fc.flow_load_home_screen()
        self.fc.flow_home_camera_scan_pages()
        self.preview.verify_preview_nav()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        self.preview.select_file_type_spinner_btn()
        self.preview.select_format_type(is_pdf=is_pdf)
        if is_pdf:
            self.preview.verify_document_size_item(invisible=False)
        else:
            self.preview.verify_document_size_item(invisible=True)

    def test_09_rename_filename_without_saving(self):
        """
        Description:
          1. Load to Home screen
          2. Click on Add icon to access printers list
          3. Select a target printer
          4. Click on Printer Scan on Home screen
          5. Click on Scan button on Scan screen
          6. Click on Save button
          7. Click on Name field to rename the filename
          8. Click on Back button from App

        Expected Results:
          8. Verify Preview screen:
             + Title
             + "+" button
             + Print/Share/Save/Smart Tasks/Fax button
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.rename_file_name(self.test_09_rename_filename_without_saving.__name__)
        self.fc.select_back()
        self.preview.verify_preview_nav()

    def test_10_delete_single_page(self):
        """
        Description:
        1. Load to preview  screen from printer scan
        2. Click on x button on preview screen
        Expected Result:
        2. verify printer scan screen
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_preview_image_opts_btn(self.preview.DELETE_BTN)
        self.scan.verify_scan_screen()

    def test_11_delete_all_pages(self):
        """
        Description:
        1. Load to preview  screen from printer scan
        2. Click on "+" button
        3. Click on Scan button
        4. Click on x button 2 times

        Expected Results:
        4. Pictures deleted success, and go back to Scan screen
        """
        self.__load_preview_screen(is_multiple=False, from_scanner=True)
        self.preview.select_add()
        self.scan.select_scan()
        self.scan.verify_successful_scan_job()
        self.preview.select_preview_image_opts_btn(self.preview.DELETE_BTN)
        self.preview.verify_multiple_pages("1")
        self.preview.select_preview_image_opts_btn(self.preview.DELETE_BTN)
        self.scan.verify_scan_screen()

    @pytest.mark.parametrize("back_btn", ["app", "mobile"])
    def test_12_preview_back_btn(self, back_btn):
      """
      Description:
        1. Load to preview  screen from printer scan
        2. Click on back button on preview screen
        3. if back_btn: then click on Leave button

        Expected Result:
        3. verify Home screen
      """
      self.__load_preview_screen(is_multiple=False, from_scanner=True)
      if back_btn == "app":
        self.fc.select_back()
      else:
        self.driver.press_key_back()
      self.preview.verify_leave_confirmation_popup()
      self.preview.select_leave_confirm_popup_leave()
      if self.home.verify_feature_popup(raise_e=False):
        self.home.select_feature_popup_close()
      self.home.verify_home_nav()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_preview_screen(self, is_multiple=False, from_scanner=True):
        """
        1. Load App to Home screen
        2. Connect a target printer
        3. Click on Scan from Home screen
        4. Click on Scan button

        :param is_multiple: scan one more page if it is true
        """
        self.fc.flow_load_home_screen()
        if from_scanner:
            self.fc.flow_home_scan_single_page(self.p, from_tile=True)
        else:
            self.fc.flow_home_load_photo_screen(self.p, from_tile=True)
            self.local_photos.select_album_photo_by_index(album_name="jpg")
            if "novelli" in self.p.p_obj.projectName:
                self.preview.verify_print_size_screen()
                self.preview.select_print_size_btn(self.preview.PRINT_SIZE_4x6_STANDARD)
        self.preview.verify_preview_nav()
        if is_multiple:
          self.preview.select_add()
          self.scan.select_scan()
          self.scan.verify_successful_scan_job()
          self.preview.verify_preview_nav()