import sqlite3
from .utils import get_difficulty_level
from .sql import SQLStatements

DATABASE_NAME = "database.db"

def add_initial_data():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        for statement in SQLStatements.ADD_INITIAL_DATA:
            cursor.execute(statement)
        conn.commit()

def add_category(name, difficulty):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_CATEGORY, (name, difficulty))
        conn.commit()

def add_problem(title, description, category_name):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_PROBLEM, (title, description, category_name))
        conn.commit()

def add_solution(problem_id, example_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.ADD_SOLUTION, (problem_id, example_code))
        conn.commit()

def get_all_problems_with_categories():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_ALL_PROBLEMS_WITH_CATEGORIES)
        problems = [{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3]
        } for row in cursor.fetchall()]
        return problems

def get_problems_with_categories_and_difficulty():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY)
        problems = [{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3],
            'difficulty': get_difficulty_level(row[4])
        } for row in cursor.fetchall()]
        return problems

def get_problem_details(problem_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY_BY_ID, (problem_id,))
        row = cursor.fetchone()
        print(row)
        if row is None:
            return None, None


        problem = {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'category': row[3],
            'difficulty': row[4] if row[4] else 'Unknown'
        }

        cursor.execute(SQLStatements.GET_SOLUTIONS_FOR_PROBLEM, (problem_id,))
        solutions_row = cursor.fetchone()

        if solutions_row is None:
            solutions = None
        else:
            solutions = {
                'example_code': solutions_row[0]
            }

        print(solutions)

        return problem, solutions


def submit_solution(user_id, problem_id, submission_code):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.SUBMIT_SOLUTION, (user_id, problem_id, submission_code))
        conn.commit()


def track_user_problem(user_id, problem_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.TRACK_PROBLEM, (user_id, problem_id))
        conn.commit()

def get_user_submissions(user_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(SQLStatements.GET_USER_SUBMISSIONS_WITH_PROBLEM_NAME, (user_id,))
        rows = cursor.fetchall()
        submissions = []
        for row in rows:
            submissions.append({
                'submission_id': row[0],
                'problem_id': row[1],
                'problem_name': row[2],
                'submission_code': row[3],
                'submission_date': row[4],
            })
        return submissions


def add_initial_data():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()

        categories = [
            ("Algorithms", 1),
            ("Pointers", 2),
            ("Databases", 3)
        ]
        cursor.executemany("INSERT INTO categories (name, difficulty) VALUES (?, ?)", categories)

        problems = [
            ("Join tables", "Description 1", "Databases"),
            ("Add Two Numbers", "Description 2", "Algorithms"),
            ("Longest Substring Without Repeating Characters", "Description 3", "Pointers")
        ]
        cursor.executemany("INSERT INTO problems (title, description, category_name) VALUES (?, ?, ?)", problems)

        conn.commit()

        cursor.execute("SELECT id FROM problems ORDER BY id")
        problem_ids = [row[0] for row in cursor.fetchall()]

        solutions = [
            (problem_ids[0], "SELECT * FROM table1 JOIN table2 ON table1.id = table2.id;"),
            (problem_ids[1], "int add(int a, int b) { return a + b; }"),
            (problem_ids[2], "int lengthOfLongestSubstring(string s) { /* code here */ }")
        ]
        cursor.executemany("INSERT INTO solutions (problem_id, example_code) VALUES (?, ?)", solutions)

        conn.commit()
