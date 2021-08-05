import pytest
import datetime
import os
from MobileApps.libs.flows.android.hpps.flow_container import Flow_Container
from MobileApps.libs.flows.android.photos.photos import Photos
from MobileApps.resources.const.android.const import GOOGLE_PHOTOS
from MobileApps.resources.const.android.const import RESULTS
from SPL.printer_misc.db_misc import printer_database_module
from SPL.printer_misc import printer_misc
from SPL.driver.driver_factory import printer_driver_factory
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc.excel import Excel

pytest.app_info = "HPPS"


class Test_HPPS_Printer_Discovery(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, hpps_setup):
        cls = cls.__class__
        cls.driver, cls.fc = hpps_setup

        # Initialize and load flows
        cls.photos = Photos(cls.driver)
        cls.pd = Excel(os.path.join(pytest.session_result_folder, "printer_discovery/android_hpps.xls"))

        # Define variables
        cls.date = str(datetime.datetime.now().strftime('%Y-%m-%d'))
        cls.printers = cls.pd.load_printers_info()

        def clean_up_class():
            cls.pd.save()
            ma_misc.publish_to_junit(os.path.join(pytest.session_result_folder, "printer_discovery/android_hpps.xls"))
        request.addfinalizer(clean_up_class)

    def test_01_trapdoor_ui_printer_discovery(self):
        """
        Description:
            - Open Photos app
            - Select a target photo
            - CLick on Share icon/HP Print Service Plugin
            - Select target printer
            - Compare target printer 's information with title on Preview screen of HPPS via trapdoor ui
            - Make sure Print icon button display
        :param printer: actual printer information
        """
        # Load sheet name for HPPS trapdoor ui
        self.pd.load_sheet("HPPS Trapdoor UI")
        for i in range(5):
            self.pd.write_new_record(["Attemp: {}".format(i + 1), "", ""])
            for printer_info in self.printers:
                error_msg = ""
                try:
                    self.__select_photo_via_photos()
                    self.photos.select_share_with_hpps()
                    self.fc.open_and_select_printer_via_trapdoor(printer_info["ip address"], is_searched=False, timeout=30)
                    self.fc.flow["trap_door"].verify_printer_preview_screen(printer_info["bonjour name"])
                    test_result = "Pass"
                    # Go back Preview screen of photo for next printer
                    for _ in range (4):
                        self.driver.press_key_back()
                        if self.photos.verify_image_screen(raise_e=False):
                            break
                except Exception as ex:
                    test_result = "Fail"
                    error_msg = ex.message if getattr(ex, "message", False) else  ex.msg
                self.pd.write_new_record([self.date, "{} ({})".format(printer_info["ip address"], printer_info["bonjour name"]),
                                        test_result, error_msg])
            self.pd.save()

    def test_02_system_ui_printer_discovery(self):
        """
        Description:
            - Open Photos app
            - Select a target photo
            - Click on 3 dot icon -> click on Print button
            - Select target printer in All Printer
            - Compare target printer 's information with title on Preview screen of HPPS via trapdoor ui
            - Make sure Print icon button display
        :param printer: actual printer information
        """
        # Load sheet name for HPPS trapdoor ui
        self.pd.load_sheet("HPPS System UI")
        for i in range(5):
            self.pd.write_new_record(["Attemp: {}".format(i + 1), "", ""])
            for printer_info in self.printers:
                error_msg = ""
                try:
                    self.__select_photo_via_photos()
                    self.photos.select_3dot_menu()
                    self.photos.select_print()
                    self.fc.open_and_select_printer_via_system_ui(printer_info["bonjour name"], is_searched=False, timeout=40)
                    test_result = "Pass"
                except Exception as ex:
                    test_result = "Fail"
                    error_msg = ex.message if getattr(ex, "message", False) else  ex.msg
                self.pd.write_new_record([self.date, "{} ({})".format(printer_info["bonjour name"], printer_info["ip address"]),
                                        test_result, error_msg])
            self.pd.save()

    # -----------------     PRIVATE FUNCTIONS       ---------------------
    def __select_photo_via_photos(self):
        """
        Description:
            - Open Photos app
            - Click on Device Folder on left side navigation bar
            - Select a photo
        """
        if not self.photos.verify_image_screen(raise_e=False):
            self.photos.open_google_photos()
            self.photos.select_side_menu()
            self.photos.select_device_folder()
            self.photos.select_photos_folder(GOOGLE_PHOTOS.JPG)
            self.photos.select_image()

