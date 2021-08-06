from MobileApps.libs.flows.android.hpbridge.flows.wechat import WeChat
from MobileApps.libs.flows.android.hpbridge.flows.bind_printer import BindPrinter
from MobileApps.libs.flows.android.hpbridge.flows.mp_home import MPHome
from MobileApps.libs.flows.android.hpbridge.flows.url_print import URLPrint
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.flows.print_setting import PrintSetting
from MobileApps.libs.flows.android.hpbridge.flows.print_flow import PrintFlow
from MobileApps.libs.flows.android.hpbridge.flows.pa_home import PAHome
from MobileApps.libs.flows.android.hpbridge.flows.pa_my_printer import PAMyPrinter
from MobileApps.libs.flows.android.hpbridge.flows.pa_print_history import PAPrintHistory
from MobileApps.libs.flows.android.hpbridge.flows.pa_hp_supply import PAHPSupply
from MobileApps.libs.flows.android.hpbridge.flows.invoice_print import InvoicePrint
from MobileApps.libs.flows.android.hpbridge.flows.baidu_print import BaiduPrint
from MobileApps.libs.flows.android.hpbridge.flows.pa_search_help import PASearchHelp
from MobileApps.libs.flows.android.hpbridge.flows.mp_faq import MPFAQ
from MobileApps.libs.flows.android.hpbridge.flows.mp_message_center import MPMessageCenter
from MobileApps.libs.flows.android.hpbridge.flows.print_notice import PrintNotice


class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {
            "wechat": WeChat(self.driver),
            "bind_printer": BindPrinter(self.driver),
            "mp_home": MPHome(self.driver),
            "url_print": URLPrint(self.driver),
            "print_setting": PrintSetting(self.driver),
            "print_flow": PrintFlow(self.driver),
            "pa_home": PAHome(self.driver),
            "pa_my_printer": PAMyPrinter(self.driver),
            "pa_print_history": PAPrintHistory(self.driver),
            "pa_hp_supply": PAHPSupply(self.driver),
            "invoice_print": InvoicePrint(self.driver),
            "baidu_print": BaiduPrint(self.driver),
            "pa_search_help": PASearchHelp(self.driver),
            "mp_faq": MPFAQ(self.driver),
            "mp_message_center":MPMessageCenter(self.driver),
            "print_notice":PrintNotice(self.driver)

        }

    @property
    def flow(self):
        return self.fd


    # *********************************************************************************
    # ACTION FLOWS                                     *
    # *********************************************************************************
    #   -----------------------         FROM HOME       -----------------------------

    def remove_all_bound_printers(self):
        """
        remove all bound printer under the user account for case clean up
        :return:
        """
        apiutility = APIUtility()
        apiutility.unbind_all_printers()

    # def flow_home_delete_all_files_device_storage(self):
    #     """
    #         - At Home screen, click on Files icon on bottom navigation bar
    #         - Click on Scanned Files
    #         - Delete all files
    #     """
    #     self.flow_load_home_screen()
    #     self.fd[FLOW_NAMES.HOME].select_nav_file()
    #     self.fd[FLOW_NAMES.FILES_PHOTOS].select_local_item(self.fd[FLOW_NAMES.FILES_PHOTOS].SCANNED_FILES_TXT)
    #     timeout = time.time() + 60
    #     while time.time() < timeout:
    #         try:
    #             self.fd[FLOW_NAMES.LOCAL_FILES].select_all_displayed_files()
    #         except NoSuchElementException:
    #             break
    #         self.fd[FLOW_NAMES.LOCAL_FILES].device_file_delete_selected_files()
    #
    #
    # #   -----------------------         FROM Printer       -----------------------------
    # def is_printer_ready(self, printer_obj):
    #     """
    #     Verify printer is ready for making any job:
    #         - Check printer assert -> reset printer
    #         - Check printer ready
    #     :param printer_obj: printer object (SPL)
    #     :return: True -> ready. False -> not ready
    #      """
    #     printer_obj.check_init_coredump()
    #     return printer_obj.is_printer_status_ready()
