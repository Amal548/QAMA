from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES, TILE_NAMES
from MobileApps.libs.flows.android.smart.smart_tasks import SmartTasks
from MobileApps.libs.flows.android.smart.printers import Printers
from MobileApps.libs.flows.android.smart.file_photos import FilePhotos
from MobileApps.libs.flows.android.google_drive.google_drive import GoogleDrive
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

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.smart_tasks = cls.fc.flow[FLOW_NAMES.SMART_TASKS]
        cls.files_photos = cls.fc.flow[FLOW_NAMES.FILES_PHOTOS]
        cls.online_photos = cls.fc.flow[FLOW_NAMES.ONLINE_PHOTOS]
        cls.scan = cls.fc.flow[FLOW_NAMES.SCAN]
        cls.files = cls.fc.flow[FLOW_NAMES.LOCAL_FILES]
       
        # Clean up Download and Pictures folders before testing
        #cls.fc.clean_up_download_and_pictures_folders()

        # transfer file for testing
        #cls.fc.transfer_test_data_to_device([cls.pdf_fn]) 
        
        #def clean_up_class():
            # Clean up Download and Pictures folders after testing
            #cls.fc.clean_up_download_and_pictures_folders()
            #cls.fc.flow_home_delete_all_smart_tasks(cls.hpid_username, cls.hpid_pwd)
        #request.addfinalizer(clean_up_class)


        # Define variables
        cls.hpid_username = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["username"]
        cls.hpid_pwd = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPID_ACCOUNT))["hpid"]["account_06"]["password"]
        cls.email_address = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.GMAI_ACCOUNT))["email"]["qa.mobiauto"]["username"]
        cls.pkg_name = PACKAGE.SMART.get(cls.driver.session_data["pkg_type"], PACKAGE.SMART["default"])
        cls.pdf_fn = TEST_DATA.ONE_PAGE_PDF
    
    def test_create_smarttask(self):
        self.fc.flow_load_home_screen(username=self.hpid_username, password=self.hpid_pwd)
        #self.driver.swipe()
        time.sleep(5)
    
        #click personalize tile btn on home screen
        #self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        #time.sleep(5)
        
        #click addPrinter + Icon btn
        self.fc.fd[FLOW_NAMES.HOME].select_big_add_icon()
        #select printer use IP address
        self.fc.fd[FLOW_NAMES.PRINTERS].select_printer(self.printer_ip, is_searched=True, keyword=self.printer_ip)
        time.sleep(5)
    
        #import pdb;pdb.set_trace()     
        #self.fc.flow_load_home_screen(username=self.hpid_username, password=self.hpid_pwd)      
        #self.driver.swipe() 
        #self.driver.wdvr.save_screenshot('mycap3.png')
         
        #click personalize tile btn on home screen 
        #self.fc.fd[FLOW_NAMES.HOME].select_personalize_tiles()	
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        #self.driver.swipe()
        #self.driver.wdvr.save_screenshot('mycap4.png')       
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].check_and_enable_tile("Mobile Fax")
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].flow_home_enable_softfax_tile()
        #import pdb;pdb.set_trace()
        #click smart task tile btn on home screen
        self.fc.fd[FLOW_NAMES.HOME].select_tile_by_name("Smart Tasks")
        #self.driver.wdvr.save_screenshot('mycap11.png')
        #####################################################
        #######create smart task                      #######
        #####################################################
        #import pdb;pdb.set_trace()
        #click get started popup window
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_get_started_btn()   
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_learn_more_btn()

        self.driver.wdvr.save_screenshot("mycap12.png")
        #wait for smart task create screen
        ##self.fc.fd[FLOW_NAMES.SMART_TASKS].load_smart_task_create_screen()
        #click and enter the smart task name on combobox 
        ##self.fc.fd[FLOW_NAMES.SMART_TASKS].input_smart_task_name("smartTask3")
        
        self.fc.flow_smart_task_load_smart_task_create_screen("smartTask9")
        #add smart task for saveTo(default option) and enter the acc_name
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].add_smart_task_for_saving("save_to_ggdrive")
        import pdb;pdb.set_trace()
        save_options = {"google_drive": self.smart_tasks.SAVE_TO_GGDRIVE}
        #self.smart_tasks.add_smart_task_for_saving(save_options)
        self.smart_tasks.add_smart_task_for_saving(save_options["google_drive"])
        self.smart_tasks.select_save_btn()
        try:
           self.smart_tasks.dismiss_smart_task_created_popup()
        except TimeoutException:
            self.smart_tasks.select_btn_on_saved_screen(is_checked=True)

        #self.fc.fd[FLOW_NAMES.GOOGLE_DRIVE].select_account("qa.mobiauto@gmail.com")
        self.fc.fd[FLOW_NAMES.ONLINE_DOCS].select_gdrive_gmail_account("qa.mobiauto@gmail.com")

        """        
        file_sources = {
             "from_scanner": self.smart_tasks.FROM_SCANNER,
             "from_facebook": self.smart_tasks.FROM_PHOTOS
        }
        #self.__load_smart_task_source_type_screen("smartTask4", self.smart_tasks.SAVE_TO_GGDRIVE, file_sources[file_source])
        #if file_source == "from_scanner":
           #self.scan.select_scan()
           #self.scan.verify_successful_scan_job()
        #self.__verify_home_screen(smart_task_name)
        
    #def __load_smart_task_source_type_screen(self,smart_task_name, acc_name, source_type):
        #self.fc.flow_home_load_smart_task_screen(self.hpid_username, self.hpid_pwd, create_acc=False, printer_obj=self.p)
        #self.fc.flow_smart_task_load_smart_task_create_screen(smart_task_name)
        #self.smart_tasks.add_smart_task_for_saving(acc_name)
        #self.smart_tasks.select_save_btn()
        #self.smart_tasks.dismiss_smart_task_created_popup()
        #self.smart_tasks.select_smart_task(smart_task_name)

          

       
    #def __verify_home_screen(self, smart_task_name):
      
        #self.smart_tasks.verify_smart_tasks_list_screen(is_empty=False)
        #self.smart_tasks.select_smart_task_from_preview_screen(smart_task_name)
        #self.smart_tasks.dismiss_smart_tasks_complete_popup_screen()
        #if self.home.verify_photomyne_awareness_popup(raise_e=False):
            #self.home.dismiss_photomyne_awareness_popup()
        #self.home.verify_home_nav()      
        """          
        #document handling settings
        #self.fc.transfer_test_data_to_device("pdf")
        #click save btn
        ##self.fc.fd[FLOW_NAMES.SMART_TASKS].select_save_btn()
        #click start smarttask btn on saved on screen
        #self.fc.fd[FLOW_NAMES.SMART_TASKS]..select_btn_on_saved_screen("start_this_smart_task_btn")
        #click ok btn
        ##self.fc.fd[FLOW_NAMES.SMART_TASKS].select_ok_btn()
        #import pdb;pdb.set_trace()
        #select your created smart task 
        ##self.fc.fd[FLOW_NAMES.SMART_TASKS].select_smart_task("smartTask7")
        #select source Type("smart_task_scanner", "smart_task_files", "smart_task_photos", "smart_task_camera")
        #self.fc.fd[FLOW_NAMES.SMART_TASKS].select_smart_task_source_type("smart_task_scanner")

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
        self.fc.fd[FLOW_NAMES.SMART_TASKS].delete_single_smart_task("smartTask3")
        #delete all created smart task
        #self.fc.fd[FLOW_NAMES.PERSONALIZE].get_enabled_tiles_list()
        self.fc.fd[FLOW_NAMES.PERSONALIZE].select_back()
        #self.driver.swipe()
