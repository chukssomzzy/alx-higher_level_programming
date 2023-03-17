#!/usr/bin/python

"""lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ != "__main__":
    sys.exit(1)

argv = sys.argv[1:]
username = argv[0]
password = argv[1]
db_name = argv[2]

conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute("""SELECT t2.id, t2.name, t1.name
                FROM states AS t1 INNER JOIN cities AS t2
                ON t2.state_id = t1.id;""")

for row in cur._rows:
    print(row)
conn.close()
