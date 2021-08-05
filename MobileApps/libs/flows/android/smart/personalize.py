from selenium.common.exceptions import NoSuchElementException
from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time


class Personalize(SmartFlow):
    flow_name = "personalize"

    TILE_STATUS_ON = "on_txt"
    TILE_STATUS_OFF = "off_txt"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def select_back(self):
        """
        Click on Back button in Personalize screen
        """
        self.driver.click("_share_back_btn")
        self.driver.wait_for_object("_share_back_btn", invisible=True)
        self.driver.wait_for_object("tile_switch", invisible=True)

    def toggle_tile_by_name(self, tile_name, on=True, raise_e=True):
        """
        Enable a tile by its name

        :param tile_name: text string. Using TILE_NAMES constant to get string
        :return: True if it is enabled. Otherwise, False
        """
        self.driver.wait_for_object("tile_title", format_specifier=[tile_name])
        self.driver.check_box("tile_switch", format_specifier=[tile_name], uncheck= not on)
        if on != (self.driver.get_attribute("tile_switch", attribute="checked", format_specifier=[tile_name]) == 'true'):
            if raise_e:
                raise NoSuchElementException("Toggle of {} is not matched with expectation {}".format(tile_name, on))
            else:
                return False
        return True

    def get_enabled_tiles_list(self):
        """
        Get name of all enabled tiles on Personalize screen

        :return: list of enabled tiles' names
        """
        #Scroll to top of personalize
        self.driver.scroll("_shared_print_photos_tile", "up", timeout=20, check_end=False)
        tiles_title = []
        bottom = False
        on_txt = self.get_text_from_str_id("on_txt")
        timeout = time.time() + 30
        while not bottom and time.time() < timeout:
            tiles = self.driver.find_object("tile_title", multiple=True)
            for title in tiles:
                current_tile = title.text
                if current_tile not in tiles_title:
                    tile_toggle = self.driver.find_object("tile_switch", format_specifier=[current_tile])
                    if tile_toggle.text == on_txt:
                        tiles_title.append(current_tile)
            bottom = self.driver.swipe(direction="down", check_end=True)[1]
        return tiles_title

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_personalize_screen(self):
        """
        Verify that current screen is Personalize screen
        """
        self.driver.wait_for_object("title")
        self.driver.wait_for_object("_share_back_btn")

    def verify_existed_tile(self, tile_name):
        """
        Verify visible tiles on Personalize screen
        :param tile_name:
        """
        self.driver.scroll("_shared_get_ink_tile", "up", timeout=20, check_end=False)
        self.driver.scroll("tile_title", direction="down", format_specifier=[tile_name], timeout=30,
                                   check_end=False)
