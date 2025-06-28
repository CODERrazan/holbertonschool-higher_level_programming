#!/usr/bin/python3
"""
Script that takes a state name as argument and displays
all matching states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
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

        # Create query with parameterized input
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        
        # Execute the query with the state_name as parameter
        cur.execute(query, (state_name,))

        # Fetch all matching rows
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close cursor and connection if they exist
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
