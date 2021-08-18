from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
"""This is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).click()

    def send_key(self, by_locator, text):
        #time.sleep(10)
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        time.sleep(5)
        #WebDriverWait(self.driver, 20).until(ec.title_is(title))
        return self.driver.title
