-- СТРУКТУРА ТАБЛИЦ!
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:16:12 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: MarvelCharacters
CREATE TABLE IF NOT EXISTS "MarvelCharacters" (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    page_id INTEGER,

    name TEXT,

    urlslug TEXT,

    identity_id INTEGER,

    align_id INTEGER,

    eye_id INTEGER,

    hair_id INTEGER,

    sex_id INTEGER,

    GSM TEXT,

    status_id INTEGER,

    APPEARANCES INTEGER,

    FIRST_APPEARANCE TEXT,

    Year INTEGER,





    FOREIGN KEY (identity_id) REFERENCES Identity(identity_id),

    FOREIGN KEY (align_id) REFERENCES Alignment(align_id),

    FOREIGN KEY (eye_id) REFERENCES EyeColor(eye_id),

    FOREIGN KEY (hair_id) REFERENCES HairColor(hair_id),

    FOREIGN KEY (sex_id) REFERENCES Sex(sex_id), 

    FOREIGN KEY (status_id) REFERENCES LivingStatus(status_id)

);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

```
```sql
--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:17:13 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Identity
CREATE TABLE IF NOT EXISTS Identity (
    identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identity TEXT UNIQUE
);
INSERT INTO Identity (identity_id, identity) VALUES (1, 'Secret Identity');
INSERT INTO Identity (identity_id, identity) VALUES (2, 'Public Identity');
INSERT INTO Identity (identity_id, identity) VALUES (3, 'No Dual Identity');
INSERT INTO Identity (identity_id, identity) VALUES (4, 'Known to Authorities Identity');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:17:59 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Alignment
CREATE TABLE IF NOT EXISTS Alignment (
    align_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
INSERT INTO Alignment (align_id, name) VALUES (1, 'Good Characters');
INSERT INTO Alignment (align_id, name) VALUES (2, 'Neutral Characters');
INSERT INTO Alignment (align_id, name) VALUES (3, 'Bad Characters');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:18:16 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: EyeColor
CREATE TABLE IF NOT EXISTS EyeColor (
    eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);
INSERT INTO EyeColor (eye_id, color) VALUES (1, 'Hazel Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (2, 'Blue Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (3, 'Brown Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (4, 'Green Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (5, 'Grey Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (6, 'Yellow Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (7, 'Gold Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (8, 'Red Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (9, 'Black Eyeballs');
INSERT INTO EyeColor (eye_id, color) VALUES (10, 'Amber Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (11, 'Variable Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (12, 'Black Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (13, 'White Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (14, 'Orange Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (15, 'Silver Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (16, 'Purple Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (17, 'Pink Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (18, 'One Eye');
INSERT INTO EyeColor (eye_id, color) VALUES (19, 'Violet Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (20, 'Multiple Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (21, 'Magenta Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (22, 'Yellow Eyeballs');
INSERT INTO EyeColor (eye_id, color) VALUES (23, 'No Eyes');
INSERT INTO EyeColor (eye_id, color) VALUES (24, 'Compound Eyes');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:18:27 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: HairColor
CREATE TABLE IF NOT EXISTS HairColor (
    hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);
INSERT INTO HairColor (hair_id, color) VALUES (1, 'Brown Hair');
INSERT INTO HairColor (hair_id, color) VALUES (2, 'White Hair');
INSERT INTO HairColor (hair_id, color) VALUES (3, 'Black Hair');
INSERT INTO HairColor (hair_id, color) VALUES (4, 'Blond Hair');
INSERT INTO HairColor (hair_id, color) VALUES (5, 'No Hair');
INSERT INTO HairColor (hair_id, color) VALUES (6, 'Blue Hair');
INSERT INTO HairColor (hair_id, color) VALUES (7, 'Red Hair');
INSERT INTO HairColor (hair_id, color) VALUES (8, 'Bald');
INSERT INTO HairColor (hair_id, color) VALUES (9, 'Auburn Hair');
INSERT INTO HairColor (hair_id, color) VALUES (10, 'Grey Hair');
INSERT INTO HairColor (hair_id, color) VALUES (11, 'Silver Hair');
INSERT INTO HairColor (hair_id, color) VALUES (12, 'Purple Hair');
INSERT INTO HairColor (hair_id, color) VALUES (13, 'Strawberry Blond Hair');
INSERT INTO HairColor (hair_id, color) VALUES (14, 'Green Hair');
INSERT INTO HairColor (hair_id, color) VALUES (15, 'Reddish Blond Hair');
INSERT INTO HairColor (hair_id, color) VALUES (16, 'Gold Hair');
INSERT INTO HairColor (hair_id, color) VALUES (17, 'Orange Hair');
INSERT INTO HairColor (hair_id, color) VALUES (18, 'Pink Hair');
INSERT INTO HairColor (hair_id, color) VALUES (19, 'Variable Hair');
INSERT INTO HairColor (hair_id, color) VALUES (20, 'Yellow Hair');
INSERT INTO HairColor (hair_id, color) VALUES (21, 'Light Brown Hair');
INSERT INTO HairColor (hair_id, color) VALUES (22, 'Magenta Hair');
INSERT INTO HairColor (hair_id, color) VALUES (23, 'Bronze Hair');
INSERT INTO HairColor (hair_id, color) VALUES (24, 'Dyed Hair');
INSERT INTO HairColor (hair_id, color) VALUES (25, 'Orange-brown Hair');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:18:33 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: LivingStatus
CREATE TABLE IF NOT EXISTS LivingStatus (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT UNIQUE
);
INSERT INTO LivingStatus (status_id, status) VALUES (1, 'Living Characters');
INSERT INTO LivingStatus (status_id, status) VALUES (2, 'Deceased Characters');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.4 в Вт май 14 12:18:46 2024
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Sex
CREATE TABLE IF NOT EXISTS Sex (
    sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);
INSERT INTO Sex (sex_id, name) VALUES (1, 'Male Characters');
INSERT INTO Sex (sex_id, name) VALUES (2, 'Female Characters');
INSERT INTO Sex (sex_id, name) VALUES (3, 'Genderfluid Characters');
INSERT INTO Sex (sex_id, name) VALUES (4, 'Agender Characters');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

-- РЕШЕНИЕ ЗАДАЧ

-- **Задание 14: Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета**
-- - **Описание:** Найдите персонажей с определенным цветом волос, у которых максимальное количество появлений среди всех персонажей с таким цветом волос. Цвет волос должен совпадать с заданным, количество появлений должно быть равно максимальному количеству появлений среди всех персонажей с таким цветом волос.
-- - **Выборка столбцов:** name, color, APPEARANCES
-- - **Условия отбора:** Цвет волос должен совпадать с заданным, количество появлений должно быть равно максимальному количеству появлений среди всех персонажей с таким цветом волос.

-- №1 - Вариант для одного конкретного цвета волос (Blond Hair)

SELECT name, color, max(APPEARANCES) as APPEARANCES
FROM MarvelCharacters
JOIN HairColor ON MarvelCharacters.hair_id = HairColor.hair_id
WHERE color = 'Blond Hair'

-- №2 - Вариант для всех цветов волос

SELECT MarvelCharacters.name, HairColor.color, max(MarvelCharacters.APPEARANCES) as APPEARANCES
FROM MarvelCharacters
JOIN HairColor ON MarvelCharacters.hair_id = HairColor.hair_id
GROUP BY MarvelCharacters.hair_id

SELECT mc.name, hc.color, max(mc.APPEARANCES) as APPEARANCES
FROM MarvelCharacters mc
JOIN HairColor hc ON mc.hair_id = hc.hair_id
GROUP BY mc.hair_id


-- **Задание 15: Персонажи с публичной личностью и наименьшим количеством появлений**
-- - **Описание:** Найдите всех персонажей с "Public Identity", у которых наименьшее количество появлений. Тип личности должен быть "Public Identity", количество появлений должно быть равно минимальному количеству появлений среди всех персонажей с такой личностью.
-- - **Выборка столбцов:** name, identity, APPEARANCES
-- - **Условия отбора:** Тип личности должен быть "Public Identity", количество появлений должно быть равно минимальному количеству появлений среди всех персонажей с такой личностью.


SELECT mc.name, i.identity, min(mc.APPEARANCES) as APPEARANCES
FROM MarvelCharacters mc
JOIN Identity i ON mc.identity_id = i.identity_id
WHERE i.identity = 'Public Identity'

-- **Задание 16: Обновление статуса персонажей**

BEGIN TRANSACTION;

UPDATE MarvelCharacters
SET status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Living Characters')
WHERE status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Deceased Characters');

-- Проверка
SELECT * FROM MarvelCharacters
WHERE status_id = (SELECT status_id FROM LivingStatus WHERE status = 'Deceased Characters');

ROLLBACK;

-- **Задание 17: -- Добавление нового персонажа Человек-Кодер
-- (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, GSM, status_id, APPEARANCES, FIRST_APPEARANCE, Year)

-- 999999
-- Человек-Кодер
-- /coderman
-- Public Identity
-- Bad Characters
-- Red Eyes
-- Bold Hair
-- Male Characters
-- Heterosexual Characters
-- Living Characters
-- 4444
-- MAY2020
-- 2020

INSERT INTO MarvelCharacters (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, status_id, APPEARANCES, FIRST_APPEARANCE, Year)
VALUES (
    999999,
    'Человек-Кодер',
    '/coderman',
    (SELECT identity_id FROM Identity WHERE identity = 'Public Identity'),
    (SELECT align_id FROM Alignment WHERE name = 'Bad Characters'),
    (SELECT eye_id FROM EyeColor WHERE color = 'Red Eyes'),
    (SELECT hair_id FROM HairColor WHERE color = 'Bold Hair'),
    (SELECT sex_id FROM Sex WHERE name = "Male Characters"),
    (SELECT status_id FROM LivingStatus WHERE status = 'Living Characters'),
    4444,
    'MAY2020',
    2020

)

-- Добудем нового персонажа по имени Человек-Кодер
SELECT * FROM MarvelCharacters
WHERE name = 'Человек-Кодер'


-- **Задание 18: Удаление персонажей с нулевыми появлениями**

BEGIN TRANSACTION;

DELETE FROM MarvelCharacters
WHERE APPEARANCES = 0;

-- Удалим блондинов через подзапрос

DELETE FROM MarvelCharacters
WHERE hair_id = (
    SELECT hair_id 
    FROM HairColor 
    WHERE color = 'Blond Hair');

-- Проверка
SELECT * FROM MarvelCharacters
WHERE APPEARANCES = 0;

SELECT * FROM MarvelCharacters
WHERE hair_id = (
    SELECT hair_id 
    FROM HairColor 
    WHERE color = 'Blond Hair');

ROLLBACK;

-- Задание 20: Добавление нового статуса**
-- - **Описание:** Добавьте новый статус "Unknown Status" в таблицу статусов. Новый статус должен быть уникальным.
-- - **Условия отбора:** Новый статус должен быть уникальным.
-- - **Действие:** Добавить новый статус.

-- Это поддерживается в PostgreSQL и в MySQL но не в SQLite
IF NOT EXISTS (SELECT * FROM LivingStatus WHERE status = 'Unknown Status')
INSERT INTO LivingStatus (status) VALUES ('Unknown Status');

INSERT INTO LivingStatus (status)
SELECT 'Unknown Status'
WHERE NOT EXISTS (
    SELECT 1
    FROM LivingStatus
    WHERE status = 'Unknown Status'
);


INSERT INTO LivingStatus (status)
VALUES ('Unknown Status')


-- Проверка

SELECT * FROM LivingStatus
WHERE status = 'Unknown Status'