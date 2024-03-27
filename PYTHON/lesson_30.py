"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Теория сериализации и десериализации
Библиотека pickle
"""

import pickle
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    city: str


# data = {"key": "value"}
data = Person("Ivan", 30, "Moscow")


serialized_data = pickle.dumps(data)
print(serialized_data)


FILE = r"data\data.pickle"


with open(FILE, "wb") as file:
    pickle.dump(data, file)


with open(FILE, "rb") as file:
    data = pickle.load(file)
    print(data)
    print(type(data))



"""
# Практика!
1. Импортируйте переменную, содержающую список городов
2. Попробуйте создать список словарей, из Городов
3. Опишите датакласс для города
4. Создайте список экземпляров датакласса
5. Сериализуйте список экземпляров датакласса в файл cities.pickle
6. Десериализуйте файл cities.pickle обратно в список экземпляров датакласса
"""