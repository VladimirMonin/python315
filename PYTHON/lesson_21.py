"""
Знакомство с ООП
- Зачем это нужно?
- Какие преимущества?
- Синтаксис
- Нейминг классов
"""


# Синтаксис - class <Имя класса>:
class LadaCar:
    price = 100500
    color = 'black'


# Нейминг классов - UpperCamelCase - каждое слово с большой буквы
# Максимально описательное имя класса

# Как объявить пустой сет?
some_set = set()

# Создание экземпляра класса
lada = LadaCar()
lada2 = LadaCar()
lada3 = LadaCar()

# Доступ к атрибутам класса
print(lada.price)

# Изменение атрибутов класса
lada.color = 'red'
lada.price = 1
print(lada.color)
print(lada.price)

print(lada2.color)
print(lada2.price)


# Атрибуты экземпляра класса и инициализация

class ToyotaCar:
    # Производитель - классовый атрибут
    manufacturer = 'Кировский завод №1'

    def __init__(self, price, color):
        self.price = price
        self.color = color
        print(f'Создан новый объект класса ToyotaCar '
              f'с ценой {self.price} и цветом {self.color}'
              f' от производителя {self.manufacturer}')

        # Распечатаем данные о производителе через обращение к классу
        print(f'Производитель: {ToyotaCar.manufacturer}')
        print(f'Производитель: {__class__.manufacturer}')

        # Распечатаем имя класса
        print(f'Имя класса: {__class__.__name__}')


toyota = ToyotaCar(200000, 'black')
print(toyota.price)

toyota2 = ToyotaCar(250000, 'yellow')
print(toyota2.price)

print(ToyotaCar.manufacturer)
# print(__class__.manufacturer)