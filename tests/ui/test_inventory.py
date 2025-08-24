# tests/ui/test_inventory.py
import pytest
import allure
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с инвентарем")
def test_add_item_to_cart(browser):
    from pages.login_page import LoginPage
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    assert "1" in browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с инвентарем")
def test_remove_item_from_cart(browser):
    from pages.login_page import LoginPage
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    inventory_page.add_item_to_cart(1)  # Добавляем второй товар с другим индексом
    browser.find_element(By.CLASS_NAME, "btn_secondary").click()
    assert "1" in browser.find_element(By.CLASS_NAME, "shopping_cart_badge").text


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с инвентарем")
def test_sorting_products(browser):
    from pages.login_page import LoginPage
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.sort_products("za")  # Сортировка от Z до A
    first_item = browser.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert "Test.allTheThings()" in first_item


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с инвентарем")
def test_product_details(browser):
    from pages.login_page import LoginPage
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.open_product_details(0)
    assert "inventory-item.html" in browser.current_url

