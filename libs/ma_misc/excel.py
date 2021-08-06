import xlwt, xlrd
import os
import logging
import time
from xlutils.copy import copy
from MobileApps.libs.ma_misc import ma_misc
from SPL.printer_misc.db_misc import printer_database_module
from SPL.printer_misc import printer_misc
from SPL.driver.driver_factory import printer_driver_factory, PrinterInUseException


class Excel(object):
    """
        It is for printer discovery tests
    """

    def __init__(self, file_path):
        """
        Initialize workbook instance with sheet instance
        :param file_path: path of Excel file
        """
        self.file_path = file_path
        self.current_row = 0
        self.workbook = ""
        self.sheet = ""
        self.load_workbook()

    def load_workbook(self):
        """
        Load a workbook
        :return:
        """
        # Load work book
        if os.path.exists(self.file_path):
            temp_workbook = xlrd.open_workbook(self.file_path)
            self.workbook =  copy(temp_workbook)
        else:
            self.workbook = xlwt.Workbook(encoding="utf-8")

    def load_sheet(self, sheet_name):
        """
        Load a sheet
        :param file_path: path of Excel file
        :param sheet_name: sheet name
        """
        # Load sheet
        try:
            self.sheet = self.workbook.add_sheet(sheet_name)
            self.current_row = 0
        except Exception as ex:
            logging.info("{} sheet is existed".format(sheet_name))
            self.save()  # Make sure .xls file is created to get current row of this sheet
            self.sheet = self.workbook.get_sheet(sheet_name)
            temp_workbook = xlrd.open_workbook(self.file_path)
            self.current_row = temp_workbook.sheet_by_name(sheet_name).nrows

    def write_new_record(self, record):
        """
        Write new record
        :param record: new record in format
            [date, printer name, result, error]
        """
        for column, value in enumerate(record):
            self.sheet.write(self.current_row,  column, value)
        self.current_row += 1

    def save(self):
        """
        Save printer discovery records to .xls file
        """
        if not os.path.exists(self.file_path):
            ma_misc.create_file(self.file_path)
        self.workbook.save(self.file_path)

    def load_printers_info(self, ssid = "", passwd = ""):
        """
        Load information of printers from printers_info.json for special printers (laserjet, ...) and from CouchDB
        :return: list of printers information
        """
        system_cfg = ma_misc.load_system_config_file()
        pp_info = system_cfg["printer_power_config"]
        # Load printer from printer_config.json if it exist
        printers_info = []
        if os.path.exists(ma_misc.get_abs_path("/config/printers_info.json")):
            printers_info = ma_misc.load_json_file("/config/printers_info.json")
        if pp_info["type"] == "pdu":
            db = printer_database_module()
            pdu_map = db.load_pdu_record(pp_info["pdu_url"])
            pcs_str_list = printer_misc.get_pcs_printer_list(pdu_map["pcs"], full_str=True)
            for pcs_string in pcs_str_list:
                timeout = time.time() + 60
                p_obj = None
                while time.time() < timeout:
                    try:
                        p_obj = printer_driver_factory(pcs_string, pp_info, power_cycle_printer=False)
                    except PrinterInUseException:
                        time.sleep(10)                  # break 10 seconds
                        continue
                # Skip this printer if is not generated p_object.
                if not p_obj:
                    logging.warning("Cannot load the printer ({})".format(pcs_string))
                    continue
                ssid = ssid if ssid else system_cfg["default_wifi"]["ssid"]
                passwd = passwd if passwd else system_cfg["default_wifi"]["passwd"]
                p_obj.connect_to_wifi(ssid, passwd)
                info = p_obj.get_printer_information()
                printers_info.append({"ip address": info["ip address"],
                                      "bonjour name": info["bonjour name"],
                                      "serial number": info["serial number"],
                                      "host name": info["host name"]})
                p_obj.close()
        return printers_info