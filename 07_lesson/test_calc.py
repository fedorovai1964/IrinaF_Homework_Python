import pytest
from page_calc import PageCalc
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculation(driver):
    page_calc = PageCalc(driver)
    page_calc.open()
    page_calc.field_delay()
    page_calc.button_calc_seven()
    page_calc.button_calc_plus()
    page_calc.button_calc_eight()
    page_calc.button_calc_equals()

    timeout = page_calc.wait_for_result()
    assert 45 <= timeout <= 50, \
        f"Ожидалась задержка ~45 секунд, получено {timeout} секунд"

    result_text = page_calc.get_result_text()
    assert result_text == "15", \
        f"Ожидался результат '15', получен '{result_text}'"
