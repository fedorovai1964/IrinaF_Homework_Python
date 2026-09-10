import allure
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageCalc:
    def __init__(self, driver):
        """Конструктор класса PageCalc.
            :param driver: Webdriver - объект драйвера Selenium
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/slow-calculator.html"
        )
        self.wait = WebDriverWait(driver, 50)
        self.button_calc = [
            "//span[normalize-space()='7']",
            "//span[normalize-space()='+']",
            "//span[normalize-space()='8']",
            "//span[normalize-space()='=']",
        ]
        self.delay = "45"

    def open(self):
        """Метод открывает страницу калькулятора"""
        with allure.step(f"Открыть страницу калькулятора {self.url}"):
            self.driver.get(self.url)

    def field_delay(self):
        """Метод устанавливает время задержки delay = 45 секунд
        для выполнения операций на калькуляторе"""
        with allure.step(f"Ввести задержку delay = {self.delay} секунд "):
            delay = self.wait.until(
                EC.presence_of_element_located((By.ID, "delay")))
        delay.clear()
        delay.send_keys(self.delay)

    @allure.step("Нажать на кнопку '7' калькулятора")
    def button_calc_seven(self):
        """Метод для ввода на калькуляторе цифры 7"""
        button_seven = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.button_calc[0]))
        )
        button_seven.click()

    @allure.step("Нажать на кнопку '+' калькулятора")
    def button_calc_plus(self):
        """Метод для ввода на калькуляторе знака '+'"""
        button_plus = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.button_calc[1]))
        )
        button_plus.click()

    @allure.step("Нажать на кнопку '8' калькулятора")
    def button_calc_eight(self):
        """Метод для ввода на калькуляторе цифры 8"""
        button_eight = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.button_calc[2]))
        )
        button_eight.click()

    @allure.step("Нажать на кнопку '=' калькулятора")
    def button_calc_equals(self):
        """Метод для ввода на калькуляторе знака '='"""
        button_equals = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.button_calc[3]))
        )
        button_equals.click()

    @allure.step("Проверка результата и вычисление времени задержки")
    def wait_for_result(self):

        """ Метод проверки отображения на экране калькулятора
            результата - str(15), вычисление времени задержки
            :return: float (время в секундах) =
            time.time()(время ПОСЛЕ)-start(время ДО)
        """

        start = time.time()
        with allure.step(f"Время до выполнения вычислений = {start} "):
            self.wait.until(EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), str(15)))

        finish = time.time()
        with allure.step(f"Время после выполнения вычислений = {finish} "):
            result = finish - start
        with allure.step(f"Вычисление задержки {result} секунд"):
            return (result)

    def get_result_text(self):
        """
        Возвращает результат в экрана калькулятора
        :return: str - текст результата на экране калькулятора.
        """
        result = self.driver.find_element(By.CLASS_NAME, "screen").text
        with allure.step(
                f"Получение результата с экрана калькулятора {result}"):
            return result
