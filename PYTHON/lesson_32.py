"""
Lesson 32
03.04.2024

- Повторяем marshmallow
- Простой пример схемы
- Схема с прелоад и постлоад
- Схема с вложенными схемами
- Схема на основе датакласса (marshmallow_dataclass)
- Дополнительные парметры через метаданные в датаклассе (marshmallow_dataclass)
- Расширение своей схемой схемы созданной на основе датакласса
"""

from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_load, post_load
import marshmallow_dataclass
from marshmallow.validate import Range


@dataclass
class City:
    name: str
    district: str
    subject: str
    population: int = field(metadata={'validate': Range(min=1, max=1000000)})
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
        "population": 14816,
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

# Расширяем своей схемой, схему созданную на основе датакласса

class CoordsSchema(Schema):
    lat = fields.Float()
    lon = fields.Float()

class CitySchemaExtended(CitySchema):
    coords = fields.Nested(CoordsSchema, required=True)


# Десериализация
city_schema = CitySchemaExtended(many=True)
cities = city_schema.load(cities_list)
print(cities)

# Сериализация
result = city_schema.dump(cities)
print(result)