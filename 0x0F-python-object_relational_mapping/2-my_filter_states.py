#!/usr/bin/python3

"""Takes in an argument and display all values in the states table of
`hbtn_0e_0_usa` where name matches the argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    with MySQLdb.connect(host="localhost", passwd=sys.argv[2], port=3306,
                         user=sys.argv[1], db=sys.argv[3]) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name FROM states WHERE name LIKE\
                        BINARY '{}'\
                        ORDER BY id ASC".format(sys.argv[4]))
            states = cur.fetchall()
            for state in states:
                print(state)
