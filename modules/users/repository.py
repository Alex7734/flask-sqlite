import sqlite3
from .sql import SQLStatements

DATABASE_NAME = "database.db"

def get_user_by_username_password(username, password):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_USER_BY_USERNAME_PASSWORD, (username, password))
        return cursor.fetchone()

def insert_user(username, password):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.INSERT_USER, (username, password))
        conn.commit()
