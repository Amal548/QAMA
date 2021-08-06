import pytest
from MobileApps.libs.flows.mac.jweb.flow_container import FlowContainer
from MobileApps.libs.flows.mac.jweb.utility import jweb_utilities
from MobileApps.libs.app_package.app_class_factory import app_module_factory

def pytest_addoption(parser):
    mac_argument_group = parser.getgroup('Jweb Test Parameters')
    mac_argument_group.addoption("--mac-app-version", action="store", default=None, help="Which app-version to use. NOTE: Setting this option overrides the test fixture marker")
    mac_argument_group.addoption("--client-ip", action="store", default=exec, help="Ip address of the client machine")


@pytest.fixture(scope="session")
def install_mac_app(request):

    #Fixture only for mac app installation.
    # app install should be done before create driver
    app_version = request.config.getoption("--mac-app-version")
    client_ip = request.config.getoption("--client-ip")
    app_obj = app_module_factory(pytest.platform, pytest.app_info)
    jweb_utilities.install_app(url=app_obj.get_build_url(app_version=app_version), node_ip=client_ip, username='exec')
    jweb_utilities.install_certificate(node_ip=client_ip, username='exec')

@pytest.fixture(scope="session", autouse=True)
def mac_jweb_setup(install_mac_app, mac_test_setup):
    """
    This fixture is for Mac Jarvis Web set up :
        - Get driver instance
    :param mac_test_setup:
    :return:
    """
    driver = mac_test_setup
    fc = FlowContainer(driver)
    return driver, fc