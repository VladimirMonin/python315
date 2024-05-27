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

COMMIT;

-- Разбор практики прошлого занятия (которая стала ДЗ на среду)

-- Практика
-- Студенты, Студенческие билеты, Факультеты, Преподаватели

-- 1. Студенты и студенческие билеты (один к одному)
-- Students: StudentID, FirstName, LastName, StudentCardID
-- StudentCards: StudentCardID, StudentID, DateOfIssue, DateOfExpiry
-- Подумайте, как обеспечить связь один - к - одному между студентами и студенческими билетами.

-- У студентов не может быть двух студенческих билетов, и у студенческого билета не может быть двух студентов.


CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
);

CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER UNIQUE,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
);

-- Какая тут проблема?
-- Циклическая зависимость. Я не могу добавить запись в таблицу один, потому что вторая таблица ссылается на первую, и наоборот.
-- Выхода 2:
-- 1. Так как тут нет Not Null, то можно добавить запись в одну таблицу, а потом в другую. После добавить ID второй таблицы в первую.
-- 2. Более оптимальное решение. Смягчить требования. Убрать UNIQUE из StudentID в таблице StudentCards.
-- Или вообще убрать этот столбец, так как он не нужен. Таким образом мы сможем выдавать студенческие билеты без привязки к студенту. Например, если студент потерял студенческий билет, то мы можем выдать ему новый, не удаляя старый из базы данных.

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID)
);

CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
);

-- 2. Студенты и факультеты (один ко многим)
-- Students: Таблица уже есть. Надо добавить поле FacultyID (Команда ALTER TABLE) или пересоздать таблицу.
-- Faculties: FacultyID, FacultyName, Director
-- Подумайте, как обеспечить связь один - ко - многим между студентами и факультетами.
-- У студента может быть только один факультет, но у факультета может быть много студентов.

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FacultyID INTEGER,  -- Если тут даем UNIQUE - это будет один к одному

    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);

CREATE TABLE Faculties (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT UNIQUE NOT NULL,
    Director TEXT
);


-- 3. Преподаватели и факультеты (многие ко многим)
-- Teachers: TeacherID, FirstName, LastName
-- TeachersFaculties: TeacherID, FacultyID
-- Вам надо правильно описать связующую таблицу. У преподавателя может быть много факультетов, и у факультета может быть много преподавателей.
-- Давайте подумаем, как обеспечить связь многие - ко - многим между преподавателями и факультетами.
-- При этом не определив на дважды или трижды одного препода на одном факультете, и наоборот.

CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT DEFAULT 'Неизвестно',
    LastName TEXT
);

CREATE TABLE TeachersFaculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TeacherID INTEGER,
    FacultyID INTEGER,
    -- Добавим дату-время назначения преподавателя на факультет автоматом через функцию DATETIME('now')
    DateOfAppointment TEXT DEFAULT DATETIME('now'),
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID),
    UNIQUE (TeacherID, FacultyID)
);

CREATE TABLE TeachersFaculties (
    TeacherID INTEGER,
    FacultyID INTEGER,
    PRIMARY KEY (TeacherID, FacultyID),
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID) ON DELETE CASCADE,
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID) ON DELETE CASCADE
);

-- Что будет происходить со связанными данными при операциях UPDATE и DELETE?
-- 1. CASCADE - при удалении или обновлении родительской записи, дочерняя запись также будет удалена или обновлена.
-- 2. SET NULL - при удалении или обновлении родительской записи, дочерняя запись будет обновлена, и в столбце, который ссылается на родительскую запись, будет NULL.
-- 3. SET DEFAULT - при удалении или обновлении родительской записи, дочерняя запись будет обновлена, и в столбце, который ссылается на родительскую запись, будет значение по умолчанию.
-- 4. NO ACTION - при удалении или обновлении родительской записи, дочерняя запись не будет удалена или обновлена.
-- 5. RESTRICT - при удалении или обновлении родительской записи, дочерняя запись не будет удалена или обновлена, если нарушается целостность данных.