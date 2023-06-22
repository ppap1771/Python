import sqlite3
from flask import g
def connect_db():
    """
    connects the sqlite database to the application
    """
    sql = sqlite3.connect("./food_log.db")

    # This line of code configures the connection to return rows as sqlite3.Row objects, which provide a convenient way to access the columns of a query result by name.
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    """
        Retrieve the SQLite database connection object.

        This function checks if the connection object exists in the `g` object,
        which is a global object used for storing data during the lifetime of a
        request in a Flask application. If the connection object does not exist,
        it creates a new connection by calling the `connect_db()` function and
        stores it in `g` for future use.

        Returns:
        sqlite3.Connection: The SQLite database connection object.
    """
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
