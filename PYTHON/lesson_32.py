"""
Lesson 32
03.04.2024

- Повторяем marshmallow
- Простой пример схемы
- Схема с прелоад и постлоад
- Схема с вложенными схемами
- Схема на основе датакласса (marshmallow_dataclass)
"""

from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_load, post_load
import marshmallow_dataclass


@dataclass
class City:
    name: str
    district: str
    subject: str
    population: int
    email: str = field(default="", metadata={"load_default": "",
                                             "load_only": True})
    coords: dict = field(default_factory=dict)



cities_list = [
    {"coords": {
        "lat": "52.65",
        "lon": "90.08333"
    },
        "district": "Сибирский",
        "name": "Абаза",
        "population": -14816,
        "subject": "Хакасия"
    },

    {"coords": {
        "lat": "53.71667",
        "lon": "91.41667"
    },
        "district": "Сибирский",
        "name": "Абакан",
        "population": 187239,
        "subject": "Хакасия"
    }]


# Создание схемы на основе датакласса
CitySchema = marshmallow_dataclass.class_schema(City)

# Создание экземпляра схемы
city_schema = CitySchema(many=True)

# Десериализация данных
cities = city_schema.load(cities_list)
print(cities)

# Сериализация данных
data = city_schema.dump(cities)
print(data)