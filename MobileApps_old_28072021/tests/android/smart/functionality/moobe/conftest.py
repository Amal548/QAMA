"""
This conftest is used for MOOBE test only
"""
import pytest


@pytest.fixture(scope="class", autouse=True)
def clean_up_oobe_printer(request):
    def cleanup():
        p = request.cls.p
        if p.is_oobe_mode():
            p.exit_oobe()
            
    request.addfinalizer(cleanup)

@pytest.fixture(scope="function", autouse=True)
def set_printer_to_oobe(request):
    p = request.cls.p
        
    # Set printer to OOBE mode
    # full_oobe = True if "taccola" in p.projectName else False
    p.printer_setup_for_moobe(reset_cloud=True, ignore_usb=True, full_oobe=True)
    p.send_secure_cfg(request.config.getoption("--stack"))