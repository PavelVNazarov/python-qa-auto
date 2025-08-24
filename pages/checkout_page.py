# pages/checkout_page.py
import allure
from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполняем информацию для оформления заказа")
    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self._make_screenshot("Информация заполнена")

    @allure.step("Завершаем оформление заказа")
    def finish_checkout(self):
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()
        self._make_screenshot("Заказ завершен")

    def _make_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

