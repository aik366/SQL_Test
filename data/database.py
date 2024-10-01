import sqlite3 as sq
from data.random_parson import get_person


# Создание соединения с базой данных и создание таблицы, если она не существует
def db_start():
    # Устанавливаем соединение с базой данных
    with sq.connect('user.db') as db:
        cursor = db.cursor()
        # Создаем таблицу
        cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        name TEXT,
                        fname TEXT,
                        age INTEGER,
                        phone TEXT,
                        job_title TEXT,
                        gender TEXT)""")


# Вставка записи в таблицу user
def db_insert_random(num=100):
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()

        for i in range(1, num + 1):
            user_id = i
            name, fname, age, phone, job_title, gender = get_person()
            cursor.execute(
                f"INSERT INTO user (user_id, name, fname, age, phone, job_title, gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (user_id, name, fname, age, phone, job_title, gender))

        db.commit()


def db_insert(user_id, name, fname, age, phone, job_title, gender):
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()

        # Проверяем, существует ли уже запись с таким же названием
        if not cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchone():
            cursor.execute(
                f"INSERT INTO user (user_id, name, fname, age, phone, job_title, gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (user_id, name, fname, age, phone, job_title, gender))

        db.commit()


# Обновление записи в таблице
def db_update(user_id, name, fname, age, phone, job_title, gender):
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()

        # Обновляем запись с указанным названием
        cursor.execute(
            "UPDATE user SET name = ?, fname = ?, age = ?, phone = ?, job_title = ?, gender = ? WHERE user_id = ?",
            (name, fname, age, phone, job_title, gender, user_id))

        db.commit()


# Выбор всех записей из таблицы
def db_select():
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()
        return cursor.execute("SELECT * FROM user").fetchall()


# Удаление записи из таблицы по названию
def db_delete(user_id):
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM user WHERE user_id = ?", (user_id,))
        db.commit()


def id_exist(user_id):
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()
        return not cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchone()


def db_delete_all():
    with sq.connect('data/user.db') as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM user")
        db.commit()


if __name__ == '__main__':
    db_start()
    db_insert_random()
