import sqlite3 as sq
from data.random_parson import get_person


# Создание соединения с базой данных и создание таблицы, если она не существует
def db_start():
    # Устанавливаем соединение с базой данных
    connection = sq.connect('user.db')
    cur = connection.cursor()

    # Создаем таблицу
    cur.execute("""CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    name TEXT,
                    fname TEXT,
                    age INTEGER,
                    phone TEXT,
                    job_title TEXT,
                    gender TEXT)""")

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def db_insert_random(num=100):
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    for i in range(1, num+1):
        user_id = i
        name, fname, age, phone, job_title, gender = get_person()
        cur.execute(
            f"INSERT INTO user (user_id, name, fname, age, phone, job_title, gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_id, name, fname, age, phone, job_title, gender))

    connection.commit()
    connection.close()

        # Вставка записи в таблицу


def db_insert(user_id, name, fname, age, phone, job_title, gender):
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    # Проверяем, существует ли уже запись с таким же названием
    if not cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchone():
        cur.execute(
            f"INSERT INTO user (user_id, name, fname, age, phone, job_title, gender) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_id, name, fname, age, phone, job_title, gender))

    connection.commit()
    connection.close()


# Обновление записи в таблице
def db_update(user_id, name, fname, age, phone, job_title, gender):
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    # Обновляем запись с указанным названием
    cur.execute("UPDATE user SET name = ?, fname = ?, age = ?, phone = ?, job_title = ?, gender = ? WHERE user_id = ?",
                (name, fname, age, phone, job_title, gender, user_id))

    connection.commit()
    connection.close()


# Выбор всех записей из таблицы
def db_select():
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    users = cur.execute("SELECT * FROM user").fetchall()

    connection.close()
    return users


# Удаление записи из таблицы по названию
def db_delete(user_id):
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    cur.execute("DELETE FROM user WHERE user_id = ?", (user_id,))

    connection.commit()
    connection.close()


def id_exist(user_id):
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    return not cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchone()

    connection.commit()
    connection.close()


def db_delete_all():
    connection = sq.connect('data/user.db')
    cur = connection.cursor()

    cur.execute("DELETE FROM user")

    connection.commit()
    connection.close()

# Тестовый код
if __name__ == '__main__':
    db_start()
    db_insert_random()
    # db_insert(2, "Ayk", "Galstyan", 21, "+7(999)999-99-99")

    # db_update(2, "Ayk", "Galstyan", 21, "+7(918)450-99-99")
    # db_delete(1)
    #
    #
    # for i in db_select():
    #     print(*i)

    # db_delete('Мастер и Маргарита')
