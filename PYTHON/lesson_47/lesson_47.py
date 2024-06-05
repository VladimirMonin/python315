# Lesson 47
# 05.06.2024
# SQLite3 - встроенная библиотека для работы с базами данных

# Методы объекта подключения:
# commit() - сохранение изменений
# close() - закрытие соединения
# rollback() - откат изменений

# Основные методы курсора:
# execute() - выполнение запроса
# executemany() - выполнение запроса много раз
# executescript() - выполнение нескольких запросов
# fetchone() - получение одной строки результата
# fetchall() - получение всех строк результата
# fetchmany() - получение заданного количества строк результата

import sqlite3

ROW_SQL = """

-- Таблица котики
-- id, name, id_shop

CREATE TABLE Cats (
    CatID INTEGER PRIMARY KEY AUTOINCREMENT,
    CatName TEXT,
    ShopID INTEGER,
    FOREIGN KEY (ShopID) REFERENCES Shops (ShopID)
);

-- Таблица магазинов
-- ShopID, ShopName

CREATE TABLE Shops (
    ShopID INTEGER PRIMARY KEY AUTOINCREMENT,
    ShopName TEXT
);

-- Добавим 3 магазина и 4й без названия
INSERT INTO Shops (ShopName) VALUES
    ('Зоомагазин "Котики"'),
    ('Зоомагазин "Кошки"'),
    ('Зоомагазин "Коты"'),
    (NULL);

-- Добавим несколько котиков с именем, и без имени
INSERT INTO Cats (CatName, ShopID) VALUES
    ('Мурка', 1),
    ('Барсик', 2),
    ('Матроскин', 4),
    (NULL, 3);

"""

# Создание объекта подключения к базе данных lesson_47.db

conn = sqlite3.connect(r'./lesson_47.db')

# Создание объекта курсора - это основной объект для выполнения запросов
cursor = conn.cursor()

# Выполнение скрипта
cursor.executescript(ROW_SQL)

# Сохранение изменений
conn.commit()

#TODO - Почему база создалась в директории на 2 уровня выше а не в текущей?