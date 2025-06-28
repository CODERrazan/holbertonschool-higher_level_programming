#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by states.id and displayed as tuples.
"""
import MySQLdb
import sys


def filter_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all states where the name starts with 'N',
    sorted by state ID in ascending order.

    Args:
        username (str): MySQL username
        password (str): MySQL password
        dbname (str): Database name
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname,
            charset="utf8"
        )
        with db.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM states
                WHERE name LIKE BINARY 'N%'
                ORDER BY id ASC
            """)
            for state in cursor.fetchall():
                print(state)
    except MySQLdb.Error as e:
        print(f"MySQL Error {e.args[0]}: {e.args[1]}")
    finally:
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
