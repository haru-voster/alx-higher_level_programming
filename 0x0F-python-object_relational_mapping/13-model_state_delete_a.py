#!/usr/bin/python3
# Deletes all State objects with a name containing
# the letter a from the database hbtn_0e_6_usa.
# Usage: ./13-model_state_delete_a.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
#!/usr/bin/python3
"""
    A script that deletes all State objects from hbtn_0e_6_usa that conatin
    the letter a
    Username, password and dbname wil be passed as arguments to the script.
"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # extract states with a in them
    states = session.query(State).filter(State.name.ilike('%a%')).all()

    # delete states
    for state in states:
        session.delete(state)

    session.commit()

    session.close()
