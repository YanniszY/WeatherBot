import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# нужно для создания дб
def init_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        user_id INTEGER PRIMARY KEY,
        city TEXT,
        last_temp REAL,
        last_condition TEXT
    )
    ''')
    conn.commit()

# проверяет есть ли город для конкретного пользователя
def has_city(user_id):
    cursor.execute("SELECT COUNT(*) FROM data WHERE user_id = ?", (user_id,))
    count = cursor.fetchone()[0]
    return count > 0


# получает город пользователя
def get_city(user_id):
    cursor.execute("SELECT city FROM data WHERE user_id = ?", (user_id,))
    city = cursor.fetchone()
    
    if city:
        return city[0]
    else:
        return None


# добавляет город для конкретного пользователя
def add_city(user_id, user_city):
    cursor.execute("INSERT INTO data (user_id, city) VALUES (?, ?)", (user_id, user_city))
    conn.commit()


# обновляет город для конкретного пользователя
def update_city(user_id, user_city):
    cursor.execute("UPDATE data SET city = ? WHERE user_id = ?", (user_city, user_id))
    conn.commit()
