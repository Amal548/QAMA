from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from selenium.common.exceptions import NoSuchElementException
import pytest
from MobileApps.resources.const.android.const import PACKAGE

pytest.app_info = "SMART"


class Test_Suite_01_Dropbox(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]

        # Define variables
        cls.dropbox_username = cls.fc.get_dropbox_acc()["username"]
        cls.dropbox_pwd = cls.fc.get_dropbox_acc()["password"]
        # Log out Drop box before starting testing
        cls.fc.flow_dropbox_logout()

    def test_01_dropbox_login(self):
        """
        Description:
            1. Load Home screen
            2. Click on Files icon on navigation bar
            3. Verify Dropbox button on Files screen
            4. CLick on Dropbox button
            5. Login to Dropbox via Choose an account popup
            6. Verify Dropbox button on Files screen
        Expected Result:
            Verify:
               3. Dropbox is enable with Log in text
               4. Access to account screen
               6. Dropbox is enable with account name (username)
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.verify_cloud_not_login(self.files_photos.DROPBOX_TXT)
        self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
        self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
        self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)

    def test_02_dropbox_ui(self):
        """
        Description:
            1. If current screen is not Dropbox, following step 1-4 of test 02
            2. Verify Dropbox screen
            3. CLick on 3 dots icon button
            4. Click on each button
        Expected Results:
            Verify:
              2. Dropbox screen:
                       - Dropbox title
                       - There are some folder in the list
              3. Verify the menu:
                       - Alphabetical button
                       - Date button
              4. Dropbox screen display after clicking without crash
        """
        self.__load_dropbox_screen(is_printer=False)
        self.online_docs.select_more_opts()
        self.online_docs.verify_more_opts_menu()
        self.online_docs.select_more_options_alphabetical()
        self.online_docs.verify_online_docs_screen(self.online_docs.DROPBOX_TXT)
        self.online_docs.select_more_opts()
        self.online_docs.select_more_options_date()
        self.online_docs.verify_online_docs_screen(self.online_docs.DROPBOX_TXT)

    @pytest.mark.parametrize("file_type", ["pdf", "jpeg", "jpg", "png"])
    def test_03_dropbox_printing(self, file_type):
        """
        Description:
            1. Load Home screen
            2. Select a target printer
            3. Click on Files icon on nav bar or Print from Dropbox tile
            4. If coming from Files icon, click on Dropbox button
            5. At Dropbox screen, select a file with its extension as test name
            6. Make a printing job via HPPS trap door
        Expected Result:
            Verify:
                6. printing job is successful on app and printer.
        :param file_type: file type for target file on Dropbox
        """
        target_files = {"pdf": "testdata_cloud/documents/pdf/1page.pdf",
                        "jpeg": "testdata_cloud/images/jpeg/fish.jpeg",
                        "jpg": "testdata_cloud/images/jpg/bow.jpg",
                        "png": "testdata_cloud/images/png/star.png"}
        self.__load_dropbox_screen(is_printer=True)
        self.online_docs.select_file(target_files[file_type])
        is_edit = False if file_type == "pdf" else True 
        self.fc.flow_preview_make_printing_job(self.p, jobs=1, is_edit=is_edit)

    @pytest.mark.parametrize("file_type", ["doc", "docx", "html", "ppt", "pptx", "txt", "xls", "xlsx",
                                           "bmp", "cur", "gif", "ico", "tif", "webp", "xbm"])
    def test_04_dropbox_unsupported(self, file_type):
        """
        Description:
            1. Load Home screen
            2. Select a target printer
            3. Click on Files icon on nav bar or Print from Dropbox tile
            4. If coming from Files icon, click on Dropbox button
            5. At Dropbox screen, select a album for each unsupported extension
        Expected Result:
            Verify:
                5. "File type not supported" display.
        :param file_type: file type for target file on Dropbox
        """
        main_folders = {"documents": "testdata_cloud/documents",
                        "images": "testdata_cloud/images"}
        doc_ext_list = ["doc", "docx", "html", "ppt", "pptx", "txt", "xls", "xlsx"]
        img_ext_list = ["bmp", "cur", "gif", "ico", "tif", "webp", "xbm"]
        self.__load_dropbox_screen(is_printer=False)
        if file_type in doc_ext_list:
            folder_path= main_folders["documents"]
        elif file_type in img_ext_list:
            folder_path = main_folders["images"]
        else:
            raise NoSuchElementException("{} is not in the list".format(file_type))
        self.online_docs.select_file("{}/{}".format(folder_path, file_type))
        self.online_docs.verify_displayed_file_not_supported_txt()

    def test_05_dropbox_logout(self):
        """
        Description:
            1. Load Home screen
            2. Click on Files icon on nav bar
            3. Long press on Dropbox
            4. Click on Log out btn
        Expected Result:
            Verify:
               3. Logout popup
               4. Files screen with Dropbox button and Log in text
        """
        self.fc.flow_load_home_screen()
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        self.files_photos.load_logout_popup(self.files_photos.DROPBOX_TXT)
        self.files_photos.verify_logout_popup()
        self.files_photos.logout_cloud_item(self.files_photos.DROPBOX_TXT)
        self.files_photos.verify_files_photos_screen()
        self.files_photos.verify_cloud_not_login(self.files_photos.DROPBOX_TXT)

    # -------------------       PRIVATE FUNCTIONS       --------------------------
    def __load_dropbox_screen(self, is_printer=True):
        """
        Load Dropbox screen from Home
        :param from_tile: load this screen via tile or Files
        :param log_in: log in to an account if login screen display.
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p)
            self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
        self.home.select_bottom_nav_btn(self.home.NAV_VIEW_PRINT_BTN)
        try:
            self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
        except NoSuchElementException:
            self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
            self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
            self.files_photos.verify_cloud_added_account(self.files_photos.DROPBOX_TXT, self.dropbox_username)
        self.files_photos.select_cloud_item(self.files_photos.DROPBOX_TXT)
        self.online_docs.verify_online_docs_screen(self.online_docs.DROPBOX_TXT)
        