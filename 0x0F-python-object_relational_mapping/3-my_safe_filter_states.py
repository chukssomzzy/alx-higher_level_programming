#!/usr/bin/python

"""Takes in argument and displays all values in the states table of
`hbtn_0e_0_usa` where `name` matches the argument"""

import sys
import MySQLdb

if __name__ != "__main__":
    sys.exit(1)

argv = sys.argv[1:]
username = argv[0]
password = argv[1]
db_name = argv[2]
state_name = argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute("""SELECT * FROM states WHERE states.name = %s ORDER BY
            states.id ASC;""", (state_name,))

for row in cur._rows:
    print(row)
conn.close()
