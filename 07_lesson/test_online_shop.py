import pytest
from page_online_shop_login import PageShopLogin
from page_online_shop_main import PageShopMain
from page_online_shoping_cart import PageOnlineShoppingCart
from page_online_shop_checkout import PageCheckout
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_online_shop(driver):
    page_login = PageShopLogin(driver)
    page_main = PageShopMain(driver)
    page_cart = PageOnlineShoppingCart(driver)
    page_checkout = PageCheckout(driver)
    # Откройте сайт магазина: https://www.saucedemo.com/
    page_login.open()
    # Авторизуйтесь как пользователь standard_user
    page_login.login()
    # Добавьте в корзину товары:
    # Sauce Labs Backpack.(add-to-cart-sauce-labs-backpack)
    # Sauce Labs Bolt T-Shirt.(add-to-cart-sauce-labs-bolt-t-shirt)
    # Sauce Labs Onesie.(add-to-cart-sauce-labs-onesie)
    page_main.add_prodacts()
    # Перейдите в корзину.
    page_main.go_to_shopping_cart()
    # Нажмите Checkout.
    page_cart.checkout()
    # Заполните форму своими данными:имя/first-name,
    # фамилия/last-name, почтовый индекс/postal-code
    # Нажмите кнопку Continue.
    page_checkout.fill_checkout()
    # Прочитайте со страницы итоговую стоимость (Total)
    total = page_checkout.total_price()
   # Проверьте, что итоговая сумма равна $58.29
    assert "Total: $58.29" in total, f"Total: $58.29 != {total}"
