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

"""


# Напишем тестовый класс

class Test:

    def get_sum(self):
        return self.a + self.b


# Создадим экземпляр класса
test = Test()
test.a = 10
test.b = 20

print(test.get_sum())  # 30
print(test.__dict__)  # {'a': 10, 'b': 20}
