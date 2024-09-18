import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)

def create_users_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        first VARCHAR(100) NOT NULL,
        last VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()

def create_question_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS questions (
        id SERIAL PRIMARY KEY,
        question_text VARCHAR(100) NOT NULL,
        correct_answer VARCHAR(100) NOT NULL
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()

def create_answer_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS answers (
        id SERIAL PRIMARY KEY,
        question_id INTEGER NOT NULL,
        incorrect_answer VARCHAR(100) NOT NULL,
        FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()

def create_user_answer_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        """
         CREATE TABLE IF NOT EXISTS users_answers (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        answer_text VARCHAR(50) NOT NULL,
        is_correct BOOLEAN NOT NULL,
        time_taken TIME NOT NULL,
        FOREIGN KEY (question_id) REFERENCES question(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
        """
    )
    conn.commit()
    cur.close()
    conn.close()