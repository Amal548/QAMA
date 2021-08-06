import pytest
from MobileApps.libs.flows.android.jweb_data_collection.flow_container import FlowContainer

@pytest.fixture(scope="session", autouse=True)
def android_jweb_data_collection_setup(request, android_test_setup):
    """
    This fixture is for Android Jweb Data Collection set up :
        - Get driver instance
        - Get FlowContainer instance
    :param request:
    :param android_test_setup:
    :return:
    """
    driver = android_test_setup
    fc = FlowContainer(driver)
    return driver, fc