import allure
import pytest
from page_online_shop_login import PageShopLogin
from page_online_shop_main import PageShopMain
from page_online_shopping_cart import PageOnlineShoppingCart
from page_online_shop_checkout import PageCheckout
from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера."""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет функциональность интернет-магазина"
                    " на сайте https://www.saucedemo.com/,"
                    " используя браузер FireFox.")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_online_shop(driver):
    page_login = PageShopLogin(driver)
    page_main = PageShopMain(driver)
    page_cart = PageOnlineShoppingCart(driver)
    page_checkout = PageCheckout(driver)

    with allure.step("Открыть сайт магазина: https://www.saucedemo.com/"):
        page_login.open()

    with allure.step("Авторизоваться как пользователь standard_user"):
        page_login.login()

    with allure.step("Добавить в корзину товары:"):
        page_main.add_product_backpack()
        page_main.add_product_bolt_t_shirt()
        page_main.add_product_onesie()

    with allure.step("Перейдите в корзину."):
        page_main.go_to_shopping_cart()

    with allure.step("Нажать кнопку Checkout"):
        page_cart.checkout()

    with allure.step("Заполнить форму своими данными: "):
        page_checkout.fill_checkout()

    with allure.step("Прочитать со страницы итоговую стоимость (Total)."):
        total = page_checkout.total_price()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert total == "Total: $58.29"

