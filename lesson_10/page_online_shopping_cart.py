import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
#
class PageOnlineShoppingCart:
    def __init__(self, driver):
        """Конструктор класса PageOnlineShoppingCart для страницы корзины,
        который содержит метод для нажатия кнопки Checkout
        :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        """Метод для нажатия кнопки Checkout"""
        self.wait.until(
            EC.presence_of_element_located((By.ID, "checkout"))).click()
