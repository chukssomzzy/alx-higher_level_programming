#!/usr/bin/python3

"""Takes in the name of a state as an argument and lists all `cities` of that
    state, using the database `hbtn_0e_0_usa`
"""
import sys
import MySQLdb

if __name__ == '__main__':
    with MySQLdb.connect(host="localhost", passwd=sys.argv[2], port=3306,
                         user=sys.argv[1], db=sys.argv[3]) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT cities.name FROM cities
                            INNER JOIN
                                states
                            ON
                                (states.id = cities.state_id)
                            WHERE
                                states.name = %s
                            ORDER BY
                                cities.id ASC
                        """, (sys.argv[4],))
            cities = cur.fetchall()
            for i in range(len(cities)):
                print(cities[i][0], end='')
                if i < (len(cities) - 1):
                    print(', ', end='')
            else:
                print()
