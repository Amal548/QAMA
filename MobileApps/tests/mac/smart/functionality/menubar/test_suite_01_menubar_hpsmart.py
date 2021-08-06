#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Test_Suite_01_Menubar_HPsmart

@author: ten
@create_date: July 20, 2019
'''
import time
import logging
import pytest
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.smart.screens.menubar.feedback import Feedback
from MobileApps.libs.flows.mac.smart.screens.common.welcome import Welcome
from MobileApps.libs.flows.mac.smart.screens.common.agreement import Agreement
from MobileApps.libs.flows.mac.smart.screens.menubar.menu_bar import MenuBar
from MobileApps.libs.flows.mac.smart.screens.menubar.hp_account_information import Hpaccountinformation
from MobileApps.libs.flows.mac.smart.screens.menubar.check_for_updates_dialog import CheckforupdatesDialog
from MobileApps.libs.flows.mac.smart.screens.common.tool_bar import ToolBar
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_incomplete_dialog import PrinterSetupIncompleteDialog
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
import os

# REQUIRED
pytest.app_info = "SMART"


class Test_Suite_01_Menubar_HPsmart(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
        self.driver, self.common_flows, self.system_flows = mac_smart_setup
        self.feedback = Feedback(self.driver)
        self.menu_bar = MenuBar(self.driver)
        self.welcome = Welcome(self.driver)
        self.hp_account_information = Hpaccountinformation(self.driver)
        self.agreement = Agreement(self.driver)
        self.tool_bar = ToolBar(self.driver)
        self.main_ui = MainUI(self.driver)
        self.printer_setup_incomplete_dialog = PrinterSetupIncompleteDialog(self.driver)
        self.checkforupdates_dialog = CheckforupdatesDialog(self.driver)

    def test_01_verifymenubar(self):
        '''
        TestRail:#C14590864
        launch the app,observe the Menu Bar
        '''
        logging.debug("launch the app,observe the Menu Bar[C14590864]")
        self.welcome.wait_for_screen_load()
        self.menu_bar.verify_menubar()

    def test_02_click_hpsmartonmenubar(self):
        '''
        TestRail:#C14590865
        click HP Smart On Menu Bar-Observe the drop-down list for HP Smart

        '''
        logging.debug("click HP Smart On Menu Bar-Observe the drop-down list for HP Smart[C14590865]")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.verify_dropdownlistforhpsmart()

    def test_03_clickabouthpsmart(self):
        '''
        TestRail:#C14590867,#C14590866
        click HP Smart On Menu Bar-Observe the drop-down list  and  verify previous selection is now grayed out

        '''
        logging.debug("click HP Smart On Menu Bar-Observe the drop-down list for HP Smart and verify'About Hp Smart' dialog[C14590867]")
        self.menu_bar.click_menubar_HpSmart_abouthpsmart_btn()
        # self.verify_AboutHpSmartScreen()
        logging.debug("verify previous selection is now grayed out[C14590866]")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.verify_selectionisgrayedout()

    def test_04_sendfeedbackfunction(self):
        '''
        TestRail:#C14590868
        click Send Feedback-fill the info to required fields and click send feedback,verify the feedback send out successfully
        '''
        logging.debug("click Send Feedback-fill the info to required fields and click send feedback,verify the feedback send out successfully[C14590868]")
        os.system("pkill HP Smart")
        time.sleep(5)
        self.common_flows.launch_hpsmart_app("HP Smart")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_sendfeedback_btn()
        self.feedback.wait_for_screen_load()
        self.feedback.click_feedback_dropdown_btn_button()
        self.feedback.choose_feedback_dropdown_listitems(0)
        self.feedback.click_feedback_likely_item_10_button()
        self.feedback.input_feedback_textbox("good")
        self.feedback.click_feedback_sendfeedback_btn_button()
        self.feedback.verify_feedback_thankyou_title_enabled()

    def test_05_clickusehpaccountinformation(self):
        '''
        TestRail:#C14590870,#C14590890
        Go to Use HP Account Information page and verify screen
        '''
        logging.debug("Go to Use HP Account Information page and verify screen[C14590870]")
        self.tool_bar.click_home_btn()
        self.main_ui.wait_for_find_printer_icon_display()
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_usehpccountinformation_btn()
        self.hp_account_information.wait_for_screen_load()

        logging.debug("Verify strings are translated correctly and matching string table.[C14590890]")
        self.hp_account_information.verify_hpaccountinformation()

        logging.debug("Check and uncheck checkbox befor the 'yes...' and verify options can be check and unchecked")
        time.sleep(1)
        self.hp_account_information.click_hp_account_checkbox()
        time.sleep(2)
        self.hp_account_information.verify_hp_account_checkbox_checked_out()
        logging.debug("click 'HP Privacy Statement' link")
        self.hp_account_information.click_hp_account_hpprivacyStatement_Link()
        time.sleep(10)
        os.system("pkill Safari")

    def test_06_click_checkforupdate(self):
        '''
        TestRail:#14590871
        click on check for updates.. and verify dialog displays
        '''
        logging.debug("click on check for updates.. and verify dialog displays[C14590871]")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_checkforupdates_btn()
        self.checkforupdates_dialog.verify_checkforupdatesdialog()
        self.checkforupdates_dialog.click_ok_btn()

    def test_07_click_hide_hp_smart(self):
        '''
        TestRail:#C14590873
        click Hide HP Smart Verify Gotham app window is minimized
        '''
        logging.debug("click Hide HP Smart Verify Gotham app window is minimized[C14590873]")
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_hidehpsmart_btn()
        self.hp_account_information.verify_gothamappwindow_minimized()

    def test_08_click_hide_others(self):
        '''
        TestRail:#C14590874
        click Hide Others on the menu bar verify HP Smart is still open
        '''
        logging.debug("click Hide Others on the menu bar verify HP Smart is still open[C14590874]")
        time.sleep(3)
        self.menu_bar.click_menubar_hpsmart_icon()
        time.sleep(3)
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_hideothers_btn()
        self.hp_account_information.verify_gothamapp_opened()

    def test_09_click_showall(self):
        '''
        TestRail:#C14590875
        click Show All verify 'Show All'is clickable but'Hide Smart'&'Hide Others' are not clickable
        '''
        logging.debug("click Show All verify 'Show All'is clickable but'Hide Smart'&'Hide Others' are not clickable[C14590875]")
        time.sleep(3)
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.click_menubar_hpsmart_showall_btn()
        time.sleep(3)
        self.menu_bar.click_menubar_hpsmart()
        self.menu_bar.verify_behavior_of_buttons()

    def test_10_click_quit_hp_smart(self):
        '''
        TestRail:#C14590876
        click Quit HP Smart and verify Gotham app is closed
        '''
        logging.debug("click Quit HP Smart and verify Gotham app is closed[C14590876]")
        self.menu_bar.click_menubar_hpsmart_quithpsmart_btn()
