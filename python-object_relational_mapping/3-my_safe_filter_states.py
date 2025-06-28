#!/usr/bin/python3
"""
Safely displays all values in the states table of hbtn_0e_0_usa
where name matches user input, protected from SQL injection.
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
