-- Lesson 43
-- Аномалии. Нормализация. Целостность данных.
-- 22.05.2024

-- Простой пример связи между таблицами
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE Photos (
    PhotoID INTEGER PRIMARY KEY,
    Description TEXT,
    PersonID INTEGER,
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)
);

-- Три типа связей между таблицами:
-- 1. Один человек - одни контактные данные.
-- 2. Один ко многим. В нашем примере, одна геолокация, много фотографий.
-- 3. Многие ко многим. Один человек может быть на многих фотографиях, и на одной фотографии может быть много людей.


-- Таблица контактных данных
-- CREATE TABLE Contacts (
--     ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
--     Phone TEXT,
--     Email TEXT,
--     PersonID INTEGER UNIQUE,
--     FOREIGN KEY (PersonID) REFERENCES People (PersonID)
-- );

-- ОДИН К ОДНОМУ
-- Ограничение на уникальность PersonID гарантирует, что у каждого человека будет только один набор контактных данных.
-- Ограничение телефонов гарантирует, что у разных людей не будет одинаковых телефонов.
-- Таблица телефонов
CREATE TABLE Phones (
    PhoneID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор телефона
    Phone TEXT UNIQUE,                          -- Уникальный номер телефона
    PersonID INTEGER UNIQUE,                    -- Уникальный идентификатор человека, связанный с телефоном
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)  -- Внешний ключ на таблицу People
);

-- Таблица людей
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор человека
    FirstName TEXT,                              -- Имя человека
    MiddleName TEXT,                             -- Отчество человека
    LastName TEXT                                -- Фамилия человека
);

-- Сняв некоторые ограничения мы можем получить один ко многим

-- Таблица телефонов
CREATE TABLE Phones (
    PhoneID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор телефона
    Phone TEXT UNIQUE,                          -- Уникальный номер телефона
    PersonID INTEGER,                           -- ОДИН человек может оставить МНОГО телефонов
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)  -- Внешний ключ на таблицу People
);
-- МЫ не ограничили уникальность PersonID, теперь у одного человека может быть несколько телефонов
-- Таблица людей
CREATE TABLE People (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Уникальный идентификатор человека
    FirstName TEXT,                              -- Имя человека
    MiddleName TEXT,                             -- Отчество человека
    LastName TEXT                                -- Фамилия человека
);


CREATE Photos (
    PhotoID INTEGER PRIMARY KEY AUTOINCREMENT,
    Description TEXT,
    PersonID INTEGER,
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)
);

-- МНОГИЕ КО МНОГИМ. Связующая таблица PhotosPeople
CREATE TABLE PhotosPeople (
    
    PhotoID INTEGER,
    PersonID INTEGER,

    FOREIGN KEY (PhotoID) REFERENCES Photos (PhotoID),
    FOREIGN KEY (PersonID) REFERENCES People (PersonID)

);
