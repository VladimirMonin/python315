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