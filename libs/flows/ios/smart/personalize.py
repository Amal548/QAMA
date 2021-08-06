import logging
import re
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow


class Personalize(SmartFlow):
    flow_name = "personalize"

    TILES = [
        "print_photos", "get_supplies", "play_and_learn", "smart_tasks", "mobile_fax",
        "camera_scan", "help_and_support", "print_documents", "printer_scan", "copy", "create_photo_books"
    ]

    SWITCHES = [
        "print_photos_switch", "get_supplies_switch", "play_and_learn_switch", "smart_tasks_switch",
        "mobile_fax_switch", "camera_scan_switch", "help_and_support_switch", "print_documents_switch",
        "printer_scan_switch", "copy_switch", "create_photo_books_switch"
    ]

    MOBILE_FAX_SWITCH = "mobile_fax_switch"
########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def toggle_switch_by_name(self, tile_name, on=True):
        """
        param on: bool True to toggle on, False to toggle off
        """
        switch = self.driver.wait_for_object(tile_name)
        if int(self.driver.driver_info['platformVersion'].split(".")[0]) > 12:
            switch_value = int(switch.get_attribute("value"))
        else:
            # regex workaround for iOS 12 https://github.azc.ext.hp.com/QAMA/MobileApps/issues/851
            pattern = re.compile(r'value=\"(0|1)\" name=\"{}\"'.format(switch.get_attribute("name")))
            switch_value =  int(re.search(pattern, self.driver.wdvr.page_source).group(1))   
        if bool(switch_value) is not on:
            switch.click()  
          

    def toggle_all_tiles(self, on=True):
        self.driver.wait_for_object("tile_switch")
        tile_switches = self.driver.find_object("tile_switch", multiple=True)
        logging.info("Number of Tiles: {}".format(len(tile_switches)))
        for switch in tile_switches:
            if (bool(int(switch.get_attribute("value")))) is not on:
                logging.info("Enabling [{}]. Clicking toggle!".format(switch.get_attribute("name")))
                switch.click()

########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_personalize_screen(self):
        """
        Verify that current screen is Personalize screen
        """
        self.driver.wait_for_object("_shared_str_personalized_tiles")
        self.driver.wait_for_object("done_btn")
