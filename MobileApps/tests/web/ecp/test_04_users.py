import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import random

pytest.app_info = "ECP"

test_user_email = "automationtestuser_"+str(random.randint(1000,9999))+"@gmail.com"

class Test_01_ECP_Web(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.login = self.fc.fd["login"]
        self.hpid = self.fc.fd["hpid"]
        self.users = self.fc.fd["users"]
        self.account = ma_misc.get_ecp_account_info("pie")
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]

    def test_01_verify_users_section(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093096&group_by=cases:section_id&group_order=asc&group_id=3030499
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.verify_users_menu_btn()
        self.home.click_users_menu_btn()
        self.users.verify_userspage_title(timeout=20)
        self.users.verify_userspage_desc()

    def test_02_verify_contextual_footer(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29106547&group_by=cases:section_id&group_id=3030499&group_order=asc
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.click_select_all_items_checkbox()
        self.users.verify_contextual_footer()
        self.users.verify_contextual_footer_cancel_button()
        self.users.verify_contextual_footer_remove_user_dropdown()
        self.users.verify_contextual_footer_delete_button()
        self.users.click_contextual_footer_cancel_button()

    def test_03_verify_users_refresh_button_functionality(self):
        #Test case: https://hp-testrail.external.hp.com/index.php?/cases/view/29093611&group_by=cases:section_id&group_order=asc&group_id=3030499
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.verify_refresh_button(timeout=20)

    def test_04_verify_remove_user_popup(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093097&group_by=cases:section_id&group_order=asc&group_id=3030499
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.select_user_click_mouse_right_button()
        self.users.click_remove_user()
        self.users.verify_removeuser_popup_title(timeout=20)
        self.users.verify_removeuser_popup_cancel_button()
        self.users.verify_removeuser_popup_remove_button()
        self.users.click_removeuser_popup_cancel_button()

    @pytest.mark.parametrize('search_string', [test_user_email])
    def test_05_verify_invite_single_recipient(self, search_string):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29106549&group_by=cases:section_id&group_id=3030500&group_order=asc
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.click_invite_button()
        self.users.select_option_from_role_dropdown(0)
        self.users.enter_emails_to_invite_txt_box(search_string)
        self.users.click_invite_add_button()
        self.users.click_send_invitation_button()
        self.users.verify_email_invitation_sent_message() 
        self.users.click_all_users_tab()
        self.users.search_users(search_string, timeout=30)
         
    @pytest.mark.parametrize('search_string', ["invalidtestuser", test_user_email])
    def test_06_verify_users_search_functionality(self,search_string ):
        #Tet case: https://hp-testrail.external.hp.com/index.php?/cases/view/29093627&group_by=cases:section_id&group_order=asc&group_id=3030499
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.search_users(search_string, timeout=20)
        self.users.click_search_clear_button()

    @pytest.mark.parametrize('search_string', ["invalidtestuser", test_user_email])
    def test_07_remove_single_user(self, search_string): 
        #https://hp-testrail.external.hp.com/index.php?/cases/view/29093037&group_by=cases:section_id&group_order=asc&group_id=3030499
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        self.home.click_users_menu_btn()
        self.users.verify_remove_single_user(search_string, timeout=20)  
    