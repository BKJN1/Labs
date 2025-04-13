import psycopg2  # библиотека для подключения к PostgreSQL
import csv       # для чтения CSV-файлов

# --- Подключение к базе данных ---
conn = psycopg2.connect(
    dbname='phonebook',
    user='ArginBekezhan',
    password='4167',
    host='localhost',
    port='5432'
)
conn.autocommit = True
cur = conn.cursor()

# --- Команда для вставки записи ---
command_insert = "INSERT INTO phonebook (username, phone) VALUES (%s, %s)"

# --- Импорт контактов из CSV ---
def csvv():
    with open('Straw_hat.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                        (row['username'], row['phone']))

# --- Добавление контакта вручную ---
def insert_db():
    username = input("Name: ")
    phone = input("Phone: ")
    cur.execute(command_insert, (username, phone))

# --- Изменить имя по ID ---
def change_name():
    id = int(input("ID: "))
    new_name = input("New name: ")
    cur.execute("UPDATE phonebook SET username=%s WHERE id=%s", (new_name, id))
    print("Name updated")

# --- Изменить номер по ID ---
def change_phone():
    new_phone = input("Phone: ")
    id = int(input("ID: "))
    cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (new_phone, id))
    print("Phone updated")

# --- Поиск по части имени или номера ---
def query_data():
    filter_text = input("Enter search filter (part of name or phone): ")
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s OR phone ILIKE %s",
                ('%' + filter_text + '%', '%' + filter_text + '%'))
    results = cur.fetchall()
    for r in results:
        print(r)

# --- Удаление по имени или номеру ---
def delete_user():
    value = input("Enter name or phone to Delete: ")
    cur.execute("DELETE FROM phonebook WHERE username=%s OR phone=%s", (value, value))
    print("User deleted if existed.")

# --- Меню ---
while True:
    print("\n1 - Insert from input")
    print("2 - Change name")
    print("3 - Change phone")
    print("4 - Query data")
    print("5 - Delete")
    print("6 - Import from CSV")
    print("0 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        insert_db()
    elif choice == "2":
        change_name()
    elif choice == "3":
        change_phone()
    elif choice == "4":
        query_data()
    elif choice == "5":
        delete_user()
    elif choice == "6":
        csvv()
    elif choice == "0":
        break
    else:
        print("Invalid option.")

# --- Закрытие соединения ---
cur.close()
conn.close()
