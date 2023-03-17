#!/usr/bin/python3

"Select states with python from mysql database"
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=db_name, charset="utf8")
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
        for row in cur:
            print(row)
