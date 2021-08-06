import os, random
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.hpps.flow_container import Flow_Container
from MobileApps.libs.flows.android.adobe.adobe import Adobe
from MobileApps.libs.flows.android.photos.photos import Photos

pytest.app_info="ADOBE"

class Test_Suite_HPPS_sent_multiple_print_jobs(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        # Apps instantiation
        self.adobe = Adobe(self.driver)
        self.photos = Photos(self.driver)

        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()

        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']

    @pytest.mark.skip("INOS-4144")
    def test_01_print_multiple_pdf_through_trapdoor(self):
        """
            Test cases covered: C87012, C87013
        """
        self.adobe.open_adobe()
        self.adobe.verify_adobe_home()
        self.adobe.go_to_files_screen_of_the_device()
        self.adobe.select_all_files()
        self.fc.flow["intermediate_flow"].select_app(self.driver.return_str_id_value("trapdoor_hpps_txt", project="hpps", flow="trap_door"))
        self.fc.flow["hp_print_service"].agree_and_accept_terms_and_condition_if_present()
        self.adobe.verify_share_to_print_message_for_multi_pdf()
        self.adobe.continue_to_trapdoor()

    def test_02_print_multiple_image_through_trapdoor(self):
        """
            Test cases covered: C87014, C87015, C87016, C87017, C87018
        """
        self.photos.open_google_photos()
        self.photos.verify_google_photos_home_screen()
        self.photos.select_side_menu()
        self.photos.verify_side_menu_screen()
        self.photos.select_device_folder()
        self.photos.verify_device_folder_screen()
        self.photos.select_photos_folder(const.GOOGLE_PHOTOS.PNG)
        self.photos.select_multiple_photo_files(3)
        self.photos.select_share(share_button_obj="share_button_on_folder_screen")

        self.fc.flow["intermediate_flow"].google_photos_select_app(self.driver.return_str_id_value("trapdoor_hpps_txt",project="hpps",flow="trap_door"))
        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        self.fc.set_printer_options_in_trap_door(file_type="image")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.select_print_and_verify_results_for_trapdoor(self.p, self.printer_bonjour_name, jobs=3)