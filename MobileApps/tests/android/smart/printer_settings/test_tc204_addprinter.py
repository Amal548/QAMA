from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.libs.flows.android.smart.smart_tasks import SmartTasks
from MobileApps.libs.flows.android.smart.file_photos import FilePhotos
from MobileApps.libs.flows.android.smart.printers import Printers
from MobileApps.resources.const.android.const import TEST_DATA, PACKAGE
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import pytest
import os
import base64
import time

pytest.app_info = "SMART"

class Test_Suite_01_Android_Welcome(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session
        cls.printer_ip = cls.p.p_obj.ipAddress
        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["password"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        
    def test_hpsmart_homepage(self):
        #import pdb;pdb.set_trace()     
        self.fc.flow_load_home_screen(username=self.hpid_username, password=self.hpid_pwd)      
        #self.driver.swipe() 
    def test_hpsmart_addprinter(self):
        #import pdb;pdb.set_trace()
        #click addPrinter + Icon btn
        self.fc.fd[FLOW_NAMES.HOME].select_big_add_icon()
        #select printer use IP address
        self.fc.fd[FLOW_NAMES.PRINTERS].select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        #self.fc.fd[FLOW_NAMES.PRINTERS].select_add()
        #click select looking wifi direct printer
        #self.fc.fd[FLOW_NAMES.PRINTERS].select_looking_for_wifi_direct_printers()
        #click search btn for printer
        #self.fc.fd[FLOW_NAMES.PRINTERS].select_search_icon()
        #Enter the printer name or IP address
        #self.fc.fd[FLOW_NAMES.PRINTERS].search_printer()
        
        #load printer
        #self.fc.fd[FLOW_NAMES.HOME].load_printer_selection()
        #load printer info
        #self.fc.fd[FLOW_NAMES.HOME].load_printer_info()
        #select setup printer btn
        #self.fc.fd[FLOW_NAMES.HOME].select_set_up()
        """
        #self.driver.wdvr.save_screenshot('mycap3.png')       
        #click personalize tile btn on home screen 
        self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()	
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        self.driver.swipe()
        #self.driver.wdvr.save_screenshot('mycap4.png')       
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].check_and_enable_tile("Mobile Fax")
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].flow_home_enable_softfax_tile()
        #import pdb;pdb.set_trace()
        #click smart task tile btn on home screen
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Smart Tasks")
        self.driver.wdvr.save_screenshot('mycap11.png')
        #####################################################
        #######create smart task                      #######
        #####################################################
        #import pdb;pdb.set_trace()
        #click get started popup window
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_get_started_btn()
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_learn_more_btn()

        self.driver.wdvr.save_screenshot("mycap12.png")
        #wait for smart task create screen
        self.fc.fd[FLOW_NAMES.SMART_TASKS].load_smart_task_create_screen()
        #click and enter the smart task name on combobox 
        self.fc.fd[FLOW_NAMES.SMART_TASKS].input_smart_task_name("smartTask1")
        
        #add smart task for print(default option)
        self.fc.fd[FLOW_NAMES.SMART_TASKS].add_smart_task_for_print()
        #add smart task for print with param(copies_num=2, color_type=COLOR_BTN or GRAYSCALE_BTN, two_sided_option=TWO_SIDE_OFF or SHORT_EDGE or LONG_EDGE)
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].add_smart_task_for_print(2, "GRAYSCALE_BTN", "SHORT_EDGE")
         
        #click save btn
        self.fc.fd[FLOW_NAMES.SMART_TASKS].select_save_btn()
        #click ok btn
        self.fc.fd[FLOW_NAMES.SMART_TASKS].select_ok_btn()
        import pdb;pdb.set_trace()
        #select your created smart task 
        self.fc.fd[FLOW_NAMES.SMART_TASKS].select_smart_task("smartTask1")
        #select source Type("smart_task_scanner", "smart_task_files", "smart_task_photos", "smart_task_camera")
        self.fc.fd[FLOW_NAMES.SMART_TASKS].select_smart_task_source_type("smart_task_scanner")

        #verify local_file_photos_btn
        #self.fc.fd[FLOW_NAMES.FILES_PHOTOS].verify_local_files_photos_btns()
        #select the photos or files from file_photos ("pdfs_txt", "my_photos_txt","google_drive_txt", "google_photos_txt")
        #self.fc.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item("my_photos_txt")

       
        #select the start this smart task btn(btn_name: START_THIS_SMART_TASK_BTN, BACK_TO_SMART_TASKS_BTN, HOME_BTN)
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_btn_on_saved_screen("START_THIS_SMART_TASK_BTN") 
        #select the your created smart task
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_smart_task()
        
        #######################################################
        ########delete smart task                ##############
        ####################################################### 
        #delete single smart task
        self.fc.fd[FLOW_NAMES.SMART_TASKS].delete_single_smart_task("smartTask1")
        #delete all created smart task
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].get_enabled_tiles_list()
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        self.driver.swipe()
        """
