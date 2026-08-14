from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Создать класс:
# страницы оформления заказа, который будет содержать методы для заполнения
# формы данными (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.
class PageCheckout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Заполните форму своими данными:имя/first-name,
    # фамилия/last-name, почтовый индекс/postal-code
    def fill_checkout(self):
        name_first = self.wait.until(EC.presence_of_element_located(
            (By.ID, "first-name")))
        name_first.send_keys("Irina")
        name_last = self.wait.until(EC.presence_of_element_located((
            By.ID, "last-name")))
        name_last.send_keys("Fedorova")
        postal_code = self.wait.until(EC.presence_of_element_located(
            (By.ID, "postal-code")))
        postal_code.send_keys("940400")
        # Нажмите кнопку Continue.
        cont = self.wait.until(EC.presence_of_element_located((
            By.ID, "continue")))
        cont.click()

    # Проверка итоговой стоимости
    def total_price(self):
        price = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label"))).text
        return price
