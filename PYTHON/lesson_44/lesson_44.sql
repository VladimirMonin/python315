-- Lesson 44
-- 27.05.2024
-- Повторяем транзакции

-- Транзакции - это группа операций, которые выполняются как единое целое. (Атомарность)
-- Транзакции должны быть выполнены полностью или не выполнены вообще. (Целостность)
-- Ключевое слово для начала транзакции - BEGIN TRANSACTION
-- Ключевое слово для завершения транзакции - COMMIT - сохранить изменения
-- Ключевое слово для отката транзакции - ROLLBACK - отменить изменения

-- Создадим таблицу с транзакциями

BEGIN TRANSACTION;

CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    student_id TEXT,
    group_number TEXT
);

-- Добавим 2 записи в таблицу студенты
INSERT INTO Students (first_name, last_name, age, student_id, group_number)
VALUES ('Иван', 'Иванов', 20, '12345', 'A-123'),
       ('Петр', 'Петров', 22, '54321', 'B-321');


-- Проверим, что записи добавлены

SELECT * FROM Students;

-- Rollback - откатим транзакцию

ROLLBACK;

-- Commit - закоммитим транзакцию