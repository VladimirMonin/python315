"""
TODO - NotImplemented - почему не получаем Exception
Lesson 25
Что такое магические методы?
__init__ - конструктор
__str__ - строковое представление объекта
__repr__ - представление объекта
__bool__ - логическое представление объекта
__len__ - длина объекта

Методы сравнения
__eq__ - равенство
__ne__ - неравенство
__lt__ - меньше
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно

`NotImplemented` – специальное значение, которое можно вернуть из
метода сравнения в случае, когда сравнение между операндами невозможно, как описано выше.

`NotImplementedError` – это исключение, которое возникает, когда
абстрактный метод должен быть имплементирован классом-наследником,
 если класс_MIXIN не поддерживает этот метод, то должно быть явно указано это
 через `NotImplementedError`, однако используется он для понятия ошибки разработки
 не тестирования доступности метода сравнения разных типов объектов.


Как это работает с наследованием?

@total_ordering - декоратор, который позволяет определить все методы сравнения
Нам надо определить метод проверки на равенство
И один из методов сравнения: меньше, меньше или равно, больше, больше или равно
"""
from functools import total_ordering

"""
Опишите класс Город, у которого есть следующие атрибуты:  
- название (name)  
- население (population)  
  
Импортируйте декоратор total_ordering из модуля functools  
Используйте декоратор total_ordering для определения всех методов сравнения, описав  
лишь необходимый минимум (сравнение только по населению).
  
Опишите метод __str__ для вывода информации о городе в виде:  
"Город: <name>, Население: <population>"  
  
Создайте несколько экземпляров класса Город и сравните их между собой.
Сделайте список городов и отсортируйте его.
"""

@total_ordering
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f'Город: {self.name}, Население: {self.population}'

    def __eq__(self, other):
        return self.population == other.population

    def __lt__(self, other):
        return self.population < other.population


city_list = [
    {'name': 'Moscow', 'population': 12_000_000},
    {'name': 'Saint-Petersburg', 'population': 5_000_000},
    {'name': 'Novosibirsk', 'population': 1_600_000},
    {'name': 'Yekaterinburg', 'population': 1_500_000},
    {'name': 'Nizhny Novgorod', 'population': 1_200_000},
]

cities = [City(**city) for city in city_list]

print(cities)
[print(city) for city in cities]

cities.sort()
[print(city) for city in cities]

"""
Мы получим список типа <__main__.City object at 0x0000026A0A9EDDC0>
Где
__main__ - это модуль, в котором определен класс
City - это имя класса
object - это базовый класс для всех классов в Python
0x0000026A0A9EDDC0 - это адрес объекта в памяти
"""