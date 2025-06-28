#!/usr/bin/python3
"""
Displays all values in the states table where name matches the user input.
Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    # Escape single quotes in user input to prevent malformed queries
    safe_state = state_name.replace("'", "''")
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(safe_state)
    )
    cur.execute(query)
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
