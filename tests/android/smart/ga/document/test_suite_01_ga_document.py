from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES,TILE_NAMES
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import PACKAGE, TEST_DATA,LAUNCH_ACTIVITY
from selenium.common.exceptions import TimeoutException
import pytest
import logging

pytest.app_info = "SMART"

class Test_Suite_01_GA_Document(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]

        #Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF[TEST_DATA.ONE_PAGE_PDF.rfind("/") + 1:]
        cls.jpg_fn = TEST_DATA.BOW_JPG[TEST_DATA.BOW_JPG.rfind("/") + 1:]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

        # def clean_up_class():
        #     cls.fc.flow_home_delete_all_files_device_storage()

        # request.addfinalizer(clean_up_class)

    def test_00_transfer_test_data(self):
        """
        Descriptions:
            -> transfer 1 .pdf and 1 .jpg files to /hpscan/documents and images folder in mobile device

        """
        # Transfer .pdf file
        with open(ma_misc.get_abs_path(TEST_DATA.ONE_PAGE_PDF), 'rb') as f:
            data = f.read()
            path = "{}/{}".format(TEST_DATA.MOBILE_DOC_PATH, self.pdf_fn)
            self.driver.wdvr.push_file(path, data.encode('base64'))
            logging.debug("Pushed file to device: {}".format(path))

        # Transfer .jpg file
        with open(ma_misc.get_abs_path(TEST_DATA.BOW_JPG), 'rb') as f:
            data = f.read()
            path = "{}/{}".format(TEST_DATA.MOBILE_IMG_PATH, self.jpg_fn)
            self.driver.wdvr.push_file(path, data.encode('base64'))
            logging.debug("Pushed file to device: {}".format(path))

    def test_01_ga_document(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from search icon)
        - Verify Home Screen with printer connected
        - Click on Document icon on Navigation bar
        - Verify App Permission screen
        - Click on Allow button on App Permission screen
        - Verify Files screen
        - Click on PDFs
        - Verify PDFs screen
        - Click on More Option button
        - Click on Sort by
        - Select Date
        - Long press any a file
        - Click on delete button
        - Verify PDF file delete screen
        - Click on Yes button
        - Verify PDFs empty screen
        - Click on Back button of left top of screen

        - Verify File screen
        - Click on Scanned Files
        - Verify scanned-files screen
        - Click on More Option button
        - Click on Sort by
        - Select Date
        - Long press any a file
        - Click on delete button
        - Verify scanned-files delete screen
        - Click on Yes button
        - Verify scanned-file empty screen
        - Click on Back button on left top of screen
        - Verify File screen

        - Click on Google Drive
        - Verify Google Drive screen
        - Select one account
        - Click on OK button
        - Verify Files screen with Google Drive account login success
        - Click on Google Drive
        - Verify Google Drive screen
        - Click on More Option button
        - Click on Alphabetical
        - Click on More Option button
        - Click on Date
        - Click on Back button of left top of screen
        - Verify Files screen
        - Long press Google Drive account
        - Verify remove google drive account screen
        """
        self.driver.wdvr.start_activity(PACKAGE.SMART, LAUNCH_ACTIVITY.SMART)
        self.__verify_home_screen(is_status=False)
        self.home.select_big_add_icon()
        self.printers.select_printer(self.printer_ip, wifi_direct=False)
        self.__verify_home_screen(is_status=True)
        self.home.select_nav_file(is_permission=True, ga=True)
        self.files.verify_files_screen()

        # GA tracking for PDF files part
        self.files.select_files_doc_type(doc_type=self.files.FILES_PDF_TXT)
        self.__verify_file_and_delete_screen_by_files_type(title=self.files.FILES_PDF_TXT,
                                                           sort_type=self.files.SORT_BY_DATE, file_name=self.pdf_fn)
        self.__select_files_type(doc_type=self.files.FILES_PDF_TXT)
        self.files.verify_empty_list()
        self.__verify_files_screen_from_previous_screen()

        # GA tracking for Scanned-files part
        self.files.select_files_doc_type(doc_type=self.files.FILES_SCANNED_FILES_TXT)
        self.__verify_file_and_delete_screen_by_files_type(title=self.files.FILES_SCANNED_FILES_TXT,
                                                         sort_type=self.files.SORT_BY_DATE, file_name=self.jpg_fn)
        self.__select_files_type(doc_type=self.files.FILES_SCANNED_FILES_TXT)
        self.files.verify_empty_list()
        self.__verify_files_screen_from_previous_screen()

        # GA tracking for Google Drive
        self.files.select_online_doc_type(online_doc_type=self.files.FILES_GOOGLE_DRIVE_TXT, ga=True)
        self.online_docs.select_gdrive_gmail_account(gmail_address=self.email_address)


        self.files.select_online_doc_type(online_doc_type=self.files.FILES_GOOGLE_DRIVE_TXT, ga=False)
        self.online_docs.verify_online_docs_screen(cloud_name=self.online_docs.GOOGLE_DRIVE_TXT)

        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_alphabetical()
        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_date()
        self.fc.select_back()
        self.files.verify_files_screen()
        self.files.load_online_doc_logout_popup(doc_type=self.files.FILES_GOOGLE_DRIVE_TXT)
        self.files.verify_online_docs_logout_popup()
        self.files.select_logout()


    # ------------------        PRIVATE FUNCTIONS       ------------------------------------
    def __verify_home_screen(self, is_status=True):

        """
        Verify Home screen with "+" icon button
        """
        if is_status:
            self.home.verify_home_nav_add_printer_icon()
            try:
                self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
                status = "ready"
            except TimeoutException:
                status = "error/warning"
            self.home.verify_loaded_printer()
        else:
            self.home.verify_add_new_printer()

        tile_names = self.home.get_tile_titles()
        for tile_name in tile_names:
            if tile_name != self.home.get_text_from_str_id(TILE_NAMES.PERSONALIZE):
                self.home.verify_tile(tile_name)
        self.home.verify_home_nav(num_tile=len(tile_names))

    def __verify_file_and_delete_screen_by_files_type(self, title, sort_type, file_name):
        """
        1. Click on More Option  button on PDFs screen or Scanned-files screen
        2. Click on Rename button on both PDFs and Scanned-files screen
        :param title:
        :param sort_type:
        :param file_name:
        """
        self.files.verify_device_file_screen(title=title)
        self.files.select_sort_by_opt(sort_type=sort_type)
        self.files.select_file(file_name=file_name, long_press=True)
        self.files.select_device_file_delete_icon()
        self.files.verify_delete_popup()

    def __select_files_type(self, doc_type):
        """
        Click on PDFs or Scanned-files after we delete the file from previous file type
        :param doc_type:
        :return:
        """
        self.files.select_device_file_delete_popup_yes()
        self.fc.select_back()
        self.files.select_files_doc_type(doc_type=doc_type)

    def __verify_files_screen_from_previous_screen(self):
        """
        Verify File screen after clicking Back button from previous screen
        """
        self.fc.select_back()
        self.files.verify_files_screen()

