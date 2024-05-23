import sqlite3

DATABASE_NAME = "database.db"

def init_db():
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                name TEXT PRIMARY KEY,
                difficulty INTEGER NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                category_name TEXT,
                FOREIGN KEY (category_name) REFERENCES categories(name)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS solutions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                problem_id INTEGER NOT NULL,
                example_code TEXT NOT NULL,
                FOREIGN KEY (problem_id) REFERENCES problems(id)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS USERS (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS submissions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                problem_id INTEGER NOT NULL,
                submission_code TEXT NOT NULL,
                submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES USERS(id),
                FOREIGN KEY (problem_id) REFERENCES problems(id)
            );
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS user_problems (
                user_id INTEGER NOT NULL,
                problem_id INTEGER NOT NULL,
                started_on DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES USERS(id),
                FOREIGN KEY (problem_id) REFERENCES problems(id),
                PRIMARY KEY (user_id, problem_id)
            );
        ''')

