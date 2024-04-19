"""
Lesson 37
Pytest

Установка pytest - pip install pytest
assert - проверка условия
assert exception - проверка исключения
главная проблема assert - остановка выполнения теста
тестовые функции должны начинаться с test_
файлы с тестами должны начинаться с test_ или заканчиваться _test
где и как должны лежать тесты?
@pytest.mark.slow - маркировка тестов slow - придуманный маркер
Запуск тестов с маркером pytest -m "slow"
Запуск тестов без маркера pytest -m "not slow" (подробнее в конспекте)
@pytest.mark.parametrize - параметризация тестов
xfail - тест который ожидает провал
xfail в параметризации обычного текста
@pytest.fixture - фикстуры, это заготовки для тестов
scope - как часто будет пересоздаваться фикстура
test_class - тестовый класс для группировки тестов
"""

import pytest


def is_palindrome(word):
    return word.lower().replace(' ', '') == word[::-1].lower().replace(' ', '')


def test_is_palindrome_registr():
    assert is_palindrome('Дед') == True, 'Ваша функция не обрабатывает регистр'
    # ТАК НЕ НАДО. Потому что, если тест упадет, то дальше не пойдет
    # assert is_palindrome('а роза упала на лапу азора') == True, 'Ваша функция не обрабатывает многословные палиндромы'



@pytest.mark.slow
def test_is_palindrome_multiple_words():
    assert is_palindrome('а роза упала на лапу азора') == True, 'Ваша функция не обрабатывает многословные палиндромы'


test_set = [
    ('дуд', True),
    ('дудка', False),
    ('банан', False),
    ('bob', True),
    ('bobik', False),
    ('бобер', False),
    pytest.param('бобер', True, marks=pytest.mark.xfail),
]

@pytest.mark.param # дали придуманный маркет
@pytest.mark.parametrize('word, result', test_set) # параметризация тестов
def test_is_palindrome_param(word, result):
    assert is_palindrome(word) == result, f'Слово {word} не является палиндромом'

# Тесты которые ожидают провал 

@pytest.mark.xfail
def test_is_palindrome_fail():
    assert is_palindrome('дудка') == True, 'Ваша функция посчитала слово дудка палиндромом'


# Тест который ожидает что внутри функции произойдет исключение
@pytest.mark.xfail
def test_is_palindrome_int_slice_type_error():
    with pytest.raises(Exception):
        is_palindrome(123), "Ваша функция не обрабатывает исключения"

# scope - как часто будет пересоздаваться фикстура
# session - один раз на все тесты
# module - один раз на модуль
# class - один раз на класс
# function - один раз на функцию
        
@pytest.fixture(scope='session')
def level_one():
    print('Фикстура level_one создана')
    return "I'm level one"

# @pytest.fixture
# def level_two(level_one):
#     return f"{level_one}. I depend on level_one."

def test_dependency(level_one):
    assert level_one == "I'm level one"

def test_not_dependency(level_one):
    assert level_one != "I'm level two"


# Тестовый класс - для группировки тестов
# Название класса должно начинаться с Test
# Каждый метод в классе - отдельный тест (или подготовка к тесту)
    
class TestClass:
    def test_dependency(self, level_one):
        assert level_one == "I'm level one"

    def test_not_dependency(self, level_one):
        assert level_one != "I'm level two"