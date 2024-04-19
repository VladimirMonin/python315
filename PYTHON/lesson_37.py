"""
Lesson 37
Pytest

Установка pytest - pip install pytest
assert - проверка условия
assert exception - проверка исключения
"""

is_happy = False

# assert is_happy, "Похоже, что я не счастлив"

def test_is_happy():
    try:
        assert is_happy, "Похоже, что я не счастлив"
    
    except AssertionError as e:
        print(e)
        return False
    
test_is_happy()