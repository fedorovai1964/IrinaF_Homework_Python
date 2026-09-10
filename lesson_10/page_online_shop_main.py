import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
#
class PageShopMain:
    def __init__(self, driver):
        """Конструктор класса PageShopMain для главной страницы магазина,
        который будет содержать методы для добавления товаров в корзину
        и перехода в корзину;
        :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]

    def add_product_backpack(self):
        """Метод добавления продукта backpack в корзину"""
        with allure.step(f"Добавить продукт {self.products[0][23:]}"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.ID, self.products[0]))).click()

    def add_product_bolt_t_shirt(self):
        """Метод добавления продукта bolt_t_shirt в корзину"""
        with allure.step(f"Добавить продукт {self.products[1][23:]}"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.ID, self.products[1]))).click()

    def add_product_onesie(self):
        """Метод добавления продукта onesie в корзину"""
        with allure.step(f"Добавить продукт {self.products[2][23:]}"):
            self.wait.until(
                EC.presence_of_element_located((
                    By.ID, self.products[2]))).click()

    @allure.step("Нажать на кнопку перехода в корзину")
    def go_to_shopping_cart(self):
        """Метод для нажатия на кнопку перехода в корзину"""
        shopping_cart = self.wait.until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "shopping_cart_link"))
        )
        shopping_cart.click()
