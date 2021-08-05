from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrintSetting, SupplyStatus, SupplyInfo
from time import sleep
import enum


class PAMyPrinter(HPBridgeFlow):
    flow_name = "pa_my_printer"

    def select_printer(self, printer_name):
        """
        Using the printer name to select the printer from device list page
        :param printer_name: the printer name used to identify the printer
        :return:
        """
        self.driver.click("printer_spec", format_specifier=[printer_name])
        self.driver.wait_for_object("printers")

    def verify_printer_under_account(self, printer_name, invisible=False):
        """
        Check the printer is bound with user or not
        :param printer_name: the printer name used to identify the printer
        :param invisible: if set it to False, verify the printer is bound with user,
         otherwise, verify printer is unbound
        :return:
        """
        self.driver.wait_for_object("printer_spec", format_specifier=[printer_name], invisible=invisible)

    def unbind_printer(self, printer_name):
        """
        Unbind the printer
        :param printer_name: The printer name used to identify the printer
        :return:
        """
        self.select_printer(printer_name)
        current_printer = self.driver.find_object("current_printer")
        self.driver.click("unbinding_btn", root_obj=current_printer)
        self.driver.wait_for_object("confirm_unbinding_btn").click()
        self.verify_printer_under_account(printer_name, invisible=True)

    def change_printer_name(self, new_name):
        """
        in the printer home page, change the printer name with the new given name
        :param new_name: the new printer name you want to set
        :return:
        """
        self.driver.click("change_name_btn")
        self.driver.wait_for_object("dialog_title")
        self.driver.send_keys("input_printer_name", new_name)
        self.driver.click("save_btn")
        current_printer = self.driver.wait_for_object("current_printer")
        printer_name = self.driver.get_text("printer_name", root_obj=current_printer)
        assert printer_name == new_name, AssertionError("Failed to change the printer name")

    def select_file_printer_setting(self):
        """
        select file print setting tab on printer home page
        :return:
        """
        self.driver.click("file_print_tab")

    def select_photo_printer_setting(self):
        """
        select photo print setting tab on printer home page
        :return:
        """
        self.driver.click("img_print_tab")

    def select_supply_info(self):
        """
        select supply info tab on printer home page
        :return:
        """
        self.driver.click("ink_info_tab")

    def get_setting_option_offset(self):
        """
        Because the duplex option only exist in doc settings, so the other setting's option index
        is different between doc and photo settings page
        :return: the index offset for the the setting option
        """
        if len(self.driver.find_object("setting_list", multiple=True)) > 4:
            return 1
        else:
            return 0

    def get_duplex_checkbox_status(self):
        """
        check the duplex checkbox status, if the duplex checkbox is checked, return true, otherwise, return false.
        and also check the enabled status, if enable, return true, otherwise, return false
        :return: check status, enabled status
        """
        duplex = self.driver.wait_for_object("setting_list")
        duplex_check_status = self.driver.get_attribute("checkbox", "class", root_obj=duplex) \
                              == "slide_btn defaultPrinter"

        duplex_enabled_status = self.driver.get_attribute("checkbox_enabled", "class", root_obj=duplex) \
                                == "slide_module disabledBtn"

        return duplex_check_status, duplex_enabled_status

    def get_color_checkbox_status(self):
        """
        check the color checkbox status, if the duplex checkbox is checked, return true, otherwise, return false.
        and also check the enabled status, if enable, return true, otherwise, return false
        :return: check status, enabled status
        """
        index_offset = self.get_setting_option_offset()
        color = self.driver.find_object("setting_list", index=0 + index_offset)
        color_check_status = self.driver.get_attribute("checkbox", "class", root_obj=color) \
                             == "slide_btn defaultPrinter"
        color_enabled_status = self.driver.get_attribute("checkbox_enabled", "class", root_obj=color) \
                               == "slide_module disabledBtn"

        return color_check_status, color_enabled_status

    def get_paper_size_setting(self):
        """
        get the current paper size setting, and also return the enabled status
        :return:
        """
        index_offset = self.get_setting_option_offset()
        paper_size = self.driver.find_object("setting_list", index=1 + index_offset)
        paper_size_value = self.driver.get_text("setting_value", root_obj=paper_size)
        paper_enabled_status = self.driver.get_attribute("setting_value", "class", root_obj=paper_size) \
                               == "ng-binding graycolor floatr"

        return paper_size_value, paper_enabled_status

    def get_paper_type_setting(self):
        """
        get the current paper type setting, and also return the enabled status
        :return:
        """
        index_offset = self.get_setting_option_offset()
        paper_type = self.driver.find_object("setting_list", index=2 + index_offset)
        paper_type_value = self.driver.get_text("setting_value", root_obj=paper_type)
        paper_enabled_status = self.driver.get_attribute("setting_value", "class", root_obj=paper_type) \
                               == "ng-binding graycolor floatr"
        return paper_type_value, paper_enabled_status

    def get_quality_setting(self):
        """
        get the current quality setting, and also return the enabled status
        :return:
        """
        index_offset = self.get_setting_option_offset()
        quality = self.driver.find_object("setting_list", index=3 + index_offset)
        quality_value = self.driver.get_text("setting_value", root_obj=quality)
        quality_enabled_status = self.driver.get_attribute("setting_value", "class", root_obj=quality) \
                                 == "ng-binding graycolor floatr"
        return quality_value, quality_enabled_status

    def check_print_setting(self, print_setting):
        """
        check the file print setting is the same as user's file print setting
        :param print_setting: the setting should be the object of class PrintSetting
        :return:
        """
        index_offset = self.get_setting_option_offset()
        if isinstance(print_setting, PrintSetting):
            if index_offset == 1:
                duplex_checked = self.get_duplex_checkbox_status()[0]
                assert duplex_checked == print_setting.duplex
            assert self.get_color_checkbox_status()[0] == print_setting.color
            assert self.get_paper_size_setting()[0] == print_setting.media_size
            assert self.get_paper_type_setting()[0] == print_setting.media_type
            assert self.get_quality_setting()[0] == print_setting.quality

        else:
            raise TypeError("doc_setting needs to be an object of class PrintSetting")

    def check_supply_info(self, target_supply_info):
        """
        using printer_id calling API to get the current supply information,
        the response saved into the variable target_supply_info
        and then check the ink in the device home page
        :param target_supply_info: the printer's supply info from the api response
        :return:
        """
        if isinstance(target_supply_info, SupplyStatus):
            pass
        else:
            if not isinstance(target_supply_info, SupplyInfo):
                raise TypeError("the input target supply info should be instance of SupplyInfo class")
            if target_supply_info.m_cartridge:
                percentage_style = "width: " \
                                   + str(target_supply_info.m_cartridge.remaining_percent) + "%;"
                assert self.driver.get_attribute("cartridge_percentage_spec", "style",
                                                 format_specifier=["red"]) == percentage_style
            if target_supply_info.c_cartridge:
                percentage_style = "width: " \
                                   + str(target_supply_info.c_cartridge.remaining_percent) + "%;"
                assert self.driver.get_attribute("cartridge_percentage_spec", "style",
                                                 format_specifier=["blue"]) == percentage_style
            if target_supply_info.y_cartridge:
                percentage_style = "width: " \
                                   + str(target_supply_info.y_cartridge.remaining_percent) + "%;"
                assert self.driver.get_attribute("cartridge_percentage_spec", "style",
                                                 format_specifier=["yellow"]) == percentage_style
            if target_supply_info.k_cartridge:
                percentage_style = "width: " \
                                   + str(target_supply_info.k_cartridge.remaining_percent) + "%;"
                assert self.driver.get_attribute("cartridge_percentage_spec", "style",
                                                 format_specifier=["black"]) == percentage_style
            if target_supply_info.cmy_cartridge:
                percentage_style = "width: " \
                                   + str(target_supply_info.cmy_cartridge.remaining_percent) + "%;"
                assert self.driver.get_attribute("cartridge_percentage_spec", "style",
                                                 format_specifier=["cmy"]) == percentage_style






