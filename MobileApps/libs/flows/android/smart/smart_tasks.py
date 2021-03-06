from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging
import time
from SAF.exceptions.saf_exceptions import ObjectFoundException

class SmartTasks(SmartFlow):
    flow_name = "smart_tasks"
    FROM_CAMERA = "smart_task_camera"
    FROM_SCANNER = "smart_task_scanner"
    FROM_FILES = "smart_task_files"
    FROM_PHOTOS = "smart_task_photos"
    TILE_STATUS_ON = "on_txt"
    TILE_STATUS_OFF = "off_txt"
    SAVE_TO_DROPBOX = "save_to_dropbox"
    SAVE_TO_GGDRIVE = "save_to_ggdrive"
    TWO_SIDE_OFF = "two_side_off"
    SHORT_EDGE = "short_edge"
    LONG_EDGE = "long_edge"
    GRAYSCALE_BTN = "smart_task_print_black_btn"
    COLOR_BTN = "smart_task_print_color_btn"
    START_THIS_SMART_TASK_BTN = "start_this_smart_task_btn"
    BACK_TO_SMART_TASKS_BTN = "back_to_smart_tasks_btn"
    HOME_BTN = "home_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def smart_task_str_id_cleaner(self, obj_name, replacement_string):
        """
        There are a lot of strings including string "Smart Task", but use "%1$s" instead of string "Smart Task"
        :param obj_name:
        :param obj_name_for_dynamic_string: odj_name which the String_ID is for dynamic string translated in all languages
        """
        actual_str = self.driver.return_str_id_value(obj_name)
        replace_str = self.driver.return_str_id_value(replacement_string)
        actual_str = actual_str.replace("%1$s", replace_str)
        return actual_str

    def select_get_started_btn(self):
        """
        Click on Get Started button on Smart Tasks welcome screen
        """
        self.driver.click("get_started_btn")
    
    def select_learn_more_btn(self):
        """
        Click on What is a Smart Task? Learn more button on Smart Tasks welcome screen
        """
        self.driver.click("smart_tasks_learn_more_btn")

    def load_smart_task_create_screen(self):
        """
        Load to Create New Smart Task screen via:
            - Click on CREATE NEW SMART TASK button on Smart Tasks screen with empty smart tasks lists
              or click on "+" button on Smart Tasks screen

        End of flow: Create New Smart Tasks screen
        """
        if self.driver.wait_for_object("create_smart_task_btn", timeout=15, raise_e=False):
            self.driver.click("create_smart_task_btn", change_check={"wait_obj": "create_smart_task_btn", "invisible": True})
        else:
            self.driver.click("add_smart_task_btn", change_check={"wait_obj": "add_smart_task_btn", "invisible": True})

    def input_smart_task_name(self, smart_task_name):
        """
        1. Click on "Name Your New Smart Task" on Create Smart Task screen
        2. Input a name
        :param: smart_task_name
        """
        self.driver.send_keys("smart_task_name_edit", smart_task_name)

    def select_ok_btn(self):
        """
        Click on Ok button if any screen has OK button on Smart Tasks w
        """
        self.driver.click("ok_btn")

    def add_smart_task_for_print(self, copies_num="", two_sided_option="", color_type=""):
        """
        1. Click on Print on Create new smart task screen
        2. Enable print
        3. Click on Copies button, then choose copies number
        4. Click on Color button, then can choose options
        5. Click on Two-sided, then can choose options:
        :param copies_num:
        :param: two_sided_option:
                - TWO_SIDE_OFF
                - SHORT_EDGE
                - LONG_EDGE
        :param color_type:
               - COLOR_BTN
               - GRAYSCALE_BTN
        """
        self.driver.click("print_item")
        self.toggle_new_smart_task_on_off()
        if copies_num:
            self.driver.click("copies_btn")
            copy_num = self.driver.find_object("copies_spinner").text
            if int(copy_num) != copies_num:
                self.driver.scroll("copies_spinner", direction="down", format_specifier=[copies_num], check_end=False)
            self.select_ok_btn()
        if two_sided_option:
            self.driver.click("two_sided_btn")
            self.driver.click(two_sided_option)
        if color_type:
            self.driver.click("color_btn")
            self.driver.click(color_type)
        self.driver.press_key_back()

    def add_smart_task_for_email(self, to_email):
        """
        1. Click on Email on Create new smart task screen
        2. Enable Email
        3. Type email address
        4. Click on Back button on Email screen
        :param to_email:
        """
        self.driver.click("email_item")
        self.toggle_new_smart_task_on_off()
        self.driver.send_keys("email_address_hint", to_email)
        self.driver.press_key_back()

    def add_smart_task_for_saving(self, acc_name):
        """
        1. Click on Save on Create new smart task screen
        2. Enable cloud account name
        3. Click on Back button
        :param acc_name:
        """
        self.driver.click("save_item")
        self.toggle_cloud_account_on_off_for_saving(acc_name, on=True)
        self.driver.press_key_back()

    def toggle_cloud_account_on_off_for_saving(self, acc_name, on=True):
        """
        Enable a cloud account by its name for saving files/photos through smart tasks
        :param acc_name:
           - SAVE_TO_DROPBOX
           - SAVE_TO_GGDRIVE
        :param on: True or False
        :param raise_e:
        """
        # Smart Tasks take some time to load to Save To screen
        self.driver.wait_for_object("cloud_acc_title", timeout=10, format_specifier=[self.driver.return_str_id_value(acc_name)])
        cloud_acc_switch = self.driver.find_object("cloud_acc_switch", format_specifier=[self.driver.return_str_id_value(acc_name)])
        if on != (cloud_acc_switch.get_attribute("checked").lower() == "true"):
            cloud_acc_switch.click()
        # For toggle cloud account on smart tasks, take around 40s to finish it
        self.driver.wait_for_object("loading_message", invisible=True, timeout=40)
        self.driver.wait_for_object("cloud_acc_switch", format_specifier=[self.driver.return_str_id_value(acc_name)])
        cloud_acc_current_switch_status = self.driver.get_attribute("cloud_acc_switch", attribute="checked", format_specifier=[self.driver.return_str_id_value(acc_name)])
        assert on == (cloud_acc_current_switch_status.lower() == "true"), "Toggle of {} is not matched with expectation {}".format(cloud_acc_current_switch_status, on)

    def select_save_btn(self):
        """
        Click on Save button on Create New Smart Task screen
        """
        self.driver.click("save_btn")

    def select_smart_task_source_type(self, source_type, is_checked=True, invisible=True):
        """
        On source of your image or document screen, you can choose below type
        :param source_type:
               - FROM_CAMERA
               - FROM_SCANNER
               - FROM_FILES
               - FROM_PHOTOS
        :param is_checked: True or False
        :param invisible: True or False
        """
        if is_checked:
            self.driver.wait_for_object("smart_task_camera")
            self.driver.wait_for_object("smart_task_scanner", invisible=invisible)
            self.driver.wait_for_object("smart_task_files")
            self.driver.wait_for_object("smart_task_photos")
        self.driver.click(source_type, change_check={"wait_obj": source_type, "invisible": True})

    def select_btn_on_saved_screen(self, is_checked=True, btn_name=""):
        """
        Click button on Saved! screen:
             - Start This Smart Task button
             - Back To Smart Tasks button
             - Home button
        :param btn_name:
             - START_THIS_SMART_TASK_BTN
             - BACK_TO_SMART_TASKS_BTN
             - HOME_BTN
        """
        if is_checked:
            self.driver.wait_for_object("smart_task_saved_title")
            self.driver.wait_for_object("smart_task_saved_icon")
        if btn_name:
            self.driver.click(btn_name, change_check={"wait_obj": btn_name, "invisible": True})

    def select_smart_task(self, smart_task_name, click_obj=True):
        """

        :param smart_task_name:
        :return:
        """
        try:
            self.driver.scroll("smart_tasks_header", direction="down", format_specifier=[smart_task_name], timeout=60, check_end=False, click_obj=click_obj)
        except NoSuchElementException:
            self.driver.scroll("smart_tasks_header", direction="up", format_specifier=[smart_task_name], timeout=60, check_end=False, click_obj=click_obj)

    def select_smart_task_from_more_option(self, smart_task_name, from_option_icon=True):
        """
        Select any smart task from smart tasks list
        Click on More Option icon
        Click on Start button
        :param smart_task_name:
        :param from_option_icon: True or False
        """
        self.select_smart_task(smart_task_name, click_obj=not from_option_icon)
        self.driver.click("smart_tasks_options_icon", format_specifier=[smart_task_name])
        self.driver.click("start_btn")

    def edit_smart_task(self, smart_task_name):
        """
        Select any smart task from smart tasks list
        Click on More Option icon
        Click on Edit button
        :param smart_task_name:
        """
        self.select_smart_task(smart_task_name, click_obj=False)
        self.driver.click("smart_tasks_options_icon", format_specifier=[smart_task_name])
        self.driver.click("edit_btn")

    def select_smart_task_from_preview_screen(self, smart_task_name):
        """
        Select any smart task from preview screen
        Click on Start button
        :param smart_task_name:
        """
        self.driver.scroll("smart_tasks_header", direction="down", scroll_object="smart_tasks_list_lv", format_specifier=[smart_task_name], full_object=False, timeout=30, check_end=False)
        self.driver.click("start_btn_from_preview", format_specifier=[smart_task_name])

    def delete_single_smart_task(self, smart_task_name, is_delete=True, raise_e=True):
        """
        - Select any smart task from smart tasks list screen
        - Click on More Option screen
        - Click on Delete button, then can choose delete or cancel
        :param smart_task_name:
        :param is_delete: True or False
        """
        try:
            self.select_smart_task(smart_task_name, click_obj=False)
            self.driver.click("smart_tasks_options_icon", format_specifier=[smart_task_name])
            self.driver.click("delete_btn")
            if is_delete:
                self.driver.click("delete_smart_task_popup_delete")
            else:
                self.driver.click("delete_smart_task_popup_cancel")
            return True
        except (TimeoutException, NoSuchElementException)as ex:
            if raise_e:
                raise ex
            return False

    def dismiss_smart_tasks_complete_popup_screen(self, is_checked=True):
        """
        Verify " Your Smart Task is on its way!" popup
          - Message
          - HOME button
        Click on HOME button on Smart Task upload complete screen
        """
        if is_checked:
            self.driver.wait_for_object("_system_txt_place_holder", timeout=90, format_specifier=[self.smart_task_str_id_cleaner("smart_task_complete_title", "smart_task_title")])
        self.driver.click("smart_task_home_btn")

    def dismiss_smart_task_created_popup(self, is_checked=True):
        """
        1. Verify "You just created a smart task1" popup
        2. Then click on OK button
        :param is_checked: True or False
        """
        if is_checked:
            self.driver.wait_for_object("smart_task_created_title")
            self.driver.wait_for_object("ok_btn")
        self.driver.click("ok_btn")

    def dismiss_smart_task_skip_btn(self, is_checked=True):
        """
        Dismiss Smart Tasks welcome popup screen
        """
        if is_checked:
            self.driver.wait_for_object("smart_task_welcome_title")
            self.driver.wait_for_object("skip_btn")
        self.driver.click("skip_btn")

    def toggle_new_smart_task_on_off(self, enable=True):
        """
        switch on/off button for adding or removing new smart task
        :param enable: True or False
        """
        on_off_switch = self.driver.find_object("on_off_btn")
        if enable != (on_off_switch.get_attribute("checked").lower() == "true"):
            on_off_switch.click()
        # verify if current status of switch icon is not matched with expectation
        current_status_of_off_switch = self.driver.find_object("on_off_btn")
        if enable != (current_status_of_off_switch.get_attribute("checked").lower() == "true"):
            raise NoSuchElementException("Toggle of {} is not matched with expectation {}".format(current_status_of_off_switch, enable))

    def __count_smart_tasks(self):
        """
        Get name of all smart tasks name on Smart Tasks list screen
        """
        self.driver.wait_for_object("smart_tasks_list_lv", timeout=20)
        smart_tasks_list = []
        bottom = False
        timeout = time.time() + 90
        while not bottom and time.time() < timeout:
            smart_task_titles = self.driver.find_object("smart_tasks_header", multiple=True)
            for each_smart_task in smart_task_titles:
                if each_smart_task.text not in smart_tasks_list:
                    smart_tasks_list.append(each_smart_task.text)
            bottom = self.driver.swipe(check_end=True)[1]
        return smart_tasks_list

    def delete_all_smart_tasks(self):
        """
        Delete all specific smart tasks from Smart Tasks list screen
        """
        smart_tasks_list = self.__count_smart_tasks()
        smart_task_partial_name = self.driver.driver_info["desired"]["udid"]
        for smart_task in smart_tasks_list:
            if smart_task_partial_name in smart_task:
                self.delete_single_smart_task(smart_task, is_delete=True, raise_e=False)


    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    def verify_smart_tasks_without_login_screen(self):
        """
        Verify that current screen is Smart Tasks screen via:
            - title
            - body message
            - Get Started button
        """
        self.driver.wait_for_object("smart_task_sigin_btn")
        self.driver.wait_for_object("get_started_btn")

    def verify_smart_tasks_welcome_screen(self):
        """
        Verify Smart Tasks welcome screen with:
           - Title: Welcome to Smart Tasks!
           - Body message: Create custom Smart Tasks to complete your repetitive tasks
           - Sign In link: Already have Smart Tasks? Sign In
        :param invisible:
        """
        self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[self.smart_task_str_id_cleaner("welcome_smart_task_title", "smart_tasks_title")])
        self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[self.smart_task_str_id_cleaner("custom_smart_tasks_message", "smart_tasks_title")])

    def verify_smart_tasks_screen(self):
        """
        Verify Smart Tasks screen with:
         - Title
         - "+" button
        """
        self.driver.wait_for_object("smart_tasks_title")
        self.driver.wait_for_object("add_smart_task_btn")

    def verify_smart_tasks_learn_more_screen(self):
        """
        - Click on What is a Smart Task? Learn more button
        - Verify Smart Tasks learn more screen via:
            - body message
            - Get Started button
        """
        self.driver.wait_for_object("smart_task_welcome_title")
        self.driver.wait_for_object("get_started_btn")

    def verify_smart_tasks_list_screen(self, is_empty=True):
        """
        Verify Smart Tasks screen with a list or empty list
        :param is_empty:
                    - True, then verify empty list screen
                    - False, then verify smart tasks list screen
        """
        if is_empty:
            self.driver.wait_for_object("create_smart_task_btn", timeout=90)
            self.driver.wait_for_object("no_smart_tasks_msg")
        else:
            self.driver.wait_for_object("smart_tasks_list_lv", timeout=90)

    def verify_smart_task_invalid_name_popup(self, is_missing=True):
        """
        If smart task name is missing, then:
           - Verify Smart Task name missing popup
        If smart task name already existed, then:
           - Verify Smart Task existed name popup screen
        """
        if is_missing:
            self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[self.smart_task_str_id_cleaner("smart_task_name_missing_msg", "smart_task_title")])
        else:
            self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[self.smart_task_str_id_cleaner("smart_task_name_exist_msg", "smart_task_title")])

    def verify_invalid_email_popup_screen(self, is_empty=True):
        """
        - If the email address area is empty, then:
             Verify empty email address popup screen
        - If the email address is invalid, but not empty, then:
             Verify invalid email address popup screen
        :param is_empty:  True or False (invalid email address)
        """
        if is_empty:
            self.driver.wait_for_object("empty_email_msg")
        else:
            self.driver.wait_for_object("invalid_email_msg")

    def verify_are_you_sure_popup(self):
        """
        Verify " Are you sure you want to leave this screen without saving this Smart Task?" popup
        :return:
        """
        self.driver.wait_for_object("_system_txt_place_holder", format_specifier=[self.smart_task_str_id_cleaner("are_you_sure_popup", "smart_task_title")])

    def verify_smart_task_name(self, expected_name):
        """
        - Get new smart task name on create smart task screen
        - Then verify smart task name should not match expected name
        :param expected_name
        """
        smart_task_name = self.driver.get_text("smart_task_name_edit")
        if smart_task_name == expected_name:
            raise NoSuchElementException("{} should not match expected name {}".format(smart_task_name, expected_name))

    def verify_non_existed_smart_task(self, smart_task_name):
        """
        Verify the target smart task is invisible on smart tasks list screen
        :param smart_task_name
        """
        try:
            self.driver.scroll("smart_tasks_header", format_specifier=[smart_task_name], timeout=30, check_end=False, click_obj=False)
            raise ObjectFoundException("A smart task: "+ smart_task_name + " is found when it shouldn't be")
        except NoSuchElementException:
            return True

    def verify_smart_task_history_list(self , is_empty=False):
        """
        Verify empty/non_empty list of Smart Task History
        """
        if is_empty:
            #return self.driver.wait_for_object("empty_smart_task_title") is not False
            return self.driver.wait_for_object("empty_smart_task_message") is not False
        else:    
            self.driver.wait_for_object("smart_task_status_icon")
            self.driver.click("smart_task_completed")
            self.driver.wait_for_object("smart_task_message")
            return True
                                                                                                                                                               
