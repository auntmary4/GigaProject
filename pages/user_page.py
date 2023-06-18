import time

from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class User_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    menu_more = "//a[@id='menuMore']"
    users = "//a[@id='menuUsersOpener']"
    add_users = "//a[@id='addUser']"

    # Getters

    def get_menu_more(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.menu_more)))

    def get_users(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.users)))

    def get_add_users(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.add_users)))

    # Actions

    def click_menu_more(self):
        self.get_menu_more().click()

    def click_users(self):
        self.get_users().click()

    def click_add_users(self):
        self.get_add_users().click()

    # Methods

    def open_users(self):
        self.click_menu_more()
        self.click_users()
        self.click_users()
        self.click_add_users()