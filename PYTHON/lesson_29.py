"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Метаклассы - как концепция
Декорация классов
"""

from dataclasses import dataclass, field, fields, asdict


@dataclass(order=True)
class Person:
    # Исключим лишние поля
    name: str = field(compare=False, metadata={"description": "Имя"})
    age: int = field(metadata={"description": "Возраст"})
    city: str = field(compare=False, metadata={"description": "Город"})

    def __str__(self):
        """
        Неоправданно завышенная сложность
        Просто, чтобы показать возможности метаинформации
        :return:
        """
        meta_str = ", ".join([f"{f.metadata['description']}: {getattr(self, f.name)}" for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Employee(Person):
    position: str = field(metadata={"description": "Должность"})
    salary: int = field(metadata={"description": "Зарплата"})


p1 = Employee("Вася", 25, "Москва", "Программист", 100_000)
p2 = Employee("Маша", 30, "Москва", "Программист", 100_000)

print(p1)
print(p2)