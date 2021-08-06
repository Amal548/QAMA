from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import time
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_GA_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        #Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]

        #Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress

    def test_01_ga_scan(self):
        """
        Steps:
        - Launch HP Smart
        - Verify Home screen with big "+" on printer area
        - Click on big "+" button
        - Verify Printer screen
        - Selected target printer on the list (not from search icon)
        - Verify Home Screen with printer connected
        - Click on Scan icon button on Navigation bar
        - Verify APP Permission screen
        - Click on ALLOW button
        - Verify Scan screen
        - Click on Back button in the top bar
        - Verify Home screen with printer connected
        - Click on Scan icon button on Navigation bar
        - Verify Scan screen
        - CLick on Settings icon
        - Verify Scan Settings screen
        - Click on Sources settings
        - Verify Scan source screen
        - Select Scanner Glass
        - Click on Color screen
        - Verify Scan Color screen
        - Select Color
        - Click on Resolution
        - Verify Scan Resolution screen
        - Select 300dpi
        - Click on CLOSE button
        - Click on Preview button on Scan screen
        - Click on Scan button on Scan screen
        - Click on Cancel button
        - Click on OK button
        - Click on Scan button on Scan screen
        - Verify Scan success or not
        - Verify landing page screen
        - Click on Back button in the top bar
        - Verify "Leave Pop up" screen
        - Click on Leave button
        - Verify Home screen with printer connected
        - Click on Scan icon button on Navigation bar
        - Verify Scan screen
        - CLick on Settings icon
        - Verify Scan Settings screen
        - Click on Sources settings
        - Verify Scan source screen
        - Select Scanner Glass
        - Click on Color screen
        - Verify Scan Color screen
        - Select Black
        - Click on Resolution
        - Verify Scan Resolution screen
        - Select 200dpi
        - Click on CLOSE button
        - Click on Preview button on Scan screen
        - Click on Scan button on Scan screen
        - Click on Cancel button
        - Click on OK button
        - Click on Scan button on Scan screen
        - Verify Scan success or not
        - Verify landing page screen
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()
        self.home.select_big_add_icon()
        self.printers.verify_printers_screen()
        self.printers.select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        self.__verify_scan_screen(is_permission=True, ga=True, title_name=TILE_NAMES.PRINTER_SCAN)
        self.scan.select_back()
        self.__verify_scan_screen(is_permission=False, ga=False, title_name=TILE_NAMES.PRINTER_SCAN)
        self.__preview_job_with_diff_settings(source_type=self.scan.SOURCE_OPT_GLASS,
                                              color_type=self.scan.COLOR_OPT_COLOR,
                                              resolution_opt=self.scan.RESOLUTION_300, size_opt=self.scan.PAPER_SIZE_3_5)
        time.sleep(20)
        self.scan.select_scan()
        self.scan.select_cancel()
        self.scan.select_ok_btn()
        self.__verify_landing_page(ga=True)
        self.fc.select_back()
        self.preview.verify_leave_confirmation_popup()
        self.preview.select_leave_confirm_popup_leave(number_of_items_deleted=1)
        self.driver.press_key_back()

        self.__verify_scan_screen(is_permission=False, ga=False, title_name=TILE_NAMES.PRINTER_SCAN)
        self.__preview_job_with_diff_settings(source_type=self.scan.SOURCE_OPT_GLASS,
                                              color_type=self.scan.COLOR_OPT_BLACK,
                                              resolution_opt=self.scan.RESOLUTION_200, size_opt=self.scan.PAPER_SIZE_3_5)

        time.sleep(10)
        self.__verify_landing_page(ga=True)

    # ------------------        PRIVATE FUNCTIONS       ------------------------------------
    def __verify_scan_screen(self, is_permission, ga, title_name):
        """
        Verify Scan screen
        :param is_status:
        :param is_permission:
        :param title_name:
        :return:
        """
        self.home.verify_home_nav_add_printer_icon()
        self.home.verify_loaded_printer()
        self.home.verify_all_tiles_ga()
        self.home.select_nav_scan(is_permission=is_permission, ga=ga)
        self.scan.verify_scan_screen()

    def __preview_job_with_diff_settings(self, source_type, color_type, resolution_opt, size_opt):
        """
        Click on Preview button after we changed source/color/resolution from scan settings screen
        :param source_type:
        :param color_type:
        :param resolution_opt:
        """
        self.scan.select_scan_settings_btn()
        self.scan.verify_scan_settings_popup()
        self.scan.select_source_option(source_type=source_type)
        self.scan.select_color_option(color_opt=color_type)
        self.scan.select_resolution_option(resolution_opt=resolution_opt)
        self.scan.select_scan_settings_close()
        self.scan.select_scan_size(size_opt=size_opt)
        self.scan.select_preview()

    def __verify_landing_page(self, ga):
        """
        Verify landing page screen after we click Scan button on scan screen
        :param title_name:
        """
        self.scan.select_scan()
        self.scan.verify_successful_scan_job(ga=ga)
        self.preview.verify_preview_nav()