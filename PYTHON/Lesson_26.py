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

"""

# ADD

class Pins:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f'Блин весом {self.weight} кг.'

    def __add__(self, other):
        if isinstance(other, Pins):
            return Pins(self.weight + other.weight)

    def get_sum(self, other):
        if isinstance(other, Pins):
            return Pins(self.weight + other.weight)
        else:
            raise ValueError('Нельзя складывать пинцеты с чем-то другим')

p1 = Pins(10)
p2 = Pins(10)
p3 = p1 + p2
print(p3)
print(p1.get_sum(p2))

pins_list = [p1, p2, p3]
sum_pins = sum(pins_list, Pins(0))
print(sum_pins)

"""
В Python функция sum используется для подсчета суммы элементов 
итерируемого объекта, начиная с некоторого начального значения. 

По умолчанию, это начальное значение равно 0 для чисел. 
Однако, когда вы работаете с объектами пользовательского класса, 
вам нужно обеспечить начальное значение, которое является экземпляром вашего класса. 
Это необходимо, потому что Python не знает, как складывать ваши пользовательские 
объекты без явного указания.
"""