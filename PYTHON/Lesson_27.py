"""
Lesson 27
18.03.2024
Разбор hw_35
Dataclasses
- как определяется repr
- как определяется eq
- сериализация и десериализация
- field(default_factory=list) - для изменяемых типов
- field(compare=False) - для исключения из сравнения
- __post_init__ - для валидации
- fields(default = 0) - Значение по умолчанию

"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Person:
    """
    Уберем age, city из сравнения
    """
    name: str
    city: str = field(compare=False)
    hobbies: List[str]
    age: int = field(compare=False, default=0)

    def __post_init__(self):
        self.age = self.validate_age(self.age)

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        elif age > 150:
            raise ValueError("Возраст не может быть больше 150")

        return age


p1 = Person("Вася", "Москва", ["программирование", "JS"], 25)
p2 = Person("Маша", "Москва", ["программирование", "JS"], 25)
p1.hobbies.append("программирование")
p2.hobbies.append("JS")

print(f'{p1=}')
print(f'{p2=}')

"""
Практика!
Опишите дата-класс City
Атрибуты
- название
- население
- широта
- долгота
- регион

Опишите возможность стравнения городов по населению и названию
Вы можете исключить остальное из сравнения
или переопределить метод __eq__

"""


@dataclass
class City:
    name: str
    population: int
    lat: float = field(compare=False)
    lon: float = field(compare=False)
    region: str = field(compare=False)


c1 = City("Москва", 12_000_000, 55.755773, 37.617761, "Центр")
c2 = City("Санкт-Петербург", 5_351_935, 59.9342802, 30.3350986, "Север")
c3 = City("Москва", 12_000_000, 55.773, 37.61, "Центр")

print(f'{c1=}')
print(f'{c2=}')
print(f'{c3=}')

print(f'{c1 == c2=}')
print(f'{c1 == c3=}')