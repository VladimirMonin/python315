"""
Lesson 37
Pytest

Установка pytest - pip install pytest
assert - проверка условия
assert exception - проверка исключения
"""

city_dict = {
    'name': 'Moscow',
    'population': '13143',
    'area': '13143',
    'country': 'Russia',
}

def validate_name(name):
    """
    Проверка наличия имени
    """
    if isinstance(name, str):
        return True
    else:
        return False
    
def validate_population(population):
    """
    Проверка наличия населения
    """
    if isinstance(population, int):
        return True
    else:
        return False
    

def validate_area(area):
    """
    Проверка наличия площади
    """
    if isinstance(area, int):
        return True
    else:
        return False
    

# if validate_name(city_dict['name']):
#     print('Имя города валидно')
# else:
#     raise ValueError('Имя города не валидно')

# if validate_population(city_dict['population']):
#     print('Население города валидно')
# else:
#     raise ValueError('Население города не валидно')

# if validate_area(city_dict['area']):
#     print('Площадь города валидна')
# else:
#     raise ValueError('Площадь города не валидна')


assert validate_name(city_dict['name']) == True, 'Имя города не валидно'
assert validate_population(city_dict['population']) == True, 'Население города не валидно'
assert validate_area(city_dict['area']) == True, 'Площадь города не валидна'


"""
Ключевая проблема подобного кода - изобретение велосипеда заново.
Эти тесты будут останавливаться полностью, на первом же неудачном случае.

Так же, нам придется писать управляющий модуль, который будет собирать тесты с 
разных файлов и запускать их. Попутно решая огромное количество проблем.

Pytest - это фреймворк для тестирования, который позволяет писать тесты в
удобном и понятном виде, а так же управлять ими.
"""

