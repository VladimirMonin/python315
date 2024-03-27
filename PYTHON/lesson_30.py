"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Сериализация
"""

# 2 половины конструктора класса __init__ и __new__


class First:
    def __init__(self, name):
        self.name = name
        print("First.__init__")

    def __new__(cls, *args, **kwargs):
        print("First.__new__")
        return super().__new__(cls)
    
    def custom_method(self, x):
        print(f"First.custom_method {x}")


class Second(First):
    def __init__(self, name, last_name):
        self.last_name = last_name
        print("Second.__init__")
        super().__init__(name)

    def custom_2_method(self, x):
        print("Second.custom_2_method")
        # First.custom_method(self, x)
        super().custom_method(x)

s = Second("Ivan", "Ivanov")
s.custom_2_method(1111111111111111111111)