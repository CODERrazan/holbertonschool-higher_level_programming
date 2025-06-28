#!/usr/bin/python3
"""
Fetches the State object with the specified name from the database
and prints its id. Safe from SQL injection.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name, state_name = sys.argv[1:5]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    session = Session(engine)
    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
