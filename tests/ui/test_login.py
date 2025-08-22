# tests/ui/test_login.py
import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import allure

@pytest.mark.ui
@allure.feature("UI")
@allure.story("Авторизация")
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    with allure.step("Проверяем, что авторизация прошла успешно"):
        assert "inventory.html" in browser.current_url
        allure.attach(browser.get_screenshot_as_png(), "Финальный скриншот - главная страница", attachment_type=allure.attachment_type.PNG)


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Авторизация")
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("locked_out_user", "wrong_pass")
    with allure.step("Проверяем сообщение об ошибке"):
        error = login_page.driver.find_element(By.CSS_SELECTOR, "h3").text
        assert "Epic sadface" in error
        allure.attach(browser.get_screenshot_as_png(), "Сообщение об ошибке", attachment_type=allure.attachment_type.PNG)