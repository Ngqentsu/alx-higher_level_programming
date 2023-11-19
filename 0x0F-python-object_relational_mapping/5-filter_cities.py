#!/usr/bin/python3
"""Lists all cities of a given state from hbtn_0e_4_usa"""

import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """Lists all cities of a given state."""
    try:
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=database, port=3306)
        cur = db.cursor()
        query = ("""SELECT cities.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id
                 WHERE states.name=%s ORDER BY cities.id ASC""")
        cur.execute(query, (state_name,))
        unique_cities = set()
        rows = cur.fetchall()
        for row in rows:
            unique_cities.add(row[0])
        for city in unique_cities:
            print(city)

    except MySQLdb.Error:
        pass

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
    else:
        username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

        list_cities(username, password, database, state_name)
