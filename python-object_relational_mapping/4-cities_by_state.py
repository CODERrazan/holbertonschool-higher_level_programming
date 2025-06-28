#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa,
along with their corresponding state names.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
