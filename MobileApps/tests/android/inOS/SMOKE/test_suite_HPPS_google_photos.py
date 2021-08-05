import os
import pytest

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.photos.photos import Photos, NoSuchElementException

pytest.app_info = "GOOGLE_PHOTOS"
class Test_Suite_HPPS_google_photos(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup

        self.sys_config = ma_misc.load_system_config_file()
        self.photos = Photos(self.driver)

        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']


    @pytest.mark.parametrize('file', [const.GOOGLE_PHOTOS.JPG])
    def test_01_google_photos_system_ui(self, file):
        """
            Description:
            Before executing the script, make sure that the phone and printer are connected to same wifi network (eg.rdfishbowl24).
                   Step-1: Install and enable HPPS:
                           1) Install HPPS from Play Store.
                           2) Open Android settings.
                           3) Search for Printing settings.
                           4) Remove old print jobs.
                           5) Select HP INC.
                           6) Turn on HP Print service plugin, if turned off.
                           7) Click on 'Ok' to allow the document to pass through he service.
                   Step-2: Set HPPS prtocol:
                           1) Click on 'More' button.
                           2) Click on 'Printing Settings'.
                           3) Click on 'Advanced Settings'./home/qama/Desktop/Forked/MobileApps/tests/android/inOS/google_photo
                           4) Select the desired print protocol type.
                           5) Click on 'Back Button'.
                   Step-3: Open 'Google Photos'.
                   Step-4: Select Side Menu from top left corner of the screen.
                   Step-5: Select 'Device folders' from the menu.(Google Photos should be signed in)
                   Step-6: Select an image.
                   Step-7: Click on 3-dot-menu button from top right corner of the screen.
                   Step-8: Select 'Print'.from MobileApps.libs.flows.android.hpps.trap_door import Trap_Door
                   Step-9: Open and select printer via System UI.
                           1) Agree and accept terms and conditions if present.
                           2) Accept all access alerts.
                           3) Select 'All printers' from dropdown.
                           4) Select 'Search' from top of the screen.
                           5) Search and select printer by name.
                   Step-10: Select collapse button.
                   Step-11: Set System UI printer options, such as 'Copies', 'Color' etc.
                   Step-12: Select 'More options'
                   Step-13: Set values for more options such as 'Borderless' etc.
                   Step-14: Go back to the Printer preview screen.
                   Step-15: Select 'Print' and verify the results.
                           1) Select 'Print'.
                           2) Select 'Ok' for document passing.
                           3) Get printing results.
                   Step-16: Go to home screen.

            Expected Result:
                   Step-1.3: Verify Printing screen.
                   Step-1.5: Verify HP print service screen.
                   Step-2.1: Verify more options list.
                   Step-2.2: Verify 'Printing Settings' screen.
                   Step-3:   Verify Google Photos home screen.
                   Step-4:   Verify Si/home/qama/QAMA/MobileApps/tests/android/inOS/google_photosde Menu screen.
                   Step-5:   Verify 'Device folders' screen.
                   Step-6:   Verify image screen.
                   Step-7:   Verify 3-dot-menu screen.
                   Step-8:   Verify the print menu screen.
                   Step-9.2: Verify System UI screen.
                   Step-9.3: Verify 'All printers' screen.
                   Step-9.5: Verify System UI preview screen with print button.
                   Step-10:  Verify System UI print options screen.

        """
        self.photos.open_google_photos()
        self.photos.verify_google_photos_home_screen()
        self.photos.select_search()
        self.photos.verify_search_screen()
        self.photos.search_for_file(file)

        self.photos.verify_image_screen()
        self.photos.select_3dot_menu()
        self.photos.verify_3dot_menu_screen()
        self.fc.flow["intermediate_flow"].google_photos_select_app(self.driver.return_str_id_value_from_id("button_label__print", project="hpps"))

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type="image")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)

    @pytest.mark.parametrize('file', [const.GOOGLE_PHOTOS.PNG])
    def test_02_google_photos_trapdoor(self, file):
        """
            Description:
            Before executing the script, make sure that the phone and printer are connected to same wifi network (eg.rdfishbowl24).
                   Step-1: Install and enable HPPS:
                         1) Install HPPS from Play Store.
                         2) Open Android settings.
                         3) Search for Printing settings.
                         4) Remove old print jobs.
                         5) Select HP INC.
                         6) Turn on HP Print service plugin, if turned off.
                         7) Click on 'Ok' to allow the document to pass through he service.
                   Step-2: Set HPPS protocol:
                         1) Click on 'More' button.
                         2) Click on 'Printing Settings'.
                         3) Click on 'Advanced Settings'.
                         4) Select the desired print protocol type.
                         5) Click on 'Back Button'.
                   Step-3: Open 'Google Photos'.
                   Step-4: Select Side Menu from top left corner of the screen.
                   Step-5: Select 'Device folders' from the menu. (Google Photos should be signed in)
                   Step-6: Select an image.
                   Step-7: Click on 'Share' button (from bottom of the screen).
                   Step-8: Select 'HP Print Service' Plugin from the trapdoor.
                         1) Agree and accept terms and conditions if present.
                         2) Accept all access alerts.
                         3) Click on 'Search' from top right corner of the screen.
                         4) Select the printer.
                   Step-9:  Set values for printer options self.p, self.printer_bonjour_namelike 'Color', 'Copies' etc.
                   Step-10: Scroll and select 'More Options' from trapdoor.
                   Step-11: Set values for more options such as 'Scaling', 'Color Mode' etc.
                   Step-12: Go back to the Printer preview screen.
                   Step-13: Select 'Print' and verify the results.
                         1) Select 'Print'.
                         2) Open android notifications from the notification drawer.
                         3) Select the Print notification.
                         4) Get printing results.
                   Step-15: Go to home screen.

            Expected Result:
                   Step-1.3: Verify Printing screen.self.p, self.printer_bonjour_name
                   Step-1.5: Verify HP print service screen.
                   Step-2.1: Verify more options list.
                   Step-2.2: Verify 'Printing Settings' screen.
                   Step-3:   Verify Google Photos home screen.
                   Step-4:   Verify Side Menu screen.
                   Step-5:   Verify 'Device folders' screen.
                   Step-6:   Verify image screen.
                   Step-8.2: Verify 'Select Printer' screen.
                   Step-8.4: Verify Printer Preview screen.
                   Step-12:  Verify printer preview screen.
                   Step-13.3:Verify print job screen.
        """
        self.photos.open_google_photos()
        self.photos.verify_google_photos_home_screen()
        self.photos.select_search()
        self.photos.verify_search_screen()
        self.photos.search_for_file(file)
        self.photos.select_share()

        self.fc.flow["intermediate_flow"].google_photos_select_app(self.driver.return_str_id_value("trapdoor_hpps_txt",project="hpps",flow="trap_door"))
        self.fc.open_and_select_printer_via_trapdoor(self.printer_bonjour_name)
        self.fc.set_printer_options_in_trap_door(file_type="image")
        self.fc.flow["trap_door"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["trap_door"].verify_printer_preview_screen()
        self.fc.select_print_and_verify_results_for_trapdoor(self.p, self.printer_bonjour_name)
