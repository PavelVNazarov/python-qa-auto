# tests/ui/test_checkout.py
import pytest
import allure


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Оформление заказа")
def test_complete_checkout(browser):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.fill_info("John", "Doe", "12345")
    checkout_page.finish_checkout()

    assert "complete" in browser.current_url


@pytest.mark.ui
@allure.feature("UI")
@allure.story("Оформление заказа")
def test_checkout_without_info(browser):
    from pages.login_page import LoginPage
    from pages.inventory_page import InventoryPage
    from pages.cart_page import CartPage
    from pages.checkout_page import CheckoutPage

    login_page = LoginPage(browser)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_item_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(browser)
    cart_page.checkout()

    checkout_page = CheckoutPage(browser)
    checkout_page.finish_checkout()  # Пропускаем заполнение информации

    assert "error" in browser.current_url

