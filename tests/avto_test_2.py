import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.add_page import Add_page
from pages.login_page import Login_page
from pages.user_page import User_page


def test_smoke():  # тест критического пути авторизация - пользователи - добавить - добавляем
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    login = Login_page(driver)
    login.authorization()

    up = User_page(driver)
    up.open_users()

    ap = Add_page(driver)
    ap.add_new_users()

    driver.close()
