import os
import pytest
from MobileApps.resources.const.android import const
from MobileApps.libs.flows.android.google_drive.google_drive import GoogleDrive

from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "GOOGLE_DRIVE"
class Test_Suite_HPPS_google_drive(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, hpps_setup ,load_printers_session):
        self = self.__class__
        self.driver, self.fc = hpps_setup
        self.drive = GoogleDrive(self.driver)

        self.sys_config = ma_misc.load_system_config_file()
        self.p = load_printers_session
        self.printer_info = self.p.get_printer_information()
        # Printer variables
        self.printer_bonjour_name = self.printer_info['bonjour name']
        self.printer_ip = self.printer_info['ip address']


    @pytest.mark.parametrize('file',[const.GOOGLE_DRIVE.PDF_1])
    def test_01_google_drive_system_ui(self, file):
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
                 Step-3: Open 'Google Drive'.
                 Step-4: Select 'Search' from top of the screen and open the file.
                 Step-5: Click on 3-dot-menu button from top-right side of the screen.
                 Step-6: Select 'Print'.
                 Step-7: Open and select printer via System UI.
                         1) Agree and accept terms and conditions if present.
                         2) Accept all access alerts.
                         3) Select 'All printers' from dropdown.
                         4) Select 'Search' from top of the scrren.
                         5) Search and select printer by name.
                 Step-8: Select collapse button.
                 Step-9: Set System UI printer options, such as 'Copies', 'Color' etc.
                 Step-10: Select 'More options'
                 Step-11: Set values for more options such as 'Borderless' etc.
                 Step-12: Go back to the Printer preview screen.
                 Step-13: Select 'Print' and verify the results.
                         1) Select 'Print'.
                         2) Select 'Ok' for document passing.
                         3) Get printing results.
                 Step-14: Go to home screen.

            Expected Result:
                 Step 3:   Verify 'Google Drive' home screen.
                 Step-4:   Verify file screen.
                 Step-5:   Verify 3-dot-menu screen.
                 Step-7.2: Verify System UI screen.
                 Step-7.3: Verify 'All printers' screen.
                 Step-7.5: Verify System UI preview screen with print button.
                 Step-9:   Verify System UI print options screen.

        """
        # Google drive has no welcome screen
        self.drive.launch_google_drive()
        self.drive.verify_home_screen()
        self.drive.search_and_open_file(file)
        self.drive.verify_opened_file_screen()
        self.drive.click_on_3_dot_menu()
        self.drive.verify_3_dot_menu_screen()
        self.drive.select_print()

        self.fc.open_and_select_printer_via_system_ui(self.printer_bonjour_name)
        self.fc.flow["system_ui"].select_collapse_button()
        self.fc.flow["system_ui"].verify_system_ui_print_options_screen()
        self.fc.set_printer_options_in_system_ui(file_type="document")
        self.fc.flow["system_ui"].select_more_options()
        self.fc.set_more_options()
        self.fc.flow["more_options"].select_back()

        self.fc.flow["system_ui"].verify_system_ui_preview_screen_with_print_button()
        self.fc.select_print_and_verify_results_for_system_ui(self.p)
