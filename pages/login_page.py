# pages/login_page.py
from selenium.webdriver.common.by import By
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу Saucedemo")
    def open(self):
        self.driver.get("https://www.saucedemo.com")
        self._make_screenshot("Открыта страница входа")

    @allure.step("Вводим логин: {username}")
    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)
        self._make_screenshot(f"Введён логин: {username}")

    @allure.step("Вводим пароль")
    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        self._make_screenshot("Введён пароль")

    @allure.step("Нажимаем кнопку Вход")
    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        self._make_screenshot("Клик по кнопке Вход")

    @allure.step("Выполняем логин: {username} / {password}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def _make_screenshot(self, name):
        """Вспомогательный метод для прикрепления скриншота в Allure"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )