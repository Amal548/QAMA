from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Load_Smart_Dashboard_With_Basic_Account(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]

        # Define the variable
        cls.fc.set_hpid_account("basic", False, False)

    def test_01_load_smart_dashboard_by_base_account(self):
        """
        Description:
          1. Load to Home screen without user onboarding account
          2. Login an Base HPID account through app settings
          3. Click on Back button to Home screen
          4. Click on Account button
        Expected Result:
          5. Verify Smart Dashboard screen via set up new printer screen
        """
        self.fc.flow_home_smart_dashboard()