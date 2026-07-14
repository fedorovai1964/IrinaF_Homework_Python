from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    # Откройте страницу https://httpbin.org/forms/post.
    driver.get("https://httpbin.org/forms/post")
    sleep(5)

    # Найдите поле ввода с названием custname.
    # Введите в него ваше имя.
    driver.find_element(By.NAME, "custname").send_keys('Irina')
    sleep(5)

    # Найдите кнопку Submit и нажмите на нее.
    driver.find_element(By.XPATH,
                        "//button[normalize-space()='Submit order']").click()
    # Проверьте, что после нажатия URL изменился.
    assert driver.current_url != "https://httpbin.org/forms/post"
    driver.quit()
