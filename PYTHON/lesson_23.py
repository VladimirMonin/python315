"""

- Понятие родительского класса и дочернего класса
- Когда наследование имеет смысл?
- Синтаксис наследования
- Наследование без явного указания инициализатора родительского класса
- Переопределение методов и атрибутов родительского класса
- Работа с инициализатором и явное указание инициализатора родительского класса
- Super - вызов методов родительского класса
- Практика
- Решение практики
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

# Понятие родительского класса и дочернего класса
"""
Родительский класс (суперкласс) - класс, от которого наследуются свойства и методы
Дочерний класс (подкласс) - класс, который наследует свойства и методы родительского класса
"""


class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def speak(self):
        print(f"Меня зовут {self.name}.")

    def __str__(self):
        return f'Animal: {self.name, self.age}'


class Dog(Animal):
    def speak(self):
        print(f"Меня зовут {self.name}, и я собака. Woof!")


dog1 = Dog('Rex')
dog1.speak()
print(dog1)
