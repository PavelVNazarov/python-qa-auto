# pages/inventory_page.py
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавляем товар в корзину")
    def add_item_to_cart(self, index=0):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        items[index].find_element(By.CLASS_NAME, "btn_inventory").click()
        self._make_screenshot("Товар добавлен в корзину")

    @allure.step("Сортируем товары")
    def sort_products(self, value):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value(value)
        self._make_screenshot(f"Сортировка товаров по: {value}")

    @allure.step("Открываем детали товара")
    def open_product_details(self, index=0):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        items[index].click()
        self._make_screenshot("Детали товара")

    @allure.step("Переходим в корзину")
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self._make_screenshot("Переход в корзину")

    def _make_screenshot(self, name):
        """Вспомогательный метод для прикрепления скриншота в Allure"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )