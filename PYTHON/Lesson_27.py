"""
Lesson 27
18.03.2024
Разбор hw_35
Dataclasses
- как определяется repr
- как определяется eq
- сериализация и десериализация
- field(default_factory=list) - для изменяемых типов
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
    hobbies: list = field(default_factory=list)


p1 = Person("Иван", 35, "Москва", ["плавание", "путешествия"])
p2 = Person("Анна", 28, "Санкт-Петербург", ["рафтинг", "манга"])
p1.hobbies.append("программирование")
p2.hobbies.append("JS")

print(f'{p1=}')
print(f'{p2=}')
