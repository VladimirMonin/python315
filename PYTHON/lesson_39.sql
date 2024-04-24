-- Lesson 39: Знакомство с SQL
-- 24.04.2024

-- SELECT - выбрать (столбцы)
-- FROM - из (таблицы)
-- ; - конец запроса
-- Регистронезависимый язык

SELECT * 
FROM MarvelCharacters;

-- Мы можем выбрать нужные столбцы

SELECT name, identify, hair, sex, APPEARANCES 
FROM MarvelCharacters;

-- Мы можем использовать простую фильтрацию
-- WHERE - где, пишут после SELECT и после FROM
-- Персонажи где появлений больше 100
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100;

-- ORDER BY - сортировать по (столбцу) DESC - по убыванию
-- Сортировка может быть по нескольким столбцам
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100
ORDER BY HAIR, name

-- В WHERE могут быть логические условия (похожие на пайтон)
-- Приоритет логических операторов
-- () - скобки. Первыми выполняются внутри скобок
-- NOT - не
-- AND - и
-- OR - или
SELECT name, identify, hair, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES > 100 AND sex = Female Characters
ORDER BY APPEARANCES DESC