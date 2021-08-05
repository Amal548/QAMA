from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from selenium.common.exceptions import TimeoutException
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}

class Test_Suite_01_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        # Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.fc.set_hpid_account("hp+", True, False)

        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    def test_01_scan_multiple_pages(self):
        """
        Description:
            1/ Load Home screen
            2/ Connect to target printer and make a scan job for single page with default scan settings
             (If scan tile is not on Home screen, then enable it in Personalize screen)
            3/ At Preview, add 1 more page via Add icon button
        Expected Result:
            3/ Verify Preview:
                 - Navigation bar: Back, Edit, and 3dots icon buttons, and  Preview title
                 - There are at least 3 icons at bottom navigation bar
                 - Total page is "2"
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p)
        self.preview.verify_preview_nav()
        self.preview.select_add()
        self.scan.verify_scan_screen()
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
        self.scan.verify_successful_scan_job()
        self.preview.verify_preview_nav()
        self.preview.verify_multiple_pages("2")
        self.preview.verify_bottom_nav_btn(self.preview.PRINT_BTN)
        self.preview.verify_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_bottom_nav_btn(self.preview.SAVE_BTN)

    def test_02_scan_pdf_share_gmail(self):
        """
        Description:
            1/ Load Home screen
            2/ Connect to target printer and make a scan job for single page with default scan settings
            (If scan tile is not on Home screen, then enable it in Personalize screen)
            3/ At Preview, click on Share btn on bottom navigation
            4/ Rename file name, toggle pdf on, click on bottom button
            5/ Go through Share flow to send an email via Gmail

        Expected Result:
            2/ Verify Preview:
                - Navigation bar: Back, Edit, and 3dots icon buttons, and  Preview title
                - Main button is "Share"
            3/ Share Option screen display
            5/ Verify that the email is sent to Gmail account.
        """
        file_name = self.test_02_scan_pdf_share_gmail.__name__
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p)
        self.preview.verify_preview_nav()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_option_screen(self.preview.SHARE_OPTION_TITLE)
        self.preview.make_action_option(file_name, is_pdf=True)
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                                  "{}".format(file_name),
                                             from_email=self.email_address)

    def test_03_scan_print_trapdoor_ui(self):
        """
        Description:
            1/ If current screen is not Preview from test 02, implement 2 first steps of test 02
            2/ At Preview, click on Print button on bottom navigation bar
            3/ If App Permission display, dismiss it.
            4/ Make a printing job via HPPS trapddor ui

        Expected Result:
            4/ Verify printing job on:
                - Printer
                - HPPS app via trapdoor ui
        """
        self.__scan_load_landing_page()
        self.fc.flow_preview_make_printing_job(self.p)

    def test_04_scan_pdf_save(self):
        """
        Description:
            1/ Continue test 03 by pressing Back key of mobile device.  If current screen is not Preview from test 02, implement 2 first steps of test 02
            2/ At Preview, click on Save button on bottom navigation bar
            3/ Rename file name, toggle pdf on, click on bottom button
            4/ Wait for toast message invisible

        Expected Result:
            2/ Save Option screen display
            4/ Verify Preview
        """
        file_name = self.test_04_scan_pdf_save.__name__
        self.driver.back()
        self.__scan_load_landing_page()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        self.preview.make_action_option(is_pdf=True)
        self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()
        self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))

    def test_05_scan_jpg_save(self):
        """
        Description:
            Save as test 04, but on Save Option screen, toggle pdf off

        Expected Result:
            2/ Save Option screen display
            4/ Verify Preview:
        """
        file_name = self.test_05_scan_jpg_save.__name__
        self.__scan_load_landing_page()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        self.preview.make_action_option(file_name, is_pdf=False)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()
        self.fc.verify_existed_file("{}/{}.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))

    #-----------------------       PRIVATE FUNCTIONS - ---------------------------------
    def __scan_load_landing_page(self):
        """
        If current screen is not Preview, make a scanning job with single page from home screen:
        """
        try:
            self.preview.verify_preview_nav()
        except TimeoutException:
            self.fc.flow_load_home_screen()
            self.fc.flow_home_scan_single_page(self.p)
            self.preview.verify_preview_nav()