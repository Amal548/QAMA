from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
import datetime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Create_New_Smart_Tasks(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.hpid = cls.fc.flow[FLOW_NAMES.HPID]
        cls.ows_value_prop = cls.fc.flow[FLOW_NAMES.OWS_VALUE_PROP]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.ucde_privacy = cls.fc.flow[FLOW_NAMES.UCDE_PRIVACY]
        cls.google_chrome = cls.fc.flow[FLOW_NAMES.GOOGLE_CHROME]

        # Define the variable
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_01"]["password"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]

        def clean_up_class():
            cls.fc.flow_home_delete_all_smart_tasks(cls.hpid_username, cls.hpid_pwd)

        request.addfinalizer(clean_up_class)
    '''
    def test_01_smart_tasks_login_by_creating_account_via_tile(self):
        """
        Description:
          1. Load to Home screen
          2. Click on Smart Tasks tile
          3. Click on Create Account button
          4. Create a new HPID account

        Expected Result:
          4. Verify Smart Tasks empty lists screen
        """
        self.__load_hpid_sign_in_screen()
        # Handle for welcome screen of Google Chrome
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context("WEBVIEW_chrome")
        self.hpid.verify_hp_id_sign_up()
        self.hpid.create_account()
        self.driver.wait_for_context(WEBVIEW_CONTEXT.SMART)
        #Todo: Wait for designer's reply for updating timeout.
        self.ucde_privacy.skip_ucde_privacy_screen(timeout=30)
        self.home.check_run_time_permission(accept=True, timeout=15)
        self.smart_tasks.dismiss_smart_task_skip_btn(is_checked=False)
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=True)

    def test_02_smart_tasks_login_by_creating_account_via_app_settings(self):
        """
        Description:
          1. Load to Home screen
          2. Click on App Settings, and Click in Sign In button
          3. Create a new HPID account
          4. Click on Back button on App settings
          5. Click on Smart Tasks tile on Home screen
          6. Click on Learn More button

        Expected Result:
          5. Verify Smart Tasks empty lists screen
          6. Verify Smart Tasks learn more screen
        """
        self.fc.flow_home_load_smart_task_screen(create_acc=True)
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=True)
        self.smart_tasks.select_learn_more_btn()
        self.smart_tasks.verify_smart_tasks_learn_more_screen()

    def test_03_smart_tasks_login_via_tile(self):
        """
        Description:
          1. Load to Home screen
          2. Go to App Setting to logout HPID account
          3. Click on Back button
          4. Click on Smart Tasks tile
          5. Click on Sign In button
          6. Login HPID account

        Expected Result:
          6. Verify Smart Tasks screen:
             - Title
             - "+" button
        """
        self.__load_hpid_sign_in_screen(index=1)
        # Handle for welcome screen of Google Chrome
        self.google_chrome.handle_welcome_screen_if_present()
        self.driver.wait_for_context("WEBVIEW_chrome")
        self.hpid.verify_hp_id_sign_in()
        self.hpid.login(self.hpid_username, self.hpid_pwd, change_check={"wait_obj": "sign_in_button", "invisible": True})
        #Todo: From HPID login to Smart Tasks screen will take to 20s. And has CR GDG-1768 for tracking this issue
        self.home.check_run_time_permission(accept=True, timeout=20)
        self.smart_tasks.verify_smart_tasks_screen()

    @pytest.mark.parametrize("invalid_name",[".12", "%ab", " a1", "long_name"])
    def test_04_new_smart_task_invalid_name(self, invalid_name):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name starts with period or space or any special characters
             Or type smart task name ends with period or space or any special characters

        Expected Result:
          3. Verify New Smart Task name:
            - If start with period, space or special characters: cannot see in new smart task name
            - If name typed more than 255 characters: error message "smart task name missing" popup
        """
        if invalid_name == "long_name":
            invalid_name = "".join("long" for _ in range(64))
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd)
        self.fc.flow_smart_task_load_smart_task_create_screen(invalid_name)
        if invalid_name == "long_name":
            self.smart_tasks.add_smart_task_for_print()
            self.smart_tasks.select_save_btn()
            self.smart_tasks.verify_smart_task_invalid_name_popup(is_missing=True)
        else:
            self.smart_tasks.verify_smart_task_name(invalid_name)

    def test_05_create_new_smart_task_without_saving(self):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Print
          5. Enable print to your smart task
          6. Click on Back button
          7. Click on Back button

        Expected Result:
          7. Verify popup without saving smart task screen:
             + body message
             + LEAVE button
             + GO BACK button
        """
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd)
        self.fc.flow_smart_task_load_smart_task_create_screen("print_photo")
        self.smart_tasks.add_smart_task_for_print()
        self.fc.select_back()
        self.smart_tasks.verify_are_you_sure_popup()

    @pytest.mark.parametrize("print_option",["two_sided_off,color,single_copies",
                                             "short_edge,color,single_copies",
                                             "long_edge,color,single_copies",
                                             "two_sided_off,black,single_copies",
                                             "short_edge,black,single_copies",
                                             "long_edge,black,single_copies",
                                             "two_sided_off,color,multi_copies",
                                             "short_edge,color,multi_copies",
                                             "long_edge,color,multi_copies",
                                             "two_sided_off,black,multi_copies",
                                             "short_edge,black,multi_copies",
                                             "long_edge,black,multi_copies"
                                             ])
    def test_06_create_new_smart_task_for_print(self, print_option):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Print
          5. Enable print to your smart task
          6. For print type:
             - color_two_sided_off
             - color_short_edge: Click on Two-sided, select Short Edge
             - color_long_edge: Click on Two-sided, select Long Edge
             - black_two_sided_off: Click on Color, select Black
             - black_short_edge: Click on Color, select Black. And, Click on Two-sided, select Short Edge
             - black_long_edge: Click on Color, select Black. And, Click on Two-sided, select Long Edge
          7. Click on Back button
          8. Click on Save button
          9. Click on OK button if "You just created a Smart Task" popup
             Or Click on BACK TO SMART TASK BUTTON if "Smart Tasks saved" popup

        Expected Result:
          8. If print type is color_two_sided_off, then verify "You just created a Smart Task" popup
             Other options from step 6, then verify "Smart Tasks saved" popup with below points:
                - Title
                - START THIS SMART TASK BUTTON
                - BACK TO SMART TASK BUTTON
                - HOME BUTTON
          9.  Verify Smart Tasks lists screen if clicking "BACK TO SMART TASKS" button from Step 9
        """
        print_option = print_option.split(",")
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], print_option[1], (datetime.datetime.now()))
        sides_option = {
            "two_sided_off": self.smart_tasks.TWO_SIDE_OFF,
            "short_edge": self.smart_tasks.SHORT_EDGE,
            "long_edge": self.smart_tasks.LONG_EDGE}
        color_option = {
            "color": self.smart_tasks.COLOR_BTN,
            "black": self.smart_tasks.GRAYSCALE_BTN}
        copies_num = {"single_copies": 1,
                      "multi_copies": 2}
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print(copies_num=copies_num[print_option[2]], 
                                                  two_sided_option=sides_option[print_option[0]], 
                                                  color_type=color_option[print_option[1]])
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=True, btn_name=self.smart_tasks.BACK_TO_SMART_TASKS_BTN)
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)

    @pytest.mark.parametrize("email_option", ["", "qa.mobiautotest"])
    def test_07_create_new_smart_task_with_invalid_email(self, email_option):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Email
          5. Enable email to your smart task
          6. For email type:
             - empty_email: Leave email filed empty
             - invalid_email: type invalid email address
          7. Click on Back button
          8. Click on OK button

        Expected Result:
          7. If empty recipient from step 6, then verify empty recipient popup:
                - Message
            If invalid recipient from step 6, then verify invalid email address popup:
                - Message
        """
        smart_task_name = "{}_{:%Y_%m_%d_%H_%M_%S}".format(email_option, (datetime.datetime.now()))
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_email(email_option)
        if email_option == "qa.mobiautotest":
            self.smart_tasks.verify_invalid_email_popup_screen(is_empty=False)
        else:
            self.smart_tasks.verify_invalid_email_popup_screen(is_empty=True)
        self.smart_tasks.select_ok_btn()

    def test_08_create_new_smart_task_for_email(self):
        """
        Description:
          1. Load to Smart Tasks screen with an new HPID account
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Email
          5. Enable email to your smart task
          6. Type an email address
          7. Click on Back button
          8. Click on Save button

        Expected Result:
          8. Verify "Smart Tasks saved" popup
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "email", (datetime.datetime.now()))
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_email(to_email=self.email_address)
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=True, btn_name=self.smart_tasks.BACK_TO_SMART_TASKS_BTN)
        '''
    @pytest.mark.parametrize("save_option", ["google_drive", "dropbox"])
    def test_09_create_new_task_for_saving(self, save_option):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Save
          5. Enable Dropbox or Google Drive account for saving
          6. Click on Back button
          7. Click on Save button

        Expected Result:
          4. Verify Save to screen with below points:
             + Title
             + Cloud accounts list
          7. Verify Saved! screen popup with
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], save_option, (datetime.datetime.now()))
        save_options = {"google_drive": self.smart_tasks.SAVE_TO_GGDRIVE,
                        "dropbox": self.smart_tasks.SAVE_TO_DROPBOX
                        }
        import pdb;pdb.set_trace()
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd, create_acc=False)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_saving(save_options[save_option])
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=True)
        '''
    def test_10_create_new_smart_task_with_existed_name(self):
        """
        Description:
          1. Load to Smart Tasks screen
          2. Click on CREATE NEW SMART TASKS or "+" button
          3. Type smart task name
          4. Click on Print
          5. Enable Print
          6. Click on Back button
          7. Click on Save button
          8. Click on OK button
          9. Click on "+" button
          10. Type the same Smart Task name from step2
          11. Click on Print
          12. Enable Print
          13. Click on Back button
          14. Click on Save button

        Expected Result:
          7. Verify Smart Tasks Saved! popup screen
          14. Verify smart task existed name popup with:
                - message: A Smart Task name already existed....
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.driver.driver_info["desired"]["udid"], "existed_name", (datetime.datetime.now()))
        self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd, create_acc=False)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_print()
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=True, btn_name=self.smart_tasks.BACK_TO_SMART_TASKS_BTN)
        self.smart_tasks.load_smart_task_create_screen()
        self.smart_tasks.input_smart_task_name(smart_task_name)
        self.smart_tasks.add_smart_task_for_print()
        self.smart_tasks.select_save_btn()
        self.smart_tasks.verify_smart_task_invalid_name_popup(is_missing=False)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_hpid_sign_in_screen(self, index=0):
        """
        1. Logout HPID if HPID still login
        2. Load to Home screen
        3. Click on Smart Tasks tile, and click on get started button
        """
        self.fc.reset_app()
        self.driver.clear_app_cache(PACKAGE.GOOGLE_CHROME)
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.select_tile_by_name(self.home.get_text_from_str_id(TILE_NAMES.SMART_TASKS))
        self.ows_value_prop.verify_ows_value_prop_screen(tile=True)
        self.ows_value_prop.select_value_prop_buttons(index=index)
        '''
