"""
 Project name: Pré-TPI Quest-ICT
 File : database.py
 description: Module for managing user data persistence (logging in, checking for existing profiles and adding new ones to the SQLite database).
 Author : Anthony Simond
 Date : 2026/03/10
 last modified : 2026/03/10
 Version : 1.1

"""
import sqlite3
import os

def get_connection():
    """
    Establishes a connection to the project’s SQLite database.

    Calculates the absolute path to the .sqlite file from the current directory
    to ensure that the connection works regardless of where the script is run.

    Returns:
        sqlite3.Connection: An active connection object to the quiz_db.sqlite database.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir,"..",".."))
    db_path = os.path.join(root_dir, "database","quiz_db.sqlite")
    return sqlite3.connect(db_path)

def check_user_exists(pseudo):
    """
    Checks whether a user already exists in the database.

    Args:
        pseudo (str): The username to search for in the “users” table.

    Returns:
        bool: True if the pseudo already exists, False otherwise.

    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE pseudo = ?', (pseudo,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def add_user(pseudo):
    """
    Adds a new user to the database.

    Args:
        pseudo (str): The username chosen by the user.

    Returns:
         bool:
            True if the user has been added,
            False if they already exist or if an error occurs.

    """

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

def save_game_result(users_id,themes_id,final_score,total_time):
    """
    Saves the result of a game in the "games" table.
    :param users_id: The user's unique identifier (foreign key to the users table).
    :type users_id: int
    :param themes_id: The ID of the theme selected for the game (foreign key to the themes table).
    :type themes_id: int
    :param final_score: The number of points scored by the player
    :type final_score: int
    :param total_time: The total time taken to answer the questions, in seconds.
    :type total_time: int
    :return: True if the backup was successful, False if a database error occurred.
    :rtype: bool
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO games (final_score,date_time,total_time,themes_id,users_id) 
            VALUES (?,CURRENT_TIMESTAMP,?,?,?)
            """, (final_score,total_time,themes_id,users_id))
        conn.commit()
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du score : {e}")
    finally:
        conn.close()