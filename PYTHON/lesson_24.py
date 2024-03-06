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
        pass




# abstract = AbstractMatryoshka() # TypeError: Can't instantiate abstract class AbstractMatryoshka with abstract methods open

big = BigMatryoshka('Красный')
print(big)


class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B, C):
    pass

print(D.mro())

print(issubclass(D, A))
print(issubclass(D, C))
print(issubclass(D, D))
print(issubclass(D, object))

print(isinstance(big, BigMatryoshka))
print(isinstance(big, AbstractMatryoshka))

#
# TypeError: Cannot create a consistent method resolution order (MRO) for bases
# ПОЛУЧИМ ЕГО!

