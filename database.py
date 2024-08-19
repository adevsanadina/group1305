import sqlite3
from pprint import pprint

DB_PATH = 'our_db_130524.sqlite3'


with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS schools(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_number INTEGER,
            address TEXT,  
            floors INTEGER
        )
    """
    cursor.execute(query)

    query = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(20),
            name VARCHAR(20),
            specialization VARCHAR(20),
            school_number INTEGER,
            FOREIGN KEY (school_number) REFERENCES schools(school_number)  
        )
    """
    cursor.execute(query)

    first_school = [1, 'Новобудівельна 14', 3]
    query = """
        INSERT INTO schools(school_number, address, floors)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, first_school)

    second_school = [6, 'Судова 4', 5]
    cursor.execute(query, second_school)

    third_school = [21, 'Центральна 1А', 4]
    cursor.execute(query, third_school)

    students_in_schools = (
        ('Коваленко', 'Іван', 'Математика', 1),
        ('Петренко', 'Ольга', 'Фізика', 21),
        ('Іванов', 'Олександр', 'Хімія', 6),
        ('Сидоренко', 'Марія', 'Біологія', 21),
        ('Гнатенко', 'Андрій', 'Інформатика', 6),
        ('Олексієнко', 'Катерина', 'Географія', 1),
        ('Мельник', 'Дмитро', 'Фізика', 1),
        ('Тимошенко', 'Людмила', 'Математика', 21),
        ('Шевченко', 'Сергій', 'Хімія', 6),
        ('Гриценко', 'Анна', 'Література', 1),
        ('Бондаренко', 'Олег', 'Біологія', 6),
        ('Довженко', 'Юлія', 'Історія', 1),
        ('Лисенко', 'Наталія', 'Математика', 21),
        ('Кравчук', 'Петро', 'Фізика', 1),
        ('Мороз', 'Оксана', 'Географія', 6),
        ('Захаренко', 'Юрій', 'Хімія', 21),
        ('Василенко', 'Ірина', 'Література', 1),
        ('Тарасенко', 'Віктор', 'Інформатика', 6),
        ('Семененко', 'Олена', 'Математика', 21),
        ('Гончаренко', 'Ігор', 'Фізика', 1),
        ('Костенко', 'Михайло', 'Географія', 6),
        ('Чорненко', 'Аліна', 'Хімія', 21),
        ('Романенко', 'Євген', 'Біологія', 1),
        ('Стеценко', 'Людмила', 'Література', 21),
        ('Макаренко', 'Арсен', 'Історія', 6),
        ('Пономаренко', 'Іванна', 'Математика', 1),
        ('Вороненко', 'Олексій', 'Фізика', 21),
        ('Леоненко', 'Ірина', 'Інформатика', 6),
        ('Гребенюк', 'Світлана', 'Хімія', 1),
        ('Поліщук', 'Андрій', 'Географія', 6)
    )

    query = """
        INSERT INTO students(surname, name, specialization, school_number)
        VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, students_in_schools)

    query = """
        SELECT * FROM Students
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=60)


