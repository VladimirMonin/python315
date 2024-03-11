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

    def __len__(self) -> int:
        return self.weight

    def __eq__(self, other: 'Kettlebell') -> bool:
        # Проверка на принадлежность к классу
        if not isinstance(other, Kettlebell):
            raise ValueError('Неверный тип')
        return self.weight == other.weight and self.length == other.length and self.width == other.width


ket1 = Kettlebell(16, 45, 11)
print(ket1)
if ket1:
    print('Гиря настоящая')

print(len(ket1))

ket2 = Kettlebell(16)
ket3 = Kettlebell(24)

print(ket1 == ket2) # TODO - Как сравниваются объекты автоматически?
