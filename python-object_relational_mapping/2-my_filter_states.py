#!/usr/bin/python3
"""
Script that takes a state name as argument and displays
all matching states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Validate argument count
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)

    # Get arguments
    username, password, db_name, state_name = sys.argv[1:5]

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
        
        # Create cursor
        cur = db.cursor()
        
        # Create query using format() as required
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        
        # Execute query
        cur.execute(query)
        
        # Fetch and display results
        for row in cur.fetchall():
            print(row)
            
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Clean up
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
