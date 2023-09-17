#!/usr/bin/python3
""" This module takes an argument and displays all values states
    database hbtn_0e_0_usa WHERE name matches the argument.
"""

import MySQLdb
import sys


def main():
    """
        Function containing code to select the state provided
        in the argument and is implemented in a safe way to prevent
        an SQL injection.
    """

    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    curs = conn.cursor()
    # Select states
    state_name = sys.argv[4]
    curs.execute(
            "SELECT * FROM states WHERE\
                    name = %s ORDER BY id ASC", (state_name, ))
    query_rows = curs.fetchall()
    for row in query_rows:
        print(row)
    curs.close()
    conn.close()


if __name__ == "__main__":
    main()

