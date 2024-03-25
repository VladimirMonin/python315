"""
Lesosn 29
25.03.2024
Датаклассы Ч2
@dataclass(order=True) - для сравнения
Метаинформация в полях (для сериализации и других целей)
Наследование датаклассов
Декорация классов
Метаклассы - как концепция
"""

from dataclasses import dataclass, field, fields, asdict


@dataclass(order=True)
class AbstractPerson:
    first_name: str = field(metadata={"description": "Имя"})

    def __str__(self):
        """
        Оправданная сложность.
        В наследниках все работает автоматически
        :return:
        """
        meta_str = ", ".join([f"{f.metadata['description']}: {getattr(self, f.name)}" for f in fields(self)])
        return meta_str


@dataclass(order=True)
class Person(AbstractPerson):
    # Исключим лишние поля
    age: int = field(metadata={"description": "Возраст"})
    city: str = field(compare=False, metadata={"description": "Город"})


@dataclass(order=True)
class Employee(Person):
    position: str = field(metadata={"description": "Должность"})
    salary: int = field(metadata={"description": "Зарплата"})


p1 = Employee("Вася", 25, "Москва", "Программист", 100_000)
p2 = Employee("Маша", 30, "Москва", "Программист", 100_000)
p3 = Employee("Аня", 25, "Москва", "Тимлид", 150_000)

"""
### Практика

Задание 1: Сравнение товаров

Цель: Научиться использовать датаклассы для моделирования объектов с возможностью их сравнения.

Описание:
Создайте датакласс Product, который будет описывать товар. 
Датакласс должен включать следующие атрибуты: name (название товара, строка), category (категория, строка), 
price (цена, вещественное число). 

Используйте параметр order=True, чтобы автоматически генерировать методы сравнения на основе цены.

Создайте наследника датакласса Product - датакласс Notebook
с атрибутами
- screen_size (размер экрана, вещественное число).
- cpu (процессор, строка).
- ram (объем оперативной памяти, вещественное число).
Исключите эти атрибуты из сравнения

Создайте еще одного наследника датакласса Product - датакласс Phone
с атрибутами
- brand (бренд, строка).
- os (операционная система, строка).
- memory (объем памяти, вещественное число).

Исключите эти атрибуты из сравнения

Требования к заданию:

    Реализуйте датакласс Product.
    Реализуйте датакласс Notebook.
    Реализуйте датакласс Phone.
    Создайте несколько экземпляров товаров.
    Демонстрируйте сравнение товаров по цене.
    Выведите товары в отсортированном порядке по цене.
"""


@dataclass(order=True)
class Product:
    name: str = field(compare=False)
    category: str = field(compare=False)
    price: float

@dataclass(order=True)
class Notebook(Product):
    screen_size: float = field(compare=False)
    cpu: str = field(compare=False)
    ram: float = field(compare=False)


@dataclass(order=True)
class Phone(Product):
    brand: str = field(compare=False)
    os: str = field(compare=False)
    memory: float = field(compare=False)


n1 = Notebook("Notebook 1", "Notebooks", 1000, 15.6, "Intel Core i5", 8)
n2 = Notebook("Notebook 2", "Notebooks", 1500, 15.6, "Intel Core i7", 16)
n3 = Notebook("Notebook 3", "Notebooks", 1200, 15.6, "Intel Core i5", 8)

p1 = Phone("Phone 1", "Phones", 500, "Samsung", "Android", 128)

products = [n1, n2, n3]
print(sorted(products))

products2 = [n1, n2, n3, p1]
# print(sorted(products2)) # TypeError: '<' not supported between instances of 'Notebook' and 'Phone'
print(sorted(products2, key=lambda product: product.price))