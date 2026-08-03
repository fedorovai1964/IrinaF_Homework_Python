import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Создать класс для страницы калькулятора, который будет содержать
# методы для взаимодействия с элементами:


class PageCalc():
    def __init__(self, driver):
        self.driver = driver
        self.url = ("https://bonigarcia.dev/"
                    "selenium-webdriver-java/slow-calculator.html")
        self.wait = WebDriverWait(driver, 50)

    # Метод открытия страницы калькулятора
    def open(self):
        self.driver.get(self.url)

    # Метод для поля ввода задержки (локатор #delay).
    def field_delay(self):
        delay = self.wait.until(
            EC.presence_of_element_located((By.ID, "delay")))
        delay.clear()
        delay.send_keys("45")

    # Метод для ввода на калькуляторе (цифры, операторы, кнопка =).
    def button_calc(self):
        button_calc = [
            "//span[normalize-space()='7']",
            "//span[normalize-space()='+']",
            "//span[normalize-space()='8']",
            "//span[normalize-space()='=']"
        ]
        for button in button_calc:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, button))).click()

    # Методы проверки,  что в окне отобразится результат 15 через 45 секунд.

    def wait_for_result(self):
        start = time.time()
        self.wait.until(EC.text_to_be_present_in_element((
            By.CLASS_NAME, "screen"), str(15)))
        return time.time() - start

    def get_result_text(self):
        return self.driver.find_element(By.CLASS_NAME, "screen").text
