from MobileApps.libs.flows.web.hp_connect.hp_connect_flow import HPConnectFlow
from SAF.decorator.saf_decorator import screenshot_capture
class HelpCenter(HPConnectFlow):

    flow_name="help_center"

    ABOUT_HP_SMART = "about_hp_smart_link"
    HP_PLUS = "hp_plus_link"
    PRINTER_AND_CONNECTION = "printer_connection_information_link"
    PRINT_SCAN_AND_SHARE = "print_scan_share_link"
    ADDITIONAL_HELP_AND_SUPPORT = "additional_help_and_support_link"
    GETTING_TO_KNOW_HP_SMART = "getting_to_know_hp_smart_link"
    STARTING_OFF = "starting_off_link"
    SHARING_FILES = "sharing_files_link"
    SHORTCUTS = "shortcuts_link"
    WHAT_IS_HP_PLUS = "what_is_hp_plus_link"
    HP_INSTANT_INK = "hp_instant_ink_link"
    HP_SMART_SECURITY = "hp_smart_security_link"
    PRINT_ANYWHERE = "print_anywhere_link"
    PRINTING = "printing_link"
    SCANNING = "scanning_link"
    FAX = "fax_link"
    VIEW_PRINT = "view_print_link"
    PRINT_ANYWHERE_ONLINE_SUPPORT = "print_anywhere_online_support_link"
    SHORTCUTS_SUPPORT = "shortcuts_online_support_link"
    HP_MOBILE_PRINTING = "hp_mobile_printing_link"
    GO_TO_HP_SUPPORT = "go_to_hp_support_link"
    PRINTER_SUPPORT = "printer_support_link"
    FINDING_YOUR_PRINTER = "finding_your_printer_link"
    CONNECTING_TO_YOUR_PRINTER = "connecting_to_your_printer_link"
    VIEWING_PRINTER_INFORMATION = "viewing_printer_information_link"
    PRINT_SERVICE_PLUGIN = "print_service_plugin_link"

    def __init__(self,driver, context=None):
        super(HelpCenter, self).__init__(driver, context=context)


    ###############################################################################
    #                             Action flows
    ###############################################################################
    
    def click_link_on_help_center_screen(self, link_name):
        """
        Click on a link on or under Help Center screen
        :param link_name: use class constants:
                ABOUT_HP_SMART
                HP_PLUS
                PRINTER_AND_CONNECTION
                PRINT_SCAN_AND_SHARE
                ADDITIONAL_HELP_AND_SUPPORT
                GETTING_TO_KNOW_HP_SMART
                STARTING_OFF
                SHARING_FILES
                SMART_TASKS
                WHAT_IS_HP_PLUS
                HP_PLUS_PRINT_PLANS
                HP_SMART_SECURITY
                PRINT_ANYWHERE
                PRINTING
                SCANNING
                FAX_LINK
                VIEW_PRINT
                PRINT_ANYWHERE_ONLINE_SUPPORT
                SMART_TASKS_ONLINE_SUPPORT
                HP_MOBILE_PRINTING
                GO_TO_HP_SUPPORT
                PRINTER_SUPPORT
                FINDING_YOUR_PRINTER
                CONNECTING_TO_YOUR_PRINTER
                VIEWING_PRINTER_INFORMATION
                PRINT_SERVICE_PLUGIN
        """
        self.driver.click(link_name)

    ###############################################################################
    #                            Verification flows
    ###############################################################################

    def verify_help_center_menu(self, timeout=20, invisible=False):
        """"
        Verify Help Center menu screen via:
         - ABOUT_HP_SMART
         - HP_PLUS (UCDE account won't have this item)
         - PRINTER_AND_CONNECTION
         - PRINT_SCAN_AND_SHARE
         - ADDITIONAL_HELP_AND_SUPPORT
        """
        self.driver.wait_for_object("about_hp_smart_link", timeout=timeout)
        self.driver.wait_for_object("hp_plus_link", invisible=invisible)
        self.driver.wait_for_object("printer_connection_information_link")
        self.driver.wait_for_object("print_scan_share_link")
        self.driver.wait_for_object("additional_help_and_support_link")

    def verify_about_hp_smart(self):
        """"
        Verify About HP Smart screen via:
         - Getting to Know HP Smart item
         - Starting off item
         - Sharing files item
        """
        self.driver.wait_for_object("getting_to_know_hp_smart_link")
        self.driver.wait_for_object("starting_off_link")
        self.driver.wait_for_object("sharing_files_link")

    def verify_getting_to_know_hp_smart(self):
        """"
        Verify Getting to Know HP Smart screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("getting_to_know_hp_smart_title")
        self.driver.wait_for_object("help_center_container")

    def verify_starting_off(self):
        """"
        Verify Starting Off screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("starting_off_title")
        self.driver.wait_for_object("help_center_container")

    def verify_sharing_file(self):
        """"
        Verify Sharing Files screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("sharing_files_title")
        self.driver.wait_for_object("help_center_container")

    @screenshot_capture(file_name="shortcuts_screen.png")
    def verify_shortcuts(self):
        """"
        Verify Shortcuts screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("shortcuts_title")
        self.driver.wait_for_object("help_center_container")

    def verify_hp_plus(self):
        """"
        Verify HP Plus screen via:
         - What is HP+? item
         - HP Smart security item
         - Print Anywhere item
        """
        self.driver.wait_for_object("what_is_hp_plus_link")
        self.driver.wait_for_object("hp_smart_security_link")
        self.driver.wait_for_object("print_anywhere_link")

    def verify_what_is_hp_plus(self):
        """"
        Verify What is HP+?screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("what_is_hp_plus_title")
        self.driver.wait_for_object("help_center_container")

    def verify_hp_instant_ink(self):
        """"
        Verify HP Instant Ink screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("hp_instant_ink_title")
        self.driver.wait_for_object("help_center_container")

    def verify_hp_smart_security(self):
        """"
        Verify HP Smart Security screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("hp_smart_security_title")
        self.driver.wait_for_object("help_center_container")

    def verify_print_anywhere(self):
        """"
        Verify Print Anywhere screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("print_anywhere_title")
        self.driver.wait_for_object("help_center_container")

    def verify_print_scan_and_share(self):
        """"
        Verify Print, Scan and Share screen via:
         - Printing link
         - Scanning link
         - Fax link
         - View & Print link
        """
        self.driver.wait_for_object("printing_link")
        self.driver.wait_for_object("scanning_link")
        self.driver.wait_for_object("fax_link")
        self.driver.wait_for_object("view_print_link")

    def verify_printing(self):
        """"
        Verify Printing screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("printing_title")
        self.driver.wait_for_object("help_center_container")

    def verify_scanning(self):
        """"
        Verify Scanning screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("scanning_title")
        self.driver.wait_for_object("help_center_container")

    def verify_fax(self):
        """"
        Verify Fax screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("fax_title")
        self.driver.wait_for_object("help_center_container")

    def verify_view_print(self):
        """"
        Verify View & Print screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("view_print_title")
        self.driver.wait_for_object("help_center_container")

    def verify_additional_help_and_support(self):
        """"
        Verify Additional Help and Support screen via:
         - Print Anywhere Online support link
         - Shortcuts Online Support link
         - HP Mobile Printing link
        """
        self.driver.wait_for_object("print_anywhere_online_support_link")
        self.driver.wait_for_object("shortcuts_online_support_link")
        self.driver.wait_for_object("hp_mobile_printing_link")

    def verify_printer_and_connection_information(self):
        """"
        Verify Printer And Connection Information screen via:
         -Printer Support item
         - Finding Your Printer item
         - Connecting to Your Printer item
         - Viewing Printer Information item
         - Print Service Plugin item
        """
        self.driver.wait_for_object("printer_support_link")
        self.driver.wait_for_object("finding_your_printer_link")
        self.driver.wait_for_object("connecting_to_your_printer_link")
        self.driver.wait_for_object("viewing_printer_information_link")
        self.driver.wait_for_object("print_service_plugin_link")

    def verify_finding_your_printer(self):
        """"
        Verify Finding Your Printer screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("finding_your_printer_title")
        self.driver.wait_for_object("help_center_container")

    def verify_connecting_to_your_printer(self):
        """"
        Verify Connecting To Your Printer screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("connecting_to_your_printer_title")
        self.driver.wait_for_object("help_center_container")

    def verify_viewing_printer_information(self):
        """"
        Verify Viewing Printer Information screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("viewing_printer_information_title")
        self.driver.wait_for_object("help_center_container")

    def verify_print_service_plugin(self):
        """"
        Verify Print Service Plugin screen via:
         - Title
         - Message
        """
        self.driver.wait_for_object("print_service_plugin_title")
        self.driver.wait_for_object("help_center_container")