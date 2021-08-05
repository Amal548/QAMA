from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_02_Hp_Plus(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.help_center = cls.fc.flow[FLOW_NAMES.HELP_CENTER]

        # Define the variable
        cls.fc.set_hpid_account("hp+", True, True)

    def test_01_hp_plus(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP+ item

        Expected Result:
          3. Verify HP+ screen
        """
        #Guard cod to make sure test won't get affected by previous test suite
        self.fc.reset_app()
        self.fc.load_smart_dashboard_help_center_hp_plus()

    def test_02_what_is_hp_plus(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP+ item
          6. Click on What is HP+?

        Expected Result:
          3. Verify What is HP+ screen
        """
        self.fc.load_smart_dashboard_help_center_hp_plus()
        self.help_center.click_link_on_help_center_screen(self.help_center.WHAT_IS_HP_PLUS)
        self.help_center.verify_what_is_hp_plus()
    
    def test_03_hp_smart_security(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP+ item
          6. Click on HP Smart security

        Expected Result:
          3. Verify HP Smart security screen
        """
        self.fc.load_smart_dashboard_help_center_hp_plus()
        self.help_center.click_link_on_help_center_screen(self.help_center.HP_SMART_SECURITY)
        self.help_center.verify_hp_smart_security()
    
    def test_04_print_anywhere(self):
        """
        Description:
          1. Load to Home screen with an hp+ account
          2. Click on Account button
          3. Click on Menu button
          4. Click on Help Center
          5. Click on HP+ item
          6. Click on Print Anywhere

        Expected Result:
          3. Verify Print Anywhere screen
        """
        self.fc.load_smart_dashboard_help_center_hp_plus()
        self.help_center.click_link_on_help_center_screen(self.help_center.PRINT_ANYWHERE)
        self.help_center.verify_print_anywhere()