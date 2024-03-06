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


# NotImplementedError - исключение, которое вызывается, когда метод не реализован
# И

class AbstractMatryoshka:
    """
    Абстрактный класс Матрешка.
    Тут может быть реализовано общее поведение для всех матрешек.
    """
    count = 0

    def __init__(self):
        self.size = None
        self.color = None
        __class__.count += 1
        self.id = __class__.count

    def open(self):
        """
        Открывает матрешку
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

    @classmethod
    def get_count(cls):
        return cls.count

    def __str__(self):
        """
        Печатает информацию о матрешке
        :return:
        """
        return (f'Размер: {self.size}, цвет: {self.color}, id: {self.id}')


class BigMatryoshka(AbstractMatryoshka):
    """
    Большая Матрешка.
    Методы:
    - open - открывает матрешку
    """

    def __init__(self, color):
        super().__init__()
        self.size = 'Большая'
        self.color = color

    def open(self):
        """
        Открывает матрешку
        """
        print(f'{self.size} матрешка, цвет: {self.color} с ID {self.id} открывается')

big = BigMatryoshka('Красный')
big.open()
# big.display_info()

"""
Попробуйте создать классы для средней и маленькой матрешки, которые наследуются от абстрактного класса Матрешка.
Чтобы они использовали общий счетчик.
"""