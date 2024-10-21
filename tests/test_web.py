import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def driver():

    options= ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://chrome:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()   

def test_web_title(driver):
    driver.get("http://web")
    assert "Hello from the web service!" in driver.page_source