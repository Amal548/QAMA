from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from selenium.common.exceptions import TimeoutException
import pytest

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Scan_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]

        # Define variables
        cls.fc.set_hpid_account("hp+", claimable=True)

    def test_01_scan_screen(self):
        """
        Description:
            1/ Load Home screen
            2/ Select a target printer on Printer screen
            3/ Select Scan tile (if it is not visible, enable it in Personalize screen)
                 if App Permission displays, allow it
        Expected Result:
            Verify:
            1/ Scan tile is invisible.
            3/ Scan screen:
                - Scan title
                - Paper size dropdown button
                - Preview and Scan buttons
                - 'Color. Glass' of Scan settings
        """
        self.__load_scan_screen(is_tile=True)
        self.scan.verify_current_settings_info("{}, {}".format(self.scan.get_text_from_str_id(self.scan.COLOR_OPT_COLOR),
                                                               self.scan.get_text_from_str_id(self.scan.SOURCE_GLASS_SHORT)))

    def test_02_scan_settings_popup(self):
        """
        Description:
            1/ Load Scan screen via Scan icon on bottom navigation at Home screen
            2/ Click on Scan Settings icon button
            3/ For each option in Scan Settings, do following steps:
                  - Click on option dropdown button
                  - Press Backbutton of mobilde device
            4/ Click on Close button
        Expected Results:
            Verify:
                 2/ Scan Settings popup:
                          - Title of popup
                          - Close button
                 3/ Verify for each option in Scan Settings, if:
                          - Source: Scanner Glass
                          - Color: Black and Color
                          - Resolution: 75, 100, 200, 300 dpi
                 4/ Scan screen
        """
        self.__load_scan_screen(is_tile=True)
        self.scan.select_scan_settings_btn()
        self.scan.verify_scan_settings_popup()
        self.scan.select_source_option(source_type=self.scan.SOURCE_OPT_GLASS, is_checked=True)
        self.scan.select_color_option(color_opt=self.scan.COLOR_OPT_COLOR, is_checked=True)
        self.scan.select_resolution_option(resolution_opt=self.scan.RESOLUTION_200, is_checked=True)
        self.scan.select_scan_settings_close()
        self.scan.verify_scan_screen()

    def test_03_scan_paper_size_popup(self):
        """
        Description:
            1/ Load Scan screen via Scan tile at Home screen
            2/ Click on Paper Size dropdown button

        Expected Result:
            Verify:
                 2/ Paper Size popup:
                        - 3.5x5 in / 9x13cm
                        - 4x6 in / 10x15cm
                        - 5x7 in / 13x18cm
                        - Letter (8.5x11 in)
                        - A4
        """
        self.__load_scan_screen(is_tile=False)
        paper_sizes = [self.scan.PAPER_SIZE_3_5,
                       self.scan.PAPER_SIZE_4_6,
                       self.scan.PAPER_SIZE_5_7,
                       self.scan.PAPER_SIZE_LETTER,
                       self.scan.PAPER_SIZE_A4]
        for size in paper_sizes:
            self.scan.select_scan_size(size_opt=size)
            self.scan.verify_scan_screen()

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