from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from selenium.common.exceptions import TimeoutException
import pytest
import time

pytest.app_info = "SMART"


class Test_Suite_02_Scan_Preview(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        # Define variables
        cls.fc.set_hpid_account("hp+", claimable=True)

    def test_01_scan_preview_successfully(self):
        """
        Description:
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
        Expected Results:
            Verify:
              2/ Preview Cancel button.
                  Then, verify scanning job is successful by invisible Cancel button
                  Scan screen displays
        """
        self.__load_scan_screen(is_tile=True)
        self.scan.select_preview()
        self.scan.verify_successful_scan_job()
        self.scan.verify_scan_screen()

    def test_02_scan_cancel_preview_job(self):
        """
        Description:
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
            3/ Click on Cancel button
            4/ Click on OK button
        Expected Result:
            Verify:
                  3/ popup:
                          - Scan cenceled text
                          - OK buton
                  4/ Scan screen
        """
        self.__load_scan_screen(is_tile=False)
        self.scan.select_preview()
        self.scan.select_cancel()
        if not self.scan.verify_scan_canceled_popup(raise_e=False):
            self.scan.verify_scan_error_popup()
        self.scan.select_ok_btn()
        self.scan.verify_scan_screen()

    def test_03_scan_after_preview(self):
        """
        Description:
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
            3/ Change Paper Size to another size, then click on Scan button
        Expected Result:
            Verify:
              2/ Preview job is successful
              3/ Scan job is successful. Next screen is Landing Page
        """
        self.__load_scan_screen(is_tile=True)
        self.scan.select_preview()
        self.scan.verify_successful_scan_job()
        if self.scan.verify_scan_canceled_popup(raise_e=False):
            self.scan.select_ok_btn()
        self.scan.select_scan_size(size_opt=self.scan.PAPER_SIZE_4_6)
        self.scan.select_scan()
        self.scan.verify_successful_scan_job()
        self.preview.verify_preview_nav(is_edit=True)

    def test_04_scan_preview_add_page_scan_job(self):
        """
        Description:
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Scan button
            3/ Click Add icon on Landing Page
            4/ Click on Preview button
        Expected Result:
            Verify:
              2/ Scan job is successful
              4/ Preview is successful with dots on Preview area
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_scan_single_page(self.p)
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_add()
        self.scan.verify_scan_screen()
        self.scan.select_preview()
        self.scan.verify_successful_scan_job()
        self.scan.verify_scan_screen()

    @pytest.mark.parametrize("back_btn", ["mobile", "app"])
    def test_05_scan_preview_back_from(self, back_btn):
        """
        Description:
            1/ Load Scan screen via tile (a printer is selected)
            2/ Click on Preview button
            3/ Press on Back button of mobile device
            4/ Load Scan screen via icon button on Home screen
            5/ Click on Scan button
            6/ At Landing Page, click on Add icon button
            7/ Click on Preview button
            8/ Press on Back button of mobile device
        Expected Result:
            Verify:
              3/ Home screen display
              8/ Landing Page screen.
        @param back_btn: back button. True: mobile back key, False: back button on Scan screen
        """
        self.__load_scan_screen(is_tile=True)
        self.scan.select_preview()
        self.__select_back(back_btn)
        self.home.verify_home_nav()
        self.home.select_bottom_nav_btn(self.home.NAV_PRINTER_SCAN_BTN)
        self.scan.verify_scan_screen()
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
            self.scan.verify_successful_scan_job()
        self.preview.verify_preview_nav(is_edit=True)
        self.preview.select_add()
        self.scan.verify_scan_screen()
        self.scan.select_preview()
        self.__select_back(back_btn)
        self.preview.verify_preview_nav(is_edit=True)


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

    def __select_back(self, back_btn):
        """
        Click on Back button from mobile back key or back button on Scan screen
        :param mobile_back: True: mobile back key, False: back btn on Scan screen
        """
        if back_btn == "mobile":
            self.driver.press_key_back()
        else:
            self.scan.select_back()