# encoding: utf-8
'''
Description: It defines the operations of element and verification methods on the Personalize Tiles page.

@author: Ivan
@create_date: Jan 8, 2020
'''
import logging

from MobileApps.libs.flows.mac.smart.screens.smart_screens import SmartScreens
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedValueException


class PersonalizeTiles(SmartScreens):
    folder_name = "menubar"
    flow_name = "personalize_tiles"

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        super(PersonalizeTiles, self).__init__(driver)

# -------------------------------Operate Elements------------------------------
    def wait_for_screen_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Personalize Tiles page screen shows correctly.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[wait_for_screen_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("personalize_tiles_title", timeout=timeout, raise_e=raise_e)

    def wait_for_mobile_fax_item_load(self, timeout=30, raise_e=True):
        '''
        This is a method to wait Mobile fax item load on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[wait_for_mobile_fax_item_load]-Wait for screen loading... ")

        return self.driver.wait_for_object("mobile_fax_item", timeout=timeout, raise_e=raise_e)

    def get_value_of_personalize_tiles_title(self):
        '''
        This is a method to get value of Personalize Tiles page title.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_personalize_tiles_title] - Get value of Personalize Tiles page title...  ")

        return self.driver.get_value("personalize_tiles_title")

    def get_value_of_personalize_tiles_content(self):
        '''
        This is a method to get value of Personalize Tiles page content.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_personalize_tiles_text] - Get value of Personalize Tiles page content...  ")

        return self.driver.get_value("personalize_tiles_content")

    def get_value_of_smart_tasks_item(self):
        '''
        This is a method to get value of Smart Tasks item Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_item] - Get value of Smart Tasks item...  ")

        return self.driver.get_value("smart_tasks_item")

    def get_value_of_smart_tasks_content(self):
        '''
        This is a method to get value of Smart Tasks content Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_content] - Get value of Smart Tasks content...  ")

        return self.driver.get_value("smart_tasks_content")

    def get_title_of_smart_tasks_off_radio(self):
        '''
        This is a method to get value of Smart Tasks Off radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_off_radio] - Get value of Smart Tasks Off radio...  ")

        return self.driver.get_title("smart_tasks_off_radio")

    def get_title_of_smart_tasks_on_radio(self):
        '''
        This is a method to get value of Smart Tasks On radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_on_radio] - Get value of Smart Tasks On radio...  ")

        return self.driver.get_title("smart_tasks_on_radio")

    def get_value_of_smart_tasks_off_radio(self):
        '''
        This is a method to get value of Smart Tasks Off radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_off_radio] - Get value of Smart Tasks Off radio...  ")

        return self.driver.get_value("smart_tasks_off_radio")

    def get_value_of_smart_tasks_on_radio(self):
        '''
        This is a method to get value of Smart Tasks On radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_smart_tasks_on_radio] - Get value of Smart Tasks On radio...  ")

        return self.driver.get_value("smart_tasks_on_radio")

    def get_value_of_mobile_fax_item(self):
        '''
        This is a method to get value of Mobile Fax item Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_item] - Get value of Mobile Fax item...  ")

        return self.driver.get_value("mobile_fax_item")

    def get_value_of_mobile_fax_content(self):
        '''
        This is a method to get value of Mobile Fax content Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_content] - Get value of Mobile Fax content...  ")

        return self.driver.get_value("mobile_fax_content")

    def get_title_of_mobile_fax_off_radio(self):
        '''
        This is a method to get value of Mobile Fax Off radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_off_radio] - Get value of Mobile Fax Off radio...  ")

        return self.driver.get_title("mobile_fax_off_radio")

    def get_title_of_mobile_fax_on_radio(self):
        '''
        This is a method to get value of Mobile Fax On radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_on_radio] - Get value of Mobile Fax On radio...  ")

        return self.driver.get_title("mobile_fax_on_radio")

    def get_value_of_mobile_fax_off_radio(self):
        '''
        This is a method to get value of Mobile Fax Off radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_off_radio] - Get value of Mobile Fax Off radio...  ")

        return self.driver.get_value("mobile_fax_off_radio")

    def get_value_of_mobile_fax_on_radio(self):
        '''
        This is a method to get value of Mobile Fax On radio on Personalize Tiles page.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[get_value_of_mobile_fax_on_radio] - Get value of Mobile Fax On radio...  ")

        return self.driver.get_value("mobile_fax_on_radio")

    def click_smart_tasks_off_radio(self):
        '''
        This is a method to click Off radio for Smart Tasks item.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[click_smart_tasks_off_radio]-Click Off radio... ")

        self.driver.click("smart_tasks_off_radio", is_native_event=True)

    def click_smart_tasks_on_radio(self):
        '''
        This is a method to click On radio for Smart Tasks item.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[click_smart_tasks_on_radio]-Click On radio... ")

        self.driver.click("smart_tasks_on_radio", is_native_event=True)

    def click_mobile_fax_off_radio(self):
        '''
        This is a method to click Off radio for Mobile Fax item.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[click_mobile_fax_on_radia]-Click Off radio... ")

        self.driver.click("mobile_fax_off_radio", is_native_event=True)

    def click_mobile_fax_on_radio(self):
        '''
        This is a method to click On radio for Mobile Fax item.
        :parameter:
        :return:
        '''
        logging.debug("[PersonalizeTiles]:[click_mobile_fax_on_radio]-Click On radio... ")

        self.driver.click("mobile_fax_on_radio", is_native_event=True)

# -------------------------------Verification Methods--------------------------
    def verify_personalize_tiles_page(self):
        '''
        This is a verification method to check UI strings of Personalize Tiles page.
        :parameter:
        :return:
        '''
        self.wait_for_screen_load()
        logging.debug("Start to check UI strings of Personalize Tiles page")
#         assert self.get_value_of_mobile_fax_item() == ""
#         assert self.get_value_of_mobile_fax_content() == ""

    def verify_smart_tasks_toggle_button_is_enable(self):
        '''
        This is a verification method to check Smart Tasks default toggle button is enable.
        :parameter:
        :return:
        '''
        if self.get_value_of_smart_tasks_on_radio() != "1":
            raise UnexpectedValueException("The Smart Tasks default toggle button is Disable")
        return True

    def verify_smart_tasks_toggle_button_is_disable(self):
        '''
        This is a verification method to check Smart Tasks toggle button is disable.
        :parameter:
        :return:
        '''
        if self.get_value_of_smart_tasks_on_radio() == "1":
            raise UnexpectedValueException("The Smart Tasks default toggle button is Enable")
        return True
