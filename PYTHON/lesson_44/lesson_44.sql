-- Lesson 44
-- 27.05.2024
-- Повторяем транзакции
-- Повторяем типы отношений в БД
-- Смотрим, что будет происходить с данными при изменении и удалении
-- Начинаем изучать JOIN


CREATE TABLE StudentCards (
    StudentCardID INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentID INTEGER,
    DateOfIssue TEXT,
    DateOfExpiry TEXT,
    FOREIGN KEY (StudentID) REFERENCES Students (StudentID)
);

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
    StudentCardID INTEGER UNIQUE,
    FacultyID INTEGER,  -- Если тут даем UNIQUE - это будет один к одному а не многие к одному

    FOREIGN KEY (StudentCardID) REFERENCES StudentCards (StudentCardID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID)
);

CREATE TABLE Faculties (
    FacultyID INTEGER PRIMARY KEY AUTOINCREMENT,
    FacultyName TEXT UNIQUE NOT NULL,
    Director TEXT
);

CREATE TABLE Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT DEFAULT 'Неизвестно',
    LastName TEXT
);

CREATE TABLE TeachersFaculties (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    TeacherID INTEGER,
    FacultyID INTEGER,
    DateOfAppointment TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID),
    FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID),
    UNIQUE (TeacherID, FacultyID)
);

-- CREATE TABLE TeachersFaculties (
--     TeacherID INTEGER,
--     FacultyID INTEGER,
--     PRIMARY KEY (TeacherID, FacultyID),
--     FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID) ON DELETE CASCADE,
--     FOREIGN KEY (FacultyID) REFERENCES Faculties (FacultyID) ON DELETE CASCADE
-- );

