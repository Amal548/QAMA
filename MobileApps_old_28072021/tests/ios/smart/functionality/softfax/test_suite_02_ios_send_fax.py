import pytest
from SAF.misc import saf_misc
from MobileApps.libs.flows.ios.smart.flow_container import FlowContainer, sleep
from MobileApps.resources.const.ios.const import *

pytest.app_info = "SMART"


class Test_Suite_01_Ios_Send_Fax(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, session_setup):
        cls = cls.__class__
        cls.driver = session_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.stack = request.config.getoption("--stack")
        cls.home = cls.fc.fd["home"]
        cls.compose_fax = cls.fc.fd["softfax_compose_fax"]
        cls.send_fax_details = cls.fc.fd["send_fax_details"]
        cls.preview = cls.fc.fd["preview"]
        cls.recipient_info = cls.fc.recipient_info_for_os()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_compose_and_send_fax(self):
        """
        Load to Compose fax screen, enter all details, send fax and verify
        send fax status
        """
        self.fc.go_home(stack=self.stack, button_index=1)
        self.fc.nav_to_compose_fax()
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.click_add_files_option_btn(self.compose_fax.FILES_PHOTOS_BTN)
        self.fc.select_photo_from_my_photos()
        self.preview.verify_preview_screen_title(self.preview.FAX_PREVIEW_TITLE)
        self.preview.verify_an_element_and_click(self.preview.CONTINUE_TO_FAX_BTN)
        self.compose_fax.verify_compose_fax_screen()
        # @TODO:  Webview button click did not work so using native button click
        self.compose_fax.click_send_fax_native_btn()
        #TODO: Added timeout using Android test example
        self.send_fax_details.verify_send_fax_status(timeout=600)
