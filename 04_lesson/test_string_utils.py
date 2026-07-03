import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize('input_str, converted_str', [
    ('добрый день', 'Добрый день'),
    ('привет', 'Привет'),
    ('hello', 'Hello'),
])
def test_capitalize_positive(input_str, converted_str):
    assert string_utils.capitalize(input_str) == converted_str


@pytest.mark.negative
@pytest.mark.parametrize('input_str, converted_str', [
    ('', ''),
    (' ', ' '),
    ('1234hello', '1234hello'),
])
def test_capitalize_negative(input_str, converted_str):
    assert string_utils.capitalize(input_str) == converted_str


@pytest.mark.positive
@pytest.mark.parametrize('input_str, converted_str', [
    (' свобода', 'свобода'),
    ('        Привет', 'Привет'),
])
def test_trim_positive(input_str, converted_str):
    assert string_utils.trim(input_str) == converted_str


@pytest.mark.negative
@pytest.mark.parametrize('input_str, converted_str', [
    ('', ''),
    ('     ', '')
])
def test_trim_negative(input_str, converted_str):
    assert string_utils.trim(input_str) == converted_str


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, bool', [
    ('свобода', 'в', True),
    ('Hello', 'l', True),
    ('Как ваше здоровье?', 'ваше', True),
    ('Класс!', '!', True),
])
def test_contaens_positive(input_str, symbol, bool):
    assert string_utils.contains(input_str, symbol) == bool


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, bool', [
    ('привет', 'c', False),
    ('Hello', 'w', False),
    ('', ' ', False),
    ('  ', ' ', True),
    ('', '', True)
])
def test_contaens_negative(input_str, symbol, bool):
    assert string_utils.contains(input_str, symbol) == bool


@pytest.mark.positive
@pytest.mark.parametrize('input_str, symbol, converted_str', [
    ('SkyPro', 'y', 'SkPro'),
    ('SkyPro', 'Pro', 'Sky'),
    ('Как ваше здоровье?', 'ваше', 'Как  здоровье?'),
    ('Шалаш', 'ш', 'Шала'),
    ('Ф', 'Ф', '')
])
def test_delete_symbol_positive(input_str, symbol, converted_str):
    assert string_utils.delete_symbol(input_str, symbol) == converted_str


@pytest.mark.negative
@pytest.mark.parametrize('input_str, symbol, converted_str', [
    ('', 'ш', ''),
    ('SkyPro', 'l', 'SkyPro'),
    ('    ', ' ', ''),
    ('D', 'd', 'D')
])
def test_delete_symbol_negative(input_str, symbol, converted_str):
    assert string_utils.delete_symbol(input_str, symbol) == converted_str


@pytest.mark.none
def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)           # type: ignore


@pytest.mark.none
def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)             # type: ignore


@pytest.mark.none
def test_contains_none_string():
    with pytest.raises(AttributeError):
        string_utils.contains(None, 'a')        # type: ignore


@pytest.mark.none
def test_contains_none_symbol():
    with pytest.raises(TypeError):
        string_utils.contains('abc', None)        # type: ignore


@pytest.mark.none
def test_delete_symbol_none_string():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, 'a')         # type: ignore


@pytest.mark.none
def test_delete_symbol_none_symbol():
    with pytest.raises(TypeError):
        string_utils.delete_symbol('abc', None)             # type: ignore
