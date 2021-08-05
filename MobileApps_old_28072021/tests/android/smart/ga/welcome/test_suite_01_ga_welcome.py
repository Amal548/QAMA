from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_GA_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls,  android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.welcome = cls.fc.flow[FLOW_NAMES.WELCOME]
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.personalize = cls.fc.flow[FLOW_NAMES.PERSONALIZE]

    def test_01_welcome_to_home(self):
        """
            Steps:
                - Launch HP Smart
                - Verify Welcome screen
                - Click on Check box of agreement
                - Click on Start button
                - Verify Home screen with big "+" icon button on screen
        """
        self.fc.flow_load_home_screen()
        self.home.verify_add_new_printer()


