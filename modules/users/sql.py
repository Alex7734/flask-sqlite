class SQLStatements:
    INSERT_USER = "INSERT INTO USERS (username, password) VALUES (?, ?)"
    GET_USER_BY_USERNAME_PASSWORD = "SELECT * FROM USERS WHERE username=? AND password=?"
