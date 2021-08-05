from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Load_Smart_Dashboard_With_Hpplus_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hp_connect = cls.fc.flow[FLOW_NAMES.HP_CONNECT]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

        # Define the variable
        cls.fc.set_hpid_account("hp+", True, True)

    def test_01_load_smart_dashboard_by_hp_plus_account_with_printer(self):
        """
        Description:
          1. Load to Home screen without user onboarding account
          2. Click on Account button on navigation bar of Home screen

        Expected Result:
          2. Verify Smart Dashboard screen with HP+Member displays
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_smart_dashboard()

    def test_02_back_button(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Back button from mobile device

        Expected Result:
          2. App should direct into Smart app home screen
        """
        self.fc.flow_home_smart_dashboard()
        self.driver.press_key_back()
        self.home.verify_home_nav(timeout=20)
    
    def test_03_close_button(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Close button on Smart Dashboard screen

        Expected Result:
          2. App should direct into Smart app home screen
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_close_btn()
        self.home.verify_home_nav(timeout=20)
    
    def test_04_hp_support(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Click on HP Support link

        Expected Result:
          3. App should direct into HP Support page
        """
        self.__load_link_from_users_screen(self.hp_connect.HELP_SUPPORT_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"
    
    def test_05_end_user_license_agreement(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Click on End User License Agreement link on Smart Dashboard screen

        Expected Result:
          3. App should direct into end_user_license_agreement page
        """
        self.__load_link_from_users_screen(self.hp_connect.ENDER_USER_LICENSE_AGREEMENT_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"
    
    def test_06_hp_privacy(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Click on HP Privacy link on Smart Dashboard screen

        Expected Result:
          3. App should direct into HP Privacy page
        """
        self.__load_link_from_users_screen(self.hp_connect.HP_PRIVACY_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"
    
    def test_07_hp_smart_terms_of_use(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Click on HP Smart Terms Of Use link on Smart Dashboard screen

        Expected Result:
          3. App should direct into HP Smart Terms Of Use link page
        """
        self.__load_link_from_users_screen(self.hp_connect.HP_SMART_TERMS_OF_USE_LINK)
        assert (self.driver.get_current_app_activity()[0] == PACKAGE.GOOGLE_CHROME), "Google Chrome is not launching"
    
    def test_08_toggle_menu(self):
        """
        Description:
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toggle Menu button on Smart Dashboard screen

        Expected Result:
          2. Verify Smart Dashboard menu screenw with:
             + Home button
             + HP + Print Plans item
             + Printers item
             + Users item
             + Features item
             + Account item
             + Help Center item
             + Chat with Virtual Agent item
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_menu_toggle()
        self.hp_connect.verify_smart_dashboard_menu_screen()
  
    ######################################################################
    #                        PRIVATE FUNCTIONS                           #
    ######################################################################
    def __load_link_from_users_screen(self, link_name):
        """
          1. Load to Smart Dashboard screen with an hp+ account
          2. Click on Toogle menu / Users item
          3. Type each link on this screen
        """
        self.fc.flow_home_smart_dashboard()
        self.hp_connect.click_menu_toggle()
        self.hp_connect.click_users_btn()
        self.hp_connect.click_link(link=link_name)