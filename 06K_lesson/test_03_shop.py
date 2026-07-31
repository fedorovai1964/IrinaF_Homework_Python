from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    # Откройте сайт магазина: https://www.saucedemo.com/ в FireFox
    driver.get("https://www.saucedemo.com/")

    # Авторизуйтесь как пользователь standard_user
    username = wait.until(EC.presence_of_element_located(
        (By.ID, "user-name")))
    username.send_keys("standard_user")

    # Ввести пароль secret_sauce
    password = wait.until(EC.presence_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")

    # Нажать кнопку Login
    wait.until(EC.presence_of_element_located(
        (By.ID, "login-button"))).click()

    # Добавьте в корзину товары:
    # Sauce Labs Backpack.(add-to-cart-sauce-labs-backpack)
    # Sauce Labs Bolt T-Shirt.(add-to-cart-sauce-labs-bolt-t-shirt)
    # Sauce Labs Onesie.(add-to-cart-sauce-labs-onesie)

    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for product in products:
        wait.until(EC.presence_of_element_located((By.ID, product))).click()

    # Перейдите в корзину.
    shopping_cart = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "shopping_cart_link")))
    shopping_cart.click()

    # Нажмите Checkout.
    wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    # Заполните форму своими данными:имя/first-name,
    # фамилия/last-name, почтовый индекс/postal-code
    name_first = wait.until(EC.presence_of_element_located(
        (By.ID, "first-name")))
    name_first .send_keys("Irina")
    name_last = wait.until(EC.presence_of_element_located((
        By.ID, "last-name")))
    name_last.send_keys("Fedorova")
    postal_code = wait.until(EC.presence_of_element_located(
        (By.ID, "postal-code")))
    postal_code.send_keys("940400")

    # Нажмите кнопку Continue.
    cont = wait.until(EC.presence_of_element_located((By.ID, "continue")))
    cont.click()

    # Прочитайте со страницы итоговую стоимость (  Total ).
    total_price = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))

   # Проверьте, что итоговая сумма равна $58.29
    assert total_price.text == "Total: $58.29"

    driver.quit()
