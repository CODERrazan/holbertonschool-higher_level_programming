#!/usr/bin/python3
"""
Updates the name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa.
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
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
