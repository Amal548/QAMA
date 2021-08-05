from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.resources.const.android.const import TEST_DATA
from selenium.common.exceptions import TimeoutException
import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc


pytest.app_info = "SMART"

class Test_Suite_01_GA_Home(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
        cls.photo = cls.fc.flow[FLOW_NAMES.LOCAL_PHOTOS]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.printer_settings = cls.fc.flow[FLOW_NAMES.PRINTER_SETTINGS]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.help_support = cls.fc.flow[FLOW_NAMES.HELP_SUPPORT]
        cls.online_docs = cls.fc.flow[FLOW_NAMES.ONLINE_DOCS]
        cls.how_print = cls.fc.flow[FLOW_NAMES.HOW_PRINT]
        cls.file_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.dropbox_username =saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_01"][
                "username"]
        cls.dropbox_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.CLOUD_ACCOUNT))["dropbox"]["account_01"][
            "password"]

        def clean_up_class():
            cls.fc.flow_dropbox_logout()

        request.addfinalizer(clean_up_class)

    def test_01_ga_home(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from Search icon)
        - Verify Home screen with printer connected
        - Click on top "+" icon on navigation bar
        - Verify Printers screen
        - Click on Back button
        - Verify Home screen with printer connected
        - Click on Personalize tile
        - Verify Personalize screen
        - Enable all tiles
        - Click on Back button
        - Verify Home screen with printer connected
        - Click on Scan icon
        - Verify App permission screen
        - Click on Allow button on permission screen
        - Verify Scan screen
        - Click on Back button in the top bar
        - Click on Camera Scan icon
        - Verify No Camera Access screen
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on File screen
        - Verify Files screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Photo icon
        - Verify Photo screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Printers icon
        - Verify My Printer screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Print Photos tile
        - Verify Photo screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Camera Scan to Email tile
        - Verify No Camera Access screen
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on HP Instant Ink/Get Cartridges tile
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on Print Facebook Photos tile
        - Verify Facebook albums screen
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on Printer Settings tile
        - Verify My Printer screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Print Documents tile
        - Verify Files screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Get HP and Support tile
        - Verify Get HP and Support screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on How to Print tile
        - Verify How to Print screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Scan to Email tile
        - Verify Scan to Email screen
        - Click on Back button
        - Verify Home screen with printer connected
        - Click on Scan to Cloud tile
        - Verify Scan to Cloud screen
        - Click on Back button
        - Verify Home screen with printer connected
        - Click on Camera Scan to Cloud tile
        - Verify No Camera Access screen
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on Scan tile
        - Verify Scan screen
        - Click on back button in the top bar
        - Verify Home screen with printer connected
        - Click on Camera Scan tile
        - Verify No Camera Access screen
        - Click on Button on device
        - Verify Home screen with printer connected
        - Click on Print from Google Drive tile
        - Verify Google Drive login screen
        - Click on CANCEL button
        - Verify Home screen with printer connected
        - Click on Print from Dropbox tile
        - Verify Dropbox login in screen
        - Click on Back button on device
        - Verify Home screen with printer connected
        - Click on Personalize tile
        - Verify Personalize screen
        - Click on back button on device
        - Verify Home screen with printer connected
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_printer(self.printer_ip, wifi_direct=False, is_searched=True, keyword=self.printer_ip)
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_add_icon()
        self.printers.verify_printers_screen()
        self.fc.select_back()
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()

        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PERSONALIZE), is_permission=False)
        self.personalize.verify_personalize_screen()
        tiles_list = [TILE_NAMES.PRINT_PHOTOS,
                      TILE_NAMES.CAMERA_SCAN_EMAIL,
                      TILE_NAMES.PRINT_FACEBOOK_PHOTOS,
                      TILE_NAMES.HP_INSTANT_INK_1,
                      TILE_NAMES.PRINT_DOCUMENTS,
                      TILE_NAMES.PRINTER_SETTINGS,
                      TILE_NAMES.HELP_SUPPORT,
                      TILE_NAMES.HOW_TO_PRINT,
                      TILE_NAMES.SCAN_EMAIL,
                      TILE_NAMES.SCAN_CLOUD,
                      TILE_NAMES.CAMERA_SCAN_CLOUD,
                      TILE_NAMES.PRINTER_SCAN,
                      TILE_NAMES.CAMERA_SCAN,
                      TILE_NAMES.GOOGLE_DRIVE,
                      TILE_NAMES.DROPBOX,
                      TILE_NAMES.COPY]
        for tile in tiles_list:
            tile_name = "{} {}".format(self.driver.return_str_id_value(TILE_NAMES.HP_INSTANT_INK_1),
                                       self.driver.return_str_id_value(
                                           TILE_NAMES.HP_INSTANT_INK_2)) if tile == TILE_NAMES.HP_INSTANT_INK_1 else self.driver.return_str_id_value(
                tile)
            self.personalize.toggle_tile_by_name(tile_name, on=True)
        self.__verify_home_screen_ga()
        self.home.verify_home_nav_add_printer_icon()

        # GA for icon on bottom of navigation bar
        self.home.select_nav_scan(ga=True)  # select scan icon on navigation bar
        self.scan.verify_scan_screen()
        self.__verify_home_screen_ga()

        # select camera scan icon on navigation bar
        self.home.select_nav_capture(is_permission=False, ga=True)
        self.camera_scan.verify_capture_no_access_screen()
        self.__verify_home_screen_ga()

        # select File icon on navigation bar
        #TODO need update the GA when GA spec is ready for this racking since photo and files merge into one screen
        self.home.select_nav_file(is_permission=False, ga=True)
        self.file_photos.verify_files_photos_screen()
        self.__verify_home_screen_ga()

        # select Photo icon on navigation bar
        # TODO need update the GA when GA spec is ready for this racking since photo and files merge into one screen
        self.home.select_nav_photos(is_permission=False)
        self.file_photos.verify_files_photos_screen()
        self.__verify_home_screen_ga()

        # select My Printer icon on navigation bar
        self.home.select_nav_my_printer(is_permission=False, ga=True)
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])
        self.__verify_home_screen_ga()

        # GA for all Tiles on Home screen
        # select Print Photos tile on Home screen
        # TODO need update the GA when GA spec is ready for this racking since photo and files merge into one screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS))
        self.file_photos.verify_files_photos_screen()
        self.__verify_home_screen_ga()

        # select Camera Scan to Email tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN_EMAIL), is_permission=False)
        self.camera_scan.verify_capture_no_access_screen()
        self.__verify_home_screen_ga()

        # select Print Facebook Photos tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_FACEBOOK_PHOTOS),
                                      is_permission=False)
        try:
            self.online_photos.verify_online_photos_screen(acc_type=self.online_photos.FACEBOOK_TXT)
        except TimeoutException:
            self.online_photos.verify_fb_login_confirmation_screen()
            self.online_photos.select_fb_confirmation_continue()
            self.online_photos.verify_online_photos_screen(acc_type=self.online_photos.FACEBOOK_TXT)
        self.__verify_home_screen_ga()

        # select Printer Settings tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SETTINGS),
                                      is_permission=False)
        self.printer_settings.verify_my_printer(self.p.get_printer_information()["bonjour name"])
        self.__verify_home_screen_ga()

        # select Print Document tile on Home screen
        # TODO need update the GA when GA spec is ready for this racking since photo and files merge into one screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINT_DOCUMENTS),
                                      is_permission=False)
        # self.file_photos.verify_files_photos_screen()
        self.__verify_home_screen_ga()

        # select Get HP Help and Support tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.HELP_SUPPORT),
                                      is_permission=False)
        self.help_support.verify_help_support_screen(expected_title=self.help_support.HP_HELP_SUPPORT_TXT)
        self.__verify_home_screen_ga()

        # select How to Print tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.HOW_TO_PRINT),
                                      is_permission=False)
        self.how_print.verify_how_to_print_screen()
        self.__verify_home_screen_ga()

        # select Scan to Email tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.SCAN_EMAIL),
                                      is_permission=False)
        self.scan.verify_scan_screen()
        self.__verify_home_screen_ga()

        # select Scan to Cloud tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.SCAN_CLOUD),
                                      is_permission=False)
        self.scan.verify_scan_screen()
        self.__verify_home_screen_ga()

        # select Camera Scan to Cloud tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN_CLOUD),
                                      is_permission=False)
        self.camera_scan.verify_capture_no_access_screen()
        self.__verify_home_screen_ga()

        # select Camera Scan tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN),
                                      is_permission=False)
        self.camera_scan.verify_capture_no_access_screen()
        self.__verify_home_screen_ga()

        # select Scan tile on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN),
                                      is_permission=False)
        self.scan.verify_scan_screen()
        self.__verify_home_screen_ga()

        # select Print from Google Drive on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.GOOGLE_DRIVE),
                                      is_permission=False)
        self.online_docs.verify_gdrive_choose_account_popup()
        self.__verify_home_screen_ga()

        # select Print from DropBox on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.DROPBOX),
                                      is_permission=False)
        self.fc.flow_dropbox_log_in(self.dropbox_username, self.dropbox_pwd)
        self.__verify_home_screen_ga()

        # select Print from Copy on Home screen
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.COPY),
                                      is_permission=False)
        self.camera_scan.verify_capture_no_access_screen()
        self.__verify_home_screen_ga()

        # select HP INSTANT INK/Get Cartridges tile on Home screen
        self.home.select_tile_by_name("{}\n{}".format(self.home.get_text_from_str_id(TILE_NAMES.HP_INSTANT_INK_1),
                                                      self.home.get_text_from_str_id(TILE_NAMES.HP_INSTANT_INK_2)),
                                      is_permission=False)
        self.__verify_home_screen_ga()

        # ------------------        PRIVATE FUNCTIONS       ----------------------------------------------

    def __verify_home_screen_ga(self):

        """
        Click Back button from Mobile Devices after clicking icons from navigation bar or tiles from Home screen
        Verify Home screen with all GA events
        """
        self.driver.press_key_back()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()