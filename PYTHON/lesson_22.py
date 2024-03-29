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
@property - декоратор для создания геттера
@setter_name.setter - декоратор для создания сеттера
@setter_name.deleter - декоратор для создания делитера - ПОСМОТРЕТЬ в СЛ РАЗ

"""


# __len__ - метод для определения длины объекта

# класс Персона. Имя, фамилия, должность, зарплата, срок службы

class Person:
    def __init__(self, name: str, age: int,
                 surname: str, position: str,
                 salary: int, service: int):

        self.__name = name
        self.__age = age
        self._surname = surname
        self.position = position
        self.salary = salary
        self.service = service

    def __str__(self):
        return f'{self.__name} {self._surname}'

    def __repr__(self):
        return f'Person({self.__name}, {self._surname}, {self.position}, {self.salary}, {self.service})'

    @staticmethod
    def __validate_age(age):
        if isinstance(age, int) and 16 <= age <= 100:
            return True
        return False

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        """
        Проверяем что возраст число, и в диапазоне от 16 до 100
        :param age:
        :return:
        """
        if self.__validate_age(age):
            self.__age = age
        else:
            raise ValueError('Возраст должен быть числом от 16 до 100')


p1 = Person('Ivan', 30, 'Ivanov', 'developer', 1000, 5)
print(p1)
p1.age = 40
print(p1.age)

p1.age = 101
