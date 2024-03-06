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

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color

    def open(self):
        """
        Открывает матрешку
        """
        print(f'{self.size} матрешка {self.color} цвета: открывается')

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        print(f'Размер: {self.size}, цвет: {self.color}')


class MediumMatryoshka(BigMatryoshka):
    """
    Средняя Матрешка.
    Методы:
    - open - открывает матрешку
    - display_info - печатает информацию о матрешке
    """

    def __init__(self, color):
        super().__init__(color)
        self.size = 'Средняя'







big_matryoshka = BigMatryoshka("Зеленая")
big_matryoshka.open()

medium_matryoshka = MediumMatryoshka('Красная')
medium_matryoshka.open()

