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


# __len__ - метод для определения длины объекта

# класс Труба. Макрка, материал, диаметр, длина

class Pipe:
    # Допустимые марки в атрибуте класса
    def __init__(self, mark: str, material: str, diameter: int, length: int):
        self.mark = mark
        self.material = material
        self.diameter = diameter
        self.length = length

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return f'Труба {self.mark} из {self.material} диаметром {self.diameter} мм длиной {self.length} м'


pipe = Pipe('Труба', 'Сталь', 100, 500)
pipe2 = Pipe('Труба', 'Сталь', 100, 1000)

print(len(pipe))  # 500
print(len(pipe2))  # 1000

print(len(pipe) > len(pipe2))  # False