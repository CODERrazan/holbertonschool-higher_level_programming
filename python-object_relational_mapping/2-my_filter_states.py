#!/usr/bin/python3
"""
Script that filters states by user input from hbtn_0e_0_usa database.
Returns exact match for state name with proper formatting.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        # Create cursor and execute query
        cur = db.cursor()
        query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        cur.execute(query.format(state_name))

        # Fetch and print results with exact formatting
        for row in cur.fetchall():
            print("({}, '{}')".format(row[0], row[1]))

    except MySQLdb.Error:
        pass  # Silent fail as per requirements
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
