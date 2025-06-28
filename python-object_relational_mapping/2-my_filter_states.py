#!/usr/bin/python3
"""
Script that takes a state name as argument and displays
all matching states from the database hbtn_0e_0_usa
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

    # Create parameterized query using format
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the query with the state_name as parameter
    cur.execute(query, (state_name,))

    # Fetch all matching rows
    rows = cur.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
