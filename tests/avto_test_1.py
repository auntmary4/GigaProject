import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import Login_page


def test_authorization():  # тестирование формы авторизации
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()
    driver.close()
