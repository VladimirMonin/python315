"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Сериализация
"""

# Определим простой класс Car, который имеет один атрибут - brand (марка автомобиля)
class Car:
    def __init__(self, brand):
        self.brand = brand

# Создадим декоратор класса, который добавляет новый метод и атрибут к классу
def add_method_and_attribute(cls):
    cls.country = 'Japan'  # Добавляем новый атрибут класса
    def get_info(self):  # Определяем новый метод
        return f'This {self.brand} is from {self.country}'
    cls.get_info = get_info  # Добавляем метод к классу
    return cls  # Возвращаем модифицированный класс

# Применяем декоратор к классу Car
@add_method_and_attribute
class Car:
    def __init__(self, brand):
        self.brand = brand

# Создаем экземпляр класса Car и проверяем добавленный метод и атрибут
car = Car("Toyota")
info = car.get_info()
car_country = Car.country

print(info, car_country)
