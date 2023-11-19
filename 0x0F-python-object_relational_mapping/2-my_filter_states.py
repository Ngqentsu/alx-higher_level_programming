#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    """Searches and displays states based on the provided state name."""
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                 "ORDER BY id ASC".format(state_name))
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error:
        pass

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database> <state_name>")
    else:
        username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        search_states(username, password, database, state_name)
