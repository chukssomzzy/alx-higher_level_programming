#!/usr/bin/python3

"""List all `states` with a name starting with N from the databas
    e hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ != "__main__":
    sys.exit(1)
argv = sys.argv[1:]
username = argv[0]
password = argv[1]
db_name = argv[2]

conn = MySQLdb.connect(host="localhost", user=username, passwd=password,
                       port=3306, charset="utf8", db=db_name)
cur = conn.cursor()
cur.execute("""SELECT * FROM states WHERE states.name REGEXP '^N';""")
for row in cur._rows:
    print(row)
