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


class BerserkModeMixin:
    def turn_on_bersek(self):
        if not self.bersek_mode:
            self.damage *= 3
            self.bersek_mode = True
            print('Berserk mode ON')

    def turn_off_bersek(self):
        if self.bersek_mode:
            self.damage //= 3
            self.bersek_mode = False
            print('Berserk mode OFF')

class Health:
    def __init__(self, value, owner):
        self.value = value
        self.owner = owner

    def __add__(self, other):
        self.value += other
        self.owner.check_bersek_mode()
        return self.value

    def __sub__(self, other):
        self.value -= other
        self.owner.check_bersek_mode()
        return self.value

class Berserk(BerserkModeMixin):
    def __init__(self, health: int = 120, damage: int = 50):
        self.bersek_mode = False
        self.health = Health(health, self)
        self.damage = damage

    def check_bersek_mode(self):
        if self.health.value < 20:
            self.turn_on_bersek()
        else:
            self.turn_off_bersek()


# Создать персонажа
hero = Berserk(health=100, damage=30)
print(hero.health.value)

# Персонаж получает урон
hero.health - 90

# Персонаж лечится
hero.health + 50
