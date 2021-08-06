from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_About_Hp_Smart(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.fc.load_smart_dashboard_help_center_about_hp_smart()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_getting_to_know_smart(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on About HP Smart item
          6. Click on Getting to Know HP Smart

        Expected Result:
          5. Verify About HP Smart page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.GETTING_TO_KNOW_HP_SMART)
        self.help_center.verify_getting_to_know_hp_smart()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_starting_off(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on About HP Smart item
          6. Click on Starting Off

        Expected Result:
          5. Verify Starting Off page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.STARTING_OFF)
        self.help_center.verify_starting_off()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_03_sharing_files(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on About HP Smart item
          6. Click on Sharing Files

        Expected Result:
          5. Verify Sharing Files page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SHARING_FILES)
        self.help_center.verify_sharing_file()