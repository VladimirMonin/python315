"""
Lesson 30
27.03.2024
Class decorators
Meta classes
Вложенные классы
Итераторы
Сериализация
"""

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'Экземпляр класса Person: {self.name}, {self.age}'



# Класс итератор, который примет назвнаие txt файла и будет возвращать по одной строке из файла
# Преобразовывая это в экземпляр класса Person
    
class PersonTXTIterator:
    def __init__(self, file_name: str, encoding: str = "utf-8"):
        self.file_name = file_name
        self.file = open(file_name, "r", encoding="utf-8")

    def __iter__(self):
        return self

    def __next__(self) -> Person:
        line = self.file.readline().strip()
        if not line:
            self.file.close()
            raise StopIteration
        # Используем eval для преобразования строки в Person
        result = None
        try:
           result: Person = eval(line)
        except Exception as e:
            print(e)
        
        return result
    

"""
Датасет для теста (содержимое файла)
Person(name='Тимур', age=25)
Person(name='Павел', age=30)
Person(name='Оксана', age=22)
Person(name='Алексей', age=35)
Person(name='Виталий', age=27)
"""

FILE = r"data\persons.txt"
person_iterator = PersonTXTIterator(FILE)

for person in person_iterator:
    print(person)