# db.py
# Работа с PostgreSQL: вход, регистрация, сохранение результата

import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    database="Snake",              # Название твоей БД
    user="ArginBekezhan",        # Твой юзер
    password="4167",               # Пароль
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Получить пользователя или создать нового
def get_or_create_user():
    username = input("Enter your username: ")

    # Проверяем, существует ли пользователь
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    # Если нет — создаём
    if not user:
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        print("🆕 New user added.")
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
    else:
        print(f"👋 Welcome back, {username}!")

    return user[0], username  # возвращаем id и имя

# Сохранить результат игры (без времени)
def save_score(user_id, level, score):
    cur.execute("""
        INSERT INTO user_score (user_id, level, score)
        VALUES (%s, %s, %s)
    """, (user_id, level, score))
    conn.commit()
    print("💾 Score saved.")

# Закрыть соединение
def close_connection():
    cur.close()
    conn.close()