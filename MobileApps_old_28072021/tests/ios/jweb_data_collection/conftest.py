import pytest
from MobileApps.libs.flows.ios.jweb_data_collection.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def ios_jweb_data_collection_setup(request, session_setup):
    """
    This fixture is for Ios Data Collection set up :
        - Get driver instance
        - Get FlowContainer instance
        - Install latest Ios Data Collection app
    """
    driver = session_setup
    fc = FlowContainer(driver)
    return driver, fc