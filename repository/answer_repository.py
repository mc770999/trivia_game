import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.answer_model import Answer
from typing import List


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)


def create_answer_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS answers (
        id SERIAL PRIMARY KEY,
        question_id INTEGER NOT NULL,
        answer_txt VARCHAR(100) NOT NULL,
        is_correct BOOLEAN NOT NULL,
        FOREIGN KEY (question_id) REFERENCES questions(id) ON DELETE CASCADE
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()



def create_answer(answer : Answer) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into answers (question_id,answer_txt,is_correct) 
    values (%s,%s,%s) returning id
    """, (answer.question_id, answer.answer_txt, answer.is_correct))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_answers() -> List[Answer]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from answers
        """)
    res = cursor.fetchall()
    answers = [Answer(**u) for  u in res]
    cursor.close()
    connection.close()
    return answers


def get_answers_by_question_id(u_id : int) -> Answer:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from answers where question_id = (%s)
            """,(u_id,))
    res = cursor.fetchall()
    answers = [Answer(**u) for  u in res]
    cursor.close()
    connection.close()
    return answers



def delete_answer(u_id : int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM answers
    WHERE id = (%s);
    """, (u_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return u_id
