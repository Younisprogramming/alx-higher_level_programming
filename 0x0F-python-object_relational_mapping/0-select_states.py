#!/usr/bin/python3
"""  hirw iutw stohst i"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3360)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
