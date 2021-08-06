from abc import ABCMeta
from SAF.misc.ssh_utils import SSH
from MobileApps.libs.flows.base_flow import BaseFlow


class MACFlow(BaseFlow):
    __metaclass__ = ABCMeta
    system = "mac"

    def __init__(self, driver):
        super(MACFlow, self).__init__(driver)
        # self.load_mac_system_ui()

    def load_mac_system_ui(self):
        ui_map = self.load_ui_map(
            system="MAC", project="system", flow_name="system_ui", folder_name=None)
        self.driver.load_ui_map("system", "system_ui", ui_map)
        return True

    def install_certificiate(self, target_address, target_usrname, target_file_path):
        #NOTE this requires visudo to be configured to not need password for sudo commands
        ssh = SSH(target_address, target_usrname)
        ssh.send_command("sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain {}".format(target_file_path))
        return True

    def open_application(self, target_address, target_usrname, target_file_path):
        #NOTE this is to open the mac application through the open command 
        #NOTE this requires visudo to be configured to not need password for sudo commands
        ssh = SSH(target_address, target_usrname)
        #Ignore 
        ssh.send_command("open " + target_file_path)
        return True