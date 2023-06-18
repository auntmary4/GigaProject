import time

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page(Base):

    url = "http://185.67.95.60/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    user_login = '//input[@id="loginEmail"]'
    password = '//input[@id="loginPassword"]'
    login_button = '//button[@id="authButton"]'
    main_page = "h3"
    menu_auth = "//a[@id='menuAuth']"

    # Getters

    def get_user_login(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))

    def get_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_mane_page(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, self.main_page)))

    def get_menu_auth(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.menu_auth)))

    # Actions

    def input_user_login(self, u_login):
        self.get_user_login().send_keys(u_login)

    def input_password(self, u_password):
        self.get_password().send_keys(u_password)

    def click_login_button(self):
        self.get_login_button().click()

    def click_menu_auth(self):
        self.get_menu_auth().click()

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.input_user_login('student@protei.ru')
        self.input_password('student')
        self.click_login_button()
        #  main_title = WebDriverWait(self.driver, 5).until(
        #    EC.presence_of_element_located((By.TAG_NAME, self.main_page)))
        self.assert_word(self.get_mane_page(), 'Добро пожаловать!')

    def new_authorization(self):
        self.click_menu_auth()
        self.input_user_login('zxc@zxc.com')
        self.input_password('zxc')
        self.click_login_button()
        self.assert_word(self.get_mane_page(), 'Добро пожаловать!')