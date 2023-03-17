#!/usr/bin/python

"""Takes in argument and displays all values in the states table of
`hbtn_0e_0_usa` where `name` matches the argument

"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM states WHERE states.name = %s ORDER BY
                    states.id ASC;""", (sys.argv[4],))
        for row in cur:
            print(row)
