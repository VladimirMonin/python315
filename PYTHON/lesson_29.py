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
class AbstractPerson:
    first_name: str = field(metadata={"description": "Имя"})

    def __str__(self):
        """
        Оправданная сложность.
        В наследниках все работает автоматически
        :return:
        """
        meta_str = ", ".join([f"{f.metadata['description']}: {getattr(self, f.name)}" for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Person(AbstractPerson):
    # Исключим лишние поля
    age: int = field(metadata={"description": "Возраст"})
    city: str = field(compare=False, metadata={"description": "Город"})


@dataclass(order=True)
class Employee(Person):
    position: str = field(metadata={"description": "Должность"})
    salary: int = field(metadata={"description": "Зарплата"})


p1 = Employee("Вася", 25, "Москва", "Программист", 100_000)
p2 = Employee("Маша", 30, "Москва", "Программист", 100_000)
p3 = Employee("Аня", 25, "Москва", "Тимлид", 150_000)

