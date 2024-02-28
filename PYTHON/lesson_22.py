"""
Lesson 22
28.02.2024
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__`
- Функция `dir()` и метод `__dir__()`
- классы без __init__
- __str__ - пользовательское представление объекта
- __repr__ - техническое представление объекта
- eval() - встроенная функция для выполнения строки как код Python
- __len__ - метод для определения длины объекта !!!
- protected атрибуты
- private атрибуты
"""


# __len__ - метод для определения длины объекта

# класс Персона. Имя, фамилия, должность, зарплата, срок службы

class Person:
    def __init__(self, name: str, surname: str, position: str, salary: int, service: int):
        self.__name = name
        self._surname = surname
        self.position = position
        self.salary = salary
        self.service = service

    def __str__(self):
        return f'{self.__name} {self._surname}'

    def __repr__(self):
        return f'Person({self.__name}, {self._surname}, {self.position}, {self.salary}, {self.service})'

    def __len__(self):
        return self.service


# создаем объекты класса Person
person_1 = Person('Ivan', 'Ivanov', 'developer', 1000, 5)

print(person_1)  # Ivan Ivanov
# print(person_1.__name) # Ivan

new_name = 'Petr'
person_1.__name = new_name

print(person_1)  # Petr Ivanov

print(person_1.__dict__)  # {'_Person__name': 'Ivan', '_surname': 'Ivanov', 'position': 'developer', 'salary': 1000, 'service': 5, '__name': 'Petr'}


# Переопределим в Петра
person_1._Person__name = new_name

print(person_1)