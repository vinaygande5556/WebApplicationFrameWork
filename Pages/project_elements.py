from selenium.common import InvalidSelectorException, NoSuchElementException
from selenium.webdriver.common.by import By


class Elements:
    def __init__(self, driver):
        self.driver = driver

    def select_by_element(self, select_by):
        dict_path = {"xpath": By.XPATH,
                     "id": By.ID,
                     "class_name": By.CLASS_NAME,
                     "name": By.NAME
                     }
        return dict_path[select_by]

    def click(self, select_by, locator):
        return self.driver.find_element(self.select_by_element(select_by), locator).click()

    def send_text(self, select_by, locator, text=None):
        self.driver.find_element(self.select_by_element(select_by), locator).send_keys(text)
        return self

    def get_text(self, select_by, locator):
        return self.driver.find_element(self.select_by_element(select_by), locator).text

