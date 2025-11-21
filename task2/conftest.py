import time

import pytest
from selenium import webdriver



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://avito-tech-internship-psi.vercel.app/')
    yield driver
    driver.quit()

