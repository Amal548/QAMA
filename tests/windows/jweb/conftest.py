import pytest
from MobileApps.libs.flows.windows.jweb.flow_container import FlowContainer
from MobileApps.libs.flows.windows.jweb.utility import jweb_utilities
from MobileApps.libs.app_package.app_class_factory import app_module_factory

def pytest_addoption(parser):
    windows_argument_group = parser.getgroup('Jweb Test Parameters')
    windows_argument_group.addoption("--win-app-version", action="store", default=None, help="Which app-version to use")
    windows_argument_group.addoption("--client-ip", action="store", default=None, help="IP address of the target pc")

@pytest.fixture(scope="session")
def install_windows_app(request):

    #Fixture only for windows app installation.
    # app install should be done before create driver
    app_version = request.config.getoption("--win-app-version")
    client_ip = request.config.getoption("--client-ip")
    app_obj = app_module_factory(pytest.platform, pytest.app_info)
    jweb_utilities.install_app(url=app_obj.get_build_url(app_version=app_version), node_ip=client_ip)

@pytest.fixture(scope="session", autouse=True)
def windows_jweb_setup(request, install_windows_app, windows_test_setup):
    """
    This fixture is for windows Jarvis Web set up :
        - Get driver instance
    :param windows_test_setup:
    :return:
    """

    driver = windows_test_setup
    fc = FlowContainer(driver)
    return driver, fc