import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
# а;
class PageShopLogin:
    def __init__(self, driver):
        """Конструктор класса PageShopLogin для страницы авторизации,
         который содержит методы для ввода логина и пароля,
         а также для нажатия кнопки вход
        :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username = "standard_user"
        self.password = "secret_sauce"

    #
    def open(self):
        """Метод для открытия сайта магазина: https://www.saucedemo.com/"""
        self.driver.get("https://www.saucedemo.com/")

    #
    def login(self):
        """Метод для авторизации пользователя:
        standard_user с паролем secret_sauce"""
        with allure.step(
                f"Ввести имя пользователя в поле Username = {self.username}"):
            username = self.wait.until(
                EC.presence_of_element_located((By.ID, "user-name")))
            username.send_keys(self.username)
        with allure.step(
                f"Ввести пароль в поле Password = {self.password}"):
            password = self.wait.until(
                EC.presence_of_element_located((By.ID, "password")))
            password.send_keys(self.password)
        with allure.step("Нажать кнопку Login"):
            self.wait.until(EC.presence_of_element_located((
                By.ID, "login-button"))).click()
