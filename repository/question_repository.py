import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.question_model import Question
from typing import List


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)


def create_question_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        question_text VARCHAR(100) NOT NULL
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()


def create_question(questions : Question) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO questions (question_text) 
    values (%s) returning id
    """, (questions.question_text,))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_questions() -> List[Question]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from questions
        """)
    res = cursor.fetchall()
    questions = [Question(**u) for  u in res]
    cursor.close()
    connection.close()
    return questions


def get_question_by_id(u_id : int) -> Question:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from questions where id = (%s)
            """,(u_id,))
    res = cursor.fetchone()
    question = Question(**res)
    cursor.close()
    connection.close()
    return question



def delete_question(u_id : int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM questions
    WHERE id = (%s);
    """, (u_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return u_id
