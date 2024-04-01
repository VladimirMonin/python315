"""
Lesson 31
01.04.2024

Концепция валидации данных
Ручной класс сериализатор и валидатор
Установка marshmallow
pip install marshmallow marshmallow-dataclass
Валидация с помощью marshmallow
Концепция схемы и поля
PostLoad - обработка данных после загрузки
Настройки полей

"""

from dataclasses import dataclass, field
from typing import Union, Dict
from marshmallow import Schema, fields, post_load, ValidationError, pre_load
from data import cities

# print(cities.cities_list)


cities_list = [
    {
        "coords": {
            "lat": "52.65",
            "lon": "90.08333"
        },
        "district": "Сибирский",
        "name": "Абаза",
        "population": 14816,
        "subject": "Хакасия",
        "email": "a@s.ru"
    }
]


@dataclass
class City:
    name: str
    population: int
    district: str
    subject: str
    lat: float
    lon: float
    email: str


class CitySchema(Schema):
    district = fields.Str()
    name = fields.Str()
    population = fields.Int()
    subject = fields.Str()
    coords = fields.Dict()
    lat = fields.Float(required=False)
    lon = fields.Float(required=False)
    email = fields.Email()

    @post_load
    def make_city(self, data, **kwargs):
        coords = data.pop('coords')
        data['lat'] = coords['lat']
        data['lon'] = coords['lon']

        return City(**data)





city_schema = CitySchema()
city = city_schema.load(cities_list[0])
print(city)
# Преобразование данных в словарь
city_dict = city_schema.dump(city)
print(city_dict)