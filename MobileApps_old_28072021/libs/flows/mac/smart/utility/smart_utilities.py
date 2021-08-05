# encoding: utf-8
'''
Description: It defines miscellaneous which are used in the MAC code.

@author: Sophia
@create_date: July 25, 2019
'''

import os
import shutil
import datetime
import json

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.mac.const import TEST_DATA

def delete_all_files(folder_path):
    '''
    This is a method to delete all files in a folder.
    :parameter:
    :return:
    '''
    try:
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
    except OSError as e:
        raise ("Error: %s - %s." % (e.filename, e.strerror))


def kill_browser(browser_name):
    '''
    This is a method to kill browser process.
    :parameter:
    :return:
    '''
    os.system("pkill " + browser_name)


def change_sys_language_region(language_region_value=None):
    '''
    This is a method to change OSX system language and region.
    defaults read NSGlobalDomain AppleLanguages
    :parameter:
    :return:
    '''
    if language_region_value is None:
        os.system('defaults write NSGlobalDomain AppleLanguages "(en-US)"')
        # os.system('defaults write NSGlobalDomain AppleLocale "(en_US)"')
    else:
        os.system('defaults write NSGlobalDomain AppleLanguages "(' + language_region_value + ')"')


def setup_computer_network_status(hardware_port_type, hardware_port_status):
    '''
    This is a method to setup computer WiFi network.
    :parameter:
    :return:
    '''
    os.system("networksetup -setairportpower " + hardware_port_type + hardware_port_status)


def setup_computer_ethernet_network_status(hardware_port_type, hardware_port_status, os_sys_pw):
    '''
    This is a method to setup computer Ethernet network
    :parameter:
    :return:
    '''
    os.system('echo ' + os_sys_pw + ' | sudo -S ifconfig ' + hardware_port_type + hardware_port_status)


def switch_other_network(hardware_port_type, network_name, network_password):
    '''
    This is a method to switch networks
    :parameter:
    :return:
    '''
    os.system("networksetup -setairportnetwork " + hardware_port_type + network_name + " " + network_password)


def delete_pw_from_keychain(printer_key_id, os_sys_pw):
    '''
    This is a method to delete passwords which printer saved in Keychain.
    :parameter:
    :return:
    '''

    os.system('echo ' + os_sys_pw + ' | sudo -S security delete-generic-password -l "HP Smart-HP Printer-' + printer_key_id + '"')


def open_app(filepath):
    '''
    This is a method to open applications
    :parameter:
    :return:
    '''
    os.system('open ' + filepath)


def change_system_time(os_sys_pw, date_time_value=None):
    '''
    This is a method to change current system time to a specific time.
    :parameter:
    :return:
    '''

    if date_time_value is None:
        date_time_value = datetime.datetime.now() + datetime.timedelta(days=2)

    date_str_value = date_time_value.strftime("%m%d%H%M%y")
    os.system('echo ' + os_sys_pw + ' | sudo -S date ' + date_str_value)


def restore_system_time(os_sys_pw):
    '''
    This is a method to restore system time with time.apple.com.
    :parameter:
    :return:
    '''
    os.system('echo ' + os_sys_pw + ' | sudo -S sntp -sS time.asia.apple.com')


# Install hp smart app package
def install_app(package_path, os_sys_pw):
    '''
    This is a method to install HP Smart App.
    :parameter:
    :return:
    '''

    os.system('echo ' + os_sys_pw + ' | sudo -S installer -pkg ' + package_path + ' -target /')


# Uninstall hp smart app package
def uninstall_app(os_sys_pw):
    '''
    This is a method to uninstall HP Smart App.
    :parameter:
    :return:
    '''
    os.system('echo ' + os_sys_pw + ' | sudo -S rm -r -f /Applications/HP\ Smart.app ')


# extract pdsmq data
def process_file_by_line(line):
    data_list = []
    if 'schema' in line:
        data_list=line[line.find('{'):].replace('}{','}\n{').split('\n')
    return data_list


# extract pdsmq data
def get_file_data_to_dict(file_path):
    with open(os.path.expanduser(file_path)) as f:
        data_list = []
        for line in f:
            data_list = data_list + process_file_by_line(line)
    return data_list


def get_local_strings_from_table(screen_name, language_region_value=None):
    '''
    This is a method to get local strings from string table.
    :parameter:
    :return:
    '''
    if language_region_value is None:
        return ma_misc.load_json_file(TEST_DATA.MAC_SMART_LOCAL_STRINGS_INFO)["ENU"][screen_name]
    else:
        return ma_misc.load_json_file(TEST_DATA.MAC_SMART_LOCAL_STRINGS_INFO)[language_region_value][screen_name]


if __name__ == "__main__":
    pass
