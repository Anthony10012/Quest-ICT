import os.path
import sqlite3
import random


def get_random_quiz(themes_id= None,difficulty= None,limit=8):
    """
    Retrieves a quiz of 8 random questions with their respective answers.
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
                         SELECT response_text,image_path,is_correct
                         FROM answers
                         WHERE questions_id= ?
                         """,(question["id"],))
          answers = [dict(row) for row in cursor.fetchall()]

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

