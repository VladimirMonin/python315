"""
Lesson 8 - условные операторы и методы строк
18.12.2023

- Работа со строками
- Методы строк
- Вложенные условия
- Практика (замена подстроки в строке)
- Совмещаем с логическими операторами и методами строк
- Реализация сложных проверок (вложенные условия) VS плоская структура
- Проверка email (пример сложной проверки)

Методы строк. От самых часто используемых к менее используемым

str.lower() - приводит строку к нижнему регистру
str.upper() - приводит строку к верхнему регистру
str.replace() - заменяет одну подстроку на другую
str.split() - разделяет строку на части по разделителю
str.join() - склеивает строки в одну строку с помощью разделителя
str.capitalize() - приводит строку к виду "Слово cлово слово"
str.title() - приводит строку к виду "Слово Слово Слово"
str.strip() - удаляет пробелы в начале и в конце строки
str.count() - считает количество вхождений подстроки в строку
str.find() - возвращает индекс первого вхождения подстроки в строку, -1 если подстрока не найдена
str.index() - возвращает индекс первого вхождения подстроки в строку, ValueError если подстрока не найдена
str.startswith() - проверяет, начинается ли строка с подстроки
str.endswith() - проверяет, заканчивается ли строка подстрокой
str.isalpha() - проверяет, состоит ли строка только из букв
str.isdigit() - проверяет, состоит ли строка только из цифр
str.isalnum() - проверяет, состоит ли строка только из цифр и букв
str.isspace() - проверяет, состоит ли строка только из пробелов
str.istitle() - проверяет, является ли строка заголовком
str.islower() - проверяет, состоит ли строка только из символов в нижнем регистре
str.isupper() - проверяет, состоит ли строка только из символов в верхнем регистре
str.lstrip() - удаляет пробелы в начале строки
str.rstrip() - удаляет пробелы в конце строки
str.swapcase() - меняет регистр каждой буквы в строке на противоположный
str.rfind() - возвращает индекс последнего вхождения подстроки в строку
str.rindex() - возвращает индекс последнего вхождения подстроки в строку
str.rsplit() - разделяет строку на части по разделителю, начиная с конца

"""
# pal1 = "А роза упала на лапу Азора"
# pal2 = "Аргентина манит негра"
# pal3 = "Я иду с мечем судия"
# pal4 = "Я несу гусеня"
# pal5 = "Кот учён, но не чуток"
# pal6 = "А вот и харя рахитова"
#
# palindrome = pal6
# palindrome = palindrome.lower()
# palindrome = palindrome.replace(' ', '').replace(',', '').replace('ё', 'е')
#
# if palindrome == palindrome[::-1]:
#     print(f"{palindrome} - {palindrome[::-1]}- палиндром")
#
# else :
#     print(f"{palindrome} - {palindrome[::-1]}- не палиндром")


# data_user = str.lower(input('Введите слово для проверки на палиндром: '))
# print(data_user)
# data_user = " + ".join(data_user)
# print(type(data_user))
# print(len(data_user))
# if data_user == data_user[::-1]:
#     print(f'{data_user} - это палиндром')
# else:
#     print(f'{data_user} не палиндром')

# palindrome = input('Введите слово для проверки на палиндром: ').lower().replace(' ', '').replace(',', '').replace(
# 'ё', 'е')

# palindrome = input('Введите слово для проверки на палиндром: ')
# row_palindrome = palindrome.lower().replace(' ', '').replace(',', '').replace('ё', 'е')
#
# if row_palindrome == row_palindrome[::-1]:
#     print(f"{palindrome} - палиндром")
#
# else:
#     print(f"{palindrome} - не палиндром")

# TODO: Практика 1
"""
Напишите программу:
1. Пользователь вводит строку
2. Пользователь вводит подстроку которую надо заменить
3. Пользователь вводит подстроку на которую надо заменить
4. Напечатайте исходную строку
5. Напечатайте измененную строку
"""


# main_string = input('Введите строку: ')
# sub_string = input('Введите подстроку которую надо заменить: ')
# new_sub_string = input('Введите подстроку на которую надо заменить: ')
#
# print(f'Исходная строка: {main_string}')
# print(f'Измененная строка: {main_string.replace(sub_string, new_sub_string)}')

# НЕ НАДО ТАК. Это плохой код
# print(input('Введите строку: ').replace(input('Введите подстроку которую надо заменить: '),
#                                         input('Введите подстроку на которую надо заменить: ')))


# .title() - приводит строку к виду "Слово cлово слово"
# .capitalize() - приводит строку к виду "Слово слово слово"

# print(input('Введите имена друзей').title())
# friends = input('Введите имена друзей: ').title()
# print(friends)

# Плоская и вложенная структура проверки
# Проверим строку, что в ней буквы Р менее чем пороговое значение и нет цифр и нет спецзнаков
LETTER = 'р'
THRESHOLD = 2

report_string = ''
string = 'Арарат пять звёзд'

# Первая проверка, что в строке нет цифр
if string.isdigit():
    report_string += 'В строке есть цифры\n'
else:
    report_string += 'В строке нет цифр\n'

# Вторая проверка, что в строке нет спецзнаков
if not string.replace(' ', '').isalnum():
    report_string += 'В строке есть спецзнаки\n'
else:
    report_string += 'В строке нет спецзнаков\n'

# Третья проверка, что в строке буквы Р меньше чем пороговое значение
if string.lower().count(LETTER) < THRESHOLD:
    report_string += f'В строке букв {LETTER} меньше {THRESHOLD}\n'

else:
    report_string += f'В строке букв {LETTER} больше {THRESHOLD}\n'

print(report_string)

#То же самое только проверка в одну строку с AND и всего одним принтом
if string.isdigit() and not string.replace(' ', '').isalnum() and string.lower().count(LETTER) < THRESHOLD:
    print('В строке есть цифры, спецзнаки и буквы Р меньше чем пороговое значение')


# То же самое только в виде вложенной структуры

# Первая проверка, что в строке нет цифр
if string.isdigit():
    report_string += 'В строке есть цифры\n'

    # Вторая проверка, что в строке нет спецзнаков
    if not string.replace(' ', '').isalnum():
        report_string += 'В строке есть спецзнаки\n'

        # Третья проверка, что в строке буквы Р меньше чем пороговое значение
        if string.lower().count(LETTER) < THRESHOLD:
            report_string += f'В строке букв {LETTER} меньше {THRESHOLD}\n'

        else:
            report_string += f'В строке букв {LETTER} больше {THRESHOLD}\n'

    else:
        report_string += 'В строке нет спецзнаков\n'
else:
    report_string += 'В строке нет цифр\n'


# Проверка email
"""
0. спецзнаки - только: . @ - _
1. не должно быть пробелов
2. должна быть @
3. должна быть точка
- точек может быть много
- последняя точка должна быть после @

4. собака не должна быть:
- первым символом
- последним символом
- повторяться
- рядом с точкой
- после точки

Проверка на длину (сразу)
Проверка на одну собаку до того как уберем "хорошие" спецзнаки
Проверка на индекс собаки до того как уберем "хорошие" спецзнаки (он должен быть больше 0 и меньше длины строки на PROXIMITY_POINT_AT + 2
Проверка на близость собаки к точке - до того как мы убрали "хорошие" спецзнаки
Убираем "хорошие" спецзнаки через replace
Проверка на спецзнаки. Можно сделать после того как уберем "хорошие" спецзнаки

"""


# Плоская структура проверки
LEN_THRESHOLD = 5
GOOD_SPECIAL_SYMBOLS = '.@-_'
PROXIMITY_POINT_AT = 2

bad_report_string = ''

email = 'vlad@i mir_monin@dodo.pizza'

# Проверка на длину
if len(email) < LEN_THRESHOLD:
    bad_report_string += f'Email должен быть не менее {LEN_THRESHOLD} символов\n'

# Проверка на одну собаку
if email.count('@') != 1:
    bad_report_string += 'Email должен содержать одну собаку\n'

# Проверка на индекс собаки
if not 0 < email.index('@') < len(email) - PROXIMITY_POINT_AT:
    bad_report_string += 'Собака должна быть не первым и не последним символом и быть не близко к точке\n'

# Проверка на близость собаки к точке
# Найдем последнюю точку (первую справа)
last_point_index = email.rindex('.')
# Найдем индекс собаки
dog_index = email.rindex('@')

# Если последняя точка близко к собаке
if last_point_index - dog_index < PROXIMITY_POINT_AT:
    bad_report_string += 'Собака должна быть не близко к точке\n'

# Делаем серию замен
clear_email = email.replace('.', '').replace('@', '').replace('-', '').replace('_', '')

# Проверка на спецзнаки
if not clear_email.isalnum():
    bad_report_string += 'Вы использовали недопустимые символы\n'


if bad_report_string:
    print(f'Ваш email не прошел проверку по следующим причинам:\n{bad_report_string}')
else:
    print('Ваш email прошел проверку!')




