from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from MobileApps.resources.const.android.const import *
import pytest

pytest.app_info = "SMART"

class Test_Suite_03_Print_Scan_And_Share(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

    @pytest.fixture(scope="function", autouse="true")
    def function_setup(self, account_type):
        self.fc.reset_app()
        self.fc.set_hpid_account(a_type=account_type, claimable=True, ii_status=True if account_type == "hp+" else False)
        self.fc.load_smart_dashboard_help_center_print_scan_and_share()
    
    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_01_printing(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Print, Scan, and Share item
          6. Click ong Printing button

        Expected Result:
          5. Verify Printing screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINTING)
        self.help_center.verify_printing()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_02_scanning(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Print, Scan, and Share item
          6. Click on Scanning button

        Expected Result:
          5. Verify Scanning screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SCANNING)
        self.help_center.verify_scanning()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_03_fax(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Print, Scan, and Share item
          6. Click on Fax button

        Expected Result:
          5. Verify Fax screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.FAX)
        self.help_center.verify_fax()

    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_04_view_and_print(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Print, Scan, and Share item
          6. Click on View & Print button

        Expected Result:
          5. Verify View & Print screen
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.VIEW_PRINT)
        self.help_center.verify_view_print()
    
    @pytest.mark.parametrize("account_type", ["hp+", "ucde"])
    def test_05_shortcuts(self, account_type):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on Print, Scan, and Share item
          6. Click on Shortcuts

        Expected Result:
          5. Verify Shortcuts page
        """
        self.help_center.click_link_on_help_center_screen(self.help_center.SHORTCUTS)
        self.help_center.verify_shortcuts()