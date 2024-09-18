import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.question_model import Question
from model.user_answer_model import UserAnswer
from typing import List

def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)

def create_user_answer_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS users_answers (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        answer_id INTEGER NOT NULL,
        time_taken TIME NOT NULL,
        FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE,
        FOREIGN KEY (answer_id) REFERENCES answers(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()


def create_user(user_answer : UserAnswer) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into users_answers (user_id,question_id,answer_id) 
    values (%s,%s,%s) returning id
    """,(user_answer.user_id,user_answer.question_id,user_answer.answer_id))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_users_answers() -> List[UserAnswer]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from users_answers
        """)
    res = cursor.fetchone()
    users = [UserAnswer(**u) for  u in res]
    cursor.close()
    connection.close()
    return users


def get_user_answer_by_id(u_id : int) -> UserAnswer:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from users_answers where id = (%s)
            """,(u_id,))
    res = cursor.fetchone()
    user = UserAnswer(**res) if res else None
    cursor.close()
    connection.close()
    return user





def delete_user_answer(u_id : int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM users_answers
    WHERE id = (%s);
    """, (u_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return u_id
