#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument (safe from SQL injection)
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

    # Create a cursor object
    cur = db.cursor()

    # Create the SQL query using format (safe from SQL injection)
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the query
    cur.execute(query, (state_name,))

    # Fetch all the rows
    rows = cur.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
