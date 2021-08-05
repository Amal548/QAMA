from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Scan_Jobs(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.local_files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]
        cls.is_pdf = {"pdf": True, "jpg": False}
        cls.fc.set_hpid_account("hp+", claimable=True)
        # Clean up Download and Pictures folders before testing
        cls.fc.clean_up_download_and_pictures_folders()

        def clean_up_class():
            # Clean up Download and Pictures folders after testing
            cls.fc.clean_up_download_and_pictures_folders()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("scan_settings", ["color,75,3.5x5",
                                               "color,100,4x6",
                                               "color,200,5x7",
                                               "color,300,letter",
                                               "color,300,a4",
                                               "black,75,3.5x5",
                                               "black,100,4x6",
                                               "black,200,5x7",
                                               "black,300,letter",
                                               "black,300,a4"
                                               ])
    def test_01_scan_with_settings(self, scan_settings):
        """
        Descriptions:
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Change Scan Settings base on each test case
            4/ Click on Scan button
            5/ Click Save button at Landing Page as pdf
        Expected Result:
            Verify:
               4/ Scan successfully
               5/ Pull scanned file from hpscan folder in mobile device
                    and check file's size according settings in order of list above:
                        01 - 3787
                        02 - 5818
                        03 - 27062
                        04 - 116234
                        05 - 120494
                        06 - 2469
                        07 - 4194
                        08 - 18604
                        09 - 116139
                        10 - 120745
        :param scan_settings: scan settings for scan job
        """
        scan_settings = scan_settings.split(",")
        color_settings = {"color": self.scan.COLOR_OPT_COLOR, "black": self.scan.COLOR_OPT_BLACK}
        resolution_settings = {"75": self.scan.RESOLUTION_75,
                               "100": self.scan.RESOLUTION_100,
                               "200": self.scan.RESOLUTION_200,
                               "300": self.scan.RESOLUTION_300}
        paper_settings = {"3.5x5": self.scan.PAPER_SIZE_3_5, "4x6": self.scan.PAPER_SIZE_4_6,
                          "5x7": self.scan.PAPER_SIZE_5_7, "letter": self.scan.PAPER_SIZE_LETTER,
                          "a4": self.scan.PAPER_SIZE_A4}
        self.__load_scan_screen(is_tile=False)
        self.scan.select_scan_settings_btn()
        self.scan.select_source_option(self.scan.SOURCE_OPT_GLASS)
        self.scan.select_color_option(color_opt=color_settings[scan_settings[0]])
        self.scan.select_resolution_option(resolution_opt=resolution_settings[scan_settings[1]])
        self.scan.select_scan_settings_close()
        self.scan.select_scan_size(size_opt=paper_settings[scan_settings[2]])
        self.scan.verify_current_settings_info(
            "{}, {}".format(self.scan.get_text_from_str_id(color_settings[scan_settings[0]]),
                            self.scan.get_text_from_str_id(self.scan.SOURCE_GLASS_SHORT)))
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
            self.scan.verify_successful_scan_job()
        self.preview.verify_preview_nav(is_edit=True)

    def test_02_scan_add_page_disable_scan_settings(self):
        """
        Descriptions:
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Click on Scan button
            4/ At Landing Page, click on Add icon button
            5/ At Scan screen, click on Scan icon button
        Expected Result:
            Verify:
               3/ Scan successfully
               4/ Scan screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p)
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_add()
        self.scan.verify_scan_screen()
        self.scan.select_scan_settings_btn()
        self.scan.verify_scan_screen()

    def test_03_scan_multiple_pages_print(self):
        """
        Description
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement print
        Expected Result:
            4/ Print successfully
        """
        self.__home_make_scan_two_pages()
        self.fc.flow_preview_make_printing_job(self.p, jobs=1)

    @pytest.mark.parametrize("file_type", ["pdf", "jpg"])
    def test_04_scan_multiple_pages_share_gmail(self, file_type):
        """
        Description
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement Gmail sharing as PDF/JPG on landing page
        Expected Result:
            4/ Gmail sharing successfully successfully
        """
        file_name = "{}_{}".format(self.test_04_scan_multiple_pages_share_gmail.__name__, file_type)
        self.__home_make_scan_two_pages()
        self.preview.select_bottom_nav_btn(self.preview.SHARE_BTN)
        self.preview.verify_option_screen(self.preview.SHARE_OPTION_TITLE)
        self.preview.make_action_option(file_name, is_pdf=self.is_pdf[file_type])
        self.fc.flow_preview_share_via_gmail(self.email_address,
                                             file_name,
                                             from_email=self.email_address)

    @pytest.mark.parametrize("file_type", ["pdf", "jpg"])
    def test_05_scan_multiple_pages_save(self, file_type):
        """
        Description
            1/ Load Home screen and select printer
            2/ Load Scan via tile
            3/ Make Scan job with multiple pages (using Add icon on Landing Page)
            4/ Implement Save as PDF/JPG on landing page
        Expected Result:
            4/ Save successfully via checking file name in Print Document
        """
        file_name = "{}_{}".format(self.test_05_scan_multiple_pages_save.__name__, file_type)
        self.__home_make_scan_two_pages()
        self.preview.select_bottom_nav_btn(self.preview.SAVE_BTN)
        self.preview.verify_option_screen(self.preview.SAVE_OPTION_TITLE)
        self.preview.make_action_option(file_name, is_pdf=self.is_pdf[file_type])
        if self.is_pdf[file_type]:
            self.local_files.save_file_to_downloads_folder(file_name)
        self.preview.dismiss_saved_files_message_popup()
        self.preview.verify_preview_nav()
        if self.is_pdf[file_type]:
            self.fc.verify_existed_file("{}/{}.pdf".format(TEST_DATA.MOBILE_DOWNLOAD, file_name))
        else:
            self.fc.verify_existed_file("{}/{}.jpg".format(TEST_DATA.MOBILE_PICTURES, file_name))

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_scan_screen(self, is_tile=False):
        """
        If current screen is not Scan screen, load it via following steps:
            - Load Home screen
            - Select target printer
            - Load Scan screen via tile or icon on bottom navigation
        :param is_tile: from Scan tile or icon on bottom navigation
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_load_scan_screen(self.p, from_tile=is_tile)

    def __home_make_scan_two_pages(self):
        """
        Make a scan job with 2 pages from Home screen
            - At Home, select printer
            - Click on target tile name for scanning (scan, scan to email, scan to cloud)
            - At Scan screen, click on Scan
            - At Landing Page, click on Add icon
            - Click on Scan again on Scan screen
            - Verify Landing Page
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p)
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_add()
        self.scan.verify_scan_screen()
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
            self.scan.verify_successful_scan_job()
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.verify_multiple_pages("2")