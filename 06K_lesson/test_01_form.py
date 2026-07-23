from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-java
    # /data-types.html в Edge или Safari.
    (driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))
    driver.maximize_window()

    # Заполните форму значениями:
    field_values = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for key, value in field_values.items():
        field = wait.until(EC.presence_of_element_located((By.NAME, key)))
        field.clear()
        field.send_keys(value)

    # Нажмите кнопку Submit.
    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "btn-outline-primary")))
    submit_button.click()

    # Проверьте (assert), что поле  Zip code  подсвечено красным.
    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    zip_class = zip_code.get_attribute("class") or ""
    assert "alert-danger" in zip_class, \
        "Поле zip code не подсвечено красным (нет класса 'alert-danger')"

    # Проверьте (assert), что остальные поля подсвечены зеленым.
    other_fields = [key for key in field_values if key != "zip-code"]
    for key in other_fields:
        field = driver.find_element(By.ID, key)
        field_class = field.get_attribute("class") or ""
        assert "alert-success" in field_class, \
            f"Поле '{key}' не подсвечено зеленым (нет класса 'alert-success')"

    driver.quit()
