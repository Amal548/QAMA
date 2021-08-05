# encoding: utf-8
'''
Description: It defines miscellaneous which are used to operation Virtual printer status.

@author: ten
@create_date: July 2, 2020
'''

import paramiko
from MobileApps.resources.const.mac.const import TEST_DATA
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.mac.smart.exceptions.smart_exceptions import UnexpectedValueException


class SshHost:
    def __init__(self, hostip, username=None, key_path=None, port=22):
        if username:
            self.username = username
            self.key_path = key_path
        else:
            self.username = ma_misc.load_json_file(TEST_DATA.MAC_SMART_ACCOUNT)["mac_smart"]["account_os_user"]["username"]  #'itest'
            self.key_path = ma_misc.load_json_file(TEST_DATA.MAC_SMART_APP_INFO)["mac_smart"]["ssh_key_path"]["key_path"] #'/Users/itest/Desktop/sshkey'
        self.port = port
        self.hostip = hostip
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostip, self.port, self.username, key_filename=self.key_path)

    def control_virtual_printer(self, printer_ip, serial_number, code_number=None, method=None):

        if method == 'connect':
            cmd = 'ConnectJetMobileClient.exe -c ' + printer_ip + ' ' + serial_number
        elif method == 'disconnect':
            cmd = 'ConnectJetMobileClient.exe -d ' + printer_ip + ' ' + serial_number
        elif method == 'resume':
            cmd = 'ConnectJetMobileClient.exe -s ' + printer_ip + ' -m Ready' + ' -d ' + serial_number + ' -p B'
        elif method == 'setup':
            cmd = 'ConnectJetMobileClient.exe -s ' + printer_ip + ' -m ' + code_number + ' -d ' + serial_number + ' -p B'
        else:
            raise UnexpectedValueException("need choose type as connect or disconnect or resume or setup")
        stdin, stdout, stderr = self.client.exec_command(r'cd C:\Program Files\HP\ConnectJet Mobile & ' + cmd)

    def close(self):
        self.client.close()

