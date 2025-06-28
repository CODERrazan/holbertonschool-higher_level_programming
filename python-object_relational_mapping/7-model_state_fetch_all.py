#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa,
sorted by id ascending.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username, password, db_name = sys.argv[1:4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
    session.close()
