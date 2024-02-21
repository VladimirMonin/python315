"""
Lesson 2
06.12.2023

Знакомство с Python
Комментарии в коде
Переменные
В Пайтон - все - объекты!
Смотрим на то что две переменных могут указывать на один объект
Синтаксические и логические ошибки
Правила именования переменных
Основные (простые) типы данных
Строки. Управляющие последовательности
Экранирование
Многострочные строки
"""
# Комментарии в коде
# Первый принт!
print('Hello, Python315!')  # Выводим приветствие

# Переменные
# a = 'Привет!'
# b = "Привет!"

# ID - идентификатор объекта
# print(id(a))
# print(id(b))

# print(1/0) # ZeroDivisionError: division by zero
# print(b # SyntaxError

# НЕ НАДО ТАК!
# имя = "Владимир"
# фамилия = "Монин"
# возраст = 20
# print(имя, фамилия, возраст)
#
# imia = "Владимир"
# familia = "Монин"
# vozrast = 20
#
# a = "Владимир"
# b = "Монин"
# c = 20

"""
Правила именования переменных

0. Регистрозависимость
1. Английский язык
2. Существительные
3. Имя должно быть осмысленным
4. Имя должно передавать суть переменной
5. Имя не должно быть слишком длинным
6. Имя не должно начинаться с цифры
7. Имя не должно содержать спецсимволов и пробелов
8. _  - можно
9. Имя не должно быть ключевым словом, функцией, зарезервированным словом
10. Snake case - имя_переменной
"""
# Сломал принт!
# print = 5
# print(print)

# Основные (простые) типы данных
# Строки. String. str. Функция str()
# Целые числа. Integer. int. Функция int()
# Вещественные числа. Float. float. Функция float()
# Пока остановимся тут!)

# Оставим на потом...
# Логический тип данных. Boolean. bool. Функция bool()
# Список. List. list. Функция list()
# Кортеж. Tuple. tuple. Функция tuple()
# Множество. Set. set. Функция set()
# Словарь. Dictionary. dict. Функция dict()


# Строки!
name = "Cергей"
surname = 'Петров'

print(name, surname)
print(name)
print(surname)

message_string = 'Сегодня я ел "Наполеон"'
print(message_string)

poem = """
Скажи-ка, дядя, ведь не даром,
Москва, спаленная пожаром,
Французу отдана?

Ведь были ж схватки боевые,
Да, говорят, еще какие!
Недаром помнит вся Россия
Про день Бородина!

            М. Ю. Лермонтов
"""

print(poem)

# Управляющие последовательности
# \n - перенос строки
# \t - табуляция

print("Скажи-ка, дядя, ведь не даром,\n"
      "Москва, спаленная пожаром,\n"
      "Французу отдана?\n\n"
      "Ведь были ж схватки боевые,\n"
      "Да, говорят, еще какие!\n"
      "Недаром помнит вся Россия\n"
      "Про день Бородина!"
      "\n\n\t\t\t\t\tМ. Ю. Лермонтов")

# \ - экранирование

print("Вот почему я не ем \"Наполеон\"")
print('\\')

# Печатаем пароль!
difficult_password = "\nsfs\t234dfg\\"
print(difficult_password)

difficult_password2 = r"\nsfs\t234dfg\\"
print(difficult_password2)

# Форматированные строки
name = "Владимир"
surname = "Монин"
age = 35

message = "Привет, меня зовут" + " " + name + " " + surname + " " + "мне" + " " + str(age) + " " + "лет"
message_2 = f"Привет, меня зовут {name} {surname} мне {age} лет"
message_3 = f'Привет, меня зовут {name} {surname} мне {str(age)} лет'
print(message)
print(message_2)
print(message_3)