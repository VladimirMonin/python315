"""
Знакомство с ООП
- Зачем это нужно?
- Какие преимущества?
- Синтаксис
- Нейминг классов
- Атрибуты класса
- Атрибуты экземпляра класса
- Инициализация экземпляра класса
- self
- Конструктор класса
- Методы экземпляра класса
- self в методах
"""


# Синтаксис - class <Имя класса>:
class LadaCar:
    price = 1000  # Атрибут класса

    def __init__(self, model: str, color: str, year: int):  # Инициализация экземпляра класса
        self.model = model
        self.color = color
        self.year = year

    def get_price(self):
        return f'Цена автомобиля {self.price}'

    def get_color(self):
        return f'Цвет автомобиля {self.color}'



# Создание экземпляра класса
lada_kalina = LadaCar('Kalina', 'white', 2020)
lada_priora = LadaCar('Priora', 'black', 2015)

print(lada_kalina.get_color())
print(lada_priora.get_color())