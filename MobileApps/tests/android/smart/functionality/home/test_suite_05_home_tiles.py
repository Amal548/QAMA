from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import *
import pytest


pytest.app_info = "SMART"

class Test_Suite_05_Home_Tiles(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.app_settings = cls.fc.flow[FLOW_NAMES.APP_SETTINGS]
        cls.photo_books = cls.fc.flow[FLOW_NAMES.PHOTO_BOOKS]

    @pytest.mark.capture_screen
    def test_01_print_photos(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Print Photos tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Print Photos tile on Home screen
        Expected Result:
         4. Verify Print Photos screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.PRINT_PHOTOS)
        self.file_photos.verify_files_photos_screen()

    def test_02_print_docs(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Printer Documents tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Printer Documents tile on Home screen
        Expected Result:
         4. Verify Files and Photos screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.PRINT_DOCUMENTS)
        self.file_photos.verify_files_photos_screen()

    def test_03_help_support(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Get HP Help and Support tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Get HP Help and Support tile on Home screen
        Expected Result:
         4. Verify Get HP Help and Support screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.HELP_SUPPORT)
        self.app_settings.verify_help_support_screen()

    def test_04_printer_scan(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Scan tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Scan on Home screen
        Expected Result:
         4. Verify No Camera Access screen
        """
        self.__load_tile_screen(is_printer=True, tile_name=TILE_NAMES.PRINTER_SCAN)
        self.scan.verify_scan_screen()

    @pytest.mark.capture_screen
    def test_05_camera_scan(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Camera Scan tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Camera Scan on Home screen
        Expected Result:
         4. Verify No Camera Access screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.CAMERA_SCAN)
        self.camera_scan.verify_capture_no_access_screen()

    def test_06_copy(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Copy tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Copy on Home screen
        Expected Result:
         4. Verify No Camera Access screen
        """
        self.__load_tile_screen(is_printer=True, tile_name=TILE_NAMES.COPY)
        self.camera_scan.verify_capture_no_access_screen()

    def test_07_smart_tasks(self):
        """
        Description:
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Enable Smart Task tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Smart Task on Home screen
        Expected Result:
         4. Verify Smart Tasks learn more screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.SMART_TASKS)
        self.smart_tasks.verify_smart_tasks_screen()
    
    def test_08_create_photo_book(self):
        """
        Description:
         1. Load Home screen
         2. Enable Create Photo Book tile from Personalize screen if not enabled
         3. Click on Back button on Personalize screen
         4. Click on Create Photo Book on Home screen
        Expected Result:
         4. Verify Create Photo Book screen
        """
        self.__load_tile_screen(is_printer=False, tile_name=TILE_NAMES.CREATE_PHOTO_BOOKS)
        self.photo_books.verify_create_photo_books_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_tile_screen(self, is_printer=False, tile_name=""):
        """
        If current screen is not Home screen, load to Home screen.
        If there is no connected printer, select a target printer
        If current tile is not enabled on Home screen, then:
           - Click on Personalize tile
           - Enable current tile
           - Select back button to Home screen
           - Click on the tile you need
        - params: tile_name from constant TILE_NAME in flow container
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        if is_printer:
            self.fc.flow_home_select_network_printer(self.p, is_searched=True)
            self.fc.flow_home_verify_ready_printer(self.p.get_printer_information()["bonjour name"])
        if not self.home.verify_tile(self.home.get_text_from_str_id(tile_name), raise_e=False):
            self.home.select_personalize_tiles()
            self.personalize.toggle_tile_by_name(self.personalize.get_text_from_str_id(tile_name), on=True)
            self.personalize.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(tile_name))