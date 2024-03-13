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

class Mana:
    def __init__ (self, value):
        self.value = value

    def __sub__ (self, other):
        if isinstance(other, int):
            self.value -= other
        else:
            raise ValueError('Можно вычитать только целые числа')
        return self.value


class Mage:
    def __init__ (self):
        self.mana = Mana(100)


# Как реализовать логику вычитания маны у мага?
mage = Mage()
mage.mana - 30
print(mage.mana.value)