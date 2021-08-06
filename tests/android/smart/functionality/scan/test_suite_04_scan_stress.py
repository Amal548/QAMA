from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_04_Scan_Stress(object):

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

    @pytest.mark.parametrize("back_btn", ["mobile", "app"])
    def test_01_scan_back_from(self, back_btn):
        """
        Description:
            1/ Load Scan screen via tile with selecting printer at Home screen
            2/ Click on Scan button
            3/ Press Back from app or mobile device
            4/ Load Scan screen
            5/ Click on Scan button
            6/ At Landing Page, click on Add icon button
            7/ Click on Scan button on Scan screen
            8/ Press Press Back from app or mobile device
        Expected Result:
            Verify:
              3/ Home screen display
              8/ Landing Page screen.
        @param back_btn: back button. True: mobile back key, False: back button on Scan screen
        """
        self.fc.flow_load_home_screen()
        self.fc.flow_home_load_scan_screen(self.p, from_tile=True)
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
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
        if self.fc.is_printer_ready(self.p):
            self.scan.select_scan()
        self.__select_back(back_btn)
        self.preview.verify_preview_nav(is_edit=True)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __select_back(self, back_btn):
        """
        Click on Back button from mobile back key or back button on Scan screen
        :param mobile_back: True: mobile back key, False: back btn on Scan screen
        """
        if back_btn == "mobile":
            self.driver.press_key_back()
        else:
            self.scan.select_back()