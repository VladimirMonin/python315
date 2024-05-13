-- Lesson 40: Запросы в одной таблице
-- 13.05.2024

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


-- Логические операторы в WHERE
-- По приоритету:

-- () - скобки
-- NOT - не
-- AND - и
-- OR - или

-- Операторы сравнения в WHERE
-- = - равно
-- <> - не равно
-- > - больше
-- < - меньше
-- >= - больше или равно
-- <= - меньше или равно
-- BETWEEN - между
-- IN - в списке
-- IS NULL - пусто
-- IS NOT NULL - не пусто
-- LIKE - похоже на


-- Знакомимся с логическими операторами в SQL
-- 1. Персонажи Blond Hair и Blue Eyes

SELECT name, hair, eye, APPEARANCES
FROM MarvelCharacters
WHERE hair = 'Blond Hair' AND eye = 'Blue Eyes'
ORDER BY APPEARANCES DESC
LIMIT 5;

-- Практика
-- 2. Персонажи с красными глазами или черными волосами
-- Появлений больше 100 сортированы по году появления и по количеству появлений по убыванию

SELECT name, hair, eye, APPEARANCES, year
FROM MarvelCharacters
WHERE (eye = 'Red Eyes' OR hair = 'Black Hair')
AND APPEARANCES > 100
ORDER BY year, APPEARANCES DESC


-- Уберем NULL значения

SELECT name, hair, eye, APPEARANCES, year
FROM MarvelCharacters
WHERE (eye = 'Red Eyes' OR hair = 'Black Hair')
AND APPEARANCES > 100
AND eye NOT NULL
AND hair NOT NULL
AND year NOT NULL
ORDER BY year, APPEARANCES DESC

-- Практика
-- Выборка: имя, цвет глаз, количество появлений, год появления
-- Найдите персонажей с  Variable Eyes
-- Появлений больше 100, исключите все NULL значения
-- Сортировка по году появления и по количеству появлений по убыванию