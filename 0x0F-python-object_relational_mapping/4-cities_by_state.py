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
    cur = db.cursor()
    cur.execute(
                 "SELECT cities.id, cities.name, \
                 states.name FROM states \
                 INNER JOIN cities \
                 ON states.id = cities.state_id;"
               )
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
