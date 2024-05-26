class SQLStatements:
    ADD_INITIAL_DATA = [
        "INSERT INTO categories (name, difficulty) VALUES ('Algorithms', 1)",
        "INSERT INTO categories (name, difficulty) VALUES ('Pointers', 2)",
        "INSERT INTO categories (name, difficulty) VALUES ('Databases', 3)",
        "INSERT INTO problems (title, description, category_name) VALUES ('Join tables', 'Description 1', 'Databases')",
        "INSERT INTO problems (title, description, category_name) VALUES ('Add Two Numbers', 'Description 2', 'Algorithms')",
        "INSERT INTO problems (title, description, category_name) VALUES ('Problem 3', 'Longest Substring Without Repeating Characters', 'Pointers')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (1, 'print(1)')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (2, 'print(2)')",
        "INSERT INTO solutions (problem_id, example_code) VALUES (3, 'print(3)')"
    ]
    ADD_CATEGORY = "INSERT INTO categories (name, difficulty) VALUES (?, ?)"
    ADD_PROBLEM = "INSERT INTO problems (title, description, category_name) VALUES (?, ?, ?)"
    ADD_SOLUTION = "INSERT INTO solutions (problem_id, example_code) VALUES (?, ?)"
    GET_ALL_PROBLEMS_WITH_CATEGORIES = "SELECT problems.id, problems.title, problems.description, categories.name FROM problems JOIN categories ON problems.category_name = categories.name"
    GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY = "SELECT problems.id, problems.title, problems.description, categories.name, categories.difficulty FROM problems JOIN categories ON problems.category_name = categories.name"
    TRACK_PROBLEM = "INSERT OR IGNORE INTO user_problems (user_id, problem_id) VALUES (?, ?)"
    SUBMIT_SOLUTION = "INSERT INTO submissions (user_id, problem_id, submission_code, score) VALUES (?, ?, ?, ?)"
    GET_PROBLEM_DETAILS = "SELECT problems.title, problems.description, categories.name FROM problems JOIN categories ON problems.category_name = categories.name WHERE problems.id = ?"
    GET_SOLUTIONS_FOR_PROBLEM = "SELECT example_code FROM solutions WHERE problem_id = ?"
    GET_PROBLEMS_WITH_CATEGORIES_AND_DIFFICULTY_BY_ID = """
        SELECT problems.id, problems.title, problems.description, categories.name, categories.difficulty
        FROM problems
        JOIN categories ON problems.category_name = categories.name
        WHERE problems.id = ?
        """
    GET_USER_SUBMISSIONS_BY_USER_ID = "SELECT * FROM submissions WHERE user_id = ?"
    GET_USER_SUBMISSIONS_WITH_PROBLEM_NAME = """
        SELECT s.id, s.problem_id, p.title as problem_name, s.submission_code, s.submission_date, s.score
        FROM submissions s
        JOIN problems p ON s.problem_id = p.id
        WHERE s.user_id = ?
    """
    FILTER_PROBLEMS_BY_CATEGORY ="""
        SELECT problems.id, problems.title, problems.description, categories.name, categories.difficulty
        FROM problems
        JOIN categories ON problems.category_name = categories.name
        WHERE problems.title LIKE ? AND categories.name LIKE ? AND categories.difficulty LIKE ?
    """
    GET_PROFILE_INFO = """
        SELECT
            username,
            (SELECT COUNT(*) FROM submissions WHERE user_id = ?) as problems_submitted,
            (SELECT AVG(score) FROM submissions WHERE user_id = ?) as average_score
        FROM users
        WHERE id = ?
    """

