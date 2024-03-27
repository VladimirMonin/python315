"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Теория сериализации и десериализации
Библиотека pickle
Практика pickle
"""

import pickle
from dataclasses import dataclass, field

# @dataclass
# class Person:
#     name: str
#     age: int
#     city: str
#
#
# # data = {"key": "value"}
# data = Person("Ivan", 30, "Moscow")
#
#
# serialized_data = pickle.dumps(data)
# print(serialized_data)
#
#
# FILE = r"data\data.pickle"
#
#
# with open(FILE, "wb") as file:
#     pickle.dump(data, file)
#
#
# with open(FILE, "rb") as file:
#     data = pickle.load(file)
#     print(data)
#     print(type(data))

"""
# Практика!
1. Импортируйте переменную, содержающую список городов
2. Попробуйте создать список словарей, из Городов
3. Опишите датакласс для города
4. Создайте список экземпляров датакласса
5. Сериализуйте список экземпляров датакласса в файл cities.pickle
6. Десериализуйте файл cities.pickle обратно в список экземпляров датакласса
"""

# из data.cities import cities_list

from data.cities import cities_list

# print(cities_list)


@dataclass
class City:
    coords: tuple
    district: str
    name: str
    population: int
    subject: str
    

cities = [City(**city) for city in cities_list]


print(cities[:5])
print(cities[0].coords)
print(cities[1].coords)
print(type(cities[0].coords))
FILE = r"../data/cities.pickle"

with open(FILE, "wb") as file:
    pickle.dump(cities, file)


with open(FILE, "rb") as file:
    cities = pickle.load(file)
    print(cities[:5])
    print(type(cities))
    print(type(cities[0]))


print(cities[:5])
print(cities[0].coords)
print(cities[1].coords)
print(type(cities[0].coords))