"""
Lesson 25
Что такое магические методы?
__init__ - конструктор
__str__ - строковое представление объекта
__repr__ - представление объекта
__bool__ - логическое представление объекта
__len__ - длина объекта

Методы сравнения
__eq__ - равенство
__ne__ - неравенство
__lt__ - меньше
__le__ - меньше или равно
__gt__ - больше
__ge__ - больше или равно

Как это работает с наследованием?

@total_ordering - декоратор, который позволяет определить все методы сравнения
"""


class Kettlebell:
    """
    Гиря.
    """
    def __init__(self, weight, length=40, width=10):
        self.weight = weight
        self.length = length
        self.width = width

    def __str__(self) -> str:
        return f'Гиря весом {self.weight} кг'

    def __bool__(self) -> bool:
        return self.weight > 0

    # def __len__(self) -> int:
    #     return self.length


ket1 = Kettlebell(16)
print(ket1)
if ket1:
    print('Гиря настоящая')

print(len(ket1))