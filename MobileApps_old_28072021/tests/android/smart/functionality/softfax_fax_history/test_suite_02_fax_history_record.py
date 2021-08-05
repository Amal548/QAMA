import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_Fax_History_Record(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_history =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_HISTORY]
        cls.send_fax_details = cls.fc.flow[FLOW_NAMES.SEND_FAX_DETAILS]

        # Define variables
        cls.recipient_phone = cls.fc.get_softfax_recipient_info()["phone"]
        cls.recipient_code = cls.fc.get_softfax_recipient_info()["code"]
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_01_records(self, tab):
        """
        Description:
            1/ Load to Compose Fax and make a send fax job / save as draft
            2/ Click on 3 dot menu/ Fax history
            3/ Click to Sent/Draft button
        Expected Result:
            3/
              - List of sent records,
              - Disappear 'You have no sent fax history' text
              - Compose new Fax button
        """
        #Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        if tab == "sent":
            phone_no = self.__load_fax_history_after_sending_fax(create_acc=True)
            self.fax_history.click_sent_tab()
            self.fax_history.verify_sent_fax_history_list(is_empty=False, phone_number=phone_no)
        else:
            phone_no = self._load_fax_history_after_saving_draft(create_acc=True)
            self.fax_history.click_draft_tab()
            self.fax_history.verify_draft_fax_history_list(is_empty=False, phone_number=phone_no)
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_02_record_delete(self, tab):
        """
        Description:
            1/ Load Fax History/Sent - Draft as test 04
            2/ Swipe to left -> Click on Delete button
            3/ Click on Yes button on popup
        Expected Result:
            2/Confirmation popup display
            3/ Fax History/Sent screen displays with empty list
        """
        #Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        if tab == "sent":
            self.__load_fax_history_after_sending_fax(create_acc=True)
            self.fax_history.click_sent_tab()
            self.fax_history.open_record_menu_item(self.fax_history.SENT_RECORD_CELL)
        else:
            self._load_fax_history_after_saving_draft(create_acc=True)
            self.fax_history.click_draft_tab()
            self.fax_history.open_record_menu_item(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.click_record_delete_btn()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_03_record_cancel_deletion(self, tab):
        """
        Description:
            1/ Load Fax History/Sent - Draft as test 04
            2/ Swipe to left -> Click on Delete button
            3/ Click on No button on popup
        Expected Result:
            2/Confirmation popup display
            3/ Fax History/Sent screen displays
        """
        if tab == "sent":
            phone_no = self.__load_fax_history_after_sending_fax(create_acc=False)
            self.fax_history.click_sent_tab()
            self.fax_history.open_record_menu_item(self.fax_history.SENT_RECORD_CELL)
        else:
            phone_no = self._load_fax_history_after_saving_draft(create_acc=False)
            self.fax_history.click_draft_tab()
            self.fax_history.open_record_menu_item(self.fax_history.DRAFT_RECORD_CELL)
        self.fax_history.click_record_delete_btn()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=False)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.click_sent_tab()
            self.fax_history.verify_sent_fax_history_list(is_empty=False, phone_number=phone_no)
        else:
            self.fax_history.click_draft_tab()
            self.fax_history.verify_draft_fax_history_list(is_empty=False, phone_number=phone_no)

    def test_04_send_record_export(self):
        """
        Description:
            1/ Load Fax History/Sent as test 05
            2/ Swipe to left -> Click on Export button
        Expected Result:
            2/ HOme screen of app
        """
        self.__load_fax_history_after_sending_fax(create_acc=False)
        self.fax_history.click_sent_tab()
        self.fax_history.open_record_menu_item(self.fax_history.SENT_RECORD_CELL)
        self.fax_history.click_record_export_btn()
        self.fax_history.verify_export_btn(invisible=True, from_edit=False)

    # ----------------      PRIVATE FUNCTIONS   --------------------------------------
    def __load_fax_history(self):
        """
        Load to Fax History screen
                - Load Compose Fax screen
                - CLick on Fax History on menu
        """
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_HISTORY_BTN)
        self.fax_history.verify_fax_history_screen()

    def __load_fax_history_after_sending_fax(self, create_acc=False, number_faxes=1):
        """
        Load Compose Fax screen
        Sending a fax (don't need to check whether sending fax successful or not)
        Load Fax History from compose screen
        :return: full phone number of recipient which is used to select a record on fax history screen
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=create_acc)
        for _ in range(number_faxes):
            self.fc.make_send_fax_job(self.recipient_phone, self.sender_info["name"], self.sender_info["phone"])
            self.send_fax_details.click_back()
        self.__load_fax_history()
        return "{} {}".format(self.recipient_code, self.recipient_phone)

    def _load_fax_history_after_saving_draft(self, create_acc=False, number_saving=1):
        """
        Load Compose Fax screen
        Entering recipient phone number
        CLick on Save as draft in menu
        Load Fax History from compose screen
        :return: full phone number of recipient which is used to select a record on fax history screen
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=create_acc)
        for _ in range(number_saving):
            self.compose_fax.enter_recipient_information(self.recipient_phone)
            self.compose_fax.enter_sender_information(self.sender_info["name"], self.sender_info["phone"])
            self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_SAVE_DRAFT_BTN)
            self.fax_history.click_back()
        self.__load_fax_history()
        return "{} {}".format(self.recipient_code, self.recipient_phone)