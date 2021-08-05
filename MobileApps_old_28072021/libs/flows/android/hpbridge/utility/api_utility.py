# coding: utf-8
import requests
import logging
import json
from MobileApps.libs.flows.android.hpbridge.utility import utlitiy_misc
from MobileApps.libs.flows.android.hpbridge.utility.random_utility import RandomUtility
from MobileApps.libs.flows.android.hpbridge.utility.prototype_uitility import PrinterInfo, PrintSetting, SupplyInfo, Cartridge, SupplyStatus
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import time


class APIUtility(object):

    timeout = 120
    encoding = "utf-8"

    def __init__(self):
        stack = utlitiy_misc.load_stack_info()
        user = utlitiy_misc.load_user_device()[0]
        self.test_stack = stack["stack"]
        self.host = stack["host"]
        self.client = stack["client"]
        self.user_id = user["hpid"][self.test_stack.lower()]
        self.access_token = self.get_user_token()

    def get_user_token(self):
        """
        Using hpbridge user id to get the user access token
        :return:
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Basic ' + self.client}
        params = {'userId': self.user_id, 'grant_type': 'client_credentials'}
        r = requests.post(self.host + "/oauth2/token", params=params, headers=headers, timeout=self.timeout)
        r.encoding = self.encoding
        assert r.status_code == 200
        user_token = r.text.split("\"access_token\":\"")[1].split("\",\"expires_in")[0]
        return user_token

    def get_bound_printers(self):
        """
        Get all bound printers for the given user
        :return: the bound printer list
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.get(self.host + "/iot/users/" + self.user_id + "/devices", headers=headers, timeout=self.timeout)
        r.encoding = self.encoding
        assert r.status_code == 200
        return r.text

    def get_printer_amount(self):
        """
        Get the user's bound printers' amount
        :return: the printers' amount
        """
        return len(json.loads(self.get_bound_printers()))

    def get_printer_status(self, printer_id):
        """
        Get the printe's status
        :param printer_id: the printer id in HP Bridge DB
        :return:
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.get(self.host + "/iot/devices/" + printer_id + "/status", headers)
        r.encoding = self.encoding
        if r.status_code == 200:
            return json.loads(r.text)["printerState"]
        else:
            logging.warning("Failed to get the printer's status with reqeust status = %s" % r.status_code)
            return None

    def get_printer_id_by_name(self, printer_name):
        """
        Using the customised printer name to get the printer id from DB,
        only can get the printers which are bound with the user
        :param printer_name: the customised printer name
        :return:
        """
        printer_list = json.loads(self.get_bound_printers())
        for printer in printer_list:
            if printer["deviceName"] == printer_name:
                return printer["deviceId"]

        raise KeyError("Failed to find the match printer with the given name: %s " % printer_name)

    def unbind_printer(self, printer_id):
        """
        Unbind the printer from the user
        :param printer_id: the printer id need to be unbound
        :return:
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.delete(self.host + "/iot/users/" + self.user_id + "/devices/" + printer_id, headers=headers,
                            timeout=self.timeout)
        r.encoding = self.encoding
        assert r.status_code == 204

    def unbind_all_printers(self):
        """
        Unbind all the bound printers under the user
        """
        printer_list = json.loads(self.get_bound_printers())
        for printer in printer_list:
            self.unbind_printer(printer["deviceId"])

        logging.info("Unbind all the printers under the user for clean up")

    def bind_printer(self, printer_id, custom_printer_name, default_device=True, device_group="客厅"):
        """
        For some cases' request, we need bind some printers before test, and the bind printer steps is not the key step
         for these test cases, im order to save time, we use bind printer API to satisfy the cases' precondition
        :param printer_id: The printer's device ID in HP Bridge DB
        :param custom_printer_name: customise the printer's name
        :param default_device: if true, set the device as user's default device
        :param device_group: set the device's group
        :return:
        """
        body = {"deviceId": printer_id, "defaultDevice": default_device,
                "deviceName": custom_printer_name, "deviceGroup": device_group}
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.post(self.host + "/iot/users/" + self.user_id + "/devices", headers=headers, data=json.dumps(body), timeout=self.timeout)
        assert r.status_code == 200
        logging.info("Succeed to bind a printer to the user with customised printer name: " + custom_printer_name)

    def bind_default_printer(self, printer_name=None):
        """
        From the test printers.json file to load the default printer info, and bind the printer to the user
        :return:
        """
        printer = utlitiy_misc.load_printer(printer_name, stack=self.test_stack, api_used=True)
        custom_printer_name = RandomUtility.generate_digit_letter_strs(10)
        self.bind_printer(printer["printer_id"], custom_printer_name)
        return custom_printer_name, printer["printer_id"]

    def get_printer_info(self, printer_id):
        """
        Using the device id to get the bound device's default print setting
        :param printer_id: the printer id
        :return:
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.get(self.host + "/iot/users/" + self.user_id + "/devices/" + printer_id, headers=headers,
                         timeout=self.timeout)
        r.encoding = self.encoding
        assert r.status_code == 200
        printer_json = json.loads(r.text)
        return PrinterInfo(printer_json=printer_json)

    def get_supply_info(self, printer_id):
        """
        Get the supply information for Gen1 printers, for Gen2 printers, the API will return "not support" message
        :param printer_id: the printer's device id in bridge DB
        :return:
        """

        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        r = requests.get(self.host + "/iot/supply/" + printer_id + "/supplyInfo", headers=headers,
                         timeout=self.timeout)
        r.encoding = self.encoding
        response_status = r.status_code
        response_body = json.loads(r.text)
        if response_status == 404 and response_body["errorCode"] == "40416":
            return SupplyStatus.NotSupport
        elif response_status == 200:
            return SupplyInfo(supply_json=response_body)
        else:
            return SupplyStatus.Error


    def get_print_jobs(self):
        """
        Get current user's print job history, only get the last five jobs
        :return:
        """
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer ' + self.access_token}
        params = {'page': 0, 'size': 5}
        r = requests.get(self.host + "/iot/users/" + self.user_id + "/printjobs", headers=headers, params=params,
                         timeout=self.timeout)
        r.encoding = self.encoding
        assert r.status_code == 200
        job_list = json.loads(r.text)["content"]
        return job_list

    def wait_last_print_job_complete(self, timeout=180):
        """
        Get the the user's last job's status. wait for it complete, no matter it succeed or failed
        :param timeout: the timeout
        :return:
        """
        job_status = self.get_print_jobs()[0]["printJobStatus"]
        start_time = time.time()
        time_cost = 0
        while job_status in [1, 2, 3] and time_cost <= timeout:
            job_status = self.get_print_jobs()[0]["printJobStatus"]
            time.sleep(5)
            time_cost = time.time() - start_time

        if time_cost > timeout:
            raise TimeoutError("Print job not finised in %s seconds" % timeout)

        return True
