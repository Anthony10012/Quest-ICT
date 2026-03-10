import sqlite3
import os

def get_connection():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir,"..",".."))
    db_path = os.path.join(root_dir, "database","quiz_db.sqlite")
    return sqlite3.connect(db_path)

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
        cursor.execute('INSERT INTO users (pseudo,creation_date) VALUES (?,CURRENT_TIMESTAMP)', (pseudo,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
        return False
    finally:
        conn.close()