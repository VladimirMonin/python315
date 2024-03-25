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
    hobbies: list[str] = field(default_factory=list, compare=False, metadata={"description": "Хобби"})

    def __str__(self):
        """
        Неоправданно завышенная сложность
        Просто, чтобы показать возможности метаинформации
        :return:
        """
        meta_str = ", ".join([f"{f.metadata['description']}: {getattr(self, f.name)}" for f in fields(self)])
        return meta_str

p1 = Person("Вася", 25, "Москва", ["программирование", "JS"])
p2 = Person("Маша", 25, "Москва", ["программирование", "Python"])

print(p1 == p2)
print(p1)

# Получим метаинформацию о полях из экземпляра p2
# Получили список полей, представленных в виде экземпляров Field
print(fields(p2))
# Получим из fields метаинформацию,
print(fields(p2)[0].metadata)

[print(s.metadata) for s in fields(p2)]

# Получим данные из fields
result = [f"{f.metadata['description']}: {getattr(p1, f.name)}" for f in fields(p1)]
print(result)

# Сделаем это в виде цикла
result = []

for f in fields(p1):
    meta_description = f.metadata['description']
    value = getattr(p1, f.name)
    result.append(f"{meta_description}: {value}")

print(result)

