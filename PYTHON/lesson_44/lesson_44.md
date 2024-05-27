### Диаграмма 1: Студенты и студенческие билеты (один к одному)

```plantuml
@startuml
entity "Students" as students {
    * StudentID : INTEGER
    --
    FirstName : TEXT
    LastName : TEXT
    StudentCardID : INTEGER
}

entity "StudentCards" as studentcards {
    * StudentCardID : INTEGER
    --
    StudentID : INTEGER
    DateOfIssue : TEXT
    DateOfExpiry : TEXT
}

students ||--|| studentcards : "possesses"
@enduml
```

### Диаграмма 2: Студенты и факультеты (один ко многим)

```plantuml
@startuml
entity "Students" as students {
    * StudentID : INTEGER
    --
    FirstName : TEXT
    LastName : TEXT
    StudentCardID : INTEGER
    FacultyID : INTEGER
}

entity "Faculties" as faculties {
    * FacultyID : INTEGER
    --
    FacultyName : TEXT
    Director : TEXT
}

faculties ||--o{ students : "has"
@enduml
```

### Диаграмма 3: Преподаватели и факультеты (многие ко многим)

```plantuml
@startuml
entity "Teachers" as teachers {
    * TeacherID : INTEGER
    --
    FirstName : TEXT
    LastName : TEXT
}

entity "Faculties" as faculties {
    * FacultyID : INTEGER
    --
    FacultyName : TEXT
    Director : TEXT
}

entity "TeachersFaculties" as teachersfaculties {
    * TeacherID : INTEGER
    * FacultyID : INTEGER
}

teachers ||--o{ teachersfaculties
faculties ||--o{ teachersfaculties
@enduml
```

### Пояснения

1. **Диаграмма 1**:
   - Студенты и студенческие билеты связаны отношением "один-к-одному". 
   - В таблице `Students` есть внешний ключ `StudentCardID`, который ссылается на `StudentCardID` в таблице `StudentCards`.
   - В таблице `StudentCards` есть уникальный внешний ключ `StudentID`, который ссылается на `StudentID` в таблице `Students`.

2. **Диаграмма 2**:
   - Студенты и факультеты связаны отношением "один-ко-многим".
   - В таблице `Students` есть внешний ключ `FacultyID`, который ссылается на `FacultyID` в таблице `Faculties`.
   - Один факультет может иметь много студентов, но каждый студент может быть только на одном факультете.

3. **Диаграмма 3**:
   - Преподаватели и факультеты связаны отношением "многие-ко-многим".
   - Для реализации этого отношения создана связующая таблица `TeachersFaculties`, которая содержит внешние ключи `TeacherID` и `FacultyID`, ссылающиеся на соответствующие поля в таблицах `Teachers` и `Faculties`.
   - У преподавателя может быть много факультетов, и у факультета может быть много преподавателей.

Эти диаграммы должны помочь в визуализации структуры вашей базы данных и понимании отношений между таблицами.