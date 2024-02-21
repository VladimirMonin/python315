"""
hw_28.py - Разбор домашнего задания Игра в Города на функциях
"""
import json
from typing import List, Dict, Any, Set

from data.cities import cities_list

CITIES_JSON = '../../data/cities.json'


def write_cities_to_json(cities_list: List[Dict[str, Any]], file_path=CITIES_JSON) -> None:
    """
    Функция для записи списка городов в файл json
    :param cities_list: Список городов из cities.py
    :param file_path: Путь к файлу
    """
    data = [city['name'] for city in cities_list]
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def read_cities_from_json(file_path: str = CITIES_JSON) -> Set[str]:
    """
    Функция для чтения сета городов из файла json
    :param file_path: Путь к файлу
    :return: Set городов
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return set(data)


def get_unique_letters_set(cities_set: Set[str]) -> Set[str]:
    """
    Функция для получения сета уникальных букв, который используется
    при поиске плохих букв
    :param cities_set: Сет городов
    :return: Сет уникальных букв
    """
    return set(''.join(cities_set).lower())


def get_bad_letters_set(cities_set: Set[str], unique_letters_set: Set[str]) -> Set[str]:
    """
    Функция для получения сета плохих букв. Ищет такие буквы, с которых не начинается
    ни один город из сета городов.
    :param unique_letters_set:
    :param cities_set: Сет городов
    :return: Сет плохих букв
    """
    bad_letters_set = set()

    # Берем букву и идем проверять
    for letter in unique_letters_set:
        # Берем город и проверяем его первую букву
        for city in cities_set:
            # Город НЕ плохой, буква НЕ плохая
            # Нет смысла итерироваться дальше по городам
            if city[0].lower() == letter:
                break
        else:
            # Цикл закончился без break - буква плохая
            bad_letters_set.add(letter)

    return bad_letters_set


def is_last_letter_match(first_city: str, second_city: str) -> bool:
    """
    Функция для проверки заканчивается ли первый город на последнюю букву второго города
    :param first_city: Первый город
    :param second_city: Второй город
    :return: True если последняя буква первого города совпадает с первой буквой второго города
    """
    return first_city[-1].lower() == second_city[0].lower()



# 1. Проверка правил игры (проверка на плохие буквы)
# 2. Ход игрока
# 3. Ход компьютера


def main() -> None:
    # write_cities_to_json(cities_list)
    cities_set = read_cities_from_json()
    unique_letters_set = get_unique_letters_set(cities_set)
    bad_letters_set = get_bad_letters_set(cities_set, unique_letters_set)

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
            if not is_last_letter_match(computer_city, user_city):
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
            # Проверка функией is_last_letter_match
            if is_last_letter_match(user_city, city):
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


if __name__ == '__main__':
    main()