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


