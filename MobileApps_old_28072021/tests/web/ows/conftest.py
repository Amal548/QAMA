import pytest
import random
import string
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.libs.ma_misc.conftest_misc as c_misc

from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.resources.const.web.const import TEST_DATA
from MobileApps.libs.flows.web.ows.ucde_privacy import UCDEPrivacy
from MobileApps.libs.flows.web.ows.ows_emulator import OWSEmulator
from MobileApps.libs.flows.web.ows.ows_printer import OWSEmuPrinter
from MobileApps.libs.flows.web.ows.ows_fc_factory import ows_fc_factory
from MobileApps.libs.flows.web.ows.sub_flow.connected_printing_services import ConnectedPrintingServices

def pytest_addoption(parser):
    web_argument_group = parser.getgroup('OWS Test Parameters')
    web_argument_group.addoption("--emu-printer", action="store", default="palermo", help="Choose which emulated printer to run against")
    web_argument_group.addoption("--emu-platform", action="store", default=None, help="Choose which platfrom to emulate")
    web_argument_group.addoption("--emu-error", action="store", default=None, help="Choose an error state (currently this is used for both calibration and ink step)")

    yeti_argument_group = parser.getgroup("OWS YETI Test Parameters")
    yeti_argument_group.addoption("--printer-profile", action="store", default="skyreach", help="Choose which emulated printer to run against")
    yeti_argument_group.addoption("--printer-biz-model", action="store", default="E2E", help="Choose which emulated printer to run against")

@pytest.fixture(scope="class")
def ows_test_setup(web_session_setup, request):
    driver = web_session_setup
    driver.set_size("max")
    driver.set_global_cms_sys_arg(["--emu-printer","--emu-platform"])
    stack = request.config.getoption("--stack")
    account = ma_misc.get_hpid_account_info(stack, a_type="basic", claimable=False)
    hpid_username = account["email"]
    hpid_pwd = account["password"]
    try:
        ows_emulator = OWSEmulator(driver)
        emu_printer = request.config.getoption("--emu-printer")
        emu_platform = request.config.getoption("--emu-platform")
        driver.navigate(ows_emulator.emulator_url[stack])
        ows_emulator.verify_emulator_load()
        ows_emulator.select_dev_menu_list_item()
        ows_emulator.click_hpid_login_button()
        hpid = HPID(driver)
        hpid.verify_hp_id_sign_up(timeout=20)
        hpid.handle_privacy_popup()
        hpid.click_sign_in_link_from_create_account()
        hpid.login(hpid_username, hpid_pwd)
        ows_emulator.verify_emulator_load()
        ows_emulator.dismiss_banner()
        liveui_version, ows_status = ows_emulator.launch_flow_by_printer(emu_printer, emu_platform)
        driver.add_window("OWSEmuPrinter")
        ows_printer = OWSEmuPrinter(emu_printer, driver, liveui_version, ows_status, window_name="OWSEmuPrinter")
        ows_printer.verify_page_load()
        fc = ows_fc_factory(driver, ows_printer)
        connected_printing_services = ConnectedPrintingServices(driver)
        connected_printing_services.verify_connected_printing_services()
        connected_printing_services.click_connected_printing_services()
        
    except:
        attachment_root_path = c_misc.get_attachment_folder()
        for window, _ in driver.session_data["window_table"].items():
            driver.switch_window(window)
            c_misc.save_source_and_publish(driver, attachment_root_path, file_name="page_source_{}.txt".format(window))
            c_misc.save_screenshot_and_publish(driver,
                                            "{}/screenshot_{}_{}.png".format(attachment_root_path, request.node.name, window))
        raise

    return (driver, emu_platform, ows_printer, fc)