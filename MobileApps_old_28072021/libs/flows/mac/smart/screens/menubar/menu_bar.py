# encoding: utf-8
'''
menu bar

@author: ten
@create_date: July 29, 2019
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedItemPresentException
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility


class MenuBar(SmartScreens):
    folder_name = "menubar"
    flow_name = "menu_bar"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(MenuBar, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self):
        pass

    def wait_for_hp_smart_drop_down_list_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait HP Smart drop down list load correctly after clicking HP Smart item.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_hp_smart_drop_down_list_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("menu_bar_about_hp_smart_btn", timeout=timeout, raise_e=raise_e)

    def wait_for_about_hp_smart_screen_display(self, timeout=30, raise_e=True):
        '''
        This is a method to wait About HP Smart screen load correctly after clicking About HP Smart item.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[wait_for_about_hp_smart_screen_display]-Wait for screen loading... ")

        return self.driver.wait_for_object("menu_bar_about_hp_smart_contents_1", timeout=timeout, raise_e=raise_e)

    def click_menubar_hpsmart(self):
        '''
        Click menubar HP Smart option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_HPSmart]-Click tHPSmart... ")
        self.driver.click("menu_bar_hp_smart")

    def click_menubar_hpsmart_quithpsmart_btn_after_welcome_flow(self):
        '''
        Click menubar quit hpsmart option after welcome flow
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_HPSmart]-Click tHPSmart... ")
        self.driver.click("menu_bar_quit_hp_smart_btn_after_welcome_flow") 

    def click_menubar_hpsmart_abouthpsmart_btn(self):
        '''
        Click about hpsmart option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menubar_DataCollectionNoticeSettings_btn]-Click 'AboutHPSmart' button... ")

        self.driver.click("menu_bar_about_hp_smart_btn")

    def click_crtl_shift_on_about_hp_smart_screen(self):
        '''
        This is a method to go to Reset Device Region Screen by clicking Ctrl + Shift + right click on About screen.
        :parameter:
        :return:
        '''
#         self.driver.context_click("menu_bar_about_hp_smart_contents_1", is_need_press_key=True, is_key_first=True)
        self.driver.control_shift_and_right_click("menu_bar_about_hp_smart_contents_1")

    def click_menubar_hpsmart_sendfeedback_btn(self):
        '''
        Click SendFeedback button
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_HPSmart_SendFeedback_btn]-Click 'SendFeedback' button... ")

        self.driver.click("menu_bar_send_feedback_btn")

    def click_menubar_personalize_tiles_btn(self):
        '''
        Click menubar_personalize_tiles_btn
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_personalize_tiles_btn]-menubar_personalize_tiles_btn... ")

        self.driver.click("menubar_personalize_tiles_btn")

    def click_menubar_hpsmart_privacy_settings_btn(self):
        '''
        Click menubar_hpsmart_privacy_settings_btn
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_hpsmart_privacy_settings_btn]-menubar_hpsmart_privacy_settings_btn... ")

        self.driver.click("menubar_hpsmart_privacy_settings_btn")

    def click_menubar_hpsmart_hidehpsmart_btn(self):
        '''
        Click HideHPSmart option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menubar_HPSmart_HideHPSmart_btn]-Click 'HideHPSmart' button... ")

        self.driver.click("menu_bar_hide_hp_smart_btn")

    def click_menubar_hpsmart_hideothers_btn(self):
        '''
        Click HideOthers option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_HPSmart_HideOthers_btn]-Click 'HideOthers' button... ")

        self.driver.click("menu_bar_hide_others_btn")

    def click_menubar_hpsmart_showall_btn(self):
        '''
        Click show all option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_HPSmart_ShowAll_btn]-Click 'ShowAll' button... ")

        self.driver.click("menu_bar_show_all_btn")

    def click_menubar_hpsmart_quithpsmart_btn(self):
        '''
        Click quit hp smart option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[menubar_HPSmart_QuitHPSmart_btn]-Click 'QuitHPSmart' button... ")

        self.driver.click("menu_bar_quit_hp_smart_btn")

    def click_menubar_hpsmart_icon(self):
        '''
        Click hp smart option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menubar_HPSmart_Icon-Click 'menubar_HPSmart_Icon' button... ")

        self.driver.click("menu_bar_hp_smart_icon")

    def click_menubar_edit(self):
        '''
        Click edit option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menubar_Edit-Click 'menubar_Edit' button... ")

        self.driver.click("menu_bar_edit")

    def click_menubar_printers(self):
        '''
        Click printers option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menubar_Printers-Click 'menubar_Printers' button... ")

        self.driver.click("menu_bar_printers")

    def click_add_setup_a_printer(self):
        '''
        Click add_setup_a_printer option
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_add_setup_a_printer]-Click 'add_setup_a_printer' button... ")

        self.driver.click("menu_bar_add_setup_a_printer")

    def click_diagnose_fix(self):
        '''
        This is a method to click Diagnose & Fix option under Printer menu.
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_diagnose_fix]-Click  Diagnose & Fix option... ")

        self.driver.click("menu_bar_diagnose_fix")

    def click_close_btn(self):
        '''
        Click close button
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_close_btn-Click 'close' button... ")

        self.driver.click("close_btn", is_native_event=True)

    def click_menu_bar_about_hp_smart_image_ten_times(self):
        '''
        Click menu_bar about hp smart image
        :parameter:
        :return:
        '''
        logging.debug("[Menubar]:[click_menu_bar_about_hp_smart_image-menu_bar_about_hp_smart_image... ")
        for i in range(10):
            self.driver.click("menu_bar_about_hp_smart_image")

    def tigger_prompts_screen(self):
        '''
        This is a method to right click find printer icon.
        :parameter:
        :return:
        '''
        logging.debug("[MainScreen]:[tigger_prompts_screen... ")

        self.driver.context_click("menu_bar_about_hp_smart_image", is_need_press_key=True, is_key_first=True)

    def get_value_of_menubar_apple(self):
        '''
        get value of apple icon
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_Apple]-Get the contents of menubar_Apple ...  ")

        return self.driver.get_title("menu_bar_apple")

    def get_value_of_menubar_hpsmart(self):
        '''
        get value of hpsmart option
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart]-Get the contents of menubar_HPSmart...  ")

        return self.driver.get_title("menu_bar_hp_smart") 

    def get_value_of_menubar_edit(self):
        '''
        get value of edit option
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_Edit]-Get the contents of menubar_Edit...  ")

        return self.driver.get_title("menu_bar_edit")

    def get_value_of_menubar_printers(self):
        '''
        get value of printers
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_Printers]-Get the contents of menubar_Printers ...  ")

        return self.driver.get_title("menu_bar_printers")

    def get_value_of_menubar_hpsmart_abouthpsmart_btn(self):
        '''
        get value of about hpsmart button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_AboutHPSmart_btn]-Get the contents of menubar_HPSmart_AboutHPSmart_btn ...  ")

        return self.driver.get_title("menu_bar_about_hp_smart_btn")

    def get_value_of_menubar_hpsmart_sendfeedback_btn(self):
        '''
        get value of about send feedback button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_SendFeedback_btn]-Get the contents of menubar_HPSmart_SendFeedback_btn ...  ")

        return self.driver.get_title("menu_bar_send_feedback_btn")

    def get_value_of_menubar_hpsmart_personalize_tiles_btn(self):
        '''
        get value of menubar_personalize_tiles_btn
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_personalize_tiles_btn]-Get the contents of menubar_personalize_tiles_btn...  ")

        return self.driver.get_title("menubar_personalize_tiles_btn")

    def get_value_of_menubar_hpsmart_privacy_settings_btn(self):
        '''
        get value of menubar_hpsmart_privacy_settings_btn
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_hpsmart_privacy_settings_btn]-Get the contents of menubar_hpsmart_privacy_settings_btn...  ")

        return self.driver.get_title("menubar_hpsmart_privacy_settings_btn")

    def get_value_of_menu_bar_hpsmart_notification_settings_btn(self):
        '''
        get value of menubar_hpsmart_privacy_settings_btn
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_hpsmart_privacy_settings_btn]-Get the contents of menubar_hpsmart_privacy_settings_btn...  ")

        return self.driver.get_title("menu_bar_notification_settings_btn")

    def get_value_of_menubar_hpsmart_hidehpsmart_btn(self):
        '''
        get value of HideHPSmart button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_HideHPSmart_btn]-Get the contents of menubar_HPSmart_HideHPSmart_btn...  ")

        return self.driver.get_title("menu_bar_hide_hp_smart_btn")

    def get_value_of_menubar_hpsmart_hideothers_btn(self):
        '''
        get value of HideOthers button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_HideOthers_btn]-Get the contents of menubar_HPSmart_HideOthers_btn...  ")

        return self.driver.get_title("menu_bar_hide_others_btn")

    def get_value_of_menubar_hpsmart_showall_btn(self):
        '''
        get value of showall button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_ShowAll_btn]-Get the contents of menubar_HPSmart_ShowAll_btn ...  ")

        return self.driver.get_title("menu_bar_show_all_btn")

    def get_value_of_menubar_hpsmart_quithpsmart_btn(self):
        '''
        get value of quithpsmart button
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_HPSmart_QuitHPSmart_btn]-Get the contents of menubar_HPSmart_QuitHPSmart_btn...  ")

        return self.driver.get_title("menu_bar_quit_hp_smart_btn")

    def get_value_of_menubar_hpsmart_abouthpsmart_contents_1(self):
        '''
        get value of AboutHPSmart contents
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_HPSmart_AboutHPSmart_contents_1]-Get the contents of HPSmart_AboutHPSmart_contents_1...  ")

        return self.driver.get_value("menu_bar_about_hp_smart_contents_1")

    def get_value_of_menubar_hpsmart_abouthpsmart_contents_2(self):
        '''
        get value of AboutHPSmart contents
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_HPSmart_AboutHPSmart_contents_2]-Get the contents of HPSmart_AboutHPSmart_contents_2...  ")

        return self.driver.get_value("menu_bar_about_hp_smart_contents_2")

    def get_value_of_menubar_hpsmart_abouthpsmart_contents_3(self):
        '''
        get value of AboutHPSmart contents
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_HPSmart_AboutHPSmart_contents_3]-Get the contents of HPSmart_AboutHPSmart_contents_3...  ")

        return self.driver.get_value("menu_bar_about_hp_smart_contents_3")

    def get_value_of_menubar_edit_copy(self):
        '''
        get value of copy
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_Edit_Copy]-Get the contents of menubar_Edit_Copy...  ")

        return self.driver.get_title("menu_bar_copy")

    def get_value_of_menubar_edit_paste(self):
        '''
        get value of paste
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menubar_Edit_Paste]-Get the contents of menubar_Edit_Paste...  ")

        return self.driver.get_title("menu_bar_paste")

    def get_value_of_add_setup_a_printer(self):
        '''
        get value of add/setup a printer
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menu_bar_add_setup_a_printer]-Get the contents of menu_bar_add_setup_a_printer")

        return self.driver.get_title("menu_bar_add_setup_a_printer")

    def get_value_of_diagnose_fix(self):
        '''
        get value of diagnose fix
        :parameter:
        :return:
        '''
        logging.debug("[MenuBar]:[get_value_of_menu_bar_add_setup_a_printer]-Get the contents of menu_bar_diagnose_fix")

        return self.driver.get_title("menu_bar_diagnose_fix")

# -------------------------------Verification Methods--------------------------
    def verify_menubar(self):
        '''
        Verify menu bar option UI string
        :parameter:
        :return:
        '''
        logging.debug("verify the menu bar")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='menu_bar')
        assert self.get_value_of_menubar_apple() == test_strings['menubar_apple']
        assert self.get_value_of_menubar_hpsmart() == test_strings['menubar_hpsmart']
        assert self.get_value_of_menubar_edit() == test_strings['menubar_edit']
        assert self.get_value_of_menubar_printers() == test_strings['menubar_printers']

    def verify_hp_smart_drop_down_list(self):
        '''
        This is a verification method to check UI strings of HP Smart Drop-down list.
        :parameter:
        :return:
        '''
        test_strings = smart_utility.get_local_strings_from_table(screen_name='menu_bar')
        self.wait_for_hp_smart_drop_down_list_display()
        logging.debug("Start to verify UI string of HP Smart Drop-down list")
        assert self.get_value_of_menubar_hpsmart_abouthpsmart_btn() == test_strings['abouthpsmart_btn']
        assert self.get_value_of_menubar_hpsmart_personalize_tiles_btn() == test_strings['personalize_tiles_btn']
        assert self.get_value_of_menubar_hpsmart_sendfeedback_btn() == test_strings['sendfeedback_btn']
        assert self.get_value_of_menubar_hpsmart_privacy_settings_btn() == test_strings['privacy_settings_btn']
        assert self.get_value_of_menu_bar_hpsmart_notification_settings_btn() == test_strings['notification_settings_btn']
        assert self.get_value_of_menubar_hpsmart_hidehpsmart_btn() == test_strings['hidehpsmart_btn']
        assert self.get_value_of_menubar_hpsmart_hideothers_btn() == test_strings['hideothers_btn']
        assert self.get_value_of_menubar_hpsmart_showall_btn() == test_strings['showall_btn']
        assert self.get_value_of_menubar_hpsmart_quithpsmart_btn() == test_strings['quithpsmart_btn']

    def verify_selectionisgrayedout(self):
        '''
        Verify selection is grayed out
        :parameter:
        :return:
        '''
        logging.debug("verify About HpSmart disabled")
        if self.driver.is_enable("menu_bar_about_hp_smart_btn"):
            raise UnexpectedItemPresentException("the option can be clicked")
        return True

    def verify_behavior_of_buttons(self):
        '''
        verify 'Show All'is not clickable but'Hide Smart'&'Hide Others' are clickable 
        :parameter:
        :return:
        '''
        logging.debug("verify 'Show All'is clickable but'Hide Smart'&'Hide Others' are not clickable")
        if not self.driver.is_enable("menu_bar_hide_hp_smart_btn"):
            raise UnexpectedItemPresentException("the option can not be clicked")   

        if not self.driver.is_enable("menu_bar_hide_others_btn"):
            raise UnexpectedItemPresentException("the option can not be clicked")

        if self.driver.is_enable("menu_bar_show_all_btn"):
            raise UnexpectedItemPresentException("the option can be clicked")

        return True

    def verify_edit_options(self):
        '''
        verify both option'copy'&'paste'display there, but they are grey out and not clickable
        :parameter:
        :return:
        '''
        logging.debug("verify both option'copy'&'paste'display there, but they are grey out and not clickable")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='menu_bar')
        assert self.get_value_of_menubar_edit_copy() == test_strings['edit_copy']
        assert self.get_value_of_menubar_edit_paste() == test_strings['edit_paste']
        if self.driver.is_enable("menu_bar_copy"):
            raise UnexpectedItemPresentException("the option can be clicked")

        if self.driver.is_enable("menu_bar_paste"):
            raise UnexpectedItemPresentException("the option can be clicked")

        return True

    def verify_before_oobe_printersmenu(self):
        '''
        verify 2 options displays there 
        :parameter:
        :return:
        '''
        logging.debug("1 options displays there and are grayout and not clickable: 'Add / Setup a Printer")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='menu_bar')
        assert self.get_value_of_add_setup_a_printer() == test_strings['add_printer']
        assert self.get_value_of_diagnose_fix() == test_strings['diagnose_fix']
        if self.driver.is_enable("menu_bar_add_setup_a_printer") and self.driver.is_enable("menu_bar_diagnose_fix"):
            raise UnexpectedItemPresentException("the option can be clicked")
        return True

    def verify_after_oobe_printersmenu(self):
        '''
        verify 1 options displays there
        :parameter:
        :return:
        '''
        logging.debug("4 options displays there and 'Add / Setup a Printer'option is clickable")
        test_strings = smart_utility.get_local_strings_from_table(screen_name='menu_bar')
        assert self.get_value_of_add_setup_a_printer() == test_strings['add_printer']
        assert self.get_value_of_diagnose_fix() == test_strings['diagnose_fix']
        if not self.driver.is_enable("menu_bar_add_setup_a_printer"):
            raise UnexpectedItemPresentException("the option can not be clicked")
        return True

    def verify_checkforupdates_option_grayed_out(self):
        '''
        verify 'Check for Updates..' option is grayed out
        :parameter:
        :return:
        '''
        logging.debug("verify 'Check for Updates..' option is grayed out")
        if self.driver.is_enable("menu_bar_check_for_updates_btn"):
            raise UnexpectedItemPresentException("the option can be clicked")
        return True
