"""
Lesson 24
06.03.2024

План:
- Завершение практики с матрешками
- Цепочка наследования
- Переопределение методов
- Повторение материала
- Множественное наследование
- Многоуровневое наследование
- MRO
- `.mro()`
- `isinstance()` и `issubclass()`
- Разрешение конфликтов
- Абстрактные классы
- Миксины
- Инициализация и при наследовании
"""


class BigMatryoshka:
    """
    Большая Матрешка.
    Методы:
    - open - открывает матрешку
    """
    big_count = 0

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color
        BigMatryoshka.big_count += 1
        self.id = BigMatryoshka.big_count

    def open(self):
        """
        Открывает матрешку
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_big_count(cls):
        return cls.big_count

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        return (f'Размер: {self.size}, цвет: {self.color}, id: {self.id}')


class MediumMatryoshka(BigMatryoshka):
    """
    Средняя Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)
        self.big_matryoshka = BigMatryoshka(color)
        self.size = 'Средняя'

    def open(self):
        """
        Открывает матрешку
        """
        self.big_matryoshka.open()
        print(f'{self.size} матрешка {self.color} цвета: открывается')


big_matryoshka = BigMatryoshka('Красный')
print(big_matryoshka)
print(big_matryoshka.get_big_count())

big_matryoshka2 = BigMatryoshka('Синий')
big_matryoshka3 = BigMatryoshka('Зеленый')

print(big_matryoshka.get_big_count())
print(big_matryoshka)
print(big_matryoshka2)
print(big_matryoshka3)
