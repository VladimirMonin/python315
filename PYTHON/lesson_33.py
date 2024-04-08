"""
Lesson 33
08.04.2024
- Повторяем dataclasses
"""

from dataclasses import dataclass, field

@dataclass(order=True)
class Person:
    first_name: str = field(compare=False)
    last_name: str = field(compare=False)
    age: int
    growth: float = field(default=0.0, compare=False)
    is_checked: bool = field(default=False, compare=False)

    
    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if self.growth < 0:
            raise ValueError("Рост не может быть отрицательным")
    
    def __bool__(self):
        return self.is_checked
    
    def __len__(self):
        return self.growth




p1 = Person("Филлип", "Киркоров", 50, 2.10)
p2 = Person("Лариса", "Гузеева", 56, 1.65)

print(p1 > p2)
print(p1 < p2)
print(p1)
p1_str = str(p1)
p1_str1 = repr(p1)
print(p1_str)
print(p1_str1)
p1_new = eval(p1_str1)
p1_new1 = eval(p1_str)
print(p1_new)
print(p1_new1)
