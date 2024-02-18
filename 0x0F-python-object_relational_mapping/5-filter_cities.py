#!/usr/bin/python3
"""
my documentation ...
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(
                         host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    target = sys.argv[4]
    cur = db.cursor()
    cur.execute(
                "SELECT cities.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id \
                WHERE states.name = %s;", (target,)
               )
    states = cur.fetchall()
    for state in states:
        print(state, end="")
    db.close()
