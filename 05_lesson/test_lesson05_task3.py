from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()

    # Откройте страницу https://httpbin.org/links/10.
    driver.get("https://httpbin.org/links/10")

    # Найдите все ссылки на странице (тег <a>).
    num_element = driver.find_elements(By.TAG_NAME, "a")
    for i, num_el in enumerate(num_element, 1):
        print(f'Номер элемента {i} ')

    # Проверьте, что количество ссылок равно 9.
    assert len(num_element) == 9

    # Проверьте, что текст первой ссылки содержит "1".
    first_element = num_element[0].text
    assert first_element == "1"
    driver.quit()
