#!/usr/bin/python3
"""Inserts a new state object "Louisiana" to the DB htbn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Sessions = sessionmaker(bind=engine)
    sessions = Sessions()

    state = State(name="Louisiana")
    sessions.add(state)
    sessions.commit()
    print(state.id)

