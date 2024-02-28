"""
Lesson 22
28.02.2024
- Функция `hasattr()`
- Функция `delattr()`
- Функция `setattr()`   ???
- Функция `getattr()`
- Атрибут `__dict__`
- Функция `dir()` и метод `__dir__()`

"""


# Напишем тестовый класс

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Создадим экземпляр класса
test = Test(1, 2)

# Проверим, есть ли атрибут `a` у экземпляра класса
print(hasattr(test, 'a'))  # True
print(hasattr(test, 'c'))  # False

# Удалим атрибут `a` у экземпляра класса
delattr(test, 'a')
print(hasattr(test, 'a'))  # False

# Установим атрибут `a` у экземпляра класса
setattr(test, 'a', 10)
print(hasattr(test, 'a'))  # True
print(test.a)  # 10

# Прямое назначение атрибута
test.z = 'z'

# Отличия между прямым назначением атрибута и использованием функции `setattr()`
new_attr_name = 'c'
new_attr_value = 100
test.new_attr_name = new_attr_value
print(test.new_attr_name)  # 100


# Get attribute
print(getattr(test, 'a'))  # 10


test2 = Test(3, 4)
test2.x = 100

# __dict__ - словарь атрибутов экземпляра класса
# __dir__() - список атрибутов экземпляра класса
print(test2.__dict__)  # {'a': 3, 'b': 4, 'x': 100}
print(test.__dict__)
# print(dir(test2))  # ['a', 'b', 'x', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
