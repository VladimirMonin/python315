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
    count = 0

    def __init__(self, color):
        self.size = 'Большая'
        self.color = color
        __class__.count += 1
        self.id = __class__.count

    def open(self):
        """
        Открывает матрешку
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_big_count(cls):
        return cls.count

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
        self.big_matryoshka = BigMatryoshka(color)
        super().__init__(color)
        self.size = 'Средняя'

    def open(self):
        """
        Открывает матрешку
        """
        self.big_matryoshka.open()
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')


medium_matryoshka = MediumMatryoshka('Красный')
medium_matryoshka.open()
print(medium_matryoshka.get_big_count())