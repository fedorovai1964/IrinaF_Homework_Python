from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
# главной страницы магазина, который будет содержать методы для добавления
# товаров в корзину и перехода в корзину;
class PageShopMain():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_prodacts(self):
        products = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie"
        ]
        for product in products:
            self.wait.until(EC.presence_of_element_located((
                By.ID, product))).click()

    def go_to_shopping_cart(self):
        shopping_cart = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "shopping_cart_link")))
        shopping_cart.click()
