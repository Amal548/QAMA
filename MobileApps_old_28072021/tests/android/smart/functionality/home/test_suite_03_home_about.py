import pytest
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import TEST_DATA
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES

pytest.app_info = "SMART"

class Test_Suite_03_Home_About(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.about = cls.fc.flow[FLOW_NAMES.ABOUT]
        cls.system_flow = cls.fc.flow[FLOW_NAMES.SYSTEM_FLOW]

        # Define variables
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["account_01"][
            "username"]

    def test_01_home_opt_about_legal_info(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on About button
         4. Click on Legal Information link on About screen
         5. Click on OK button
        Expected Result:
         4. Verify Legal Information Link screen
        """
        self.__load_more_option_about_screen()
        self.about.select_legal_info()

    def test_02_home_opt_about_license_agreement(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on About button
         4. Click on End User License Agreement on About screen
        Expected Result:
         4. About screen disappear
        """
        self.__load_more_option_about_screen()
        self.about.select_license_agreement()
        self.about.verify_about_screen(invisible=True)

    def test_03_home_opt_about_hp_privacy(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on About button
         4. Click on HP Privacy Link on About screen
        Expected Result:
         4.  About screen disappear
        """
        self.__load_more_option_about_screen()
        self.about.select_hp_privacy()
        self.about.verify_about_screen(invisible=True)

    def test_04_home_opt_about_share_gmail(self):
        """
        Description:
         1. Load Home screen
         2. Click on 3 dots on Home top navigation bar
         3. Click on About button
         4. Click on Share this app on About screen
         5. Click on gmail
        Expected Result:
         4. Verify Share with screen
        """
        self.__load_more_option_about_screen()
        self.about.select_share_btn()
        if self.about.verify_share_with_screen(raise_e=False):
            self.system_flow.select_app(self.driver.return_str_id_value("share_gmail_btn", project="smart", flow="preview"))
        self.fc.flow_gmail_send_email(self.email_address, self.test_04_home_opt_about_share_gmail.__name__, from_email=self.email_address)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_more_option_about_screen(self):
        """
        - Load to Home screen.
        - Click on More Option icon on Home screen
        - Click on About button under More Option menu
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_more_options_about()
        