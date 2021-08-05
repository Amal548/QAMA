import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
import datetime

pytest.app_info = "SMART"


class Test_Suite_02_Fax_Settings_Sender_Profiles(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]

        # Define variables
        cls.sender_profile_name = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]["name"]
        cls.sender_profile_phone_number = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]["phone"]
        cls.udid = cls.driver.driver_info["desired"]["udid"]

    def test_01_empty_sender_profiles(self):
        """
        Description:
        1. Load to Compose Fax with new account
        2. Click on 3 dot menu/ Fax settings
        3. Click on Sender Profiles

        Expected Result:
        3. Verify Sender Profile empty screen with:
            - Title
            - Empty sender profiles message
            - Create a New Sender Profile button
        """
        self.__load_fax_sender_profile_screen()
        self.fax_settings.verify_sender_profiles_screen(is_empty=True)

    def test_02_create_sender_profile(self):
        """
        Description:
        1. Load to Compose Fax with account as the one in precondition
        2. Click on 3 dot menu/ Fax settings
        3. Click on Sender Profiles
        4. Click on Create a New Sender Profile button
        5. Input Phone Number /Profile title/Name/Fax Number/Organization Name/Email
        6. Click on Save button

        Expected Result:
        3. Verify New Sender Profile screen with:
            - Title
            - Sender Profile Details
        6.  - New sender profile save success
            - Edit button is visible
        """
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_fax_sender_profile_screen()
        self.__create_a_new_sender_profile(profile_title)

    def test_03_sender_profile_edit_cancel(self):
        """
        Description:
        1. Load to Sender Profiles with account as the one in precondition
        2. Click on Edit button
        3. Click on Cancel button
        
        Expected Result:
        2. Verify Sender Profiles edit screen with:
           - Cancel button
           - Title
        3. Verify Sender Profiles screen with:
           - Title
           - Create a New Sender Profile button
        """
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_fax_sender_profile_screen()
        self.__create_a_new_sender_profile(profile_title)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
        self.fax_settings.verify_sender_profiles_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_CANCEL_BTN)
        self.fax_settings.verify_sender_profiles_screen()
    
    def test_04_edit_sender_profile_save(self):
        """
        Description:
        1. Load to Sender Profiles screen with sender profiles list
        2. Click any sender profile
        3. Edit Profile title
        4. Click on Save button
        
        Expected Result:
        4. Verify the sender profile save success
        """
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_fax_sender_profile_screen()
        self.__create_a_new_sender_profile(profile_title)
        self.fax_settings.select_single_sender_profiles(profile_title)
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.fax_settings.add_edit_sender_profile_page(profile_title, self.sender_profile_name, self.sender_profile_phone_number, is_new=False)
        self.fax_settings.verify_sender_profile_list(profile_title)

    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_05_sender_profiles_delete(self, btn_name):
        """
        Description:
        1. Load to Sender Profiles screen with sender profiles list
        2. Click on Edit button
        3. Select a sender profile
        4. Click on Delete button
        5. If btn_name == cancel, then click on CANCEL button
           If btn_name == delete, then click on DELETE button
        
        Expected Result:
        4. Verify "Are you sure?" popup:
            - Title
            - CANCEL button
            - DELETE button
        5. If btn_name == cancel, then verify Sender Profile edit screen
           If btn_name == Delete, then verify Sender Profile screen
        """
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_fax_sender_profile_screen()
        self.__create_a_new_sender_profile(profile_title)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.SENDER_PROFILE_SELECT_BTN)
        self.fax_settings.select_single_sender_profiles(profile_title)
        self.fax_settings.click_sender_profiles_delete_btn(is_edited=False)
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_sender_profiles_edit_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_sender_profiles_screen()

    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_06_edit_sender_profile_delete(self, btn_name):
        """
        Description:
        1. Load to Sender Profiles screen with sender profiles list
        2. Click any sender profile
        3. Click on Delete button
        4. If btn_name == cancel, then click on CANCEL button
           If btn_name == delete, then click on DELETE button
        
        Expected Result:
        4. If btn_name == cancel, then verify Edit Sender Profile screen
           If btn_name == delete, then verify Sender Profile screen
        """
        profile_title = "{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        self.__load_fax_sender_profile_screen()
        self.__create_a_new_sender_profile(profile_title)
        self.fax_settings.select_single_sender_profiles(profile_title)
        self.fax_settings.verify_edit_sender_profile_screen()
        self.fax_settings.click_sender_profiles_delete_btn(is_edited=True)
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_edit_sender_profile_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_sender_profiles_screen()

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    
    def __load_fax_sender_profile_screen(self):
        """
        - Load to Sender Profile screen
        - Load Compose Fax screen
        - Click on Fax Settings on menu
        - Click on Sender Profile menu
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()
        self.fax_settings.click_fax_settings_option(self.fax_settings.SEND_PROFILES_OPT)

    def __create_a_new_sender_profile(self, profile_title):
        """
        - Click on Create a new Sender Profile button
        - Fill all information
        - Click on Save button
        """
        self.fax_settings.verify_sender_profiles_screen()
        self.fax_settings.click_create_a_new_sender_profile_btn()
        self.fax_settings.add_edit_sender_profile_page(profile_title, self.sender_profile_name, self.sender_profile_phone_number, is_new=True)
        self.fax_settings.verify_sender_profile_list(profile_title)