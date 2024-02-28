"""
Lesson 22
28.02.2024
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`
- Функция `getattr()`
- Атрибут `__dict__`
- Функция `dir()` и метод `__dir__()`
- классы без __init__
- __str__ - пользовательское представление объекта
- __repr__ - техническое представление объекта
- eval() - встроенная функция для выполнения строки как код Python
- __len__ - метод для определения длины объекта !!!
"""


# Напишем класс Person, который будет содержать информацию о человеке

class Person:
    def __init__(self, name: str, age, address: str):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self) -> str:
        """
        Метод для представления объекта в виде строки
        Используется для вывода информации о объекте через print()
        :return:
        """
        return f"Информация о человеке: {self.name}, {self.age}, {self.address}"

    def __repr__(self) -> str:
        """
        Метод для представления объекта в виде строки
        Используется для возможности воссоздать объект через eval()
        Вторично: для вывода информации о объекте через print()
        :return:
        """
        return f"{self.__class__.__name__}('{self.name}', '{self.age}', '{self.address}')"


# Создадим экземпляр класса Person
person = Person('Николай', 25, 'USA')
person2 = Person("Абрахам", 35, "Канада")

persons = [person, person2]

print(person)
print(person2)

[print(person) for person in persons]

print(dir(person))

# Получим значение __repr__ для person
repr_str = repr(person)
print(repr_str)
# Воссоздадим объект person из строки
# Person('Николай', 25, 'USA')
# Person(Николай, 25, USA)

new_person = eval(repr_str)
print(new_person)
# Практика
"""
Касса самообслуживания
1. Опишите класс Product, который будет содержать информацию о товаре:
- инициализатор
- Название
- Цена
__str__

Опишите цикл ввода товаров в кассу, который будет принимать название и цену товара.
На каждой итерации создавайте экземпляр продукта и складывайте его в список продуктов.

2. Если пользователь вводит ничего, цикл останавливается и выводит список продуктов.
3. Если пользователь вводит более 4 продуктов - raise ValueError - Можно не более 4 продуктов
"""


class Product:
    """
    Класс для создания товаров
    """
    def __init__(self, name: str, price: float):
        """
        Инициализатор класса
        :param name: Название товара
        :param price: Цена товара
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"Товар: {self.name}, Цена: {self.price}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.price}')"


products = []
PRODUCT_LIMIT = 4

while True:
    if len(products) > PRODUCT_LIMIT:  # Если пользователь ввел более 4 продуктов
        raise ValueError(f"Можно не более {PRODUCT_LIMIT} продуктов")

    name = input("Введите название товара: ")  # Вводим название товара

    if not name:  # Если пользователь ввел пустую строку
        break

    price = float(input("Введите цену товара: "))  # Вводим цену товара

    product = Product(name, price)  # Создаем экземпляр класса Product
    products.append(product)

print(products) # Это будет принт repr
[print(product) for product in products]  # Это будет принт str