# coding: utf-8
import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import GroupName
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc

pytest.app_info = "hpbridge"


class TestChooseGroup(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mp_home = self.fc.flow["mp_home"]
        self.binding = self.fc.flow["bind_printer"]

        # Define variables
        self.api_utility = APIUtility()
        self.living_room = GroupName.LIVING_ROOM.value
        self.bed_room = GroupName.BED_ROOM.value
        self.study = GroupName.STUDY.value

        """
        PreConditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code
        """
        self.api_utility.unbind_all_printers()

    def test_01_binding_printer_choose_group(self):
        """
        Steps:
            1. Scan the QR code to binding the device on WeChat App.
            2. Check the "绑定打印机" page.
            3. Click the "卧室" or "书房" to change the other group.
            4. Multiple clicks exist in several groups to switch.
            5. Select a group and click "绑定打印机" button.
            6. Check the group information on the home page.
        Expected result:
            1. Verify the "请选择分组" should be displayed correctly on the "绑定打印机" page.
            2. Verify three groups "客厅" , "卧室" , "书房" and "+" should be displayed under the "请选择分组"
            3. Verify the other groups can be selected successfully.
            4. Verify the each group can switch normally and the selected group should be displayed with highlighted
            5. Verify the printer can be binding successfully and go to the home page.
            6. Verify the selected group should be displayed next to the state correctly.
        """
        printer = utlitiy_misc.load_printer()
        self.wechat.send_qrcode(printer["index"])
        self.wechat.scan_qrcode_to_mp()
        self.binding.select_a_group(self.study)
        self.binding.select_a_group(self.bed_room)
        self.binding.select_a_group(self.living_room)
        printer_name = self.binding.get_printer_name()
        self.binding.click_binding_btn()
        self.binding.click_start_print_btn()
        self.mp_home.verify_group_name(printer_name=printer_name, group_name=self.living_room)