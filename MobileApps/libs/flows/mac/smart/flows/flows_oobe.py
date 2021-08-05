# encoding: utf-8
'''
Description: It defines common flows in the OOBE section.

@author: Sophia
@create_date: May 6, 2019
'''

import logging
from time import sleep

import MobileApps.resources.const.mac.const as smart_const
import MobileApps.libs.flows.mac.smart.utility.smart_utilities as smart_utility
from MobileApps.libs.flows.mac.system.screens.system_preferences import SystemPreferences
from MobileApps.libs.flows.mac.smart.screens.oobe.ows import OWS
from MobileApps.libs.flows.mac.smart.screens.common.main_ui import MainUI
from MobileApps.libs.flows.mac.smart.screens.hpid.sign_up_dialog import SignUpDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.let_find_your_printer import FindYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.we_found_your_printer import WeFoundYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected_to_wifi import PrinterConnectedtoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.print_from_other_devices import PrintFromOtherDevices
from MobileApps.libs.flows.mac.smart.screens.oobe.send_another_link_dialog import SendAnotherLinkDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_to_wifi import ConnectPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.select_a_printer import SelectAPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi import ConnectingPrintertoWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.install_driver_to_print import InstallDriverToPrint
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_setup_lets_print import PrinterSetupLetsPrint
from MobileApps.libs.flows.mac.smart.screens.oobe.we_can_help_connect_your_printer import WeCanHelpConnectYourPrinter
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_using_usb import ConnectUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.choose_a_connection_method_dialog import ChooseCnnectionMethodDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.switch_to_using_wifi import SwitchToUsingWiFi
from MobileApps.libs.flows.mac.smart.screens.oobe.switch_to_using_wifi_2 import SwitchToUsingWiFi2
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_printer_with_ethernet import ConnectPrinterWithEthernet
from MobileApps.libs.flows.mac.smart.screens.oobe.we_could_not_find_your_printer_dialog import WeCouldNotFindYourPrinterDialog
from MobileApps.libs.flows.mac.smart.screens.oobe.printer_connected import PrinterConnected
from MobileApps.libs.flows.mac.smart.screens.oobe.connecting_printer_to_wifi_wireless_setup import ConnectingPrintertoWiFiSetup
from MobileApps.libs.flows.mac.smart.screens.oobe.wireless_setup_using_usb import WirelessSetupUsingUSB
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_computer_to_the_wifi_network import ConnectYourComputerToTheWiFiNetwork
from MobileApps.libs.flows.mac.smart.screens.oobe.connect_your_computer_to_the_network import ConnectYourComputerToTheNetwork


class OOBEFlows(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver

    def __designjet_flow(self, ows_screen):
        # TODO: need manual test cases
        '''
        This is a flow for DesignJet in OWS.
        :parameter:
        :return:
        '''
        pass

    def __laserjet_flow(self, ows_screen):
        '''
        This is a flow for LaserJet in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for LaserJet printer... ")

        smart_utility.kill_browser(smart_const.BROWSER_NAME.SAFARI)

    def __ciss_inkjet_flow(self, ows_screen):
        '''
        This is a flow for CISS printer in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for CISS printer or Non-II printer... ")

        self.__go_through_enjoy_hp_acct(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __taiji_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for TaiJi in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for TaiJi printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __lhasaboom_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Lhasa Boom in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Lhasa Boom printer... ")

        ows_screen.wait_for_cartridges_install_load(60)
        ows_screen.wait_for_skip_btn_shows(120)
        ows_screen.click_skip_btn_cartridges_install()

        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __others_gen1_inkjet_flow(self, ows_screen):
        '''
        This is a flow for other Gen 1 InkJet printers in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Gen 1 printer... ")

        self.__instant_ink_flow(ows_screen)
        self.__go_through_register_printer(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __verona_gen2_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Verona in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Verona family printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_enjoy_hp_acct(ows_screen)
        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __palermo_gen2_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Palermo in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for Palermo family printer... ")

        # TODO: OWS need fully reset OOBE printer to finish
        self.__go_through_enjoy_hp_acct(ows_screen)
        self.__go_through_hardware_setup(ows_screen)
        self.__instant_ink_flow(ows_screen)

        if ows_screen.wait_for_help_hp_make_better_load(raise_e=False):
            self.__help_make_better_product_flow(ows_screen)
        else:
            ows_screen.wait_for_almost_ready_load()
            ows_screen.click_continue_btn_almost_ready()

    def __tango_gen2_inkjet_flow(self, ows_screen):
        '''
        This is a flow for Tango in OWS.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow for HP Tango printer... ")

        self.__go_through_enjoy_hp_acct(ows_screen)
        # TODO: OWS need fully reset OOBE printer to finish
        self.__instant_ink_flow(ows_screen)
        self.__help_make_better_product_flow(ows_screen)

    def __go_through_enjoy_hp_acct(self, ows_screen):
        '''
        This is a flow from enjoy hp account then to hp id sign in dialog.
        :parameter:
        :return:
        '''
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_continue_btn_enjoy_hp_account()

        sign_up_dialog = SignUpDialog(self.driver)
        if sign_up_dialog.wait_for_screen_load(raise_e=False):
            sign_up_dialog.click_close_btn()

    def __go_through_hardware_setup(self, ows_screen):
        '''
        This is a flow from hardware setup finish/alignment finish/cartridges installed or
        paper loaded, then to instant ink screen.
        :parameter:
        :return:
        '''
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

    def __go_through_register_printer(self, ows_screen):
        '''
        This is a flow from register your printer with HP to next screen.
        :parameter:
        :return:
        '''
        ows_screen.wait_for_register_printer_load(60)
        ows_screen.click_skip_btn_register_printer()

    def __instant_ink_flow(self, ows_screen):
        '''
        This is a flow from instant ink advertisement screen to reminder screen.
        :parameter:
        :return:
        '''
        sleep(15)
        ows_screen.wait_for_hp_instant_ink_advertisement_load(timeout=120)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()

        sleep(15)
        ows_screen.wait_for_hp_instant_ink_plan_load()
        ows_screen.choose_no_instank_ink_radio_btn()
        ows_screen.click_continue_btn_hp_instant_ink_plan()

        ows_screen.wait_for_reminder_load(60)
        ows_screen.click_skip_btn_reminder()

    def __help_make_better_product_flow(self, ows_screen):
        '''
        This is a method to set up information on the help HP make better product screen
        :parameter:
        :return:
        '''
        ows_screen.wait_for_help_hp_make_better_load(60)
        if ows_screen.wait_for_radio_btn_shows(raise_e=False):
            ows_screen.choose_in_home_radio_btn()
            ows_screen.click_in_home_drop_down_list()
            ows_screen.choose_in_home_drop_down_list_item()
        ows_screen.set_postal_code(smart_const.PRINTER_INFO.POSTAL_CODE)
        ows_screen.click_continue_btn_help_better()

    __ows_switcher = {
        0: __designjet_flow,
        1: __laserjet_flow,
        2: __ciss_inkjet_flow,
        3: __taiji_gen1_inkjet_flow,
        4: __lhasaboom_gen1_inkjet_flow,
        5: __others_gen1_inkjet_flow,
        6: __verona_gen2_inkjet_flow,
        7: __palermo_gen2_inkjet_flow,
        8: __tango_gen2_inkjet_flow
    }

    def go_through_ows_flow(self, printer_ows_type):
        '''
        This is a method to go through OWS flow during the OOBE setup.
        :parameter:
        :return:
        '''
        logging.debug("Go through OWS workflow... ")

        ows_screen = OWS(self.driver)
        return self.__ows_switcher.get(printer_ows_type, lambda: 'Invalid printer OWS type...')(self, ows_screen)

    def go_through_to_instant_ink_flow(self):
        '''
        This is a method to go through OOBE flow to Instant Ink plan screen from Enjoy Your printer screen with Palermo GEN2 printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through Enjoy HP Account Screen")
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_continue_btn_enjoy_hp_account()
        sign_up_dialog = SignUpDialog(self.driver)
        if sign_up_dialog.wait_for_screen_load(raise_e=False):
            sign_up_dialog.click_close_btn()

        logging.debug("Go through Hardware Setup screen")
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

        logging.debug("Go through Instant Ink Plan page")
        ows_screen.wait_for_hp_instant_ink_advertisement_load(120)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()
        ows_screen.wait_for_hp_instant_ink_plan_load(60)
        ows_screen.choose_first_instank_ink_plan_radio_btn()
        ows_screen.click_continue_btn_hp_instant_ink_plan()

    def go_through_to_reminder_me_flow(self):
        '''
        This is a method to go through OOBE flow to Reminder me screen from Enjoy Your printer screen with Palermo GEN2 printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through Enjoy HP Account Screen")
        ows_screen = OWS(self.driver)
        ows_screen.wait_for_enjoy_hp_account_load(360)
        sleep(2)
        ows_screen.click_skip_btn_enjoy_hp_account()
        ows_screen.wait_for_dont_miss_out_on_your_automatic_printer_warranty_load()
        ows_screen.click_skip_btn_dont_miss_out()

        logging.debug("Go through Hardware Setup screen")
        if ows_screen.wait_for_cartridges_install_load(60, raise_e=False):
            ows_screen.click_continue_btn_cartridges_install()

        logging.debug("Go through to Reminder me screen")
        ows_screen.wait_for_hp_instant_ink_advertisement_load(120)
        ows_screen.click_continue_btn_hp_instant_ink_advertisement()
        ows_screen.wait_for_hp_instant_ink_plan_load(60)
        ows_screen.choose_no_instank_ink_radio_btn()
        ows_screen.click_continue_btn_hp_instant_ink_plan()
        ows_screen.wait_for_reminder_load(60)
        ows_screen.click_reminder_me_btn_reminder()

    def go_through_to_select_a_printer_screen(self):
        '''
        This is a setup printer flow with no beaconing printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through OOBE flow to Select a printer screen from Let's find your printer screen for without beaconing printer")
        let_find_your_printer = FindYourPrinter(self.driver)
        let_find_your_printer.verify_lets_find_your_printer_screen()
        let_find_your_printer.click_continue_btn()

        select_a_printer = SelectAPrinter(self.driver)
        select_a_printer.verify_select_a_printer_screen()

    def no_beaconing_printer_setup_flow(self, printer_name):
        '''
        This is a setup printer flow with no beaconing printer.
        :parameter:
        :return:
        '''
        logging.debug("Go through OOBE flow to Printer connected screen from Let's find your printer screen for without beaconing printer")
        self.go_through_to_select_a_printer_screen()

        select_a_printer = SelectAPrinter(self.driver)
        select_a_printer.click_to_selected_printer(printer_name)

        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.verify_we_found_your_printer_without_title_screen()
        we_found_your_printer.click_continue_btn()

        printer_connected = PrinterConnected(self.driver)
        printer_connected.verify_printer_connected_screen()
        printer_connected.click_continue_btn()

    def navigate_to_connect_printer_to_wifi_screen(self, printer_name):
        '''
        This is a flow for navigate to Connect Printer to WiFi screen from click Yes button on Agreement screen.
        :parameter:
        :return:
        '''
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        if we_found_your_printer.wait_for_screen_load(raise_e=False):
            we_found_your_printer.verify_we_found_your_printer_screen()
            we_found_your_printer.click_continue_btn()
        elif select_a_printer.wait_for_screen_load(raise_e=False):
            select_a_printer.click_to_selected_printer(printer_name)

    def navigate_to_connecting_printer_to_wifi(self, printer_name, wifi_name, wifi_password):
        '''
        This is a flow for navigate to Connecting Printer to WiFi screen with correct password input from Connect Printer to WiFi screen.
        :parameter: wifi_password - the required WIFI password on connect printer to WIFI screen.
        :return:
        '''
        connect_printer_to_wifi = ConnectPrintertoWiFi(self.driver)
        connect_printer_to_wifi.verify_connect_printer_to_wifi_screen(printer_name, wifi_name)
        connect_printer_to_wifi.input_enter_wifi_password_box(wifi_password)
        connect_printer_to_wifi.click_connect_btn()

    def go_through_connected_to_wifi_flow(self, printer_name, wifi_name, wifi_password):
        '''
        This is a flow from "connect printer to WIFI" screen to "printer connected to WIFI" screen.
        :parameter: wifi_password - the required WIFI password on connect printer to WIFI screen.
        :return:
        '''
        logging.debug("Go through printer connected to WIFI flow... ")

        self.navigate_to_connecting_printer_to_wifi(printer_name, wifi_name, wifi_password)

        connecting_printer_to_wifi = ConnectingPrintertoWiFi(self.driver)
        connecting_printer_to_wifi.verify_connecting_printer_to_wifi_screen()

        printer_connected_to_wifi = PrinterConnectedtoWiFi(self.driver)
        printer_connected_to_wifi.verify_printer_connected_to_wifi_screen()
        printer_connected_to_wifi.click_continue_btn()

    def go_to_we_can_help_connect_your_printer_screen(self):
        '''
        This is method to go to We can help connect your printer screen from select "No, Continue with Ethernet" opt on Switch to Using WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to We can help connect your printer screen")
        switch_to_using_wifi = SwitchToUsingWiFi(self.driver)
        switch_to_using_wifi.verify_switch_to_using_wifi_screen()
        switch_to_using_wifi.click_no_continue_with_ethernet_opt()
        switch_to_using_wifi.verify_continue_btn_is_enabled()
        switch_to_using_wifi.click_continue_btn()

        we_can_help_connect_your_printer = WeCanHelpConnectYourPrinter(self.driver)
        we_can_help_connect_your_printer.verify_we_can_help_connect_your_printer_screen()

    def go_to_switch_to_using_wifi_2_screen(self):
        '''
        This is method to go to Switch to Using WiFi - 2 screen from select "Yes, Switch to WiFi" opt on Switch to Using WiFi screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to We can help connect your printer screen")
        switch_to_using_wifi = SwitchToUsingWiFi(self.driver)
        switch_to_using_wifi.verify_switch_to_using_wifi_screen()
        switch_to_using_wifi.click_yes_switch_to_wifi_opt()
        switch_to_using_wifi.verify_continue_btn_is_enabled()
        switch_to_using_wifi.click_continue_btn()

        switch_to_using_wifi_2 = SwitchToUsingWiFi2(self.driver)
        switch_to_using_wifi_2.verify_switch_to_using_wifi_2_screen()
        switch_to_using_wifi_2.click_open_network_settings_button()

        network_page = SystemPreferences(self.driver)
        network_page.click_close_network_page_btn()
        switch_to_using_wifi_2.wait_for_screen_load()
        switch_to_using_wifi_2.verify_continue_btn_is_enabled()

    def go_to_check_choose_a_connection_method_dialog(self):
        '''
        This is a method to check clicking info button on We can help connect your printer screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to check choose a connection method dialog")
        we_can_help_connect_your_printer = WeCanHelpConnectYourPrinter(self.driver)
        we_can_help_connect_your_printer.click_info_btn()
        choose_a_connection_method_dialog = ChooseCnnectionMethodDialog(self.driver)
        choose_a_connection_method_dialog.verify_choose_a_connection_method_dialog()
        choose_a_connection_method_dialog.click_done_btn()
        we_can_help_connect_your_printer.wait_for_screen_load()

    def go_to_connect_your_computer_to_the_wifi_network_screen(self):
        '''
        This is method to go to Connect your printer to your WiFi network screen from select "Yes, connect to network" opt on Connect your printer to your network screen during OOBE USB flow
        :parameter:
        :return:
        '''
        connect_your_computer_to_the_network = ConnectYourComputerToTheNetwork(self.driver)
        connect_your_computer_to_the_network.verify_connect_your_computer_to_the_network_screen()
        connect_your_computer_to_the_network.select_yes_connect_to_network_opt()
        connect_your_computer_to_the_network.click_continue_btn()

        connect_your_computer_to_the_wifi_network = ConnectYourComputerToTheWiFiNetwork(self.driver)
        connect_your_computer_to_the_wifi_network.verify_connect_your_computer_to_the_wifi_network_screen()
        connect_your_computer_to_the_wifi_network.click_open_network_settings_btn()

        network_page = SystemPreferences(self.driver)
        network_page.click_close_network_page_btn()
        connect_your_computer_to_the_wifi_network.wait_for_screen_load()

    def go_to_connect_printer_with_ethernet_screen(self):
        '''
        This is method to go to Connect printer with Ethernet screen from select Ethernet opt on We can help connect your printer screen during OOBE Ethernet flow
        :parameter:
        :return:
        '''
        logging.debug("Go to Connect printer with Ethernet screen... ")
        we_can_help_connect_your_printer = WeCanHelpConnectYourPrinter(self.driver)
        we_can_help_connect_your_printer.verify_we_can_help_connect_your_printer_screen()
        we_can_help_connect_your_printer.select_ethernet_radio()
        we_can_help_connect_your_printer.click_continue_btn()

        connect_printer_with_ethernet = ConnectPrinterWithEthernet(self.driver)
        connect_printer_with_ethernet.verify_connect_printer_with_ethernet_screen()

    def go_to_connect_using_usb_screen(self):
        '''
        This is method to go to Connect Using USB screen from select USB opt on We can help connect your printer screen during OOBE Ethernet flow
        :parameter:
        :return:
        '''
        logging.debug("Go to Connect your printer to your network screen... ")
        we_can_help_connect_your_printer = WeCanHelpConnectYourPrinter(self.driver)
        we_can_help_connect_your_printer.verify_we_can_help_connect_your_printer_screen()
        we_can_help_connect_your_printer.select_usb_radio()
        we_can_help_connect_your_printer.click_continue_btn()

        connect_using_usb = ConnectUsingUSB(self.driver)
        connect_using_usb.verify_connect_using_usb_screen()

    def go_to_connecting_printer_to_wifi_wireless_setup(self):
        '''
        This is method to go to Connecting printer to WiFi... screen from select WiFi opt on We can help connect your printer screen
        :parameter:
        :return:
        '''
        logging.debug("Go to connecting printer to wifi..  screen... ")
        we_can_help_connect_your_printer = WeCanHelpConnectYourPrinter(self.driver)
        we_can_help_connect_your_printer.verify_we_can_help_connect_your_printer_screen()
        we_can_help_connect_your_printer.select_wireless_radio()
        we_can_help_connect_your_printer.click_continue_btn()

        connecting_printer_to_wifi_wireless_setup = ConnectingPrintertoWiFiSetup(self.driver)
        connecting_printer_to_wifi_wireless_setup.verify_connecting_printer_to_wifi_wireless_setup_screen()

    def go_to_wireless_setup_using_usb(self):
        '''
        This is method to go to Wireless setup using USB screen from connecting printer to wifi..screen
        :parameter:
        :return:
        '''
        logging.debug("go to Wireless setup using USB  screen... ")

        connecting_printer_to_wifi_wireless_setup = ConnectingPrintertoWiFiSetup(self.driver)
        wireless_setup_using_usb = WirelessSetupUsingUSB(self.driver)
        connecting_printer_to_wifi_wireless_setup.click_no_opt()
        connecting_printer_to_wifi_wireless_setup.click_continue_btn()
        wireless_setup_using_usb.wait_for_screen_load()

    def go_to_printer_connected_screen_in_ethernet_flow(self):
        '''
        This is a flow from Connect your printer to your network screen to Printer connected screen.
        :parameter:
        :return:
        '''
        logging.debug("Go to printer connected screen... ")
        connect_printer_with_ethernet = ConnectPrinterWithEthernet(self.driver)
        connect_printer_with_ethernet.click_connect_printer_btn()

        we_could_not_find_your_printer_dialog = WeCouldNotFindYourPrinterDialog(self.driver)
        if we_could_not_find_your_printer_dialog.wait_for_screen_load(360, raise_e=False):
            we_could_not_find_your_printer_dialog.click_try_again_btn()
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.wait_for_screen_load(300)
        we_found_your_printer.click_continue_btn()
        printer_connected = PrinterConnected(self.driver)
        printer_connected.verify_printer_connected_screen()

    def go_to_choose_a_connection_method_directly(self):
        '''
        This is method to go to choose a connection method screen during directly the OOBE setup
        :parameter:
        :return:
        '''
        logging.debug("go to choose a connection method screen... ")

        let_find_your_printer = FindYourPrinter(self.driver)
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        select_a_printer = SelectAPrinter(self.driver)
        if let_find_your_printer.wait_for_screen_load(90, raise_e=False):
            '''
            No beaconing printer
            :parameter:
            :return:
            '''
            let_find_your_printer.click_continue_btn()
            if we_found_your_printer.wait_for_screen_load(60, raise_e=False):
                we_found_your_printer.click_change_printer_btn()
        elif we_found_your_printer.wait_for_screen_load(90, raise_e=False):
            '''
            1 beaconing printer
            :parameter:
            :return:
            '''
            we_found_your_printer.click_change_printer_btn()
        elif select_a_printer.wait_for_screen_load(90, raise_e=False):
            '''
            2 or more beaconing printer
            :parameter:
            :return:
            '''
            select_a_printer.click_printer_not_listed_link()
        self.go_to_choose_a_connection_method()

    def click_change_printer_flow_on_we_found_your_printer(self):
        '''
        This is method for click change printer link flow on We Found Your Printer screen during AWC flow.
        :parameter:
        :return:
        '''
        we_found_your_printer = WeFoundYourPrinter(self.driver)
        we_found_your_printer.wait_for_screen_load(600)
        we_found_your_printer.click_change_printer_btn()

        select_a_printer = SelectAPrinter(self.driver)
        select_a_printer.wait_for_screen_load()

    def go_through_flow_to_main_ui_after_ows(self):
        '''
        This is a flow from 'printer from other devices' screen to main UI.
        Click Send Link button to go through Print from other devices screen
        Click Print button to go through Printer setup lets print screen
        :parameter:
        :return:
        '''
        logging.debug("Click Send Link button to go through Print from other devices screen")
        print_from_other_devices = PrintFromOtherDevices(self.driver)
        print_from_other_devices.verify_print_from_other_devices_screen()
        print_from_other_devices.click_send_link_btn()
        print_from_other_devices.select_email_menu_item()
        sleep(2)
        print_from_other_devices.click_quit_btn()

        send_another_link_dialog = SendAnotherLinkDialog(self.driver)
        send_another_link_dialog.verify_send_another_link_dialog()
        send_another_link_dialog.click_done_btn()

        install_driver_to_print = InstallDriverToPrint(self.driver)
        install_driver_to_print.verify_success_print_installed_dialog()
        install_driver_to_print.click_ok_btn()

        logging.debug("Click Print button to go through Printer setup lets print screen")
        printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
        printer_setup_lets_print.verify_printer_setup_lets_print_screen()
        printer_setup_lets_print.click_print_btn()
        printer_setup_lets_print.wait_for_print_dialog_load()
        printer_setup_lets_print.click_print_btn_on_print_dialog()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(60)

    def go_through_oobe_flow_after_printer_connected(self, printer_type):
        '''
        This is a flow from OWS screen to main UI.
        Click Skip sending this link button to go through Print from other devices screen
        Click No now button to go through Printer setup lets print screen
        :parameter:
        :return:
        '''
        self.go_through_ows_flow(printer_type)
        logging.debug("Click Skip sending this link button to go through Print from other devices screen")
        print_from_other_devices = PrintFromOtherDevices(self.driver)
        print_from_other_devices.verify_print_from_other_devices_screen()
        print_from_other_devices.click_skip_sending_this_link_btn()

        install_driver_to_print = InstallDriverToPrint(self.driver)
        install_driver_to_print.verify_success_print_installed_dialog()
        install_driver_to_print.click_ok_btn()

        logging.debug("Click No now button to go through Printer setup lets print screen")
        printer_setup_lets_print = PrinterSetupLetsPrint(self.driver)
        printer_setup_lets_print.verify_printer_setup_lets_print_screen()
        printer_setup_lets_print.click_not_now_btn()

        main_screen = MainUI(self.driver)
        main_screen.wait_for_screen_load(60)
