"""
Lesson 27
18.03.2024
Разбор hw_35
Dataclasses
- как определяется repr
- как определяется eq
- сериализация и десериализация
"""
from dataclasses import dataclass, field


@dataclass
class Person:
    """
    Уберем age, city из сравнения
    """
    name: str
    age: int = field(compare=False)
    city: str = field(compare=False)


p1 = Person("Вася", 20, "Архангельск")
p2 = Person("Маша", 18, "Санкт-Петербург")
p3 = Person("Вася", 20, "Москва")
p4 = Person("Вася", 21, "Москва")

p1_str = str(p1)
p1_new = eval(p1_str)

print(p1 == p4)
