import allure
import pytest
from page_calc import PageCalc
from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения работы драйвера."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора "
                    "с различными операциями.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculation(driver):
    """Тест проверяет работу калькулятора с различными операциями.
        :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    page_calc = PageCalc(driver)
    with allure.step("Открытие страницы калькулятора"):
        page_calc.open()
    with allure.step("Установка задержки времени"):
        page_calc.field_delay()
    with allure.step("Нажатие кнопок: 7 + 8 ="):
        page_calc.button_calc_seven()
        page_calc.button_calc_plus()
        page_calc.button_calc_eight()
        page_calc.button_calc_equals()
    with allure.step("Ожидание результата"):
        timeout = page_calc.wait_for_result()
        assert (45 <= timeout <= 50
                ), f"Ожидалась задержка ~45 секунд, получено {timeout} секунд"

    with ((allure.step("Проверка результата 7+8=15"))):
        result_text = page_calc.get_result_text()
        assert result_text == "15", \
            f"Ожидался результат 15, получен {result_text}"
