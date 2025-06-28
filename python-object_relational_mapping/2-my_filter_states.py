#!/usr/bin/python3
"""
Script that takes a state name as argument and displays matching states
from the database hbtn_0e_0_usa using MySQLdb with secure parameterized queries
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        
        with db.cursor() as cur:
            cur.execute(
                "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
                (state_name,)
            )
            for row in cur.fetchall():
                print(row)
                
    except MySQLdb.Error as e:
        print(f"MySQL Error [{e.args[0]}]: {e.args[1]}")
    finally:
        if 'db' in locals() and db.open:
            db.close()
