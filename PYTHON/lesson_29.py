"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Декорация классов
Метаклассы - как концепция
"""

# Класс - декоратор, который добавит к датаклассу методы

from dataclasses import dataclass, field, fields, asdict, astuple, is_dataclass


from dataclasses import dataclass, field
from types import MethodType

class CityDecorator:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        obj = self.cls(*args, **kwargs)

        # Привязываем функцию get_info как метод к экземпляру obj
        obj.get_info = MethodType(self.get_info, obj)
        return obj

    def get_info(instance):
        # Здесь self теперь относится к экземпляру City
        return f'Информация о городе: {instance.name}, {instance.population}, {instance.latitude}, {instance.longitude}, {instance.region}'

@CityDecorator
@dataclass
class City:
    name: str
    population: int
    latitude: float
    longitude: float
    region: str = field(default='Europe')

city = City('Moscow', 10000000, 55.75, 37.61)
print(city.get_info())  # Теперь должно работать корректно
