from selenium.common import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.by import By


class Elements:
    def __init__(self, driver, select_by, selector):
        self.driver = driver

    

