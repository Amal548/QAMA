import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_01_Fax_History(object):

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

    def test_01_empty_sent(self):
        """
        Description:
            1/ Load to Compose Fax with a new account
            2/ Click on 3 dot menu/ Fax history
            3/ Click on Sent tab
        Expected Result:
            3/ 'You have no sent fax history' text
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.__load_fax_history()
        self.fax_history.click_sent_tab()
        self.fax_history.verify_sent_fax_history_list(is_empty=True)

    def test_02_empty_draft(self):
        """
        Description:
            1/ Load to Compose Fax with a new account
            2/ Click on 3 dot menu/ Fax history
            3/ Click on Draft tab
        Expected Result:
            3/ 'No saved drafts' message
        """
        #Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=True)
        self.__load_fax_history()
        self.fax_history.click_draft_tab()
        self.fax_history.verify_draft_fax_history_list(is_empty=True)
    
    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_03_compose_new_fax(self, tab):
        """
            Description:
                1/ Load Fax History -> click on sent/draft tab
                2/ Click Compose New Fax button
            Expected Result:
                2/ Compose Fax screen
        """
        #Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False, check_onboarding=True)
        self.__load_fax_history()
        if tab == "sent":
            self.fax_history.click_sent_tab()
        else:
            self.fax_history.click_draft_tab()
        self.fax_history.click_compose_new_fax()
        self.compose_fax.verify_compose_fax_screen()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_04_edit_cancel(self, tab):
        """
        Description:
            1/ Load Fax History screen
            2/ Click on Edit button (with sent/draft tab)
            3/ Click on Cancel button
        Expected Result:
            3/ Fax History with Edit button, no cancel button
        """
        self.__load_fax_history_edit(tab, create_acc=False)
        self.fax_history.click_edit_cancel()
        self.fax_history.verify_fax_history_screen()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_05_edit_cancel_deletion(self, tab):
        """
        Description:
            1/ Load Fax History screen
            2/ Click on Edit button
            3/ Check some records and click on Delete button
            4/ Click on No button
        Expected Result:
            3/ Confirmation popup
            4/ Fax History with Cancel button, no Edit button
                Delete, Print fax log, and Export fax log buttons on bottom"
        """
        phone = self.__load_fax_history_edit(tab, create_acc=False)
        if tab == "sent":
            self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=phone)
        else:
            self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number=phone)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=False)
        self.fax_history.verify_edit_screen()

    @pytest.mark.parametrize("number", [1, 3])
    def test_06_edit_sent_export_fax_log(self, number):
        """
        Description:
            1/ Load Fax History screen
            2/ Click on Edit button
            3/ Check  1/multiple (3) records and click on Export Fax Log button
        Expected Result:
            3/ Fax History is invisible
        """
        phone = self.__load_fax_history_edit("sent", create_acc=False, number_faxes=number)
        if number == 1:
            self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=phone)
        else:
            self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=phone,
                                                             number_records=number)
        self.fax_history.click_edit_export_fax_log()
        self.fax_history.verify_export_btn(invisible=True, from_edit=True)

    @pytest.mark.parametrize("number", [1, 3])
    def test_07_edit_draft_export_fax_log(self, number):
        """
        Description:
            1/ Load Fax History screen -> Click on Draft tab
            2/ Click on Edit button
            3/ Check s1/multiple (3) records and click on Export Fax Log button
        Expected Result:
            3/ Fax History is visible
        """
        phone = self.__load_fax_history_edit("draft", create_acc=False, number_faxes=number)
        if number == 1:
            self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number=phone)
        else:
            self.fax_history.select_multiple_history_records(self.fax_history.DRAFT_RECORD_CELL, phone_number=phone,
                                                             number_records=number)
        self.fax_history.click_edit_export_fax_log()
        self.fax_history.verify_edit_screen()

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_08_edit_delete_record(self, tab):
        """
        Description:
            1/ Load Fax History screen
            2/ Click on Edit button
            3/ Check some records and click on Delete button
            4/ Click on Yes button
        Expected Result:
            3/ Confirmation popup
            4/ Fax History with Edit button, no Cancel button.
        """
        # Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        phone = self.__load_fax_history_edit(tab, create_acc=True)
        if tab == "sent":
            self.fax_history.select_history_record(self.fax_history.SENT_RECORD_CELL, phone_number=phone)
        else:
            self.fax_history.select_history_record(self.fax_history.DRAFT_RECORD_CELL, phone_number=phone)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)

    @pytest.mark.parametrize("tab", ["sent", "draft"])
    def test_09_edit_delete_multiple_record(self, tab):
        """
        Description:
            1/ Load Fax History screen
            2/ Click on Edit button
            3/ Check 3 records and click on Delete button
            4/ Click on Yes button
            Expected Result:
                3/ Confirmation popup
                4/ Fax History with Edit button, no Cancel button.
            """
        # Make sure not affect by previous test when HPID failed from previous test
        self.fc.reset_app()
        phone = self.__load_fax_history_edit(tab, create_acc=True, number_faxes=3)
        if tab == "sent":
            self.fax_history.select_multiple_history_records(self.fax_history.SENT_RECORD_CELL, phone_number=phone,
                                                             number_records=3)
        else:
            self.fax_history.select_multiple_history_records(self.fax_history.DRAFT_RECORD_CELL, phone_number=phone,
                                                             number_records=3)
        self.fax_history.click_edit_delete()
        self.fax_history.dismiss_delete_confirmation_popup(is_yes=True)
        self.fax_history.verify_fax_history_screen()
        if tab == "sent":
            self.fax_history.verify_sent_fax_history_list(is_empty=True)
        else:
            self.fax_history.verify_draft_fax_history_list(is_empty=True)

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

    def __load_fax_history_edit(self, tab, create_acc=False, number_faxes=1):
        """
        - Load Fax History screen after sending fax or saving draft
        - Click on Edit button
        - Verify Edit screen
        """
        if tab == "sent":
            phone = self.__load_fax_history_after_sending_fax(create_acc=create_acc, number_faxes=number_faxes)
            self.fax_history.click_sent_tab()
        else:
            phone = self._load_fax_history_after_saving_draft(create_acc=create_acc, number_saving=number_faxes)
            self.fax_history.click_draft_tab()
        self.fax_history.load_edit_screen()
        self.fax_history.verify_edit_screen()
        return phone