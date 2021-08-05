from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from selenium.common.exceptions import NoSuchElementException
import random

pytest.app_info = "SMART"

class Test_Suite_04_Home_Personalize(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize= cls.fc.flow[FLOW_NAMES.PERSONALIZE]

        # Define the variable
        cls.tiles_list = [cls.home.get_text_from_str_id(TILE_NAMES.PRINT_PHOTOS),
                          cls.home.get_text_from_str_id(TILE_NAMES.GET_INK),
                          cls.home.get_text_from_str_id(TILE_NAMES.PRINT_DOCUMENTS),
                          cls.home.get_text_from_str_id(TILE_NAMES.HELP_SUPPORT),
                          cls.home.get_text_from_str_id(TILE_NAMES.PRINTER_SCAN),
                          cls.home.get_text_from_str_id(TILE_NAMES.CAMERA_SCAN),
                          cls.home.get_text_from_str_id(TILE_NAMES.COPY),
                          cls.home.get_text_from_str_id(TILE_NAMES.SMART_TASKS),
                          cls.home.get_text_from_str_id(TILE_NAMES.FAX)]

    def test_01_personalize_ui(self):
        """
        Description:
         1. Launch the app and Load to Home screen
         2. Click on Personalize tile on Home screen
        Expected Results:
         2. Verify Personalize screen with below points:
            + Personalize title
            + Back button
            + Verify all tiles displayed
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_personalize_tiles()
        self.personalize.verify_personalize_screen()
        for tile_name in self.tiles_list:
            self.personalize.verify_existed_tile(tile_name)

    def test_02_personalize_tile_match(self):
        """
        Description:
         1. Load Home screen
         2. Get all visible tile's name on Home screen
         3. Click on Personalize screen
        Expected Results:
         3. All visible tiles from step 2 are enabled on Personalize screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        home_tiles = self.home.get_tile_titles()
        self.home.select_personalize_tiles()
        enabled_tiles = self.personalize.get_enabled_tiles_list()
        self.__comapre_tiles_list(home_tiles, enabled_tiles)

    def test_03_personalize_one_enable_tile(self):
        """
        Description:
         1. Load Home screen
         2. Click on Personalize tile on Home screen
         3. Turn off all tiles except one tile
         4. Click on Back button on navigation bar
         5. Verify Tiles on Home screen
        Expected Result:
         3. All tiles are off except Print Photos tile (Print Photos tile cannot be disable for clicking)
         5. Only Print Photos and Personalize tile on Home screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_personalize_tiles()
        enabled_tiles = self.personalize.get_enabled_tiles_list()
        enabled_tiles.pop(random.randint(0, len(enabled_tiles) - 1))
        for tiles in enabled_tiles:
            self.personalize.toggle_tile_by_name(tiles, on=False)
        enabled_tiles = self.personalize.get_enabled_tiles_list()
        assert (len(enabled_tiles) == 1), "There are more than 1 enabled tiles. Enable_tiles: {}".format(enabled_tiles)
        assert(not self.personalize.toggle_tile_by_name(enabled_tiles[0], on=False, raise_e=False)),"{} should not be disabled".format(enabled_tiles[0])
        self.personalize.select_back()
        home_tiles = self.home.get_tile_titles()
        self.__comapre_tiles_list(home_tiles, enabled_tiles)

    def test_04_home_tiles_match_from_personalize_screen(self):
        """
        Description:
         1. Load Home screen
         2. Click on Personalize tile on Home screen
         3. Disabled all default enabled tiles
         4. Enabled all default disabled tiles from step3
         5. Click on Back button on Personalize screen
        Expected Result:
         5. Make sure all tiles enabled from Personalize screen displays on Home screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_personalize_tiles()
        enabled_tiles = self.personalize.get_enabled_tiles_list()
        different_tiles = list(set(self.tiles_list) - set(enabled_tiles))
        for tiles in different_tiles:
            self.personalize.toggle_tile_by_name(tiles, on=True)
        for tiles in enabled_tiles:
            self.personalize.toggle_tile_by_name(tiles, on=False)
        self.personalize.select_back()
        home_tiles = self.home.get_tile_titles()
        self.__comapre_tiles_list(home_tiles, different_tiles)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __comapre_tiles_list(self, list1, list2):
        """
        - Compare tiles lists between Home screen and Personalize screen.
        - The number depends on enabled tiles on Personalize screen
        :param list1: Tile lists on Home screen except Personalize Tile
        :param list2: Enabled Tiles lists on Personalize screen
        """
        list1 = [s.replace('\n', ' ') for s in list1]
        assert(len(set(list1)-set(list2)) == 0), "The number of 2 tile lists are not match:\n List 1: {}\, List2: {}".format(list1, list2)
