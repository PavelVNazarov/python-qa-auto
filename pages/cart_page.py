# pages/cart_page.py
import allure
from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверяем наличие товаров в корзине")
    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    @allure.step("Нажимаем кнопку Checkout")
    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        self._make_screenshot("Переход к оформлению заказа")

    def _make_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
