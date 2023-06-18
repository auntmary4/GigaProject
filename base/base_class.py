from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method get assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word
