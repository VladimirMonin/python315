"""
Lesson 26
13.03.2024
Магические методы Ч2
Магические методы для математических операций
__add__ - сложение
__sub__ - вычитание
__mul__ - умножение
__truediv__ - деление
__floordiv__ - целочисленное деление
__mod__ - остаток от деления
__pow__ - возведение в степень


Магические методы для операций inplace
__iadd__ - сложение
__isub__ - вычитание
__imul__ - умножение
__itruediv__ - деление

Практика - игровые персонажи, здоровье и мана
"""
"""
Создать класс Health (опишите логику вычитания здоровья и добавления здоровья)
1 аттрибут - значение (value)

Создать класс Berserk
В нем есть  здоровье Health class


"""


class Health:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        self.value += other
        return self.value

    def __sub__(self, other):
        self.value -= other
        return self.value


class Berserk:
    def __init__(self, health: int = 120, damage: int = 50):
        self.health = Health(health)
        self.damage = 50

    def turn_on_bersek(self):
        self.damage *= 3

    def turn_off_bersek(self):
        self.damage //= 3


# Проверка
b = Berserk()
print(b.health.value)
b.health + 10
print(b.health.value)
b.health - 20
print(b.health.value)

# Как реализовать логику, что если здоровье меньше 20 - у нас включится режим берсерка
