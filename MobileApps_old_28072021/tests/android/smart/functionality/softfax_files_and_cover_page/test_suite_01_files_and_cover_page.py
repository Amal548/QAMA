from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from MobileApps.resources.const.android.const import *
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc

pytest.app_info = "SMART"

class Test_Suite_01_Files_And_Cover_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.fax_settings = cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]

    def test_01_files_cover_page_ui(self):
        """
        Description: C24796124
            1. Load to Compose Fax with account as the one in precondition
            2. Click on Files and Cover Page
            3. Toogle on Need a cover page?
        Expected Result:
            3. Verify Files and Cover page screen with:
               - Cover Page / 1 Page message
               - Trash icon
               - Add your files item
               - Message and Subject
        """
        self.__load_file_cover_page_screen()

    def test_02_disable_cover_page(self):
        """
        Description: C24796128
            1. Load to Compose Fax with an account as the one in precondition
            2. Click on Files and Cover Page
            3. Enable Need a cover page?
            4. Fill Subject
            4. Disable a cover page
        Expected Result:
            3. Verify Files and Cover page screen with:
               - Cover Page / 1 page message is invisible
               - Message and Subject message is invisible
               - Need a cover page? should be turned off
        """
        self.__load_file_cover_page_screen()
        self.compose_fax.toggle_need_a_cover_page_on_off(on=False)
        self.compose_fax.verify_cover_page(invisible=True)
        self.compose_fax.verify_one_cover_page(invisible=True)
        self.compose_fax.verify_subject(invisible=True)

    def test_03_invalid_message(self):
        """
        Description: C24796125
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Fill Message
            6. Click on Any button on the screen
        Expected Result:
            6. Verify invalid message with:
               - Fax Subject is required
        """
        self.__load_file_cover_page_screen()
        self.compose_fax.enter_subject(name="")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_subject_invalid_message()
    
    def test_04_trash_icon(self):
        """
        Description: C24796126
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click on Trash icon
        Expected Result:
            5. Need a cover page? should be turned off
        """
        self.__load_file_cover_page_screen()
        self.compose_fax.click_trash_icon()
        self.compose_fax.verify_cover_page(invisible=True)
        self.compose_fax.verify_one_cover_page(invisible=True)
        self.compose_fax.verify_subject(invisible=True)

    @pytest.mark.parametrize("btn_name", ["cancel", "save"])
    def test_05_save_cover_page_template(self, btn_name):
        """
        Description: C24811977, C24811978, C24811979
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Fill Subject information
            6. Click on Save cover page template button
            7. if btn_name == cancel, then click on CANCEL button
               if btn_name == save, then click on SAVE button
        Expected Result:
            7. if btn_name == cancel, then verify compose fax screen without Template: shows
               if btn_name == save, then verify Template: shows on Compose Fax screen
        """
        template_name = "test_05_{}".format(self.udid)
        self.__load_file_cover_page_screen()
        self.compose_fax.enter_subject(name="QAMA")
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.verify_name_your_cover_page_template()
        self.compose_fax.enter_cover_page_name(template_name)
        if btn_name == "cancel":
            self.compose_fax.click_cancel_btn()
            self.compose_fax.verify_cover_page(invisible=False)
            self.compose_fax.verify_one_cover_page(invisible=False)
        else:
            self.compose_fax.click_save_btn()
            self.compose_fax.verify_cover_template()
    
    def test_06_save_cover_page_template_without_name(self):
        """
        Description: C24811980
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template
            6. Click on Save button without filling Name
        Expected Result:
            6. Verify the message "A cover page template title is required"
        """
        #Make sure compose fax screen is empty, not affect by previous test
        self.fc.reset_app()
        self.__load_file_cover_page_screen()
        self.compose_fax.enter_subject(name="QAMA")
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.verify_name_your_cover_page_template()
        self.compose_fax.click_save_btn()
        self.compose_fax.verify_no_cover_page_template_title_message()

    def test_07_template_edit(self):
        """
        Description: C24813137, C24813160
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. Click on Edit button
            8. Do some change on Edit Cover Page screen
            9. Click on Save button
        Expected Result:
            7. Verify Edit Cover Page screen
            9. Verify compose fax screen with new updated template information
        """
        template_name = "test_07_{}".format(self.udid)
        new_cover_page_name = "new_{}".format(self.udid)
        subject_name = self.test_07_template_edit.__name__
        self.__load_file_cover_page_screen()
        self.__load_template(name="QAMA", template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.click_edit_btn()
        self.fax_settings.add_edit_cover_page(new_cover_page_name, subject_name, is_new=False)
        self.compose_fax.verify_template_list(new_cover_page_name)

    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_08_template_delete(self, btn_name):
        """
        Description: C24813162, C24813163
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. Click on Edit button
            8. Click on Delte button
            9. if btn_name == calcel, then click on CANCEL button
               if btn_name == delete, then click on DELETE button
        Expected Result:
            8. Verify Are you sure? popup
            9. if btn_name == calcel, then verify Edit Cover Page screen
               if btn_name == delete, then verify Compose fax screen without template
        """
        template_name = "test_08_{}_{}".format(self.udid, btn_name)
        self.__load_file_cover_page_screen()
        self.__load_template(name="QAMA", template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.click_edit_btn()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_edit_cover_page_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.compose_fax.verify_cover_template(invisible=True, raise_e=True)

    @pytest.mark.parametrize("btn_name", ["none", "create_new_one"])
    def test_09_template(self, btn_name):
        """
        Description: C24811981, C24812202, C24813164, C24813165
            1. Load to Compose Fax with HPID account login
            2. Click on Files and Cover page
            4. Turn on need a cover page?
            5. Click Save cover page template with a name
            6. Click on Template on Compose fax screen
            7. if btn_name == none, then click on None button
               if btn_name == create_new_one, then click on Create a new cover page template, and create a new cover page
        Expected Result:
            6. Verify Template screen with:
               - None
               - Edit
               - Create a new cover page template
            7. if btn_name == none, then verify compose fax screen with template == None
               if btn_name == create_new_one, verify Add Cover Page screen, and cover page can be saved success after that
        """
        template_name = "test_09_{}".format(self.udid)
        template_names = {
            "none": "None",
            "create_new_one": "test_09"
        }
        self.__load_file_cover_page_screen()
        self.__load_template(name="test_09_QAMA", template_name=template_name)
        self.compose_fax.click_template_btn()
        self.compose_fax.verify_cover_template_option_screen()
        if btn_name == "none":
            self.compose_fax.click_none_option()
            self.compose_fax.verify_cover_template()
        else:
            self.compose_fax.click_create_a_new_cover_page_template_option()
            self.fax_settings.add_edit_cover_page("test_09","test_09")
        self.compose_fax.verify_template_list(template_names[btn_name])

    
    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_file_cover_page_screen(self):
        """
        Load to Files and Cover Page screens:
            - Load Compose Fax screen
            - Click on Files and Cover Page
            - Verify Files and Cover Page screen
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,check_onboarding=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
        self.compose_fax.verify_no_updated_file()
        self.compose_fax.toggle_need_a_cover_page_on_off(on=True)
        self.compose_fax.verify_cover_page(invisible=False)
        self.compose_fax.verify_one_cover_page(invisible=False)
        self.compose_fax.verify_subject(invisible=False)
    
    def __load_template(self, name, template_name):
        """
        Load template:
            - enter subject
            - Click on save cover page template
            - Click on cover page name, and click on Save button after that
        """
        self.compose_fax.enter_subject(name=name)
        self.compose_fax.click_save_cover_page_template()
        self.compose_fax.enter_cover_page_name(cover_page_name=template_name)
        self.compose_fax.click_save_btn()