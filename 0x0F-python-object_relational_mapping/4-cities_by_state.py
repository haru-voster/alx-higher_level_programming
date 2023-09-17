#!/usr/bin/python3
""" This module lists all the cities from the
    database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to select all the cities
        from the database.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    curs = conn.cursor()
    # Select states
    curs.execute("SELECT cities.id,\
                cities.name, states.name FROM cities\
                INNER JOIN states ON\
                cities.state_id=states.id ORDER BY cities.id")
    query_rows = curs.fetchall()
    for cty in query_rows:
        print(cty)
    curs.close()
    conn.close()


if __name__ == "__main__":
    main()

