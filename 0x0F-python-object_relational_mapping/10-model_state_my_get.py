#!/usr/bin/python3
"""prints the state object with the name passed as argument from the DB"""
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
    result = sessions.query(State).order_by(State.id)
    available = 0
    for state in result:
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            available = 1
            break
    if available == 0:
        print("Not available")

