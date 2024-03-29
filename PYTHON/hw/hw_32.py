"""
Разбор домашнего задания 32
Создание декораторов


ЧАСТЬ 1

1. **Напишите функцию `password_checker`, которая будет являться декоратором**.
Декоратор должен проверять сложность пароля согласно следующим условиям:

   - Длина пароля должна быть не менее 8 символов.
   - Пароль должен содержать хотя бы одну цифру.
   - Пароль должен содержать хотя бы одну заглавную букву.
   - Пароль должен содержать хотя бы одну строчную букву.
   - Пароль должен содержать хотя бы один спецсимвол (например, !, @, #, $ и т.д.).

   Если пароль соответствует всем условиям, функция-декоратор должна вызвать
   оригинальную функцию. В противном случае, вернуть сообщение об ошибке.

2. **Напишите функцию `register_user`, которая будет принимать пароль в качестве аргумента**.
Эта функция будет возвращать сообщение о успешной регистрации, если пароль прошел проверку,
и сообщение об ошибке в противном случае.

3. **Используйте декоратор `@password_checker` для функции `register_user`**.
При вызове функции `register_user`, декоратор должен автоматически проверить сложность пароля.

4. **Напишите примеры использования декоратора для проверки сложности пароля**:
   - Вызовите функцию `register_user` с разными паролями, включая те, которые соответствуют всем условиям и те, которые
   не соответствуют хотя бы одному из условий.
   - Выведите соответствующие сообщения об успешной регистрации или об ошибках.
"""
import csv
from typing import Callable

# """
# Параметры можно захардкодить - задать жестко внутри декоратора. Это приемлимо для этого ДЗ.
# Однако, тут нужен декоратор с параметрами.
#
# Я же сделаю компромисный вариант с контантами
#
#    - Длина пароля должна быть не менее 8 символов.
#    - Пароль должен содержать хотя бы одну цифру.
#    - Пароль должен содержать хотя бы одну заглавную букву.
#    - Пароль должен содержать хотя бы одну строчную букву.
#    - Пароль должен содержать хотя бы один спецсимвол (например, !, @, #, $ и т.д.).
#
# """
#
# LEN_THRESHOLD = 8
# DIGIT_THRESHOLD = 1
# UPPERCASE_THRESHOLD = 1
# LOWERCASE_THRESHOLD = 1
# SPEC_SYMBOL_THRESHOLD = 1
SPEC_SYMBOLS = '!@#$%^&*()_+'
#
#
# def password_checker(func: Callable) -> Callable:
#     def wrapper(password: str) -> str | None:
#         if len(password) < LEN_THRESHOLD:
#             return 'Пароль слишком короткий'
#         if sum([1 for i in password if i.isdigit()]) < DIGIT_THRESHOLD:
#             return 'Пароль должен содержать хотя бы одну цифру'
#         if sum([1 for i in password if i.isupper()]) < UPPERCASE_THRESHOLD:
#             return 'Пароль должен содержать хотя бы одну заглавную букву'
#         if sum([1 for i in password if i.islower()]) < LOWERCASE_THRESHOLD:
#             return 'Пароль должен содержать хотя бы одну строчную букву'
#         if sum([1 for i in password if i in SPEC_SYMBOLS]) < SPEC_SYMBOL_THRESHOLD:
#             return 'Пароль должен содержать хотя бы один спецсимвол'
#         return func(password)
#
#     return wrapper
#
#
# @password_checker
# def register_user(password: str) -> str:
#     return f'Пользователь успешно зарегистрирован с паролем: {password}'
#
#
# print(register_user('1238Ff#234234'))  # Пароль должен содержать хотя бы одну заглавную букву

"""
# Домашнее задание. Часть 2 📃


Необходимо создать два декоратора для валидации пользовательских данных перед их сохранением в CSV формате. 

Первый декоратор (`password_validator`) проверяет:
- сложность пароля
- включая его длину
- количество букв верхнего и нижнего регистра
- и количество спец-знаков. 

Второй декоратор (`username_validator`) проверяет, что в имени пользователя **отсутствуют** пробелы. Создайте функцию (`register_user`), которая принимает имя пользователя и пароль, и дозаписывает их в CSV файл, обернув ее **обоими** декораторами.

### Требования:

1. **Декоратор `password_validator`:**
   - Принимает параметры: `min_length` (минимальная длина пароля, по умолчанию 8), `min_uppercase` (минимальное количество букв верхнего регистра, по умолчанию 1), `min_lowercase` (минимальное количество букв нижнего регистра, по умолчанию 1), `min_special_chars` (минимальное количество спец-знаков, по умолчанию 1).
   - Проверяет, соответствует ли пароль заданным критериям.
   - Если пароль не соответствует критериям, выбрасывает `ValueError` с описанием того, что именно не выполнено.

2. **Декоратор `username_validator`:**
   - Не принимает параметров.
   - Проверяет, что в имени пользователя отсутствуют пробелы.
   - Если в имени пользователя есть пробелы, выбрасывает `ValueError` с подробным описанием проблемы.

3. **Функция `register_user`:**
   - Принимает две строки: `username` (имя пользователя) и `password` (пароль).
   - Дозаписывает имя пользователя и пароль в CSV файл.
   - Оборачиваем функцию **обоими** декораторами для валидации введенных данных.
"""


def password_validator(min_length: int = 8, min_uppercase: int = 1,
                       min_lowercase: int = 1, min_special_chars: int = 1):
    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if len(password) < min_length:
                raise ValueError('Пароль слишком короткий')
            if sum([1 for i in password if i.isupper()]) < min_uppercase:
                raise ValueError('Пароль должен содержать хотя бы одну заглавную букву')
            if sum([1 for i in password if i.islower()]) < min_lowercase:
                raise ValueError('Пароль должен содержать хотя бы одну строчную букву')
            if sum([1 for i in password if i in SPEC_SYMBOLS]) < min_special_chars:
                raise ValueError('Пароль должен содержать хотя бы один спецсимвол')
            return func(username, password)

        return wrapper

    return decorator


def username_validator(func: Callable) -> Callable:
    def wrapper(username: str, password: str) -> str:
        if ' ' in username:
            raise ValueError('Имя пользователя не должно содержать пробелы')
        return func(username, password)

    return wrapper


@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
@username_validator
def register_user2(username: str, password: str) -> str:
    with open('users.csv', 'a', encoding='windows-1251') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow([username, password])


register_user2('user_name', '123sfsfFJD(&(&sf8')  # Имя пользователя не должно содержать пробелы