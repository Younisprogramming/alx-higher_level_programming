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
    cur.execute("SELECT * FROM states \
                    WHERE states.name = %s \
                    ORDER BY id ASC;", (target,))
    states = cur.fetchall()
    for state in states:
        if state[1] == target:
            print(state)

    db.close()
