import pytest
from selenium.webdriver.common.by import By  # <-- ЭТОТ ИМПОРТ БЫЛ НУЖЕН
from pages.login_page import LoginPage


@pytest.mark.ui
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url


@pytest.mark.ui
def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("locked_out_user", "wrong_pass")
    error = login_page.driver.find_element(By.CSS_SELECTOR, "h3").text
    assert "Epic sadface" in error