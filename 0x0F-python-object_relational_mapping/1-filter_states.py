#!/usr/bin/python3

import MySQLdb
import sys


def main():
    """
        Function containing code to filter all the states
        from the database.
    """

    # Create a database connection
    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    curs = conn.cursor()
    # Select states
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curs.fetchall()
    [print(state) for state in query_rows if state[1][0] == "N"]
    curs.close()
    conn.close()


if __name__ == "__main__":
    main()

