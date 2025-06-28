#!/usr/bin/python3
"""
Script that filters states by user input from hbtn_0e_0_usa database
using string formatting for the SQL query.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    # Create cursor object
    cur = db.cursor()

    # Create SQL query using string formatting as required
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    
    # Execute the query
    cur.execute(query)

    # Fetch all matching rows
    rows = cur.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
