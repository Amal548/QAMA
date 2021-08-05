import pytest
from MobileApps.resources.const.ios.const import *

@pytest.fixture(scope="function", autouse="true")
def reset_app_and_printer(request):
    request.cls.p.printer_setup_for_moobe(reset_cloud=True, ignore_usb=True)
    request.cls.p.send_secure_cfg(request.cls.stack)
    request.cls.driver.reset(BUNDLE_ID.SMART)

    def function_cleanup():
        # request.cls.ows_fc.clean_up_printer(request.cls.ssid, request.cls.password)
        if request.cls.p.is_oobe_mode():
            request.cls.p.exit_oobe()
        request.cls.p.connect_to_wifi(request.cls.ssid, request.cls.password)
    request.addfinalizer(function_cleanup)