import psycopg2
import csv

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname='Phones2',
    user='akezhanamanzhol',
    password='4167',
    host='localhost',
    port='5432'
)

conn.autocommit = True
cur = conn.cursor()

# Функция для поиска по шаблону
cur.execute("""
CREATE OR REPLACE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT p.id, p.username, p.phone 
    FROM phonebook p
    WHERE p.username ILIKE '%' || pattern || '%' 
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# Процедура: добавить или обновить одного пользователя
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(uname TEXT, uphone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = uname) THEN
        UPDATE phonebook SET phone = uphone WHERE username = uname;
    ELSE
        INSERT INTO phonebook(username, phone) VALUES(uname, uphone);
    END IF;
END;
$$;
""")

# Процедура: вставка нескольких пользователей из списка
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users(users TEXT[][])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(users, 1) LOOP
        IF users[i][2] ~ '^\\d+$' THEN
            CALL insert_or_update_user(users[i][1], users[i][2]);
        ELSE
            RAISE NOTICE 'Неправильный номер: %', users[i][2];
        END IF;
    END LOOP;
END;
$$;
""")

# Функция: получить список пользователей с лимитом и оффсетом
cur.execute("""
CREATE OR REPLACE FUNCTION get_users(limit_num INT, offset_num INT)
RETURNS TABLE(id INT, username TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY SELECT * FROM phonebook
    ORDER BY id
    LIMIT limit_num OFFSET offset_num;
END;
$$ LANGUAGE plpgsql;
""")

# Процедура: удалить пользователя по имени или номеру
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user_by_value(val TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook WHERE username = val OR phone = val;
END;
$$;
""")

# --- Вызовы процедур/функций из Python ---

# Поиск по части имени или телефона
def call_search():
    val = input("Введите часть имени или номера: ")
    cur.execute("SELECT * FROM search_pattern(%s)", (val,))
    for row in cur.fetchall():
        print(row)

# Добавление или обновление одного пользователя
def call_insert():
    name = input("Имя: ")
    phone = input("Номер: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))

# Вставка нескольких пользователей
def call_many():
    n = int(input("Сколько пользователей добавить: "))
    users = []
    for _ in range(n):
        name = input("Имя: ")
        phone = input("Номер: ")
        users.append([name, phone])
    cur.execute("CALL insert_many_users(%s)", (users,))

# Удаление по имени или номеру
def call_delete():
    val = input("Введите имя или номер для удаления: ")
    cur.execute("CALL delete_user_by_value(%s)", (val,))
    print("Удалено, если существовало.")

# Постраничный вывод с лимитом и смещением
def call_paginate():
    lim = int(input("Лимит: "))
    off = int(input("Сдвиг (offset): "))
    cur.execute("SELECT * FROM get_users(%s, %s)", (lim, off))
    for row in cur.fetchall():
        print(row)

# --- Главное меню ---
while True:
    print("\nМеню:")
    print("1 - Добавить / обновить пользователя")
    print("2 - Добавить список пользователей")
    print("3 - Поиск по шаблону")
    print("4 - Удаление по имени или номеру")
    print("5 - Показать с лимитом и сдвигом")
    print("0 - Выход")

    choice = input("Выберите вариант: ")

    if choice == "1":
        call_insert()
    elif choice == "2":
        call_many()
    elif choice == "3":
        call_search()
    elif choice == "4":
        call_delete()
    elif choice == "5":
        call_paginate()
    elif choice == "0":
        break
    else:
        print("Некорректный ввод, попробуй снова")

# Закрытие соединения с базой
cur.close()
conn.close()