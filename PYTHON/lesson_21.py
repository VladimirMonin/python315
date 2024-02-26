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
- Статические методы
- Методы класса
"""


# Синтаксис - class <Имя класса>:
class LadaCar:
    """
    Класс для создания автомобилей Lada
    """

    bodies = ['sedan', 'hatchback', 'universal']

    def __init__(self, model: str, color: str, year: int):  # Инициализация экземпляра класса
        self.model = model
        self.color = color
        self.year = year

    def get_color(self) -> str:
        """
        Метод экземпляра класса, который возвращает цвет автомобиля
        :return:
        """
        return f'Цвет автомобиля {self.color}'

    @staticmethod
    def get_lada_value(length: int, width: int, height: int):
        """
        Статический метод класса, он не имеет доступа к атрибутам экземпляра класса
        При этом непосредственно связан с классом
        :param length:
        :param width:
        :param height:
        :return:
        """
        return length * width * height

    # Метод для переназначения списка кузовов (атрибут класса)
    @classmethod
    def set_bodies(cls, bodies: list):
        cls.bodies = bodies


# Создание экземпляра класса
lada_kalina = LadaCar('Kalina', 'white', 2020)
print(lada_kalina.bodies)

lada_kalina.set_bodies(['sedan', 'hatchback', 'universal', 'crossover'])

lada_priora = LadaCar('Priora', 'black', 2015)
print(lada_kalina.bodies)
print(lada_priora.bodies)

print(lada_kalina.get_color())
print(lada_priora.get_color())


print(lada_kalina.get_lada_value(2, 3, 4))

print(LadaCar.get_lada_value(2, 3, 4))
