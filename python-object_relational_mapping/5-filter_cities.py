#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <username> <password> <db_name> <state_name>
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
    query = (
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query, (state_name,))
    city_names = [row[0] for row in cur.fetchall()]
    print(", ".join(city_names))

    cur.close()
    db.close()
