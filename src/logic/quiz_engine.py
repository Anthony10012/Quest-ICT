"""
 Project name: Pré-TPI Quest-ICT
 File : quiz_engine.py
 description: A logic engine that manages the retrieval of questions and answers from the SQLite database.
 Author : Anthony Simond
 Date : 2026/03/10
 last modified : 2026/03/23
 Version : 1.1

"""

import os.path
import sqlite3
import random


def get_random_quiz(themes_id= None,difficulty= None,limit=8):
    """
    Retrieves a quiz of 8 random questions with their respective answers.

    Args:
        themes_id (int, optional): the unique theme ID. Defaults to None.
        difficulty (str, optional): the level of difficulty ("easy","medium","hard"). Defaults to None.
        limit (int, optional): the number of questions to retrieve. Defaults to 8.

    Returns:
        list[dict]: A list of dictionaries. Each dictionary contains:
            - “question” (str): The question text.
            - “explanation” (str): The theoretical explanation.
            - “answers” (list): A list of 4 dictionaries containing answers (text, image, correct answer).
            - “themes_id” (int): The theme ID.
            - “difficulty” (str): The difficulty level.

        Note: Returns an empty list [] in the event of an error or if parameters are missing.

    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, "..",".."))
    db_path = os.path.join(root_dir, "database", "quiz_db.sqlite")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # Allows access to columns by name
    cursor = conn.cursor()

    try:
        # Select 8 questions at random
        if themes_id and difficulty:
            query = "SELECT * FROM questions WHERE themes_id = ? AND difficulty = ?  ORDER BY RANDOM() LIMIT ?"
            cursor.execute(query,(themes_id,difficulty, limit))
        else:
            return []

        questions = cursor.fetchall()
        quiz_data = []

        for question in questions:
          # For each question, retrieve its 4 answers
          cursor.execute("""
                         SELECT  DISTINCT  response_text,image_path,is_correct
                         FROM answers
                         WHERE questions_id= ?
                         LIMIT 4
                         """,(question["id"],))
          rows = cursor.fetchall()
          answers = [dict(row) for row in rows]

          # --- CLEANING OF PATHWAYS ---
          # Remove ‘assets/images/’ if it is stored in the database to avoid path errors
          for a in answers:
              if a["image_path"]:
                  a["image_path"] = a["image_path"].replace("assets/images/", "")

          # Shuffle the order of the answers
          random.shuffle(answers)

          # Constructing the complete question object
          quiz_data.append({
            "question": question["statement"],
            "explanation": question["theoretical_contribution"],
            "difficulty": question["difficulty"],
            "themes_id": question["themes_id"],
            "answers": answers,
          })
        return quiz_data
    except sqlite3.Error as e:
        print(f"Erreur lors de la génération du quiz : {e}")
        return []
    finally:
        conn.close()

