#!/usr/bin/python3

"""List all `states` with a name starting with N from the databas
e hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], port=3306, charset="utf8",
                           db=sys.argv[3])
    with conn.cursor() as cur:
        cur.execute("""SELECT *
                    FROM states
                    WHERE states.name REGEXP '^N'
                    ORDER BY states.id ASC;""")
        for row in cur:
            print(row)
