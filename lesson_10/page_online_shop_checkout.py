import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCheckout:

    def __init__(self, driver):
        """Конструктор класса PageCheckout для страницы оформления заказа,
            :param driver: Webdriver - объект драйвера Selenium
             который содержит методы для заполнения формы данными
              (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout(self):
        """Метод заполняет форму данными:имя/first-name, фамилия/last-name,
         почтовый индекс/postal-code и нажимает кнопку Continue"""
        with allure.step("Заполнить поле Имя "):
            name_first = self.wait.until(
                EC.presence_of_element_located((By.ID, "first-name")))
            name_first.send_keys("Irina")

        with allure.step("Заполнить поле Фамилия "):
            name_last = self.wait.until(EC.presence_of_element_located((
                By.ID, "last-name")))
            name_last.send_keys("Fedorova")

        with allure.step("Заполнить поле Почтовый индекс "):
            postal_code = self.wait.until(EC.presence_of_element_located((
                By.ID, "postal-code")))
            postal_code.send_keys("940400")

        with allure.step("Нажать кнопку Continue"):
            cont = self.wait.until(EC.presence_of_element_located((
                By.ID, "continue")))
            cont.click()

    def total_price(self):
        """Метод проверки итоговой стоимости"""
        with allure.step("Получить итоговую стоимость"):
            price = self.wait.until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "summary_total_label"))).text
        return price
