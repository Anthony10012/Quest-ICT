import sqlite3
import random


def get_random_quiz(limit=8):
    """
    Retrieves a quiz of 8 random questions with their respective answers.
    """
    conn = sqlite3.connect('../../database/quiz_db.sqlite')
    conn.row_factory = sqlite3.Row # Allows access to columns by name
    cursor = conn.cursor()

    try:
        # Select 8 questions at random
        cursor.execute("""
        SELECT id,statement,theoretical_contribution,difficulty
        FROM questions
        ORDER BY RANDOM() 
        LIMIT ?
        """, (limit,))

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
            "answers": answers,
          })
          return quiz_data
    except sqlite3.Error as e:
        print(f"Erreur lors de la génération du quiz : {e}")
        return []
    finally:
        conn.close()

