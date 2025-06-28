#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a'
from the database hbtn_0e_6_usa.
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
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
