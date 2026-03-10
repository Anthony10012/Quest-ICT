import sqlite3

def get_connection():
    return sqlite3.connect('../../database/quiz_db.sqlite')

def check_user_exists(pseudo):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE pseudo = ?', (pseudo,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_user(pseudo):
    if check_user_exists(pseudo):
        return False

    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (pseudo) VALUES (?)', (pseudo,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erreur : {e}")
        return False
    finally:
        conn.close()