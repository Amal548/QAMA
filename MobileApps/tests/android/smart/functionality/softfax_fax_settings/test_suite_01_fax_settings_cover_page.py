from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Fax_Settings_Cover_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]
        cls.udid = cls.driver.driver_info["desired"]["udid"]

    def test_01_fax_settings_ui(self):
        """
        Description:
            1. Load to Compose Fax with account as the one in precondition
            2. Click on 3 dot menu/ Fax Settings

        Expected Result:
            3. Verify Mobile Fax Setting screen with:
               - Title
               - Mobile Fax Account item
               - Sending item
               - About Mobile Fax item
        """
        self.__load_fax_settings()

    def test_02_empty_cover_page(self):
        """
        Description:
            1. Load to Compose Fax with an new account
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Cover Pages item

        Expected Result:
            3. Verify Cover Pages empty screen with:
               - Title: Cover Pages
               - message "You don't have any cover page templates"
        """
        self.__load_fax_settings()
        self.fax_settings.click_fax_settings_option(self.fax_settings.COVER_PAGES_OPT)
        self.fax_settings.verify_empty_cover_page_screen()

    def test_03_create_cover_pages(self):
        """
        Description:
            1. Load to Compose Fax with HPID account login
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Cover Pages item
            4. Click on Create a Cover Page button
            5. Input Cover Page name and Subject
            6. Click on Save button

        Expected Result:
            4. Verify Add Cover Page screen with:
               - Title
               - Cover Page Details item
            6. Verify Cover Page screen with cover pages list
        """
        cover_page_name = "test_03_{}".format(self.udid)
        subject = self.test_03_create_cover_pages.__name__
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page(cover_page_name)

    def test_04_edit_cover_pages_cancel(self):
        """
        Description:
            1. Load to Compose Fax with HPID account login
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Cover Pages item
            4. Click on Select button
            5. Click on Cancel button

        Expected Result:
            4. Verify edit screen:
               - Cancel button
               - Delete button
            6. Verify Cover Page screen
        """
        cover_page_name = "test_04_{}".format(self.udid)
        subject = self.test_04_edit_cover_pages_cancel.__name__
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_SELECT_BTN)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_CANCEL_BTN)
        self.fax_settings.verify_cover_page_screen()

    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_05_delete_cover_pages(self, btn_name):
        """
        Description:
            1. Load to Cover Page screen with cover pages list
            2. Click on Edit button
            3. Select a cover page
            4. Click on Delete button
            5. If btn = "cancel", then click on Cancel button
               If btn = "delete", then click on Delete button

        Expected Result:
            4. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            5. If btn = "cancel", then verify Cover Page edit screen
               If btn = "delete", then verify Cover Page screen
        """
        cover_page_name = "test_05_{}_{}".format(self.udid, btn_name)
        subject = self.test_05_delete_cover_pages.__name__
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_SELECT_BTN)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.select_single_cover_page(cover_page_name)
        self.fax_settings.click_cover_pages_delete_btn(is_edited=False)
        self.fax_settings.verify_cover_page_delete_popup()
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_cover_page_edit_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_cover_page_screen()
        
    @pytest.mark.parametrize("btn_name", ["cancel", "delete"])
    def test_06_delete_edit_cover_pages(self, btn_name):
        """
        Description:
            1. Load to Cover Page screen with cover pages list
            2. Select any cover page
            3. Click on Delete button
            4. If btn = "cancel", then click on Cancel button
               If btn = "delete", then click on Delete button

        Expected Result:
            2. Verify Edit Cover Pages screen
            3. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            3. If btn = "cancel", then verify Edit Cover Page screen
               If btn = "delete", then verify Cover Page screen
        """
        cover_page_name = "test_06_{}_{}".format(self.udid, btn_name)
        subject = self.test_06_delete_edit_cover_pages.__name__
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.select_single_cover_page(cover_page_name)
        self.fax_settings.verify_edit_cover_page_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        if btn_name == "cancel":
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
            self.fax_settings.verify_edit_cover_page_screen()
        else:
            self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
            self.fax_settings.verify_cover_page_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    
    def __load_fax_settings(self):
        """
        - Load Compose Fax screen with HPID account login or created a new HPID account
        - Click on Fax Settings on from More Option menu
        """
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True,
                                                  check_onboarding=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()
    
    def __create_a_cover_page(self, cover_page_name, subject):
        """
        - Click on Create Cover Page button
        - Add cover page name and subject
        - Click on Save button
        """
        self.fax_settings.click_fax_settings_option(self.fax_settings.COVER_PAGES_OPT)
        self.fax_settings.click_create_cover_page_btn()
        self.fax_settings.add_edit_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page_screen()