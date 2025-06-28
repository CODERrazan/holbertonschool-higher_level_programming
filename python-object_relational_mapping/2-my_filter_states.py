#!/usr/bin/python3
"""
This script takes a state name as input and displays matching states
from the hbtn_0e_0_usa database, using MySQLdb for the connection.
It demonstrates safe database querying with parameterized queries.
"""

import MySQLdb
import sys

def get_matching_states(username, password, db_name, state_name):
    """
    Retrieves and displays states matching the given name.
    
    Args:
        username: MySQL username
        password: MySQL password
        db_name: Database name
        state_name: State name to search for
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
        
        with db.cursor() as cur:
            query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
            cur.execute(query, (state_name,))
            
            for row in cur.fetchall():
                print(row)
                
    except MySQLdb.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
        sys.exit(1)
        
    _, username, password, db_name, state_name = sys.argv
    get_matching_states(username, password, db_name, state_name)
