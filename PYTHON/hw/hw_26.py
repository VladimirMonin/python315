"""
Разбор домашнего задания №26
"Начинаем делать игру в города"

"""
from data.cities import cities_list

cities_set = {city['name'].title() for city in cities_list}

# Тут надо записать сет в файл json
# Закомментировать код записи, чтобы каждый раз не перезаписывать файл

# Тут надо написать код чтения из файла json
#


# print(cities_set)

# Поиск плохих букв
iter_count = 0
bad_letters_set = set()

# Первый вариант - перебор в цикле ВСЕХ городов
# проверяем их последнюю букву, есть ли в сете город начинающийся на эту букву

for city in cities_set:
    last_letter = city[-1].lower()
    for next_city in cities_set:
        iter_count += 1
        if next_city[0].lower() == last_letter:
            break  # Останавливаем вложенный цикл, когда понимаем что буква НЕ плохая
    else:
        bad_letters_set.add(last_letter)

print(f'{iter_count=}')
print(f'{bad_letters_set=}')

# Второй вариант - перебор в цикле только уникальных букв
# Возьмем сет, превратим его в строку, приведем к регистру, превратим в сет
# Таким образом получим сет уникальных букв
unique_letters_set = set(''.join(cities_set).lower())
print(f'{unique_letters_set=}')

# Проходим циклом по уникальным буквам, проверяем есть ли в сете городов город
# Который начинается на эту букву

bad_letters_set = set()
iter_count = 0

# Берем букву и идем проверять
for letter in unique_letters_set:
    # Берем город и проверяем его первую букву
    for city in cities_set:
        iter_count += 1
        # Город НЕ плохой, буква НЕ плохая
        # Нет смысла итерироваться дальше по городам
        if city[0].lower() == letter:
            break
    else:
        # Цикл закончился без break - буква плохая
        bad_letters_set.add(letter)

print(f'{iter_count=}')
print(f'{bad_letters_set=}')


computer_city = None

# Описываем игру
while True:
    # Ход человека
    user_city = input('Введите город: ').strip().title()

    # Проверка на выход
    if user_city == '0':
        print('Кожаный мешок, ты проиграл!')
        break

    # Проверка на то, что название города есть в списке Городов
    if user_city not in cities_set:
        print('Кожаный мешок, такого города нет!')
        break

    if computer_city:
        # Проверка на последнюю букву
        if user_city[0].lower() != computer_city[-1].lower():
            print('Кожаный мешок, не та буква!')
            break

    # Мы прошли проверки. Удаляем город из сета
    cities_set.remove(user_city)

    # Если бы мы использовали функции - тут можно было бы пересобирать
    # Сет плохих букв, чтобы компьютер не использовал их

    # =======================
    # Ход компьютера

    # Поиск города, соответствующего последней букве человеческого города
    last_user_letter = user_city[-1]

    # Перебираем города в сете
    for city in cities_set:
        # Если первая буква города совпадает с последней буквой человеческого города
        if city[0].lower() == last_user_letter:
            # Проверка на плохую букву
            if city[-1].lower() in bad_letters_set:
                continue

            # Удаляем город из сета
            cities_set.remove(city)
            # Печатаем город
            print(f'Компьютер: {city}')
            # Запоминаем город
            computer_city = city
            break
    else:
        # Если не нашли город - значит компьютер проиграл
        print('Кожаный мешок, ты выиграл!')
        break
