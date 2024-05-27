-- Разбор HW_41: запросы SQL в однотабличной базе данных
-- 20.05.2024

-- Структура учебной базы

CREATE TABLE MarvelCharacters (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id          INTEGER,
    name             TEXT,
    urlslug          TEXT,
    identify         TEXT,
    ALIGN            TEXT,
    EYE              TEXT,
    HAIR             TEXT,
    SEX              TEXT,
    GSM              TEXT,
    ALIVE            TEXT,
    APPEARANCES      INTEGER,
    FIRST_APPEARANCE TEXT,
    Year             INTEGER
);

-- 1. **Лысые злодеи 90х годов**
-- - **Описание:** Отобразите имя, первое появление, частота появления. Выведите только тех персонажей, у которых Bald и они злодеи. Год появления между 1990 и 1999
-- - **Выборка:** Имя, год первого появления, количество появлений; где прическа — Bald, align — Bad Characters, и год первого появления между 1990 и 1999. 
-- - **Количество строк:** 94

SELECT name, FIRST_APPEARANCE, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = "Bald" AND ALIGN = "Bad Characters" AND Year BETWEEN 1990 AND 1999

-- 2. **Герои с тайной идентичностью и необычными глазами**
--    - **Описание**: Вывести имя, год первого появления, и цвет глаз. Выбрать персонажей с тайной идентичностью (Secret Identity) и цветом глаз не из обычного спектра (не Blue, Brown, Green).
--    - **Выборка**: Имя, год первого появления, цвет глаз; где идентификация — Secret Identity, и цвет глаз не Blue, Brown, или Green.
--    - **Количество строк**: 1080

SELECT name, FIRST_APPEARANCE, EYE
FROM MarvelCharacters
WHERE identify = "Secret Identity" AND EYE NOT IN ("Blue Eyes", "Brown Eyes", "Green Eyes")
AND APPEARANCES NOT NULL

-- 3. **Персонажи с изменяющимся цветом волос**
--    - **Описание**: Вывести имя и описание цвета волос. Интересуют персонажи с переменным цветом волос (Variable Hair).
--    - **Выборка**: Имя и описание цвета волос; где цвет волос — Variable Hair.
--    - **Количество строк**: 32

SELECT name, HAIR
FROM MarvelCharacters
WHERE HAIR = "Variable Hair"
ORDER BY APPEARANCES DESC


-- 4. **Женские персонажи с редким цветом глаз**
--    - **Описание**: Вывести имена и цвет глаз. Отфильтровать женских персонажей с цветом глаз Gold или Amber.
--    - **Выборка**: Имя, цвет глаз; где пол — женский и цвет глаз Gold или Amber.
--    - **Количество строк**: 5

SELECT name, EYE
FROM MarvelCharacters
WHERE SEX = "Female Characters" AND EYE IN ("Gold Eyes", "Amber Eyes")


-- 5. **Персонажи без двойной идентичности, сортированные по году появления**
--    - **Описание**: Вывести имя и год первого появления FIRST_APPEARANCE. Выбрать персонажей без двойной идентичности (No Dual Identity), сортировка по году появления, сначала новые.
--    - **Выборка**: Имя, год первого появления; где нет двойной идентичности, сортировка по году Year по убыванию.
--    - **Количество строк**: 1788

SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = "No Dual Identity"
ORDER BY Year DESC

-- 6. **Герои и злодеи с необычными прическами**
--    - **Описание**: Вывести имя, align, и описание прически. Найти персонажей с прическами, не являющимися стандартными (не Brown, Black, Blond, Red), а также их сторону (align) где align Good Characters или Bad Characters.
--    - **Выборка**: Имя, align, описание прически; где прическа не Brown, Black, Blond, или Red.
--    - **Количество строк**: 2744


SELECT name, ALIGN, HAIR
FROM MarvelCharacters
WHERE HAIR NOT IN ("Brown Hair", "Black Hair", "Blond Hair", "Red Hair")
AND ALIGN IN ("Good Characters", "Bad Characters")


-- 7. **Персонажи, появившиеся в определённое десятилетие**
--    - **Описание**: Вывести имя и год первого появления. Найти персонажей, первое появление которых приходится на 1960-е годы.
--    - **Выборка**: Имя, год первого появления; где год первого появления между 1960 и 1969.
--    - **Количество строк**: 1306

SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE Year BETWEEN 1960 AND 1969

-- 8. **Персонажи с уникальным сочетанием цвета глаз и волос**
--    - **Описание**: Вывести имя, цвет глаз, и цвет волос. Найти персонажей с сочетанием цвета глаз Yellow и цвета волос Red.
--    - **Выборка**: Имя, цвет глаз, цвет волос; где цвет глаз — Yellow и цвет волос — Red.
--    - **Количество строк**: 13

SELECT name, EYE, HAIR
FROM MarvelCharacters
WHERE EYE = "Yellow Eyes" AND HAIR = "Red Hair"


-- 9. **Персонажи с ограниченным количеством появлений**
--    - **Описание**: Вывести имя и количество появлений. Выбрать персонажей, количество появлений которых меньше 10.
--    - **Выборка**: Имя, количество появлений; где количество появлений меньше 10.
--    - **Количество строк**: 11938


SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES < 10


-- 10. **Персонажи с наибольшим количеством появлений**
--     - **Описание**: Вывести первые 5 имен и количество появлений. Найти персонажей с наибольшим количеством появлений, ограничить вывод первыми 5 записями.
--     - **Выборка**: Имя, количество появлений; сортировка по количеству появлений по убыванию, ограничить вывод первыми 5 записями.
--     - **Количество строк**: 5 (Человек Паук, Капитан Америка, Росомаха, Железный человек, Тор)


SELECT name, APPEARANCES
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 5


-- 11. **Персонажи, появившиеся только в одном десятилетии**
--     - **Описание**: Вывести имя и год первого появления. Выбрать персонажей, год первого появления которых начинается с 2000 и не превышает 2009.
--     - **Выборка**: Имя, год первого появления; где год первого появления между 2000 и 2009.
--     - **Количество строк**: 3086

SELECT name, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE Year BETWEEN 2000 AND 2009


-- 12. **Персонажи с самыми редкими цветами глаз**
--     - **Описание**: Вывести имя и цвет глаз. Найти персонажей с цветом глаз Magenta, Pink, или Violet.
--     - **Выборка**: Имя, цвет глаз; где цвет глаз Magenta, Pink, или Violet.
--     - **Количество строк**: 34


SELECT name, EYE
FROM MarvelCharacters
WHERE EYE IN ("Magenta Eyes", "Pink Eyes", "Violet Eyes")


-- 13. **Герои с публичной идентичностью, сортированные по году**
--     - **Описание**: Вывести имя, идентификацию, и год первого появления. Выбрать героев с публичной идентичностью (Public Identity), сортировка по году появления по возрастанию.
--     - **Выборка**: Имя, идентификация, год первого появления; где идентификация — Public Identity, сортировка по году появления по возрастанию.
--     - **Количество строк**: 4528

SELECT name, identify, FIRST_APPEARANCE
FROM MarvelCharacters
WHERE identify = "Public Identity"
AND year NOT NULL
ORDER BY Year


-- 14. **Персонажи с конкретным цветом волос и глаз, упорядоченные по имени**
--     - **Описание**: Вывести имя, цвет волос, и цвет глаз. Выбрать персонажей с цветом волос Black и цветом глаз Green, результаты упорядочить по имени в алфавитном порядке.
--     - **Выборка**: Имя, цвет волос, цвет глаз; где цвет волос — Black и цвет глаз — Green, сортировка по имени.
--     - **Количество строк**: 99


SELECT name, HAIR, EYE
FROM MarvelCharacters
WHERE HAIR = "Black Hair" AND EYE = "Green Eyes"
ORDER BY name



-- 15. **Злодеи с нестандартными физическими характеристиками**
--     - **Описание**: Вывести имя и описание пола. Найти злодеев, у которых пол не является стандартным (не Male, не Female).
--     - **Выборка**: Имя, описание пола; где align — Bad Characters и пол не Male и не Female.
--     - **Количество строк**: 20

SELECT name, sex
FROM marvelcharacters
WHERE align = "Bad Characters"
AND sex NOT IN ("Male Characters", "Female Characters")


SELECT name, year, appearances
FROM MarvelCharacters
WHERE year = (SELECT year FROM MarvelCharacters WHERE name
    LIKE "%Adolf Hitler (Clone)%"
    ORDER BY appearances DESC
    LIMIT 1)
ORDER BY APPEARANCES DESC

-- 16. **Название: Персонажи с наибольшим числом появлений по полу**
--     - **Описание:** Определить персонажей мужского и женского пола (SEX) с наибольшим количеством появлений. Вывести имена и количество появлений для топ-1 мужского и женского пола.
--     - **Выборка:** Группировка по полу, определение персонажа с максимальным количеством появлений в каждой группе.


SELECT name, sex, MAX(APPEARANCES) as MaxApp
FROM MarvelCharacters
WHERE SEX IN ("Male Characters", "Female Characters")
GROUP BY SEX

-- 17. **Название: Сравнение популярности персонажей по цвету волос и глаз**
--     - **Описание:** Сравнение общего количества появлений персонажей в зависимости от комбинации цвета волос и глаз. Необходимо сгруппировать данные по этим двум признакам и подсчитать общее количество появлений для каждой комбинации.
--     - **Выборка:** Группировка по цвету волос и глаз, подсчет количества появлений для каждой комбинации. Используйте SUM для подсчета общего количества появлений.
--     - **Количество строк**: 196


SELECT HAIR, EYE, SUM(APPEARANCES) as TotalApp
FROM MarvelCharacters
WHERE HAIR IS NOT NULL AND EYE IS NOT NULL
GROUP BY HAIR, EYE
HAVING TotalApp IS NOT NULL
ORDER BY TotalApp DESC

-- Эксперимент (ищем лидера каждой комбинации)
SELECT NAME, HAIR, EYE, MAX(APPEARANCES) as MaxApp
FROM MarvelCharacters
WHERE HAIR IS NOT NULL AND EYE IS NOT NULL
GROUP BY HAIR, EYE
HAVING MaxApp IS NOT NULL
ORDER BY MaxApp DESC


-- 18. **Название: Персонажи с максимальным количеством появлений в десятилетие**
--     - **Описание:** Найти персонажа с максимальным количеством появлений в каждом десятилетии начиная с 1940-х. Вывести десятилетие, имя персонажа и количество появлений.
--     - **Выборка:** Группировка по десятилетиям (используя год), определение персонажа с максимальным количеством появлений в каждом десятилетии.

SELECT name, MAX(APPEARANCES) as MaxApp, DECADE
FROM (
    SELECT name, APPEARANCES, (Year / 10) * 10 as DECADE
    FROM MarvelCharacters
    WHERE Year IS NOT NULL
)
GROUP BY DECADE
ORDER BY DECADE DESC


-- Вариант Тимура
SELECT name, APPEARANCES, Year, Year/10*10 as Decade
FROM MarvelCharacters
WHERE (Year/10)*10 >= 1940
GROUP BY Decade
ORDER BY Year DESC
 

-- 19. **Название: Герои и злодеи 80-х**
--     - **Описание:** Сравнение количества новых героев и злодеев, появившихся в 1980-х. Необходимо сгруппировать данные по ALIGN как Good и Bad, фильтровать по годам появления между 1980 и 1989 годами и подсчитать количество новых персонажей в каждой категории.
--     - **Выборка:** Группировка по ALIGN, фильтрация по годам между 1980 и 1989, подсчет количества новых персонажей.

-- Моё решение несколько расходится с условиями
SELECT ALIGN, COUNT(*) AS COUNT, Year
FROM marvelcharacters
WHERE ALIGN IN ("Good Characters", "Bad Characters")
AND Year BETWEEN 1980 AND 1989
GROUP BY ALIGN, Year
ORDER BY Year DESC

-- Упростим до условия
SELECT ALIGN, COUNT(*) AS COUNT
FROM marvelcharacters
WHERE ALIGN IN ("Good Characters", "Bad Characters")
AND Year BETWEEN 1980 AND 1989
GROUP BY ALIGN

-- 20. **Название: Самые популярные прически супергероев**
--     - **Описание:** Определение трех самых популярных причесок среди супергероев по общему количеству появлений. Группировать данные по типу прически и подсчитать общее количество появлений, выбрать топ-3.
--     - **Выборка:** Группировка по прическе, подсчет суммы появлений для каждой прически, выбор топ-3 по количеству появлений.


SELECT HAIR, SUM(APPEARANCES) as TotalApp
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
GROUP BY HAIR
ORDER BY TotalApp DESC
LIMIT 3

-- 21. **Название: Сколько Гитлеров вы насчитали?**
--     - **Описание:** Подсчет количества персонажей с именем "Hitler" и их общих появлений в комиксах Marvel. Необходимо найти всех персонажей, чье имя содержит "Hitler", и вывести их имена вместе с количеством появлений.
--     - **Выборка:** Фильтрация по имени, содержащему "Hitler", и вывод имени персонажа и количества его появлений.
--     - **Количество строк**: 2

SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE name LIKE "%Hitler%"