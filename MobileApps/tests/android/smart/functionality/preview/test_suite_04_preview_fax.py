from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import WEBVIEW_CONTEXT

pytest.app_info = "SMART"

class Test_Suite_01_Preview_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.preview = cls.fc.flow[FLOW_NAMES.PREVIEW]
        cls.camera_scan = cls.fc.flow[FLOW_NAMES.CAMERA_SCAN]
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]

    def test_01_softfax_screen_by_login_hpid(self):
        """
        Description:
        1. Load to Home screen with user onboarding account login
        2. Go to Home screen to click on View & Print button
        3. Click on PDFs
        4. Select any .pdf file
        5. Click on Softfax button

        Expected Results:
        5. Verify Compose Softfax screen:
           + Title
           + button
        """
        # There are multiple test suites under Preview folder. So add clear cache here to make sure no get affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_load_home_screen()
        self.fc.flow_home_verify_smart_app_on_userboarding()
        self.fc.flow_home_camera_scan_pages()
        self.preview.verify_preview_nav()
        self.preview.select_bottom_nav_btn(self.preview.FAX_BTN)
        # There are some test cases failed by No Such context issue, so add timeout for wait_for_context for fixing this issue
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART, timeout=20)
        self.compose_fax.verify_compose_fax_screen()