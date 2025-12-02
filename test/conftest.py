import pytest
from utils.helpers import get_driver

@pytest.fixture
def driver():
    #Consultar Selenium  WebDriver
    driver = get_driver()
    yield driver
    driver.quit()


