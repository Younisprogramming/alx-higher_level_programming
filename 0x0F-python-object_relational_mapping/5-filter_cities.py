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
    count = 0
    if len(states) > 0:
        for row in states:
            count += 1
            if count < (len(states)):
                print('{}, '.format(row[0]), end="")
            else:
                print('{}'.format(row[0]))
    else:
        print()
    db.close()
