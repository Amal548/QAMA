from SAF.misc.ssh_utils import SSH
from SAF.misc.saf_misc import *
from SAF.misc.package_utils import *

# install jweb app
def install_app(url, node_ip, save_path='/tmp/temp_package', username='exec'):
    '''
    This is a method to install JWEB app.
    :parameter:
    :return:
    '''
    app_version = url.split("/")[-2]
    unique_file_path = download_file(url, save_path=save_path)
    client = SSH(node_ip, look_for_keys=True, username=username)
    sleep(5)
    pwd = client.send_command('(Resolve-Path .\).Path').split(':\n')[2].split('\r')[0]
    client.send_file(unique_file_path, pwd+'\\Downloads\\jarvis.zip')
    sleep(5)
    client.send_command('powershell tar -xf '+pwd+'\\Downloads\\jarvis.zip -C '+pwd+'\\Downloads')
    sleep(5)
    client.send_command('powershell '+pwd+'\\Downloads\\HP.Jarvis.Webview.Reference.UWP_' + app_version + '_TEST\\Install.ps1 -Force true', timeout=30, raise_e=False)
    sleep(5)
    client.send_command('powershell rm '+pwd+'\\Downloads\\jarvis.zip')
    client.send_command('powershell rm -r '+pwd+'\\Downloads\\HP.Jarvis.Webview.Reference.UWP_*')

# Uninstall jweb app
def uninstall_app(node_ip, username='exec'):
    '''
    This is a method to uninstall JWEB app.
    :parameter:
    :return:
    '''
    client = SSH(node_ip, look_for_keys=True, username=username)
    client.send_command('powershell "Get-AppxPackage 1132d5c8-e05c-4b46-87cd-e31dad772e89 | Remove-AppxPackage" ', raise_e=False)
    sleep(5)

def delete_local_build(file_path='/tmp/temp_package/jarvis.zip'):
    '''
    This is a method to delete downloaded zip file
    :parameter:
    :return:
    '''
    os.remove(file_path)



if __name__ == "__main__":
    pass
