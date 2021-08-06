'''
Created on June 17, 2019
@author: sophia
'''
import pytest
import logging
import os, shutil
from time import sleep

import MobileApps.resources.const.mac.const as m_const
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.system.flows.flows_system import FlowsSystem
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.common.print_anywhere_flyer import PrintAnywhereFlyer

from selenium.common.exceptions import NoSuchElementException

pytest.app_info = "DESKTOP"

class Test_Suite_03_Install_Printer_To_Print(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, mac_smart_setup):
        self = self.__class__
       
        # Defines driver and flows
        self.driver, self.common_flows = mac_smart_setup
        self.system_flows = FlowsSystem(self.driver)
        self.main_screen=MainUI(self.driver)
        self.print_anywhere_screen=PrintAnywhereFlyer(self.driver)

        # Define variables
        self.appname=m_const.APP_NAME.SMART
        self.printerBonjourName="HP ENVY Photo 7800 series [BADBAD]" 
        self.run_times=50
        self.path=os.path.expanduser('~/Library/Application Support/HP Smart')
        
    
    def test_01_navigate_to_main_ui(self):
        
        #check welcome workflow
        logging.debug("Start to check welcome workflow... ")
        self.common_flows.launch_HPSmart_app(self.appname)
        
        self.common_flows.navigate_to_agreements_screen() 
        
        #check OWS screen (post OOBE workflow)
        logging.debug("Start to check post OOBE workflow... ")
        self.common_flows.go_to_main_ui_after_post_oobe(self.printerType)
        
    def test_02_check_install_printer_dialog(self):
        logging.debug("Print document and cancel job... ")
        
        #check print dialog
        
        #cancel job
        self.common_flows.print_file_using_default_settings(self.docName, "Document")
        
    def test_03_install_printer(self):
        #install a printer
        logging.debug("Start to installed a printer... ")
        self.system_flows.install_printer_using_printer_name(self.printerBonjourName)
    
    def test_04_print_after_printer_newly_installed(self):
        logging.debug("Print with default settings... ")
        
        self.common_flows.print_file_using_default_settings(self.docName, "Document")
        
    
   
    def delete_files(self,path):   
        try:
            if os.path.isdir(path): 
                shutil.rmtree(path)
        except OSError as e: 
            print ("Error: %s - %s." % (e.filename, e.strerror)) 
            