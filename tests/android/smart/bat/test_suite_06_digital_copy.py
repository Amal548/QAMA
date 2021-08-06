from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest


pytest.app_info = "SMART"

class Test_Suite_06_Digital_Copy(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.digital_copy = cls.fc.flow[FLOW_NAMES.DIGITAL_COPY]

    #@pytest.mark.parametrize("copy_type",["color_copy", "black_copy"])
    # Skip Black copy because of CR INOS-3861
    @pytest.mark.parametrize("copy_type", ["color_copy"])
    def test_01_start_copy(self, copy_type):
        """
        Description:
          1. Install and Launch the app
          2. Load to Home screen
          3. Select a target printer from Printer lists
          4. Click on Copy tile on Home screen
          5. Allow the access to Camera Access
          6. Click on capture button with manual mode
          7. Click on Start Color button Or Start Black copy button

        Expected Result:
          6. Verify Copy preview screen
          7.
             1) Make sure copy job send to printer successfully
             2) Verify Copy sent screen with below points:
                + Sent! Message
                + Home button
                + Back button
        """
        self.fc.flow_home_load_digital_copy_single_page(self.p)
        self.digital_copy.verify_copy_preview_screen()
        self.digital_copy.select_resize_btn()
        self.digital_copy.select_resize_type(self.digital_copy.FIT_TO_PAGE)
        if copy_type == "color_type":
            self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=True)
        else:
            self.fc.flow_digital_copy_make_copy_job(self.p, is_color_copy=False)