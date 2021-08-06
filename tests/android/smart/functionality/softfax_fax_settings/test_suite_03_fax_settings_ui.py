from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"


class Test_Suite_03_Fax_Settings_UI(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]

    def test_01_terms_of_service(self):
        """
        Description:
        1. Load to Compose Fax with an existed HPID account
        2. Click on 3 dot menu/ Fax Settings
        3. Click on Terms of Service
        4. Click on Back button

        Expected Result:
        4. Verify Fax Settings screen is visible:
        """
        self.__load_fax_settings()
        self.fax_settings.click_fax_settings_option(self.fax_settings.TERMS_OF_SERVICES_OPT)
        self.driver.press_key_back()
        self.fax_settings.verify_fax_settings_screen()

    def test_02_business_associate_agreement(self):
        """
        Description:
        1. Load to Compose Fax with an existed HPID account
        2. Click on 3 dot menu/ Fax Settings
        3. Click on Business Associate Agreement
        4. Click on Back button

        Expected Result:
         4. Verify Fax Settings screen is invisible:
        """
        self.__load_fax_settings()
        self.fax_settings.click_fax_settings_option(self.fax_settings.BUSINESS_ASSOCIATE_AGREEMENT_OPT)
        self.driver.press_key_back()
        self.fax_settings.verify_fax_settings_screen()
    
    def test_03_menu_compose_new_fax(self):
        """
        Description:
        1. Load to Compose Fax with an existed HPID account
        2. Click on 3 dot menu/ Fax Settings
        3. Click on More Option icon (three dots from top right corner)
        4. Click on Compose New Fax button

        Expected Result:
         3. User direct into Compose Fax screen:
        """
        self.__load_fax_settings()
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_COMPOSE_NEW_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        
    def test_04_menu_fax_history(self):
        """
        Description:
        1. Load to Compose Fax with an existed HPID account
        2. Click on 3 dot menu/ Fax Settings
        3. Click on More Option icon (three dots from top right corner)
        4. Click on Fax History button

        Expected Result:
         3. User direct into Fax History screen:
        """
        self.__load_fax_settings()
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()

    def test_05_menu_home(self):
        """
        Description:
        1. Load to Compose Fax with an existed HPID account
        2. Click on 3 dot menu/ Fax Settings
        3. Click on More Option icon (three dots from top right corner)
        4. Click on Home button

        Expected Result:
         3. App should direct into Home screen:
        """
        self.__load_fax_settings()
        self.fax_settings.click_menu_option_btn(self.fax_settings.MENU_HOME_BTN)
        self.driver.switch_to_webview()
        self.home.verify_home_nav()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################

    def __load_fax_settings(self):
        """
        - Load Compose Fax screen with HPID account login or created a new HPID account
        - Click on Fax Settings on from More Option menu
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()