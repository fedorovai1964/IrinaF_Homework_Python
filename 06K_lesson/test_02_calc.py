import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_02_calculation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    # Откройте страницу: https://bonigarcia.dev/selenium-webdriver-
    # java/slow-calculator.html в Google Chrome.
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # В поле ввода по локатору  delay  введите значение 45.
    delay = wait.until(EC.presence_of_element_located((By.ID, "delay")))
    delay.clear()
    delay.send_keys("45")

    # Нажмите на кнопки: 7 + 8 =
    button_calc = [
        "//span[normalize-space()='7']",
        "//span[normalize-space()='+']",
        "//span[normalize-space()='8']",
        "//span[normalize-space()='=']"
    ]
    for button in button_calc:
        wait.until(EC.presence_of_element_located((By.XPATH, button))).click()

    # Засечь время после нажатия кнопки "="
    start_time = time.time()

    # Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "screen"), str(15)))

    # Засечь время после появления результата
    end_time = time.time()
    time_result = end_time - start_time
    assert 47 >= abs(time_result) >= 45, \
        f"Ожидалась задержка 45 секунд, получено {time_result} секунд"

    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == "15", "Результат не равен 15"

    driver.quit()
