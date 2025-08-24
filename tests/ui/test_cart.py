# tests/ui/test_cart.py
import pytest
import allure
from selenium.webdriver.common.by import By


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с корзиной")
def test_cart_contents(browser):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    assert len(cart_page.get_cart_items()) == 1


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Работа с корзиной")
def test_checkout_flow(browser):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()
    assert "checkout-step-one" in browser.current_url

