import time

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Add_page(Base):  # Окно создание пользователя


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    email = "//input[@id='dataEmail']"
    add_password = "//input[@id='dataPassword']"
    name = "//input[@id='dataName']"
    select11 = "//input[@id='dataSelect11']"
    select12 = "//input[@id='dataSelect12']"
    select21 = "//input[@id='dataSelect21']"
    select22 = "//input[@id='dataSelect22']"
    select23 = "//input[@id='dataSelect23']"
    button_add = "//button[@id='dataSend']"
    add_page_tag = "//div[@class='uk-modal-body']"
    button_ok = "//button[@class='uk-button uk-button-primary uk-modal-close']"


    # Getters

    def get_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_add_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.add_password)))

    def get_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_select11(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select11)))

    def get_select12(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select12)))

    def get_select21(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select21)))

    def get_select22(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select22)))

    def get_select23(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.select23)))

    def get_button_add(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_add)))

    def get_add_page_tag(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, self.add_page_tag)))

    def get_button_ok(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.button_ok)))

    # Actions

    def input_email(self, u_email):
        self.get_email().send_keys(u_email)

    def input_add_password(self, u_password):
        self.get_add_password().send_keys(u_password)

    def input_name(self, name):
        self.get_name().send_keys(name)

    def click_select11(self):
        self.get_select11().click()

    def click_select12(self):
        self.get_select12().click()

    def click_select21(self):
        self.get_select21().click()

    def click_select22(self):
        self.get_select22().click()

    def click_select23(self):
        self.get_select23().click()

    def click_button_add(self):
        self.get_button_add().click()

    def click_button_ok(self):
        self.get_button_ok().click()

    # Methods

    def add_new_users(self):
        self.input_email("zxc@zxc.com")
        self.input_add_password('zxc')
        self.input_name('zxc')
        self.click_select22()
        self.click_button_add()
        self.click_button_ok()