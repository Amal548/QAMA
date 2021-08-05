from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import PACKAGE
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Printers_Add_Printer(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

    def test_01_add_printer_ui(self):
        """
        Description:
         1. Load Home screen
         2. Click on big "+" or small "+" icon on Home screen
         3. Click on +Add Printer button
         4. Click on Continue screen
         5. Allow App permission

        Expected Results:
         3. Verify Search for printer? Popup screen:
           + Title
           + Continue button
         5. Verify Add Printer screen with below points:
           + Title
           + Message screen
           + My Printer is not listed button
        """
        # Make sure the printer isn't connected when launch the app
        self.fc.reset_app()
        self.__load_add_printers_screen()
        self.printers.verify_search_printers_popup()
        self.printers.select_search_printers_popup_continue(is_permission=True)
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()

    def test_02_my_printer_not_listed_cancel_btn(self):
        """
        Description:
         1. Load to Add Printer screen
         2. Click on My Printer is not listed button
         3. Click on Cancel button

        Expected Result:
         2. Verify My Printer is not listed screen:
            + Dropdown menu button
            + Message: Use this app to set up the following wireless printers....
         3. Verify Home screen without printer connected
        """
        self.__load_my_printer_is_not_listed_screen()
        self.printers.verify_setup_printers_instruction_screen()
        self.printers.verify_try_again_button()
        self.printers.select_print_setup_cancel()
        self.home.verify_home_no_printer_connected()

    def test_03_instruction_my_printer_not_listed(self):
        """
        Description:
         1. Load to Add Printer screen
         2. Click on My Printer is not listed button
         3. Click on dropdown menu
         4. Select -My Printer is not listed-


        Expected Result:
         4. Verify Setup printer instruction screen with below message:
            + Your printer cannot be configured with this app. To ...etc (Verify the text)
        """
        self.__load_printer_setup_printer_model_screen(model=self.driver.return_str_id_value(self.printers.MY_PRINTER_IS_NOT_LISTED,
                                                                                               project="smart",
                                                                                               flow="printers"))
        self.printers.verify_my_printer_not_listed_help_msg()

    def test_04_instruction_with_printer_selected(self):
        """
        Description:
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list

        Expected Result:
         2. Verify Setup printer instruction screen with below message:
            + Make Sure printer is in Setup Mode
            + Make Sure your know your network name and password.
            + How do I do this? Link
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.verify_my_printer_setup_instruction()

    def test_05_my_printer_not_listed_instruction_setup_mode_link(self):
        """
        Description:
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Click on "How do I do this?" link
         4. Click on Ok button

        Expected Result:
         3. Verify How do I make sure printer in setup mode screen:
            + Title
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.select_setup_instruction_link(is_network=False)
        self.printers.verify_setup_instruction_link_popup(is_network=False)
        self.printers.select_setup_instruction_popup_ok(is_network=False)

    def test_06_my_printer_not_listed_instruction_network_link(self):
        """
        Description:
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Click on "How do I do this?" link
         4. Click on Ok button

        Expected Result:
         3. Verify How do I find my network name and pwd screen:
            + Title
        :return:
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.select_setup_instruction_link(is_network=True)
        self.printers.verify_setup_instruction_link_popup(is_network=True)
        self.printers.select_setup_instruction_popup_ok(is_network=True)

    def test_07_my_printer_not_listed_instruction_try_again(self):
        """
        Description:
         1. Load to Select your printer dropdown lists
         2. Click on any printer from the list
         3. Check one of 2 check boxes
         4. Check another check box, and Click Try Again button

        Expected Result:
         3. Try Again button is still disabled to click
         6. Verify Add Printer screen
        """
        self.__load_printer_setup_printer_model_screen(model="HP Envy")
        self.printers.toggle_setup_instruction_checkbox(is_network=False, enable=True)
        self.printers.verify_try_again_button()
        self.printers.toggle_setup_instruction_checkbox(is_network=True, enable=True)
        self.printers.verify_try_again_button(is_enabled=True)
        self.printers.select_printer_setup_try_again()
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()


    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_add_printers_screen(self):
        """
        - Load Home screen.
        - click on big + button if no printer connected before,
          otherwise clicking on small "+" button on Home screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.select_add()

    def __load_my_printer_is_not_listed_screen(self):
        """
       - Click on My printer is not listed button on Android 7/8/9 or click on Get More Help button on Android 10 or higher
        """
        self.__load_add_printers_screen()
        if self.printers.verify_search_printers_popup(raise_e=False):
            self.printers.select_search_printers_popup_continue(is_permission=True)
        if int(self.driver.platform_version) > 9:
            # Timeout 25s here, because Printer searching lists need take a while, and Printer Not Listed? button will display after that
            self.printers.verify_printer_setup_screen(timeout=25)
        else:
            self.printers.verify_add_printers_screen()
        self.printers.select_my_printer_is_not_listed()
        if int(self.driver.platform_version) > 9:
            self.printers.select_get_more_help_button()

    def __load_printer_setup_printer_model_screen(self, model=None):
        """
        - Load My printer is not listed screen
        - Click on Select your printer, and select a model
        """
        self.__load_my_printer_is_not_listed_screen()
        self.printers.select_printer_setup_printer_model(model=model)