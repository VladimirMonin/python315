# pip install requests marshmallow marshmallow-dataclass marshmallow-jsonschema
from dataclasses import dataclass
from pprint import pprint
from dataclasses import dataclass, field
from marshmallow import Schema, fields, pre_load, post_load, INCLUDE
import marshmallow_dataclass
from marshmallow.validate import Range
from marshmallow_jsonschema import JSONSchema
import requests

"""
Образец данных с API:

{'base': 'stations',
 'clouds': {'all': 100},
 'cod': 200,
 'coord': {'lat': 55.7522, 'lon': 37.6156},
 'dt': 1712151215,
 'id': 524901,
 'main': {'feels_like': 12.14,
          'grnd_level': 974,
          'humidity': 77,
          'pressure': 993,
          'sea_level': 993,
          'temp': 12.79,
          'temp_max': 13.75,
          'temp_min': 12.13},
 'name': 'Москва',
 'rain': {'1h': 0.17},
 'sys': {'country': 'RU',
         'id': 47754,
         'sunrise': 1712112865,
         'sunset': 1712160643,
         'type': 2},
 'timezone': 10800,
 'visibility': 10000,
 'weather': [{'description': 'небольшой дождь',
              'icon': '10d',
              'id': 500,
              'main': 'Rain'}],
 'wind': {'deg': 223, 'gust': 16.4, 'speed': 8.1}}
"""


def get_weather(city_name):
    api_key = "23496c2a58b99648af590ee8a29c5348"  # Можете взять мой. 23496c2a58b99648af590ee8a29c5348
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


# Пример использования
city = "Москва"
weather_data = get_weather(city)
pprint(weather_data)


@dataclass
class CityWeather:
    name: str
    temp: float
    feels_like: float
    wind_speed: float

    def __str__(self):
        return (f"Город: {self.name}, Температура: {self.temp}, "
                f"Ощущается как: {self.feels_like}, Скорость ветра: {self.wind_speed}")


# Создание схемы на основе датакласса
WeatherSchema = marshmallow_dataclass.class_schema(CityWeather)


# Расширение своей схемой, схему созданную на основе датакласса


class ExtendedWeatherSchema(WeatherSchema):
    # class Meta:
    #     unknown = INCLUDE

    temp = fields.Float(validate=Range(min=-80, max=80))

    @pre_load
    def prepare_data(self, data, **kwargs):
        data['temp'] = data['main']['temp']
        data['feels_like'] = data['main']['feels_like']
        data['wind_speed'] = data['wind']['speed']
        allowed_key = ['name', 'temp', 'feels_like', 'wind_speed']

        return {key: data[key] for key in allowed_key}


# Десериализация
city_weather_schema = ExtendedWeatherSchema()
city_weather = city_weather_schema.load(weather_data)
print(city_weather)

# Сериализация
city_weather_dict = city_weather_schema.dump(city_weather)
print(city_weather_dict)

# Десериализация - невозможна, надо делать прелоад (расширять и добавлять новую логику)
# city_weather = city_weather_schema.load(city_weather_dict)
# print(city_weather)

# На основе схемы создаем JSON схему
json_schema = JSONSchema()
schema = json_schema.dump(city_weather_schema)

pprint(schema)