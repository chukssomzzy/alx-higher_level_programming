#!/usr/bin/python3

"""Gets the lists of all states from the database `hbtn_0e_0_usa`"""
import sys
import MySQLdb

if __name__ == '__main__':
    with MySQLdb.connect(host="localhost", passwd=sys.argv[2], port=3306,
                         user=sys.argv[1], db=sys.argv[3]) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT id, name FROM states
                                 ORDER BY id ASC
                                 """)
            states = cur.fetchall()
            for state in states:
                print(state)
