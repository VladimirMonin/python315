"""
TODO - NotImplemented - почему не получаем Exception
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

`NotImplemented` – специальное значение, которое можно вернуть из
метода сравнения в случае, когда сравнение между операндами невозможно, как описано выше.

`NotImplementedError` – это исключение, которое возникает, когда
абстрактный метод должен быть имплементирован классом-наследником,
 если класс_MIXIN не поддерживает этот метод, то должно быть явно указано это
 через `NotImplementedError`, однако используется он для понятия ошибки разработки
 не тестирования доступности метода сравнения разных типов объектов.


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
        """
        Равенство
        :param other:
        :return:
        """
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight == other.weight and self.length == other.length and self.width == other.width

    def __ne__(self, other: 'Kettlebell') -> bool:
        """
        Неравенство
        :param other:
        :return:
        """
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight != other.weight

    def __lt__(self, other: 'Kettlebell') -> bool:
        """
        Меньше
        :param other:
        :return:
        """
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight < other.weight

    def __le__(self, other: 'Kettlebell') -> bool:
        """
        Меньше или равно
        :param other:
        :return:
        """
        if not isinstance(other, Kettlebell):
            return NotImplemented
        return self.weight <= other.weight


class Dumbbells:
    def __eq__(self, other):
        return NotImplemented
    pass


ket1 = Kettlebell(16, 45, 11)
print(ket1)
if ket1:
    print('Гиря настоящая')

print(len(ket1))

ket2 = Kettlebell(16)
ket3 = Kettlebell(24)

print(ket1 == ket2)
print(ket1 != ket2)
print(ket1 < ket2)
print(ket1 <= ket2)  # TODO - Как сравниваются объекты автоматически, если этот метод не описан?
print(ket1 > ket2)
print(ket1 >= ket2)

print(ket1 == ket3)
print(ket1 != ket3)
print(ket1 < ket3)
print(ket1 <= ket3)
print(ket1 > ket3)
print(ket1 >= ket3)

dumb1 = Dumbbells()


