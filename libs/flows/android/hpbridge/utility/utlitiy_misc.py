from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA
import random
import pytest


def load_stack_info():
    stacks = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPBRIDGE_TEST_STACK))
    if hasattr(pytest, "test_stack"):
        target_stack = pytest.test_stack
    else:
        target_stack = stacks["default_stack"]
    for stack in stacks["stacks"]:
        if stack["stack"] == target_stack:
            return stack

    raise KeyError("Failed to find stack for: %s " % target_stack)


def load_user_device():
    """
    This method used to load the test device and user info before AMS function integrated.
    :return:
    """
    devices = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPBRIDGE_TEST_DEVICE))
    accounts = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPBRIDGE_TEST_ACCOUNT))

    if hasattr(pytest, "test_mobile"):
        target_mobile = pytest.test_mobile
    else:
        target_mobile = devices["default_device"]

    for device in devices["devices"]:
        if device["device_name"] == target_mobile:
            test_device = device
            break
    if test_device is None:
        raise KeyError("Cannot find device for device name: %s" % devices["default_device"])

    for account in accounts["users"]:
        if account["nickname"] == test_device["wechat_user"]:
            test_user = account
            break
    if test_user is None:
        raise KeyError("Cannot find wechat user for user name: %s" % test_device["wechat_user"])

    return test_user, test_device


def load_printer(printer_name=None, stack=None, printer_type="Gen 1", status="normal", random_pick=False, api_used=False):
    """
    This method used to load the test printers which used for some special case, eg: using API to bind printer,
    then we need some device info in the HP bridge DB
    :param printer_name: the printer's name which to use
    :param stack: indicate the printer's stack
    :param printer_type: indicate the printer's type
    :param status: indicate the printer's status, if None, choose a printer which status should not be reset,
    offline and so on
    :param random_pick: if true. random to select a matchable printer, else, using the printer name or using default to select
    :param api_used: if true, default printer should be a printer with no index
    :return:
    """
    printer_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.HPBRIDGE_TEST_PRINTER))
    if not stack:
        stack = load_stack_info()["stack"]
    if not printer_name and not random_pick:
        target_printer = printer_info[stack]["api_default"] if api_used else printer_info[stack]["ui_default"]
    else:
        target_printer = printer_name
    printers = []
    for printer in printer_info[stack]["printers"]:
        if printer["model"] == target_printer:
            return printer
        else:
            if target_printer:
                continue
            elif printer["type"] == printer_type and printer["status"] == status:
                printers.append(printer)

    if len(printers) != 0:
        index = random.randrange(0, len(printers))
        return printers[index]
    else:
        raise KeyError("Cannot find match printer in the json file with printer name: " + target_printer +
                       " stack: " + stack + " , status: " + status)


def get_reset_printer(stack=None):
    """
    This method used to load a reset printer from the printer.json file, only gen 1 printer has the reset status
    :param stack: the printer's stack
    :return:
    """
    return load_printer(stack, status="reset", printer_type="Gen 1", random_pick=True)


def get_offline_printer(stack=None, printer_type="Gen 2"):
    """
    This method used to load a offline printer from the printer.json file
    :param stack:  the printer's stack
    :param printer_type: indicate the printer's type
    :return:
    """
    return load_printer(stack, status="reset", printer_type=printer_type, random_pick=True)

