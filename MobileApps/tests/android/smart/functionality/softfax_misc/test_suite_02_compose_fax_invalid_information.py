import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_Compose_Fax_Invalid_Information(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    @pytest.mark.parametrize("info", ["default", "short", "long"])
    def test_01_recipient_phone_number(self, info):
        """
        Description:
            1/ Load to Compose Fax screen
            2/ Enter a invalid recipient phone number (default - empty, short, or long)
            3/ Click on Send Fax button
        Expected result:
            3/ Validation message for recipient phone number display
        """
        invalid_info = {"short": "1234", "long": "123456789012345"}
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        if info != "default":
            self.compose_fax.enter_recipient_information(invalid_info[info])
        self.compose_fax.click_send_fax(raise_e=False)
        if info == "default":
            self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=False)
        else:
            self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=False)

    def test_02_empty_sender_name(self):
        """
        Description:
            1/ Load to Compose Fax screen
            2/ Enter a empty sender name
            3/ Click on Send Fax button
        Expected result:
            3/ error message of sender name visible
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information("", self.sender_info["phone"])
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_sender_name_error_message()

    @pytest.mark.parametrize("info", ["default", "short", "long"])
    def test_03_sender_phone_number(self, info):
        """
        Description:
            1/ Load to Compose Fax screen
            2/ Enter a empty sender phone number
            3/ Click on Send Fax button
        Expected result:
            3/  error message of sender phone number visible
        """
        invalid_info = {"default": "", "short": "1234", "long": "123456789012345"}
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], invalid_info[info])
        self.compose_fax.click_send_fax(raise_e=False)
        if info == "default":
            self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=True)
        else:
            self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=True)