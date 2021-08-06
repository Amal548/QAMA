import pytest
from MobileApps.libs.flows.web.softfax.softfax_flow import SoftFaxFlow
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from SAF.decorator.saf_decorator import screenshot_capture

class NoOrNotEnoughRecordException(Exception):
    pass

class FaxHistory(SoftFaxFlow):
    flow_name = "fax_history"

    FAILED_STATUS = "failed_icon"
    SUCCESSFUL_STATUS = "successful_icon"
    PROCESSING_STATUS = "processing_icon"
    DRAFT_RECORD_STATUS = "draft_record_label"
    SENT_RECORD_CELL = "sent_history_record_cell"
    DRAFT_RECORD_CELL = "draft_history_record_cell"
    SENT_TAB = "send_tab_btn"
    DRAFT_TAB = "draft_tab_btn"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************
    def click_sent_tab(self):
        """
        Click on Sent tab
        """
        self.driver.click("send_tab_btn")

    def click_draft_tab(self):
        """
        CLick on Draft tab
        """
        self.driver.click("draft_tab_btn")

    def click_compose_new_fax(self):
        """
        Click on Compose new Fax button
        """
        self.driver.click("compose_new_fax_btn")

    def dismiss_delete_confirmation_popup(self, is_yes=True):
        """
        Dismiss Delete confirmation popup by clicking on Cancel/Delete button
        :param is_yes: Delete. Otherwise, Cancel
        """
        self.driver.wait_for_object("delete_popup_cancel_btn", timeout=5)
        self.driver.wait_for_object("delete_popup_delete_btn", timeout=5)
        if is_yes:
            self.driver.click("delete_popup_delete_btn")
        else:
            self.driver.click("delete_popup_cancel_btn")

    def select_history_record(self, record_type, phone_number, status=None):
        """
        Start at Fax History with Sent as selected tab
        Select a sent history record by phone number and status
        :param record_type: sent/draft record cell. Using class constant.
                    SENT_RECORD_CELL
                    DRAFT_RECORD_CELL
        :param phone_number:
        :param status: for send tab and it is not in edit screen. using class constant.
                - FAILED_STATUS
                - SUCCESSFUL_STATUS
                - PROCESSING_STATUS
                - DRAFT_RECORD_STATUS
                - None: any status
        """
        self.driver.wait_for_object(record_type, timeout=30)
        record_cells= self.driver.find_object(record_type, multiple=True)
        for record in record_cells:
            try:
                rec_found = self.driver.find_object("history_record_phone_number", format_specifier=[phone_number], root_obj=record)
                if status and record_type == self.SENT_RECORD_CELL:
                    self.driver.find_object(status, root_obj=record)
                    if pytest.platform.lower() == "android":
                        record.click()
                    if pytest.platform.lower() == "ios":
                        rec_found.click()
                record.click()
                return True
            except NoSuchElementException:
                continue
        raise NoSuchElementException("There is no record for {} with '{}'status".format(phone_number, status))

    def select_multiple_history_records(self, record_type, phone_number, number_records=2):
        """
        Selecting multiple records in Edit screen
        :param record_type: sent/draft record cell. Using class constant.
                    SENT_RECORD_CELL
                    DRAFT_RECORD_CELL
        :param phone_number:
        :param number_records: at least 2 selected records. Using select_history_record() for selecting one record only.
        """
        self.driver.wait_for_object(record_type, timeout=30)
        record_cells = self.driver.find_object(record_type, multiple=True)
        for record in record_cells:
            if self.driver.find_object("history_record_phone_number", format_specifier=[phone_number], root_obj=record, raise_e=False):
                record.click()
                number_records -= 1
                if number_records == 0:
                    return True
            continue
        raise NoOrNotEnoughRecordException("There is no record or not enough {} records for {}".format(number_records, phone_number))


    #-------------------        EDIT SCREEN         -----------------------------
    def load_edit_screen(self):
        """
        Load Edit screen by:
              - CLick on 3 dot menu button
              - CLick on Select button on menu
        """
        self.driver.click("menu_btn")
        self.driver.click("menu_select_btn")

    def click_edit_cancel(self):
        """
        Click on Cancel button
        """
        self.driver.click("edit_cancel_txt")

    def click_edit_delete(self):
        """
        Click on Delete button on bottom navigation
        """
        self.driver.click("edit_delete_btn")

    def click_edit_export_fax_log(self):
        """
        Click on Export Fax Log button on Edit screen
        """
        self.driver.click("edit_export_log_btn")

    # *********************************************************************************
    #                                VERIFICATION FLOWS                               *
    # *********************************************************************************
    @screenshot_capture(file_name="fax_history.png")
    def verify_fax_history_screen(self, invisible=False, timeout=10):
        """
        Verify current screen is Fax History
        """
        self.driver.wait_for_object("title", invisible=invisible, timeout=timeout)
        self.driver.wait_for_object("menu_btn", invisible=invisible)

    def verify_sent_fax_history_list(self, is_empty=False, phone_number="", raise_e=True):
        """
        Verify empty/non_empty(using phone number) list of Sent Fax History
        """
        if is_empty:
            return self.driver.wait_for_object("empty_sent_fax_title", timeout=5, raise_e=raise_e)  is not False and \
                   self.driver.wait_for_object("empty_sent_fax_message", timeout=5, raise_e=raise_e) is not False
        else:
            try:
                self.driver.wait_for_object("sent_record_status_icon", timeout=5)
                self.driver.wait_for_object("history_record_phone_number", format_specifier=[phone_number], displayed=False)
                self.driver.wait_for_object("sent_record_number_pages_txt", timeout=5)
                self.driver.wait_for_object("sent_record_date_txt", timeout=5)
                return True
            except TimeoutException as ex:
                if raise_e:
                    raise ex
                return False

    def verify_draft_fax_history_list(self, is_empty=False, phone_number="", raise_e=True):
        """
        Verify empty list of Draft fax history
        """
        if is_empty:
            return self.driver.wait_for_object("empty_draft_message", timeout=5, raise_e=raise_e)
        else:
            try:
                self.driver.wait_for_object("draft_record_label", timeout=5)
                self.driver.wait_for_object("history_record_phone_number", format_specifier=[phone_number], displayed=False)
                self.driver.wait_for_object("draft_record_date_txt", timeout=5)
                return True
            except TimeoutException as ex:
                if raise_e:
                    raise ex
                return False

    def verify_export_btn(self, invisible=False, from_edit=False):
        """
        Verify Export button
        :param invisible:
        :param from_edit: Export button from Edit screen or from record
        :return:
        """
        if from_edit:
            self.driver.wait_for_object("edit_export_log_btn", invisible=invisible)
        else:
            self.driver.wait_for_object("record_export_btn", invisible=invisible)

    def verify_edit_screen(self):
        """
        Verify current screen is edit screen:
            - Fax History title
            - Cancel button
            - 3 buttons on bottom nav
        """
        self.driver.wait_for_object("edit_cancel_txt", timeout=10)
        self.driver.wait_for_object("edit_delete_btn", timeout=10)
        self.driver.wait_for_object("edit_export_log_btn", timeout=10)


class MobileFaxHistory(FaxHistory):
    context = "NATIVE_APP"

    def select_tab(self, tab_name):
        """
        :param tab_name: SENT_TAB
                    DRAFT_TAB
        :return:
        """
        self.driver.click(tab_name, timeout=10)

    def open_record_menu_item(self, record_type, index=0, swipe_direction="right"):
        """
        Swipe to left to open the menu items (Delete/Export buttons) of a record
        It is used for delete and export record
        :param record_type: sent/draft record cell. Using class constant.
                    SENT_RECORD_CELL
                    DRAFT_RECORD_CELL
        :param index: index of record. Start at 0
        """
        self.driver.wait_for_object(record_type, timeout=30)
        record = self.driver.find_object(record_type, index=index)
        self.driver.swipe(swipe_object=record, direction=swipe_direction)

    def click_record_delete_btn(self):
        """
        Click on Delete button in record's menu item after calling open_record_menu_item()
        """
        self.driver.click("record_delete_btn", timeout=5)

    def click_record_export_btn(self):
        """
        Click on Export button in record's menu item after calling open_record_menu_item()
        """
        self.driver.click("record_export_btn", timeout=5)
