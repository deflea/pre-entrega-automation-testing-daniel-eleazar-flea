import pytest
from utils.helpers import get_driver
from utils.helpers import login

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture
def login_driver(driver, base_url):
    driver.get(base_url)
    login(driver, "standard_user", "secret_sauce")
    return driver