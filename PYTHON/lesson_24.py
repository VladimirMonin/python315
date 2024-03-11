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
- __base__ - ссылка на родительский класс
- isubclass() - проверка наследования
- isinstance() - проверка принадлежности к классу

- Миксины
- Инициализация и при наследовании
"""
"""
Чтобы сделать это действительно абстрактным
нам нужно использовать ABC - Abstract Base Class и декоратор @abstractmethod

ABC - это класс, который не может быть инстанциирован
@abstractmethod - это декоратор, который указывает, что метод должен быть реализован в дочерних классах
"""

from abc import ABC, abstractmethod


# И

class AbstractMatryoshka(ABC):
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

    @abstractmethod
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
        print('Большая матрешка открывается')


class GlassMatryoshkaMixin:
    """
    Миксин для стеклянной матрешки
    """

    def __init__(self):
        self.material = 'Стекло'

    def open(self):
        """
        Открывает матрешку
        """
        print('Стеклянная матрешка открывается')

    def get_it_broke(self):
        print('Стеклянная матрешка разбилась')


class BigGlassMatryoshka(BigMatryoshka, GlassMatryoshkaMixin):
    """
    Большая стеклянная матрешка
    """

    def __init__(self, color):
        super().__init__(color)


# big_glass_matryoshka = BigGlassMatryoshka('Красный')
# big_glass_matryoshka.open()

# Смотрим порядок разрешения методов
print(BigGlassMatryoshka.mro())