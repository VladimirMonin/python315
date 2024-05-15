-- Lesson 41: GROUP BY и агрегатные функции
-- 15.05.2024

-- Рабочая таблица
-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identify         TEXT,
--     ALIGN            TEXT,
--     EYE              TEXT,
--     HAIR             TEXT,
--     SEX              TEXT,
--     GSM              TEXT,
--     ALIVE            TEXT,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER
-- );


-- GROUP BY и агрегатные функции
-- GROUP BY - группировка строк по значениям столбца. Похоже на DISTINCT, но с возможностью использования агрегатных функций

SELECT eye
FROM MarvelCharacters
GROUP BY eye;

SELECT DISTINCT eye
FROM MarvelCharacters;

-- В чем разница между этими запросами? 
-- Тут мы можем сделать так:

SELECT eye, COUNT(*)
FROM MarvelCharacters
GROUP BY eye
ORDER BY COUNT(*) DESC;

-- Уберем Null и значения меньше 20

SELECT eye, COUNT(*)
FROM MarvelCharacters
WHERE eye IS NOT NULL
GROUP BY eye
HAVING COUNT(*) > 20

-- В чем разница, передать * или название столбца?
-- Передать * - это считать все строки, передать название столбца - это считать только значения без NULL

-- Практика
-- Посчитайте количество персонажей, критерий: hair


-- Самый популярный цвет волос персонажей 60х
-- Найдем имя персонажа, год появления и количество появлений и цвет волос через MAX и GROUP BY

SELECT name as Имя, hair as Цвет, MAX(APPEARANCES) as Появлений, year as Год, COUNT(*) as "Всего персонажей"
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969
GROUP BY hair
ORDER BY COUNT(*) DESC

-- Практика 
-- Попробуйте выполнить этот запрос для eye (цвет глаз)
SELECT name as Имя, eye as Глаза, MAX(APPEARANCES) as Появлений, year as Год, COUNT(*) as "Всего персонажей"
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969
GROUP BY eye
ORDER BY COUNT(*) DESC



SELECT name AS Имя, Eye AS "Цвет глаз", year AS "Год появления", COUNT(*) AS "Всего персонажей"
FROM MarvelCharacters
WHERE Year BETWEEN 1960 AND 1969 AND (Eye IS NOT NULL)
GROUP BY Eye
ORDER BY COUNT(*) DESC

-- MAX - найдем персонажа с максимальным количеством появлений
SELECT name, MAX(APPEARANCES)
FROM MarvelCharacters

SELECT MAX(YEAR) as "Последний год"
FROM MarvelCharacters

-- Выведем персонажа с максимальной длиной имени
SELECT name, LENGTH(name)
FROM MarvelCharacters
ORDER BY LENGTH(name) DESC
LIMIT 1

-- Попробуем поместить length в max
SELECT name, MAX(LENGTH(name))
FROM MarvelCharacters

-- 18. **Название: Персонажи с максимальным количеством появлений в десятилетие**
--     - **Описание:** Найти персонажа с максимальным количеством появлений в каждом десятилетии начиная с 1940-х. Вывести десятилетие, имя персонажа и количество появлений.
--     - **Выборка:** Группировка по десятилетиям (используя год), определение персонажа с максимальным количеством появлений в каждом десятилетии.