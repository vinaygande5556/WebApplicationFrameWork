import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def start_fixture(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://demostore.supersqa.com/")
    if request.cls is not None:
        request.cls.driver = driver
        driver.maximize_window()
        driver.implicitly_wait(15)
    yield driver
    time.sleep(10)
    driver.quit()

