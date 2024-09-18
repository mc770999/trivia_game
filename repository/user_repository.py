import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI
from model.user_model import User
from typing import List


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


def create_user(user : User) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    insert into users (first,last,email) 
    values (%s,%s,%s) returning id
    """,(user.first,user.last,user.email))
    new_id = cursor.fetchone()["id"]
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_users() -> List[User]:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        select * from users
        """)
    res = cursor.fetchall()
    users = [User(**u) for  u in res]
    cursor.close()
    connection.close()
    return users


def get_user_by_id(u_id : int) -> User:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
            select * from users where id = (%s)
            """,(u_id,))
    res = cursor.fetchone()
    user = User(**res)
    cursor.close()
    connection.close()
    return user


def update_user(user : User) -> User:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE users
    SET first = (%s), last = (%s), email = (%s)
    WHERE id = (%s);
    """, (user.first, user.last, user.email, user.id))
    connection.commit()
    cursor.close()
    connection.close()
    return user


def delete_user(u_id : int) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    DELETE FROM users
    WHERE id = (%s);
    """, (u_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return u_id
