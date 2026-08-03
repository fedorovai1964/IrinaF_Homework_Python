from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
# для страницы авторизации, который будет содержать методы для ввода логина
# и пароля, а также для нажатия кнопки входа;
class PageShopLogin():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Метод для открытия сайта магазина: https://www.saucedemo.com/
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    # Метод для авторизации пользователя: standard_user с паролем secret_sauce
    def login(self):
        username = self.wait.until(EC.presence_of_element_located(
            (By.ID, "user-name")))
        username.send_keys("standard_user")

        password = self.wait.until(EC.presence_of_element_located(
            (By.ID, "password")))
        password.send_keys("secret_sauce")

        self.wait.until(EC.presence_of_element_located(
            (By.ID, "login-button"))).click()
