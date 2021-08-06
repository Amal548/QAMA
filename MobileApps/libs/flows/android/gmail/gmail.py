from mobiauto.mobiauto import MobiEzApp, MobiConfig
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from MobileApps.resources.const.android.eprint.EPRINT_ANDROID_CONST import *
from time import sleep


class CONST_GMAIL():
    GMAIL_PACKAGE = 'com.google.android.gm'
    MAIN_ACTIVITY = 'com.google.android.gm.ConversationListActivityGmail'


class Gmail(object):
    def __init__(self, app, cfg):
        """
        :type app: MobiEzApp
        :param app:
        :type cfg: MobiConfig
        :param cfg:

        PRE-CONDITION: desired account has already been added to the android device.
        """
        self.app = app
        self.cfg = cfg
        self.timeout = TIMEOUT.DEFAULT_TIMEOUT

    def start_app(self):
        self.app.start_activity(CONST_GMAIL.GMAIL_PACKAGE, CONST_GMAIL.MAIN_ACTIVITY)

    def switch_account(self, email):
        WebDriverWait(self.app, self.timeout).until(EC.visibility_of_element_located(
            (By.ID, "com.google.android.gm:id/content_pane")))
        self.app.click_on_element_by_pair_value(("xpath", "//android.widget.ImageButton[1]"))
        sleep(1)
        if self.app.find_element_by_id("com.google.android.gm:id/account_address").text != email:
            self.app.find_element_by_id("com.google.android.gm:id/account_list_button").click()
            self.app.find_element_by_name(email).click()
        else:
            self.app.press_keycode(4)

    def select_email_by_name(self, name):
        self.app.click_on_element_by_id("com.google.android.gm:id/search", timeout=10)
        search_box = self.app.find_element_by_id("com.google.android.gm:id/search_actionbar_query_text")
        search_box.send_keys(name)
        self.app.keyevent(66) # Enter Key
        WebDriverWait(self.app, self.timeout).until(EC.visibility_of_element_located(
            (By.ID, "com.google.android.gm:id/conversation_list_view")))
        listview = self.app.find_element_by_id("com.google.android.gm:id/conversation_list_view")
        listview.find_elements_by_class_name("android.view.View")[0].click()


    def get_eprint_activation_code(self):
        self.app.scroll_down_to_element_by_id(self.app.find_element_by_id("com.google.android.gm:id/conversation_pager"), "com.google.android.gm:id/reply_button" )

        WebDriverWait(self.app, self.timeout).until(EC.visibility_of_element_located(
            (By.ID, "com.google.android.gm:id/reply_button")))
        self.app.find_element_by_id("com.google.android.gm:id/reply_button").click()
        self.app.find_element_by_id("com.google.android.gm:id/respond_inline_button").click()
        self.app.hide_keyboard()
        body = self.app.find_element_by_id("com.google.android.gm:id/body")
        code = body.text
        print code
        self.app.back()
        code = code[(code.find("Enter the PIN code:") + len("Enter the PIN code: ")):]
        print "ACTIVATION CODE: " + code[0:4]
        return code[0:4]

    def delete_displayed_email(self):
        WebDriverWait(self.app, self.timeout).until(EC.visibility_of_element_located(
            (By.ID, "com.google.android.gm:id/delete")))
        self.app.find_element_by_id("com.google.android.gm:id/delete").click()
        try:
            self.app.find_element_by_id("com.google.android.gm:id/search_actionbar_back_button").click()
            self.app.find_element_by_id("com.google.android.gm:id/search_actionbar_back_button").click()
        except NoSuchElementException:
            pass







