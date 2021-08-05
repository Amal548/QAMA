from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from MobileApps.resources.const.android.const import PACKAGE

pytest.app_info = "SMART"

class Test_Suite_01_Photo_Books(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]
        cls.photo_books = cls.fc.flow[FLOW_NAMES.PHOTO_BOOKS]
        
    def test_01_created_photo_books(self):
        """
        Description:
         1. Load Home screen
         2. Click on Create Photo Books tile (enable it from personalize screen if not on Home screen)
        Expected Results:
         2. Verify Create Photo Books screen:
           + title
           + buttons: Get My Photo Book / No Thanks
        """
        self.__load_created_photo_books_screen()
        self.photo_books.verify_create_photo_books_screen()

    def test_02_get_my_photo_book(self):
        """
        Description:
         1. Load Home screen
         2. Click on Create Photo Books tile (enable it from personalize screen if not on Home screen)
         3. Click on Get My Photo Book button
        Expected Results:
         3. Verify Photo Book launch by Chrome browser
        """
        self.__load_created_photo_books_screen()
        self.photo_books.select_get_my_photo_book()
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"

    def test_03_no_thanks(self):
        """
        Description:
         1. Load Home screen
         2. Click on Create Photo Books tile (enable it from personalize screen if not on Home screen)
         3. Click on No Thanks button
        Expected Results:
         3. Verify Home screen screen
        """
        self.__load_created_photo_books_screen()
        self.photo_books.select_no_thanks()
        self.home.verify_home_nav()
        
    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_created_photo_books_screen(self):
        """
        If current screen is not Home screen, load to Home screen.
        - If there is no connected printer, select a target printer
        """
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        if not self.home.verify_tile(self.home.get_text_from_str_id(TILE_NAMES.CREATE_PHOTO_BOOKS), raise_e=False):
            self.home.select_personalize_tiles()
            self.personalize.toggle_tile_by_name(self.personalize.get_text_from_str_id(TILE_NAMES.CREATE_PHOTO_BOOKS), on=True)
            self.personalize.select_back()
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.CREATE_PHOTO_BOOKS))
        self.photo_books.verify_create_photo_books_screen()