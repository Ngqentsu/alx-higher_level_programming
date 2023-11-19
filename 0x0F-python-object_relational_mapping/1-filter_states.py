#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys


def list_states(username, password, database):
    """Listing all the states."""
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'
                    ORDER BY id ASC")
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
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

        list_states(username, password, database)
