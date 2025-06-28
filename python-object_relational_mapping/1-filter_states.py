#!/usr/bin/python3
"""
Lists all states with a name starting with N from database hbtn_0e_0_usa
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


def filter_states(username, password, dbname):
    """
    Filters and displays states starting with 'N'
    Args:
        username: MySQL username
        password: MySQL password
        dbname: Database name
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        states = cursor.fetchall()
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
