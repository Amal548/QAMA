from SAF.misc.ssh_utils import SSH
from SAF.misc.saf_misc import *
from SAF.misc.package_utils import *
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import *

# install jweb app
def install_app(url, node_ip, save_path='/tmp/temp_package', username='exec'):
    '''
    This is a method to install JWEB app.
    :parameter:
    :return:
    '''
    unique_file_path = download_file(url, save_path=save_path)
    client = SSH(node_ip, look_for_keys=True, username=username)
    client.send_file(unique_file_path, '/Users/'+username+'/Downloads/jarvis.zip')
    client.send_command('unzip -qq -o /Users/'+username+'/Downloads/jarvis.zip -d /Applications/')
    client.send_command('rm -r /Users/'+username+'/Downloads/jarvis.zip')

# Uninstall jweb app
def uninstall_app(node_ip, username='exec'):
    '''
    This is a method to uninstall JWEB app.
    :parameter:
    :return:
    '''
    client = SSH(node_ip, look_for_keys=True, username=username)
    client.send_command('rm -r /Applications/HP.Jarvis.WebView.Reference.app', raise_e=False)
    sleep(5)

def install_certificate(node_ip, username='exec'):
    client = SSH(node_ip, look_for_keys=True, username=username)
    client.send_file(ma_misc.get_abs_path(TEST_DATA.JWEB_CERT), '/Users/' + username + '/Downloads/authz.cer')
    client.send_command('sudo -S security delete-certificate -c pie.authz.wpp.api.hp.com', raise_e=False)
    sleep(5)
    client.send_command(
        ' sudo -S security add-trusted-cert -d -r trustAsRoot -k /Library/Keychains/System.keychain /Users/' + username + '/Downloads/authz.cer')
    sleep(5)
    client.send_command('rm -r /Users/' + username + '/Downloads/authz.cer', raise_e=False)

def delete_local_build(file_path='/tmp/temp_package/jarvis.zip'):
    '''
    This is a method to delete downloaded zip file
    :parameter:
    :return:
    '''
    os.remove(file_path)

if __name__ == "__main__":
    pass
