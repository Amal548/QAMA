from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
from SAF.misc import saf_misc
from MobileApps.resources.const.android.const import *
from selenium.common.exceptions import TimeoutException
import datetime

pytest.app_info = "SMART"
pytest.printer_feature={"scanner": True}


class Test_Suite_01_Edit_Delete_Smart_Tasks(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define the flows
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]

        # Define the variable
        cls.udid = cls.driver.driver_info["desired"]["udid"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]

        def clean_up_class():
            cls.fc.flow_home_delete_all_smart_tasks()

        request.addfinalizer(clean_up_class)

    @pytest.mark.parametrize("edit_option", ["add_printing", "add_saving"])
    def test_01_edit_smart_tasks(self, edit_option):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for email
          5. Click Edit button for smart task from step4
             - add_printing: add printing option for executing smart tasks
             - add_saving: add saving option for executing smart tasks
          6. - If add_printing, then enable Print item for this smart task
             - If add_saving, then enable Save item for this smart task
          7. Click on Save button
        Expected Result:
          7. Verify Smart Tasks list screen
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, edit_option, (datetime.datetime.now()))
        self.__load_smart_task_screen(smart_task_name)
        self.smart_tasks.edit_smart_task(smart_task_name)
        if edit_option == "add_printing":
            self.smart_tasks.add_smart_task_for_print(copies_num=1, two_sided_option=self.smart_tasks.SHORT_EDGE, color_type=self.smart_tasks.GRAYSCALE_BTN)
        else:
            self.smart_tasks.add_smart_task_for_saving(acc_name=self.smart_tasks.SAVE_TO_DROPBOX)
        self.smart_tasks.select_save_btn()
        self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)

    @pytest.mark.parametrize("delete_option", ["cancel_btn", "delete_btn"])
    def test_02_delete_smart_tasks(self, delete_option):
        """
        Description:
          1. Load to Home screen
          2. Login HPID account
          3. Load to Smart Tasks screen
          4. Create a new smart task screen for print
          5. Click Edit button for smart task from step4
          6. Click on Delete button
          7. - cancel_btn: Click on CANCEL button
             - delete_btn: Click on DELETE button

        Expected Result:
          6. Verify Smart Task delete popup:
             - Title
             - CANCEL button
             - DELETE button
          7. - cancel_btn: Verify Smart Task list screen
             - delete_btn: This smart task is removed from smart task lists
        """
        smart_task_name = "{}_{}_{:%Y_%m_%d_%H_%M_%S}".format(self.udid, delete_option, (datetime.datetime.now()))
        self.__load_smart_task_screen(smart_task_name)
        if delete_option == "cancel_btn":
            self.smart_tasks.delete_single_smart_task(smart_task_name, is_delete=False)
            self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        else:
            self.smart_tasks.delete_single_smart_task(smart_task_name, is_delete=True)
            self.smart_tasks.verify_non_existed_smart_task(smart_task_name)

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __load_smart_task_screen(self, smart_task_name):
        """
        - Load Home screen.
        - CLick on Smart Tasks tile on Home screen
        - Click on CREATE NEW SMART TASKS button or "+"
        - Input new smart task name
        - Select Print or Email or Save option on Create Smart Task screen
        """
        self.fc.flow_home_load_smart_task_screen(create_acc=False, printer_obj=None)
        self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        self.smart_tasks.add_smart_task_for_email(to_email=self.email_address)
        self.smart_tasks.select_save_btn()
        try:
            self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=False, btn_name=self.smart_tasks.BACK_TO_SMART_TASKS_BTN)