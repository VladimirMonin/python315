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
    marks = ['М-1', 'М-2', 'М-3', 'М-4', 'М-5']

    def __init__(self, mark: str, material: str, diameter: int, length: int):
        self.mark = self.mark_validate(mark)
        self.material = material
        self.diameter = diameter
        self.length = length

    def mark_validate(self, mark: str):
        if mark not in self.marks:
            raise ValueError(f'Марка {mark} не доступна для трубы. Выберите из {self.marks}')
        return mark

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        return f'Труба {self.mark} из {self.material} диаметром {self.diameter} мм длиной {self.length} м'


pipe = Pipe('М-1', 'Сталь', 100, 1000)
# pipe2 = Pipe('Труба', 'Сталь', 100, 1000) # ValueError: Марка Труба не доступна для трубы. Выберите из ['М-1', 'М-2', 'М-3', 'М-4', 'М-5']

pipe.mark = "Труба"

